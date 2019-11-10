#!/usr/bin/env groovy

// Author : Raveendiran RR
// Script to deploy a simple PHP website pipeline
// 1.  Download the source code from GIT Repo
// 2.  If the php-server container exists, delete it 
// 3.  Create the container with the latest source code 

import java.net.URL


node
{
    try
    {
        stage('Download form GIT Repo')
        {
            echo '==========GitDownload=========='
            //download the repo
            git 'https://github.com/Raveendiran-RR/simple-php-website.git'
        }

        stage('Build / deploy stage ')
        {
            echo '===============Build Image and Deploy================='
            echo '****checking if container exists and remove it ****'
            // if the remove container command fails, tweek the shell out put as success to continue the execution
            sh 'sudo docker rm -f php-server || true'
            //build the latest image
            sh 'sudo docker build . -t ravi/proj-php:v${BUILD_NUMBER}'
            //start the container 
            sh 'sudo docker run -itd -p 80:80 --name php-server ravi/proj-php:v${BUILD_NUMBER}'       
            
        }
 
    }
    catch (Exception err)
    {
        echo "******Error_found****** "
        echo "${err}"
    }
    finally
    {
        echo 'Script execution completed'
    }
}
