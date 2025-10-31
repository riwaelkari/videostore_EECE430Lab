pipeline {
    agent any

    triggers {
        // Poll GitHub every 2 minutes for changes
        pollSCM('H/2 * * * *')
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Checking out source code from GitHub..."
                git branch: 'master', url: 'https://github.com/riwaelkari/videostore_EECE430Lab.git'
            }
        }

        stage('Build in Minikube Docker') {
            steps {
                bat '''
                echo === Switching Docker to Minikube Docker ===
                call minikube docker-env --shell=cmd > docker_env.bat
                call docker_env.bat

                echo === Building Docker image inside Minikube ===
                docker build -t my-django-app:latest .
                '''
            }
        }

        stage('Deploy to Minikube') {
            steps {
                bat '''
                echo === Setting Kubernetes environment ===
                set KUBECONFIG=C:\\SPB_Data\\.minikube\\profiles\\minikube\\config
                set MINIKUBE_HOME=C:\\SPB_Data\\.minikube

                echo === Applying Kubernetes manifests ===
                kubectl apply -f deployment.yaml --validate=false
                kubectl apply -f service.yaml --validate=false

                echo === Waiting for rollout to complete ===
                kubectl rollout status deployment/videostore-deployment
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                bat '''
                echo === Verifying Minikube deployment ===
                kubectl get pods
                kubectl get svc
                '''
            }
        }
    }
}
