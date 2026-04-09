# 🚀 AWS Cost Optimization System (Serverless DevOps Project)

## 📌 Overview
This project implements an automated **AWS cost optimization system** using serverless architecture. It continuously monitors EC2 instances, identifies idle resources based on CPU utilization, and automatically stops them to reduce unnecessary cloud spending.

---

## 🧠 Architecture

EventBridge → Lambda → CloudWatch → EC2 → SNS → Email

---

## ⚙️ Key Features

- 🔍 Monitor active EC2 instances in real-time  
- 🧠 Detect idle instances (CPU Utilization < 5%)  
- 🛑 Automatically stop unused instances  
- 🔐 Tag-based filtering (Environment = Test) for safety  
- 📧 Send automated email notifications via SNS  
- 💰 Estimate daily cost savings  

---

## 🛠️ AWS Services Used

- AWS Lambda (Serverless compute)
- Amazon EC2 (Compute instances)
- Amazon CloudWatch (Monitoring & metrics)
- Amazon SNS (Notification service)
- Amazon EventBridge (Scheduling)
- IAM (Access control & permissions)

---

## 🔄 Workflow

1. EventBridge triggers the Lambda function on a schedule  
2. Lambda retrieves running EC2 instances  
3. Instances are filtered based on tags  
4. CPU utilization is analyzed using CloudWatch metrics  
5. Idle instances are automatically stopped  
6. A summary report is sent via SNS email  

---

## 📧 Sample Output

<img width="1919" height="971" alt="Screenshot 2026-04-09 161722" src="https://github.com/user-attachments/assets/89513b5f-9a3a-4f20-b044-7f001f3598d8" />
<img width="1806" height="484" alt="Screenshot 2026-04-09 161228" src="https://github.com/user-attachments/assets/968526a8-7b9b-4fd7-80c6-797662449d1a" />


## 📸 Screenshots

### 🔹 Lambda Function

<img width="1919" height="971" alt="Screenshot 2026-04-09 161722" src="https://github.com/user-attachments/assets/4655e4e8-9907-43b5-80d2-5b97f90c9a2f" />
<img width="1806" height="484" alt="Screenshot 2026-04-09 161228" src="https://github.com/user-attachments/assets/ce582998-99ac-4819-9f1a-a03918ca3736" />

### 🔹 EventBridge Trigger

<img width="1919" height="971" alt="Screenshot 2026-04-09 154224" src="https://github.com/user-attachments/assets/a08679d0-d726-4ee3-8e2a-fdf7bf7ae68f" />

### 🔹 SNS Email Alert

<img width="1806" height="484" alt="Screenshot 2026-04-09 161228" src="https://github.com/user-attachments/assets/195c864d-3437-4a4d-9b31-1dd33f53118c" />

### 🔹 EC2 Before & After

<img width="1806" height="484" alt="Screenshot 2026-04-09 161228" src="https://github.com/user-attachments/assets/94f70486-1949-432e-917c-cba295aa93e5" />
<img width="1667" height="411" alt="Screenshot 2026-04-09 154748" src="https://github.com/user-attachments/assets/dfa2e2a2-1bb7-4d09-91da-eabe34c96234" />

<img width="1919" height="654" alt="Screenshot 2026-04-09 161327" src="https://github.com/user-attachments/assets/ea4fed56-45c2-470e-a89c-131028305938" />


### 🔹 CloudWatch Logs

<img width="1919" height="827" alt="Screenshot 2026-04-09 155347" src="https://github.com/user-attachments/assets/db697d8c-499d-45a5-937e-27af9099e47a" />

---

## 💼 Real-World Use Case

In cloud environments, unused resources significantly increase costs.  
This system helps organizations:

- Automatically detect idle infrastructure  
- Reduce manual monitoring effort  
- Save cloud expenses efficiently  

---

## 🚀 Future Enhancements

- 📊 Cost monitoring dashboard (CloudWatch / Grafana)  
- 🗄️ Extend optimization to RDS and S3  
- 📩 HTML-based detailed reports  
- 🔄 CI/CD pipeline integration  
- 🏷️ Advanced tagging strategies  

---

## 🔐 Security & Best Practices

- Uses IAM roles with least privilege  
- Applies tag-based filtering to avoid accidental shutdown  
- Serverless architecture ensures scalability and cost efficiency  

---

## 👩‍💻 Author

**Charu (B.Tech IT | Cloud & DevOps Enthusiast)**  

- AWS Certified Cloud Practitioner  
- Passionate about building real-world cloud automation solutions  

---

## 🌟 Project Highlights

✔ Real-world DevOps use case  
✔ Serverless architecture  
✔ Automation-driven cost savings  
✔ Resume-ready project  

---

## ⭐ If you found this useful

Give this repository a ⭐ and feel free to fork or contribute!
