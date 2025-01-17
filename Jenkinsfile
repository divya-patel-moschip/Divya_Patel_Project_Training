pipeline {
    agent any
    stages {
        stage('List and Rename Jobs') {
            steps {
                script {
                    sh """
                        pip install jenkinsapi
                        python3 jenkins_api.py ${job_name}
                    """
                }
            }
        }
    }
}

