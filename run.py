from app import myApp
import os
port = int(os.environ.get('PORT', 5000))
 
myApp.run(host='127.0.0.1', port=port)