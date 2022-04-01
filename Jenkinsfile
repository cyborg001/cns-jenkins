pipeline {
    agent { docker { image 'python:3.10.4' } }
    stages {
        stage('Build') {
            steps {
                echo 'building'
                bat 'python3 manage.py runserver'
            }
        }
    }
}