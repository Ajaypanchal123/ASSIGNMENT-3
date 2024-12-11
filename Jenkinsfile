pipeline {
    agent any
    environment {
        AZURE_CLIENT_ID = credentials('azure-client-id')
        AZURE_CLIENT_SECRET = credentials('azure-client-secret')
        AZURE_TENANT_ID = credentials('azure-tenant-id')
        RESOURCE_GROUP = 'your-resource-group'
        FUNCTION_APP_NAME = 'your-function-app-name'
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building the Python Azure Function...'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'pytest tests/'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying Azure Function...'
                sh """
                    az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID
                    func azure functionapp publish $FUNCTION_APP_NAME
                """
            }
        }
    }
}
