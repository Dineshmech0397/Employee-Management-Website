pipeline {

    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Checking out source code from GitHub'
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


        stage('Stop Existing Containers') {
            steps {
                echo 'Stopping existing containers...'

                sh '''
                docker compose down
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

    }

}
