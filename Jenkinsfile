#!/usr/bin/env groovy

// Author : Raveendiran RR
// Script to deploy a simple PHP website pipeline
// 1. Download Config from GIt repo - master node
// 2. Update the slave machine with docker and Open JDK - From master node using Ansible
// 3. Download the Simple-PHP-Website code - Slave Node / Test Server
// 4. Deploy it on docker container named php-server and create image with build number as tag
// 5. Run the test using the Final_test.jar file
// 6. if the test result is a failure delete the container and image that was created

import java.net.URL


Pipeline
{

    node ('master')
    {
        try
        {
            stage('Download configuration files (Playbook, groovy script) from git repo - Master server')
            {
                echo'===========Download config from Git repo============='            
                git -b config 'https://github.com/Raveendiran-RR/simple-php-website.git'
            }
            stage('Run Ansible playbook (from Master Server) to install docker on test server')
            {
                echo 'install docker on test server'
                sh 'ansible-playbook ansible_updated_playbook.yml'
            }
        }
        catch exception(err):
        {
            echo '****** Error ********'
            echo '${err}'
        }
        finally
        {
            echo 'script on master completed'
        }

    }

    node ('slave')
    {
        try
        {
            stage ('Download PHP-Website files from git repo - Test Server')
            {
                echo'======Download PHP-Website files========'
                git 'https://github.com/Raveendiran-RR/simple-php-website.git'
            }
            
            stage('Build / deploy stage ')
            {
                echo '===============Build Image and Deploy================='
                echo '****checking if container exists and remove it ****'
                // if the remove container command fails, tweek the shell out put as success to continue the execution
                sh 'sudo docker rm -f php-server || true'
                //build the latest image
                sh 'sudo docker build . -t ravi/proj-php:v${BUILD_NUMBER} '
                //start the container 
                sh 'sudo docker run -itd -p 80:80 --name php-server ravi/proj-php:v${BUILD_NUMBER}'               
            }
            
            stage ('Test about page')
            {
                echo '===========Testing============'
                // This command will display the contents of the about us page.
                sh 'java -jar Final_test.jar'
                test_output = sh 'java -jar Selenium_test.jar'
                if(test_output=="PASS")
                {
                    echo ' code updated successfully'
                }
                else
                {
                    echo 'code has errors. Deleting the image ravi/proj-php:v${BUILD_NUMBER} and running images'
                    sudo docker rm -f php-server || true
                    sudo docker rmi -f ravi/proj-php:v${BUILD_NUMBER}
                }
                
            }


        }
        catch exception(err):
        {
            echo '****** Error ********'
            echo "${err}"
        }
        finally
        {
            echo 'script on slave completed'
        }
    }
}