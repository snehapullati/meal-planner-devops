pipeline {
    agent any

    stages {

        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build -t meal-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker stop meal-container || true'
                sh 'docker rm meal-container || true'
                sh 'docker run -d -p 5000:5000 --name meal-container meal-app'
            }
        }
    }
}