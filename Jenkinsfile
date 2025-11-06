pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/Ani011104/FastAPI-Docker-jenkins-CICDpipline.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                docker build -t fastapi-app .
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                docker run --rm fastapi-app pytest -q
                """
            }
        }

        stage('Delivery (Skip for now)') {
            steps {
                echo "Delivery step will be added once deployment environment is ready."
            }
        }
    }
}
