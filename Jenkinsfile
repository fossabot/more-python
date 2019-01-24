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
                sh 'bash <(curl -s https://codecov.io/env) --token=$CODECOV_TOKEN'
            }
        }
    }
}