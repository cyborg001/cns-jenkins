pipeline {
    agent { docker { image 'python:3.10.4' } }
    stages {
        stage('build') {
            steps {
                bat 'python --version'
                echo 'lanzando el servidor en localhost:8000'
                bat 'runserver.bat'
            }
        }
    }
}