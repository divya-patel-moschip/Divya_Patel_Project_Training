pipeline {
    agent any
    stages {
        stage('List and Rename Jobs') {
            steps {
                script {
                    sh 'python3 jenkins_api.py ${job_name}'
                }
            }
        }
    }
}

