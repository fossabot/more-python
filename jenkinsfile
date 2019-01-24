pipeline {
    agent {
        dockerfile true
    }
    environment {
        CODECOV_TOKEN = credentials('CODECOV_TOKEN')
    }
    stages {
        stage('Test') {
            steps {
                sh 'coverage run tests.py'
                sh 'codecov --token=$CODECOV_TOKEN'
            }
        }
    }
}