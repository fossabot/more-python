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
                sh 'whereis bash; whereis sh; whereis zsh'
                // sh 'ci_env=`bash <(curl -s https://codecov.io/env)`'
                // sh 'bash <(curl -s https://codecov.io/bash)'
            }
        }
    }
}