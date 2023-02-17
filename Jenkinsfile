pipeline {
    agent any 
    stages {
    stage('clone'){
            steps{
                    sh 'sudo rm -rf  /var/lib/jenkins/workspace/gitapp/clone/*'
                    sh 'sudo rm -rf  /var/lib/jenkins/workspace/gitapp/clone/.git'
                    sh 'sudo rm -rf  /var/lib/jenkins/workspace/gitapp/clone/.env'
                    sh 'sudo git clone https://github.com/yoyothan22/gitapp /var/lib/jenkins/workspace/gitapp/clone'
            }        

       
        }
        stage('pip') { 
            steps {
              
               sh 'sudo apt install python3-pip'
               sh 'pip3 install python-dotenv'
               sh 'sudo python3 -m venv env'
              
                
            }
        }
        stage('apptest') { 
            steps {
               
                sh 'cd /var/lib/jenkins/workspace/gitapp/clone'
                sh 'sudo python3 gitapp.py'
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
            
            cd /var/lib/jenkins/workspace/gitapp/clone
            sudo touch jenk.txt
            git add .
            git commit -m "jenktest"
            git remote set-url origin git@github.com:yoyothan22/gitapp.git
            git push
           

            '''
    }
}

}
        
}    
    
