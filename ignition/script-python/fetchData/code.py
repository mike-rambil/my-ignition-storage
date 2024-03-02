
import myWMSFuncs.networking.testScript as testScript
from myWMSFuncs.networking.testScript import myTestFunc
    
def fetchData():
	import urllib2
	import json
	
	# Define the URL and bearer token
	url = 'http://localhost:3000/api/users'
	bearer_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjbHQzanVveTcwMDAwdXI5ZjRjZzhvbGlwIiwidXNlcm5hbWUiOiJhZG1pbiIsImlhdCI6MTcwOTIyNjUxOSwiZXhwIjoxNzA5Mzk5MzE5fQ.ZP2SYn7TafQDWRYf3WAgCFq3C26xfakuh2jXuXJJ4Fw'
	
	# Create a request object with the bearer token
	request = urllib2.Request(url)
	request.add_header('Authorization', 'Bearer ' + bearer_token)
	
	try:
	    # Send the request and get the response
	    response = urllib2.urlopen(request)
	    
	    # Read the response data and parse JSON
	    response_data = response.read()
	    users = json.loads(response_data)
	    
	    # Process the user data
	    # Adding it to the default tag provider
	    system.tag.write("[default]user_json", users)
	    for user in users:
	        print("User ID:", user['id'])
	        print("Username:", user['username'])
	        print("Email:", user['email'])
	except urllib2.HTTPError as e:
	    print("HTTP Error:", e.code)
	    # Handle HTTP errors
	except urllib2.URLError as e:
	    print("URL Error:", e.reason)
	    # Handle URL errors
	except Exception as e:
	    print("Error:", e)