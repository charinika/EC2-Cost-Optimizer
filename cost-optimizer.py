import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    cloudwatch = boto3.client('cloudwatch')
    sns = boto3.client('sns')
    
    stopped_instances = []
    checked_instances = 0
    
    # Get only running instances
    response = ec2.describe_instances(
        Filters=[
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            
            instance_id = instance['InstanceId']
            checked_instances += 1
            
            # STEP 1: TAG FILTER (Safety)
            tags = instance.get('Tags', [])
            is_test_instance = False
            
            for tag in tags:
                if tag['Key'] == 'Environment' and tag['Value'] == 'Test':
                    is_test_instance = True
            
            # Skip non-test instances
            if not is_test_instance:
                print(f"Skipping {instance_id} (Not a Test instance)")
                continue
            
            # STEP 2: GET CPU USAGE
            metrics = cloudwatch.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[
                    {'Name': 'InstanceId', 'Value': instance_id}
                ],
                StartTime=datetime.utcnow() - timedelta(minutes=15),
                EndTime=datetime.utcnow(),
                Period=300,
                Statistics=['Average']
            )
            
            datapoints = metrics['Datapoints']
            
            if datapoints:
                avg_cpu = datapoints[-1]['Average']
                print(f"{instance_id} CPU: {avg_cpu}")
                
                # STEP 3: CHECK IF IDLE
                if avg_cpu < 5:
                    print(f"{instance_id} is IDLE → Stopping...")
                    
                    # STEP 4: STOP INSTANCE
                    ec2.stop_instances(InstanceIds=[instance_id])
                    stopped_instances.append(instance_id)
                else:
                    print(f"{instance_id} is ACTIVE → Skipping")
    
    # STEP 5: COST SAVINGS ESTIMATION
    # t2.micro ≈ $0.0116/hour
    estimated_savings = len(stopped_instances) * 0.0116 * 24
    
    # STEP 6: DAILY SUMMARY EMAIL
    message = f"""
Daily EC2 Cost Optimization Report

Total Instances Checked: {checked_instances}
Idle Instances Stopped: {len(stopped_instances)}

Estimated Savings (24h): ${estimated_savings:.2f}

Stopped Instance IDs:
{chr(10).join(stopped_instances) if stopped_instances else "None"}

Time (UTC): {datetime.utcnow()}
"""
    
    # Send email
    sns.publish(
        TopicArn='YOUR_SNS_TOPIC_ARN',
        Message=message,
        Subject='Daily EC2 Cost Optimization Report'
    )
    
    return {
        'statusCode': 200,
        'body': {
            'checked_instances': checked_instances,
            'stopped_instances': stopped_instances,
            'estimated_savings': estimated_savings
        }
    }
