<div align="center">

![HTML](https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![AWS Lambda](https://img.shields.io/badge/AWS%20Lambda-FF9900?style=for-the-badge&logo=awslambda&logoColor=white)
![API Gateway](https://img.shields.io/badge/API%20Gateway-FF4F00?style=for-the-badge&logo=amazonapigateway&logoColor=white)
![Amazon DynamoDB](https://img.shields.io/badge/Amazon%20DynamoDB-4053D6?style=for-the-badge&logo=amazondynamodb&logoColor=white)
![Amazon S3](https://img.shields.io/badge/Amazon%20S3-569A31?style=for-the-badge&logo=amazons3&logoColor=white)

</div>




# 💼 Job Application Recruiter Portal – Serverless Web Application Using AWS

A fully serverless job application platform that enables applicants to submit their details and resumes, and allows recruiters to securely and efficiently view submitted applications. Built entirely using AWS services, the system is designed to run securely, scalably, and cost-effectively — even at zero cost within the AWS Free Tier.

---

# 🛠️ Tech Stack

<div align="center">


| Layer        | Technology                           |
| ------------ | ------------------------------------ |
| Frontend     | HTML, CSS (Hosted on S3)             |
| Backend      | AWS Lambda (Python), API Gateway     |
| Database     | Amazon DynamoDB                      |
| File Storage | Amazon S3                            |

</div>

---
 
# ✨ Key Features

  + 📄 Applicants can submit personal information and upload resumes

  + ☁️ Resumes are securely stored in Amazon S3

  + 🧾 Application metadata is saved in Amazon DynamoDB

  + 🔍 Recruiters can view all applications through a protected portal

  + ⚡ Serverless architecture ensures high scalability and low cost

---
     
# 🧱 Architecture Diagram

![job-recruiter](https://github.com/user-attachments/assets/1e4c3919-da4b-4060-9e93-ac46ffaa1fb7)

---

# 📝 How It Works

## 👤 Applicant Workflow 📥

**1.  User fills out an online form and uploads a resume.**

**2.  Form sends a POST request to an API Gateway endpoint.**

**3.  An AWS Lambda function:**

   + Uploads the resume to S3

   + Stores user data (name, email, position, etc.) in DynamoDB

## 📸 Screenshots

![job3](https://github.com/user-attachments/assets/23b5abca-626d-4957-b271-a91fbf969700)

![job2](https://github.com/user-attachments/assets/52cd16c0-1749-4446-a3f2-41c2e176e87f)



## 👥 Recruiter Workflow 📥

**1. Recruiter accesses a protected HTML portal.**

**2. A GET request is sent to a separate API Gateway endpoint.**

**3. A Lambda function:**

  +  Fetches application records from DynamoDB

  +  Generates public S3 links for the resumes

## 📸 Screenshot

![upscalemedia-transformed (2)](https://github.com/user-attachments/assets/88f5f8e1-431f-44b4-9931-9b5bb3c4f5a5)

---

# 🚀 Deployment Steps

**1.🔧 Backend Deployment (Lambda Functions)**

+ Deploy using:

     +  AWS Console, SAM, or Serverless Framework

+ Set required IAM roles and permissions for:

     +  S3 access

     +  DynamoDB access

**2.🌐 Frontend Hosting (Static Website)**

+  Upload HTML, CSS, and JS files to Amazon S3

+  Enable static website hosting on the S3 bucket

---
# 🗂️ Suggested Project Structure

```
job-application-portal/
│
├── Job_Applicants_Code/
│   ├── Applicants-Lambda-Code.py    # 📤 Lambda: Submit applicant data to backend
│   ├── index.html                   # 🌐 Applicant portal UI
│   ├── error.html                   # 🚫 Applicant error page (if any)
│   └── sample-postman.json          # 📬 Postman sample for testing API
│
├── Recruiter_Portal_Code/
│   ├── recruiter-lambda-code.py     # 📥 Lambda: Fetch applicant data for recruiters
│   ├── recruiter.html               # 🌐 Recruiter portal UI
│   └── recruiter.css                # 🎨 Recruiter UI styles
│
├── Bucket_Policy.txt               # 📂 S3 bucket policy configuration
└── README.md                       # 📘 Project overview & setup instructions

```
---

___Give it a ⭐️ if you found it useful!___    

---

# </> with ♡ by Niharika B  

📞 **Connect With Me – Gayatri G**

📧 Email: [niharika.bandaru5002@gmail.com](mailto:niharika.bandaru5002@gmail.com)  
💼 LinkedIn: [linkedin.com/in/niharika-bandaru](https://www.linkedin.com/in/niharika-bandaru/)  
💻 GitHub: [github.com/Niharika07-B](https://github.com/Niharika07-B)


---

# 💬 **Let’s Connect!**  
For queries, collaborations, or feedback, feel free to reach out via GitHub or LinkedIn.
































