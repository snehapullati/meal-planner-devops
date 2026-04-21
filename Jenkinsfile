pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t meal-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop meal-container || true'
                sh 'docker rm meal-container || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name meal-container meal-app'
            }
        }
    }
}