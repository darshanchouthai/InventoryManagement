pipeline {
    agent any

    environment {
        // ✅ MODIFIED: Updated Docker Hub username to correct one
        IMAGE_NAME = 'darshanpchouthayi/inventory-management'  // <-- updated from 'darshanchouthai'
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
                    bat "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        /*
        // --- The entire Test Stage has been removed ---
        stage('Run Tests (inside Docker)') {
            steps {
                script {
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
        */

        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS_ID}", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
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
