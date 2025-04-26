pipeline {
    agent any
    environment {
        IMAGE_NAME = "apettit3/swe645-ec"
        DOCKER_CREDS = credentials('docker-password')
    }
    stages {
        stage("Build and Push Docker Image") {
            steps {
                script {
                    sh "docker login -u apettit3 -p ${DOCKER_CREDS_PSW}"
                    sh "docker build -t ${IMAGE_NAME}:${env.BUILD_ID} ."
                    sh "docker push ${IMAGE_NAME}:${env.BUILD_ID}"
                }
            }
        }
        stage("Deploy to Kubernetes") {
            steps {
                script {
                    withKubeConfig([credentialsId: 'kubeconfig']) {
                        sh "kubectl set image deployment/swe645-hw2 container-0=${IMAGE_NAME}:${env.BUILD_ID} -n default"
                    }
                }
            }
        }
    }
}