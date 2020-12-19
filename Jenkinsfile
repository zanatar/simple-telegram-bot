pipeline {
  agent {
    node {
      label 'Slave_1'
      }
    }
  stages {
    //stage ('root priveleges'){
      //steps {
        // sh 'chown root:jenkins /run/docker.sock'
      //}
    //}
    stage ('build') {
//      agent {
//       node {
//          checkout scm
//          docker.image('zanatar/telegram').withRun(-p 8888:80') { c ->
//          sh 'curl https://api.telegram.org/bot1060484360:AAEjYmNL-qcz1ngqOksgRFAV_rq6AHZCuvo/sendMessage?chat_id=-1001134991563&text=I%20am%20alive!'
//            }
//          }
//      }
      steps{
        script{
          try {
            sh 'docker run --name=telegram -d -p 8888:80 zanatar/telegram'
            }
            catch(err){
            sh 'docker stop telegram'
            sh 'docker rm telegram'
            sh 'docker run --name=telegram -d -p 8888:80 zanatar/telegram'
            }
          }
      }
    }
    stage('test') {
      steps{
        sh 'curl 127.0.0.1:8888?message=I%20am%20alive!'
      }
    }
  }
}
