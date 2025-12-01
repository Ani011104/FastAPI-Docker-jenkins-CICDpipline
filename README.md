# 🚀 FastAPI Task Manager

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Jenkins](https://img.shields.io/badge/jenkins-%232C5263.svg?style=for-the-badge&logo=jenkins&logoColor=white)

A robust, containerized Task Manager application built with **FastAPI**, designed for high performance and scalability. This project demonstrates a complete CI/CD workflow using **Jenkins** and **Docker**, ensuring automated testing and seamless deployment.

---

## ✨ Features

- **Create Tasks**: Add new tasks with ease.
- **View Tasks**: Retrieve a list of all managed tasks.
- **Delete Tasks**: Remove tasks that are no longer needed.
- **Containerized**: Fully Dockerized for consistent environments.
- **Automated Testing**: Integrated with Jenkins for automated pipeline execution.

---

## 🛠️ Tech Stack

- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Language**: Python 3.12
- **Containerization**: Docker
- **CI/CD**: Jenkins
- **Testing**: pytest

---

## 📂 Project Structure

```
.
├── app
│   ├── controllers
│   ├── database
│   ├── models
│   ├── routes
│   │   └── task_routes.py
│   └── main.py
├── tests
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) installed on your machine.
- [Git](https://git-scm.com/) for cloning the repository.

### Installation & Running

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/Ani011104/FastAPI-Docker-jenkins-CICDpipline.git
    cd FastAPI-Docker-jenkins-CICDpipline
    ```

2.  **Build the Docker Image**

    ```bash
    docker build -t fastapi-app .
    ```

3.  **Run the Container**

    ```bash
    docker run -d -p 8000:8000 fastapi-app
    ```

    The API will be available at `http://localhost:8000`.

4.  **Explore the API**

    Visit the interactive API documentation at:
    - Swagger UI: `http://localhost:8000/docs`
    - ReDoc: `http://localhost:8000/redoc`

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/tasks` | Create a new task |
| `GET` | `/tasks` | Retrieve all tasks |
| `DELETE` | `/tasks/{task_id}` | Delete a specific task |

---

## 🔄 CI/CD Pipeline

This project uses a **Jenkins** pipeline defined in `Jenkinsfile` to automate the development workflow.

### Pipeline Stages

1.  **Checkout**: Pulls the latest code from the repository.
2.  **Build Docker Image**: Builds the Docker image for the application.
3.  **Run Tests**: Runs `pytest` inside the container to ensure code quality.
4.  **Delivery**: (Placeholder) Prepares for deployment.

