pipeline {
    agent any

    stages{
        stage('Build Docker Image'){
            steps{
                sh '/usr/local/bin/docker build -t mock-api:latest .'
            }
        }
    }
}