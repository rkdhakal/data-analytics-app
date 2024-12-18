pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Install Python dependencies
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                // Run unit tests using pytest
                sh '''export PYTHONPATH=$PYTHONPATH:$PWD/src
                      pytest'''
            }
        }

        stage('Docker Build') {
            steps {
                // Build a Docker image
                sh 'docker build -t data-analytics-app .'
            }
        }

        stage('Deploy to Minikube') {
            steps {
                // Deploy to Kubernetes cluster using kubectl
                sh 'kubectl apply -f k8s/deployment.yaml'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
