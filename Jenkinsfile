pipeline {
  agent any
  stages {
    stage('Source') { steps { checkout scm } }
    stage('Build')  { steps { echo 'Compilando...' } }
    stage('Test')   { steps { echo 'Ejecutando pruebas...' } }
    stage('Deploy') { steps { echo 'Desplegando...' } }
  }
}
