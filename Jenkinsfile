pipeline {
    agent {
        docker { image 'kennethreitz/pipenv'}
    }
    stages {
        stage('Test') {
            steps {
                sh 'python3 --version'
            }
        }
    }
}