pipeline {
    agent any 
    stages {
    stage('clone'){
            steps{
                    sh 'sudo rm -rf  /var/lib/jenkins/workspace/gitappv1/clone/*'
                    sh 'sudo rm -rf  /var/lib/jenkins/workspace/gitappv1/clone/.git'
                    sh 'sudo rm -rf  /var/lib/jenkins/workspace/gitappv1/clone/.env'
                    sh 'sudo git clone https://github.com/yoyothan22/gitapp /var/lib/jenkins/workspace/gitappv1/clone'
            }        

       
        }
        stage('pip') { 
            steps {
                
               sh 'pip install python-dotenv'
               sh 'python3 -m venv env'
            }
        }
        stage('apptest') { 
            steps {
               
                sh 'cd /var/lib/jenkins/workspace/gitappv1/clone'
                sh 'python3 /var/lib/jenkins/workspace/gitappv1/clone/gitapp.py'
            }
        }
         stage('deploy') { 
            steps {
                sh 'sudo docker build -t gitapp:v1  /home/yonathane/project'
                sh 'sudo docker container run -p 80:80  gitapp:v1    /bin/bash'
            }
        }
       

    stage('Push') {
        steps {
            sh '''
            
            cd /var/lib/jenkins/workspace/gitappv1/clone
           
            ssh -T git@github.com

            '''
    }
}

}
        
}    
    
