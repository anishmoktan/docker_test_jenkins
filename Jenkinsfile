pipeline {
    agent any 
    // environment {
    //     dockerImage = ''
    //     registry = "anishmoktan/jenkins_docker"
    //     // registry = "test123"

    //     // //- update your credentials ID after creating credentials for connecting to Docker Hub
    //     registryCredential = 'dockerhub_id'
        
    // }
    
    // stages {
    //     stage('Cloning Git') {
    //         steps {
    //             checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '', url: 'https://github.com/anishmoktan/docker_test_jenkins']]])       
    //         }
    //     }
    
    // Building Docker images
    stages {
        stage('Updating python packages') {

            steps{
                sh 'sudo -u root pip3 install -r requirements.txt'

            }
        }
        stage('Testing') {

            steps{
                sh 'python3 Test.py'

            }
        }

     }

    
}