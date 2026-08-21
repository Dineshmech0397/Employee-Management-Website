# 🏢 Enterprise Employee Management System
### A Production-Grade Three-Tier DevOps & CI/CD Pipeline Architecture

---

## 📑 Table of Contents
1. [Project Overview](#-project-overview)
2. [System Architecture & Workflow](#-system-architecture--workflow)
3. [Technology Stack](#-technology-stack)
4. [Repository Directory Structure](#-repository-directory-structure)
5. [Core Technical Components](#-core-technical-components)
6. [CI/CD Automation & Webhook Integration](#-cicd-automation--webhook-integration)
7. [Step-by-Step Deployment Guide](#-step-by-step-deployment-guide)
8. [Database Management & Verification](#-database-management--verification)

---

## 1. 📌 Project Overview
The **Employee Management System** is a cloud-native, fully containerized web application designed to demonstrate a robust, real-world **DevOps lifecycle**. It allows organizations to seamlessly track employee records (such as Employee ID, Full Name, Department, Designation, Salary, and Joining Date) through an interactive web interface backed by a resilient relational database, automated reverse-proxy routing, and continuous integration/continuous deployment (CI/CD).

---

## 2. 🏗️ System Architecture & Workflow

The solution implements a strict **Three-Tier Architecture** integrated with a dedicated automation server and cloud infrastructure:

[ Developer Commit ]
│
▼ (Push to GitHub)
[ GitHub Webhook ] ──(HTTP POST)──► [ Jenkins Server (Port 8080 Container) ]
│
▼ (SSH Agent Secure Credentials)
[ AWS EC2 Instance ]
│
├─► git pull origin main
├─► docker-compose down -v
└─► docker-compose up --build -d


### End-to-End Execution Flow:
1. **Source Control:** Developers write code changes in the [Employee-Management-Website Repository](https://github.com/Dineshmech0397/Employee-Management-Website).
2. **Webhook Event:** Every `git push` event fires an HTTP POST payload to the Jenkins CI/CD automation server.
3. **Jenkins Orchestration (`Port 8080`):** Running inside an independent container, Jenkins processes the pipeline steps defined in the `Jenkinsfile`.
4. **Secure Remote Deployment:** Using SSH agent credentials, Jenkins logs into the target **AWS EC2 Ubuntu Instance**, pulls the latest version of the repository, and executes clean Docker Compose container lifecycle commands.

---

## 3. 🛠️ Technology Stack

| Layer / Domain | Technology Used | Description |
| :--- | :--- | :--- |
| **Frontend Tier** | React.js (Node.js 20) | High-performance single-page web user interface. |
| **Web Server / Proxy** | Nginx (Alpine Linux) | Serves static React bundles and proxies API requests securely. |
| **Backend Tier** | Python Flask, Gunicorn | RESTful API framework powered by production multi-workers. |
| **Database Tier** | MySQL 8.0, PyMySQL | Relational database engine with automated initialization schemas. |
| **Containerization** | Docker & Docker Compose | Multi-container networking, bridge setups, and volume persistence. |
| **CI/CD Automation** | Jenkins & GitHub Webhooks | Automated build, test, and remote container deployment pipelines. |
| **Cloud Hosting** | AWS EC2 (Ubuntu) | Production-ready cloud computing environment. |

---

## 4. 📂 Repository Directory Structure

```text
Employee-Management-Website/
├── backend/
│   ├── application.py         # Flask REST API endpoints & DB connection handlers
│   ├── requirements.txt       # Python package list (Flask, PyMySQL, Gunicorn, Flask-CORS)
│   └── Dockerfile             # Container configuration script for Flask backend
├── database/
│   └── init.sql               # Automated schema generation and table creation script
├── frontend/
│   ├── src/                   # React source code components (Form & Table modules)
│   ├── default.conf           # Custom Nginx reverse-proxy configuration rules
│   ├── Dockerfile             # Multi-stage build setup for Node.js assets & Nginx
│   └── package.json           # Node.js project dependencies & build scripts
├── Jenkinsfile                # Declarative pipeline script for CI/CD automation
├── docker-compose.yml         # Multi-container orchestration & networking configuration
└── README.md                  # Comprehensive project documentation

5. ⚙️ Core Technical Components

A. Frontend & Nginx Reverse-Proxy Integration
To eliminate the vulnerability of hardcoding volatile EC2 public IP addresses (which change upon instance reboots), the frontend uses relative paths (/employees).

* **default.conf Configuration:** Intercepts traffic destined for /employees at the Nginx layer and proxies it internally across Docker’s bridge network (3tier-network) directly to http://emp-backend:5000/employees.
* **Resilience:** Even if the cloud server public IP changes, the internal routing remains uninterrupted.

B. Backend REST API & Database Connectivity
* Built with Flask and served via a production Gunicorn WSGI application server.
* Communicates with MySQL using PyMySQL, complete with automatic exception handling and full Cross-Origin Resource Sharing (Flask-CORS) support.

C. Persistent Relational Database
* Initialized via automated SQL migration scripts (init.sql) stored in the /database directory.
* Leverages named Docker volumes (db_volume) to ensure data integrity and persistence across container restarts.

---

🚀 6. Step-by-Step Deployment Guide

**Prerequisites**
Docker and Docker Compose installed on your host machine or target EC2 instance.

**Step 1: Clone the Repository**
```bash
git clone [https://github.com/Dineshmech0397/Employee-Management-Website.git](https://github.com/Dineshmech0397/Employee-Management-Website.git)
cd Employee-Management-Website
Step 2: Build and Launch the StackExecute Docker Compose in detached mode with forced builds to instantiate the three tiers:Bashdocker-compose up --build -d
Step 3: Validate Container StatusVerify that all containers are healthy and running:Bashdocker ps
Expected Active Containers:emp-frontend (Port 80 mapped to host)emp-backend (Port 5000 mapped to host)emp-database (Port 3306 isolated internal network)🔍 7. Database Management & VerificationTo inspect, query, or verify saved employee records directly inside the MySQL database container without leaving your terminal, run:Bashdocker exec -it emp-database mysql -u root -p
