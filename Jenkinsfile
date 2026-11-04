
pipeline {
    agent "demo"

    stages {
        stage('Code Checkout') {
            steps {
                echo 'Jenkinsfile loaded from GitHub'
                checkout scm
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t python-app:${BUILD_NUMBER} .'
            }
        }

        stage('Docker Run') {
            steps {
                sh 'docker stop python-app || true'
                sh 'docker rm python-app || true'
                sh 'docker run -d --name python-app -p 80:5000 python-app:${BUILD_NUMBER}'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed'
        }
    }
}
