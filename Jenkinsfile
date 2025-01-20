pipeline {
    agent any
    stages {
        stage('List and Rename Jobs') {
            steps {
                script {
                    sh """
                        python3 -m venv myvenv
                        source myvenv/bin/activate
                        pip install -r requirements.txt
                        python3 jenkins_api.py --job ${job_name}
                        deactivate
                    """
                }
            }
        }
        stage('Send Email'){
            steps{
                emailext(
                    subject: "This is subject",
                    body: "This is body part",
                    attachLog: true,
                    attachmentsPattern: 'mylog.log, requirements.txt',
                    to: 'divya.patel@moschip.com'
                )
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'mylog.log,requirements.txt', fingerprint: true
            junit 'mylog.log'
            cleanWs()
        }
    }
}

