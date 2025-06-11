pipeline {
    agent any

    environment {
        IMAGE_NAME = 'darshanpchouthayi/inventory-management'
        IMAGE_TAG = 'latest'
        DOCKER_CREDENTIALS_ID = 'dockerhub-creds'

        PYTHONANYWHERE_CICD_URL = 'https://invmgmt.pythonanywhere.com/pull_and_reload'
        PYTHONANYWHERE_CICD_TOKEN = credentials('pythonanywhere-cicd-token') // Jenkins secret text
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

        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(
                        credentialsId: "${DOCKER_CREDENTIALS_ID}",
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )]) {
                        bat """
                            echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin
                            docker push ${IMAGE_NAME}:${IMAGE_TAG}
                        """
                    }
                }
            }
        }

        stage('Deploy to PythonAnywhere') {
            steps {
                script {
                    bat """
                        curl -X POST ${PYTHONANYWHERE_CICD_URL} ^
                        -H "X-Auth-Token: ${PYTHONANYWHERE_CICD_TOKEN}"
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning workspace...'
            cleanWs()
        }
        success {
            echo '✅ CI/CD pipeline completed successfully.'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
} 