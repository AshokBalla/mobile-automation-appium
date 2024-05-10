pipeline {
  agent any
  stages {
    stage('Validate') {
      steps { sh 'npm test' }
    }
    stage('Mobile Smoke') {
      steps { sh 'npm run test:e2e:android || true' }
    }
  }
}
