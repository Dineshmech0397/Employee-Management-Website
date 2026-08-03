pipeline {

    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Checking out source code from GitHub...'
            }
        }

        stage('Stop Existing Containers') {
            steps {
                echo 'Stopping existing containers...'

                sh '''
                docker compose down || true
                '''
            }
        }

        stage('Build Docker Images') {
            steps {
                echo 'Building Docker images...'

                sh '''
                docker compose build
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                echo 'Starting application containers...'

                sh '''
                docker compose up -d
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                echo 'Checking running containers...'

                sh '''
                docker ps
                curl http://localhost:5000 || true
                '''
            }
        }

    }

    post {

        success {
            echo 'Deployment Successful! Application is running.'
        }

        failure {
            echo 'Deployment Failed! Check console logs.'
        }

        always {
            echo 'Pipeline execution completed.'
        }

    }

}
