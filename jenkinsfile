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
                sh 'bash -c "bash <(curl -s https://codecov.io/bash) -t ${$CODECOV_TOKEN}"'
            }
        }
    }
}