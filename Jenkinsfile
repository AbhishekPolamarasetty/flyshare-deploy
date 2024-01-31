pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
               checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/AbhishekPolamarasetty/flyshare_project1.git']])
            }
        }
        stage('Build'){
            steps{
                sh 'docker build -t abhishekpola/flyshare1 .'
            }
        }
  
        stage('push'){
            steps{
                withCredentials([usernamePassword(credentialsId: 'f5e5b886-4d15-482f-bb92-8dc7d946854d', passwordVariable: 'DOCKER_HUB_PASSWORD', usernameVariable: 'DOCKER_HUB_USERNAME')]) {
    // some block
                   sh 'echo $DOCKER_HUB_PASSWORD | docker login -u $DOCKER_HUB_USERNAME --password-stdin'
                   sh 'docker push abhishekpola/flyshare1'
         
                }
            }
        }
        stage('deploy') {
            steps {
                
                sh 'docker run -d -p 5000:5000 --name demo-container abhishekpola/flyshare1'
            }
        }
    }
}
