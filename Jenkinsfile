
pipeline {
    agent any
   
    stages {
        stage('Code Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/adarsh0331/Project_03_CICD_Python_Docker.git'
                echo 'Checked out code from Git'
            }
        }
       
        stage('Docker Build') {
            steps {
                echo 'Building Docker image'
                sh 'docker build -t python-app:${BUILD_NUMBER} .'
            }
        }
        stage('Docker Run') {
            steps {
                echo 'Deploying container'
                sh 'docker stop python-app || true'
                sh 'docker rm python-app || true'
                sh 'docker run -d --name python-app -p 80:80 python-app:${BUILD_NUMBER}'
            }
        }
    }
    post {
        always {
            echo 'Cleaning up'
            // Optional cleanup steps
        }
    }
}
