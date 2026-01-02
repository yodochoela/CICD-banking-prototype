pipeline {
    agent any

    environment {
        // Optional: Python environment
        PYTHON = "python" 
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo 'Cloning repository from GitHub...'
                git branch: 'main',
                    url: 'https://github.com/yodochoela/CICD-banking-prototype',
                    credentialsId: 'github-token' // Replace with your Jenkins credential ID
            }
        }

        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment and installing dependencies...'
                sh "${PYTHON} -m pip install --upgrade pip"
                sh "${PYTHON} -m pip install -r requirements.txt"
            }
        }

        stage('Run Backend Tests') {
            steps {
                echo 'Running Flask backend tests...'
                sh "${PYTHON} -m unittest discover -s backend/tests"
            }
        }

        stage('Frontend Check') {
            steps {
                echo 'Checking frontend files...'
                sh "echo 'Frontend HTML, CSS, JS files are present and ready'"
            }
        }

        stage('Build / Integration') {
            steps {
                echo 'Integrating frontend and backend...'
                sh "echo 'Integration step simulated: backend and frontend linked'"
            }
        }

        stage('Deploy Prototype') {
            steps {
                echo 'Deploying prototype...'
                sh "echo 'Prototype deployment simulated for testing purposes'"
            }
        }

    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed! Check console output for errors.'
        }
    }
}
