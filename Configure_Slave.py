# Add or remove the jenkins slave using this python program
import jenkins 

server = jenkins.Jenkins('http://10.128.0.10:8080', username='admin', password='697861f3a07c455b8486531a61f7009c')
# create node with parameters
params = {
    'port': '22',            # SSH Port
    'username': 'Jenkins',   # Credential where the private key of the master is stored
    'credentialsId': '2',    # Id of the credential
    'host': '104.155.131.85' # using external IP addresss coz trying this from my laptop. Use internal IP address 
}

# create a new node with the following parameters
server.create_node(
    'slave',
    nodeDescription='DevOps Test Server',
    remoteFS='/var/lib/jenkins',
    labels='TestServer',
    exclusive=True,
    launcher=jenkins.LAUNCHER_SSH,
    launcher_params=params)

nodes=server.get_nodes()
print("number of node is ",nodes)


# disable the slave node and delete 

#server.disable_node('slave',msg="test the disable thing") # name = slave1
#server.delete_node('slave')