pipeline {
    agent any

    stages{
        stage('Build Docker Image'){
            steps{
                sh 'docker build -t mock-api:latest .'
            }
        }

        stage('Run Pytest'){
            sh 'docker run --rm mock-api:latest python -m pytest -q'
        }
    }
}