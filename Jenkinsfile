pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'building'
                bat 'python3 manage.py runserver'
            }
        }
    }
}