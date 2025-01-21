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
                        python3 tree.py
                        deactivate
                    """
                }
            }
        }
        stage('Send Email'){
            steps{
                emailext(
                    subject: "${env.JOB_NAME} - Build # ${env.BUILD_NUMBER}!",
                    body: "${env.JOB_NAME} - Build # ${env.BUILD_NUMBER} :\nCheck console output at ${env.BUILD_URL} to view the results.",
                    attachLog: true,
                    attachmentsPattern: 'mylog.log, requirements.txt, report.txt',
                    to: 'divya.patel@moschip.com'
                )
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'report.xml, mylog.log, requirements.txt', fingerprint: true
            junit testResults:'report.xml'
        }
    }
}

