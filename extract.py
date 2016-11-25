import appdataextractor as data
import sys

email = sys.argv[1]
password = sys.argv[2]


data.get_app_signature('test.apk');


#master_token = data.get_master_token(email,password)


#print(master_token);
