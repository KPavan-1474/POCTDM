pipeline{
  agent any
  stages{
    stage('version'){
        steps{
          sh 'python3 --version'
        }
    }
    stage('main_cla'){
      steps{
        sh 'python3 main_cla.py'
        }
    }
  }
}