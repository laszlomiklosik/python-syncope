#!/usr/bin/env python
#
# This example will create an user: wedijkerman and will print the username and the creation date.
# Example user will have 2 roles assigned: 'child' (RoleID: 2) and 'otherchild' (RoleID: 8)
# Example user will also have 2 resources: 'ws-target-resource-1' and 'ws-target-resource-2'
#
import syncope

# Create the connection
syn = syncope.Syncope(syncope_url="http://192.168.10.12:18080/syncope", username="admin", password="password")

# Set the JSON
my_user = '{"attributes": [{"schema": "aLong","values": [],"readonly": false},{"schema": "activationDate","values": [""],"readonly": false},{"schema": "cool","values": ["false"],"readonly": false},{"schema": "email","values": ["werner@dj-wasabi.nl"],"readonly": false},{"schema": "firstname","values": ["Werner"],"readonly": false},{"schema": "fullname","values": ["Werner Dijkerman"],"readonly": false},{"schema": "gender","values": ["M"],"readonly": false},{"schema": "loginDate","values": [""],"readonly": false},{"schema": "makeItDouble","values": [],"readonly": false},{"schema": "surname","values": ["Dijkerman"],"readonly": false},{"schema": "type","values": ["account"],"readonly": false},{"schema": "uselessReadonly","values": [""],"readonly": true},{"schema": "userId","values": ["werner@dj-wasabi.nl"],"readonly": false}],"id": 0,"derivedAttributes": [{"schema": "cn","values": [],"readonly": false}],"virtualAttributes": [],"password": "password1234","status": null,"token": null,"tokenExpireTime": null,"username": "wedijkerman","lastLoginDate": null,"creationDate": null,"changePwdDate": null,"failedLogins": null}'

json_output = syn.create_user(my_user)

if json_output:
	print  "User %s created on this time %s" % (json_output['username'], json_output['creationDate'])
else:
	print "Create failed or user already exists."
