import json
import swiftclient.client as swiftclient

def swift():
    with open("VCAP_SERVICES.json") as data:
        content = json.load(data)

        cloudant_service = content['Object-Storage'][0]
        objectstorage_creds = cloudant_service['credentials']

        if objectstorage_creds:
            auth_url = objectstorage_creds['auth_url'] + '/v3'
            project_name = objectstorage_creds['project']
            password = objectstorage_creds['password']
            user_domain_name = objectstorage_creds['domainName']
            project_id = objectstorage_creds['projectId']
            user_id = objectstorage_creds['userId']
            region_name = objectstorage_creds['region']

        # Get a Swift client connection object
        conn = swiftclient.Connection(
                key=password,
                authurl=auth_url,
                auth_version='3',
                os_options={"project_id": project_id,
                            "user_id": user_id,
                            "region_name": region_name})

        container_name = 'new-container'

        # File name for testing
        file_name = 'openwhisk.mov'
        new_file_name = 'newopenwhisk.mov'

        # Create a new container
        conn.put_container(container_name)
        print "\nContainer %s created successfully." % container_name

        # List your containers
        print ("\nContainer List:")
        for container in conn.get_account()[1]:
            print container['name']

        content = open(file_name,'rb').read()
        # Create a file for uploading
        conn.put_object(container_name,file_name,content,len(content))

        # List objects in a container, and prints out each object name, the file size, and last modified date
        print ("\nObject List:")
        for container in conn.get_account()[1]:
            for data in conn.get_container(container['name'])[1]:
                print 'object: {0}\t size: {1}\t date: {2}'.format(data['name'], data['bytes'], data['last_modified'])

        # Download an object and save it to ./my_example.txt
        obj = conn.get_object(container_name, file_name)
        with open(new_file_name, 'w') as my_example:
               my_example.write(obj[1])
               print "\nObject %s downloaded successfully." % new_file_name

        # Delete an object
        #conn.delete_object(container_name, file_name)
        #print "\nObject %s deleted successfully." % file_name

        # To delete a container. Note: The container must be empty!
        #conn.delete_container(container_name)
        #print "\nContainer %s deleted successfully.\n" % container_name

if __name__ == '__main__':
    swift()
