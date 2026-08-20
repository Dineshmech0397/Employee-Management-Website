📌 Project Overview

The AWS Employee Management System is a cloud-based full-stack web application developed to demonstrate the deployment of a modern three-tier architecture on Amazon Web Services (AWS). The application enables users to perform complete employee management operations, including creating, viewing, updating, and deleting employee records.

The project follows DevOps best practices by containerizing the application using Docker, automating deployments with Jenkins CI/CD, storing container images in Amazon ECR, deploying containers on Amazon ECS Fargate, and using Amazon RDS MySQL as the backend database. An Application Load Balancer (ALB) is used to provide reliable access to the backend service.

🚀 Features

1.Employee Management (CRUD Operations)
2.Add Employee
3.View Employee List
4.Update Employee Details
5.Delete Employee
6.Responsive React Frontend
7.REST API using Flask
8.MySQL Database on Amazon RDS
9.Docker Containerization
10.CI/CD using Jenkins
11.Automated Deployment to Amazon ECS
12.Container Images Stored in Amazon ECR
13.Backend Routing through Application Load Balancer (ALB)


🛠️ Technology Stack

Frontend

1.React.js
2.HTML
3.CSS
4.JavaScript

Backend

1.Python
2.Flask
3.Gunicorn

Database

1.Amazon RDS (MySQL)
DevOps Tools

1.Docker
2.Docker Compose
3.Jenkins
4.Git
5.GitHub

AWS Services

1.Amazon EC2
2.Amazon ECS (Fargate)
3.Amazon ECR
4.Amazon RDS
5.Application Load Balancer (ALB)
6.IAM
7.VPC
8.Security Groups


🏗️ AWS Architecture

                Internet
                    │
                    ▼
        React Frontend (Amazon ECS)
                    │
                    ▼
        Application Load Balancer
                    │
                    ▼
       Flask Backend (Amazon ECS)
                    │
                    ▼
         Amazon RDS (MySQL Database)


🔄 CI/CD Pipeline

Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Webhook
    │
    ▼
Jenkins Pipeline
    │
    ├── Build Backend Docker Image
    ├── Build Frontend Docker Image
    ├── Push Images to Amazon ECR
    └── Force New Deployment in Amazon ECS
                    │
                    ▼
Updated Application Available


📂 Project Structure

aws-employee-management-system/
│
├── backend/
│   ├── application.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── Dockerfile
│
├── database/
│   └── init.sql
│
├── jenkins/
│   └── Dockerfile
│
├── docker-compose.yml
├── docker-compose.jenkins.yml
├── Jenkinsfile
├── Jenkinsfile-ECR
└── README.md


⚙️ Deployment Workflow

1.Developer pushes source code to GitHub.

2.GitHub Webhook triggers the Jenkins pipeline.

3.Jenkins checks out the latest code.

4.Backend and frontend Docker images are built.

5.Images are pushed to Amazon ECR.

6.Jenkins triggers a new deployment for Amazon ECS services.

7.ECS pulls the latest images from ECR.

8.The backend connects to Amazon RDS.

9.Users access the application through the frontend, while backend requests are routed through the Application Load Balancer.



📸 Project Screenshots

1.Include the following screenshots in this section:

2.Home Page

3.Employee List

4.Add Employee

5.Edit Employee

6.Delete Employee

7.Jenkins Pipeline Success

8.Amazon ECS Services

9.Amazon ECR Repositories

10.Amazon RDS Database

11.Application Load Balancer

12.GitHub Repository



💡 Challenges Faced

1.Configuring Docker networking between containers.

2.Connecting the backend to Amazon RDS.

3.Resolving CORS issues between frontend and backend.

4.Configuring Amazon ECS task definitions and services.

5.Integrating Jenkins with GitHub Webhooks.

6.Automating Docker image deployment to Amazon ECR.

7.Updating Amazon ECS services automatically after image pushes.

8.Configuring the Application Load Balancer for backend routing.



⭐ Conclusion

This project demonstrates an end-to-end cloud-native application deployment using AWS services and DevOps practices. It showcases containerization, continuous integration, continuous deployment, cloud database integration, load balancing, and automated application delivery using Jenkins, Amazon ECR, Amazon ECS, Amazon RDS, and an Application Load Balancer.
# Employee-Management-Website
