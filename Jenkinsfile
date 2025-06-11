pipeline {
    agent any

    environment {
        // ✅ MODIFIED: Correct Docker Hub username
        IMAGE_NAME = 'darshanpchouthayi/inventory-management'
        IMAGE_TAG = 'latest'
        DOCKER_CREDENTIALS_ID = 'dockerhub-creds'

        // ✅ ADDED: PythonAnywhere config
        PYTHONANYWHERE_API_CRED = 'pythonanywhere-token'        // secret text: token
        PYTHONANYWHERE_LOGIN_CRED = 'pythonanywhere-creds'      // username + password
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
        // --- Test Stage was removed ---
        */

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
                    withCredentials([
                        string(credentialsId: "${PYTHONANYWHERE_API_CRED}", variable: 'PA_API_TOKEN'),
                        usernamePassword(credentialsId: "${PYTHONANYWHERE_LOGIN_CRED}", usernameVariable: 'PA_USER', passwordVariable: 'PA_PASS')
                    ]) {
                        bat """
                            curl -X POST https://www.pythonanywhere.com/api/v0/user/${PA_USER}/webapps/${PA_USER}.pythonanywhere.com/reload/ ^
                            -H "Authorization: Token ${PA_API_TOKEN}"
                        """
                    }
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
            echo '✅ Pipeline completed successfully.'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}
