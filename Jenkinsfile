pipeline {
    agent any

    triggers {
        // Poll GitHub every 2 minutes for updates
        pollSCM('H/2 * * * *')
    }

    stages {

        stage('Checkout') {
            steps {
                echo "📦 Checking out source code from GitHub..."
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
                set MINIKUBE_HOME=C:\\SPB_Data\\.minikube
                set KUBECONFIG=C:\\Windows\\System32\\config\\systemprofile\\.kube\\config

                echo === Getting Minikube IP ===
                for /f %%A in ('minikube ip') do set MINIKUBE_IP=%%A
                echo Detected Minikube IP: %MINIKUBE_IP%

                echo === Applying Kubernetes manifests ===
                kubectl --server=https://%MINIKUBE_IP%:65473 --insecure-skip-tls-verify apply -f deployment.yaml --validate=false
                kubectl --server=https://%MINIKUBE_IP%:65473 --insecure-skip-tls-verify apply -f service.yaml --validate=false

                echo === Waiting for rollout ===
                kubectl --server=https://%MINIKUBE_IP%:65473 --insecure-skip-tls-verify rollout status deployment/videostore-deployment
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                bat '''
                echo === Verifying deployed resources ===
                kubectl get pods
                kubectl get svc
                '''
            }
        }
    }
}
