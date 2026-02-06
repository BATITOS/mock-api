pipeline {
    agent any

    stages{
        stage('Build Docker Image'){
            steps{
                sh 'docker build -t mock-api:latest .'
            }
        }

        stage('Run Pytest'){
            steps{
                sh 'docker run --rm mock-api:latest python -m pytest -q'
            }
        }

        stage('Push to Docker Hub'){
            steps{
                withCredentials([usernamePassword(credntialsId: 'dockerhub-creds', usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')])
                sh 'echo "$DH_PASS" | docker login -u "$DH_USER" --password-stdin'
                sh 'docker tag mock-api:latest $DH_USER/mock-api:latest'
                sh 'docker push $DH_USER/mock-api:latest'
            }
        }
    }
}