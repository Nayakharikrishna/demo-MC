
pipeline {
    agent any

    stages {
        stage('Code Checkout') {
            steps {
                echo 'Starting Code Checkout...'
                checkout scm
                echo 'Code Checkout Successful!'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Starting Docker Build...'
                sh 'docker build -t python-app:${BUILD_NUMBER} .'
                echo 'Docker Image Build Successful!'
            }
        }

        stage('Docker Run') {
            steps {
                echo 'Starting Docker Container...'
                sh 'docker stop python-app || true'
                sh 'docker rm python-app || true'
                sh 'docker run -d --name python-app -p 80:5000 python-app:${BUILD_NUMBER}'
                echo 'Docker Container Started Successfully!'
            }
        }
    }

    post {
        success {
            echo '========================================'
            echo 'SUCCESS: Pipeline executed successfully!'
            echo 'Application deployed successfully!'
            echo '========================================'
        }

        failure {
            echo '========================================'
            echo 'FAILURE: Pipeline execution failed!'
            echo 'Check Console Output for errors.'
            echo '========================================'
        }

        unstable {
            echo 'WARNING: Pipeline execution is unstable!'
        }

        aborted {
            echo 'Pipeline execution was aborted!'
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}
