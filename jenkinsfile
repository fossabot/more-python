pipeline {
    agent {
        docker { image 'kennethreitz/pipenv'}
    }
    environment {
        CODECOV_TOKEN = credentials('CODECOV_TOKEN')
    }
    stages {
        stage('Test') {
            steps {
                sh 'pip install --user codecov'
                sh 'codecov --token=$CODECOV_TOKEN'
            }
        }
    }
}