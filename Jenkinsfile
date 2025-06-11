pipeline {
    // 'agent any' will pick up any available agent. Since yours is Windows,
    // the steps below must be Windows-compatible.
    agent any

    environment {
        IMAGE_NAME = 'darshanchouthai/inventory-management'
        IMAGE_TAG = 'latest'
        DOCKER_CREDENTIALS_ID = 'dockerhub-creds'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/darshanchouthai/InventoryManagement.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Changed 'sh' to 'bat' for Windows compatibility.
                    bat "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        stage('Run Tests (inside Docker)') {
            steps {
                script {
                    // Changed 'sh' to 'bat'.
                    // Replaced Unix-specific '$PWD' with the platform-agnostic Jenkins step '${pwd()}'
                    // to get the current working directory.
                    bat """
                        docker run --rm ^
                        -v "${pwd()}:/app" ^
                        -w /app ^
                        ${IMAGE_NAME}:${IMAGE_TAG} ^
                        python -m unittest discover -s tests
                    """
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS_ID}", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        // Changed 'sh' to 'bat'. The pipe '|' command works in Windows batch as well.
                        bat """
                            echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin
                            docker push ${IMAGE_NAME}:${IMAGE_TAG}
                        """
                    }
                }
            }
        }

        stage('Deploy (Optional)') {
            steps {
                echo 'Deploying Flask App...'
                // Example deployment would also need to use 'bat' if running ssh from Windows
                // bat 'ssh user@server "docker pull darshanchouthai/inventory-management && docker-compose up -d"'
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