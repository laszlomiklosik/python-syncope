#!/usr/bin/env python
#
# This example will update the user: wedijkerman (The one we created with the example script: create_user.py).
# We made an mistake with the username: We want to update the username from 'wedijkerman' to 'wdijkerman'.
#
import syncope

# Create the connection
syn = syncope.Syncope(syncope_url="http://192.168.10.12:18080/syncope", username="admin", password="password")

# Get the id for the 'wedijkerman' user, before we update it to 'wdijkerman'
my_user_data = syn.get_user_by_name("wdijkerman")
my_user_id = my_user_data['id']
my_user = '{"id":655,"attributesToBeUpdated":[{"schema":"uselessReadonly","valuesToBeAdded":[],"valuesToBeRemoved":[]},{"schema":"loginDate","valuesToBeAdded":[],"valuesToBeRemoved":[]},{"schema":"activationDate","valuesToBeAdded":[],"valuesToBeRemoved":[]}],"attributesToBeRemoved":["aLong","makeItDouble"],"derivedAttributesToBeAdded":[],"derivedAttributesToBeRemoved":[],"virtualAttributesToBeUpdated":[],"virtualAttributesToBeRemoved":[],"resourcesToBeAdded":[],"resourcesToBeRemoved":[],"password":null,"username":"wdijkerman","membershipsToBeAdded":[],"membershipsToBeRemoved":[],"pwdPropRequest":{"resources":[],"onSyncope":false}}'

json_output = syn.update_user(my_user_id, my_user)

if json_output:
	print  "User %s updated" % (json_output['username'])
else:
	print "Update failed."
