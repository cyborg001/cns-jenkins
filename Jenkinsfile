pipeline {
    agent { docker { image 'python:3.10.4' } }
    stages {
        stage('build') {
            steps {
                bat 'runserver.bat'
            }
        }
    }
}