pipeline {
    agent any

    stages {
        stage('Checkout') {
            // the first stage will be to integrate jenkins with github
            // the code has to be run in Pipeline Mode, and under Pipeline
            // Defination: Pipeline script from SCM
            // SCM: Git
            steps {
                echo 'Welcome to PyJenkins Demonstration'
                checkout changelog: false, poll: false, scm: [$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'ZenithClown', url: 'git@github.com:ZenithClown/hello-jenkins.git']]]
            }
        }

        stage('Build') {
            // TODO - understand freestyle job vs pipeline job syntax
            // ? URL and Credentials for connecting to github (remote) repository is inserted twice
            git changelog: false, credentialsId: 'ZenithClown', poll: false, url: 'git@github.com:ZenithClown/hello-jenkins.git'
            // ! Pipeline script > Step = bat: Windows Batch Script > Script = python <filename>.py
            bat 'python main.py'
        }

        stage('completion') {
            echo 'pipeline executed succesfully'
        }
    }
}
