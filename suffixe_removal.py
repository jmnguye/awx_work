# i want to be able to remove the word in parameter of the word in an array
tabs = ["awx_myorganization_admins","awx_myorganization_users"]

for entry in tabs:
    print("i need to remove part of this entry : {0}".format(entry.replace('_admins','',1).replace('_users','',1)))