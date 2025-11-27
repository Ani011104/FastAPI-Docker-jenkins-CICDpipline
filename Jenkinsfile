// 
pipeline {
  agent { label 'docker' }

  options {
    skipDefaultCheckout(true)
    timestamps()
    buildDiscarder(logRotator(numToKeepStr: '10'))
  }

  stages {
    stage('Checkout') {
      steps {
        checkout([$class: 'GitSCM',
          branches: [[name: '*/main']],
          userRemoteConfigs: [[url: 'https://github.com/Ani011104/FastAPI-Docker-jenkins-CICDpipline.git']]
        ])
      }
    }

    stage('Build Docker Image') {
      steps {
        // run on the agent (jenkins user) which has docker available
        sh 'docker --version'
        sh 'pwd; ls -la'
        sh 'docker build --no-cache -t fastapi-app .'
      }
    }

    stage('Run Tests') {
      steps {
        // run tests inside the built image
        sh 'docker run --rm fastapi-app pytest -q'
      }
    }

    stage('Delivery (skip)') {
      steps {
        echo 'Delivery step will be added once deployment environment is ready.'
      }
    }
  }

  post {
    always {
      sh 'docker images --format "{{.Repository}}:{{.Tag}} {{.ID}}"' // quick audit
    }
    success {
      echo 'Pipeline succeeded.'
    }
    failure {
      echo 'Pipeline failed — check console output for the failing stage.'
    }
  }
}
