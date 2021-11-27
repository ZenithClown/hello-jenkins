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
            steps {
                // ? URL and Credentials for connecting to github (remote) repository is inserted twice
                git changelog: false, credentialsId: 'ZenithClown', poll: false, url: 'git@github.com:ZenithClown/hello-jenkins.git'
                // * use `bat` when host machine in windows
                // ! Pipeline script > Step = bat: Windows Batch Script > Script = python <filename>.py
                // bat 'python main.py'
                // * use `sh` when host machine is linux
                // ! Pipeline script > Step = sh: Shell Script > Script = python <filename>.py
                // ! linux mint 20.2 py3 can be accessed via `python3 <filename>.py`
                // TODO - understand how to point to a python environment using jenkins
                // * Possible Solution: https://stackoverflow.com/questions/41246161
                sh 'python3 main.py'
            }
        }

        stage('completion') {
            steps {
                echo 'pipeline executed succesfully'
            }
        }
    }
}
