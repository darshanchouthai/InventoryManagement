pipeline {
    agent any

    environment {
        IMAGE_NAME = 'darshanchouthai/inventory-management'
        IMAGE_TAG = 'latest'
        DOCKER_CREDENTIALS_ID = 'dockerhub-creds'  // Create this in Jenkins Credentials
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/darshanchouthai/InventoryManagement.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }

        stage('Run Tests (inside Docker)') {
            steps {
                script {
                    docker.image("${IMAGE_NAME}:${IMAGE_TAG}").inside {
                        sh 'python -m unittest discover -s tests'
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_CREDENTIALS_ID}") {
                        docker.image("${IMAGE_NAME}:${IMAGE_TAG}").push()
                    }
                }
            }
        }

        stage('Deploy (Optional)') {
            steps {
                echo 'Deploying Flask App...'
                // Example: SSH to remote server and restart container
                // sh 'ssh user@server "docker pull darshanchouthai/inventory-management && docker-compose up -d"'
            }
        }
    }

    post {
        always {
            echo 'Cleaning workspace...'
            cleanWs()
        }
        success {
            echo '✅ Pipeline completed successfully.'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}
