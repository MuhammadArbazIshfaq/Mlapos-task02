pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    echo 'Cloning the repository...'
                    git 'https://github.com/MuhammadArbazIshfaq/Mlapos-task02.git'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    sh 'pip install -r requirements.txt' // Adjust this based on your project structure
                }
            }
        }

        stage('Execute test.py') {
            steps {
                script {
                    echo 'Executing test.py...'
                    sh 'python test.py' // Adjust this based on your project structure
                }
            }
        }

        stage('Deploying') {
            steps {
                script {
                    echo 'Checking out the branch...'
                    def branchName = sh(script: 'git rev-parse --abbrev-ref HEAD', returnStdout: true).trim()
                    echo "Branch Name: ${branchName}"

                    if (branchName == 'main') {
                        echo 'Deploying to production'
                        // Add production deployment steps here
                    } else {
                        echo 'Deploying to UAT'
                        // Add UAT deployment steps here
                    }
                }
            }
        }
    }
}
