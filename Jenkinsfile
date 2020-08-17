pipeline {
    agent {label 'master'}
    stages {
		stage('Deploy Dev') {
		    when {expression { env.BRANCH_NAME ==~ /^(dev|hotfix|bugfix|feature|stagging|release|deploy)(.*)?/ }}
                agent {label 'NodeJS-Java-Agent'}
                steps { 
				    sh '''
                    #!/bin/bash
                    echo 'testing'
                    '''
				}
		}
	}
}
