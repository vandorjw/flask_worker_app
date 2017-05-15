node {

    currentBuild.result = "SUCCESS"

    try {
       stage('Checkout'){
            checkout scm
       }
       stage('Build Docker'){
            sh 'cd flask'
            sh 'docker build .'
            sh 'docker image ls'
       }
       stage('Archive Build') {
            echo 'Archiving Build'
       }
       stage('Deploy') {
            echo 'Deploy to remote host'
       }
    }
    catch (err) {
        currentBuild.result = "FAILURE"
        throw err
    }
}
