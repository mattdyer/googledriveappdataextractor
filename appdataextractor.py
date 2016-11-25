import requests
import zipfile
import tempfile

def get_app_signature(apk_name):
	tempdirectory = tempfile.gettempdir()

	certfilepath = apk_name + ''

	apk = zipfile.ZipFile(apk_name)

	filelist = apk.namelist()

	for file in filelist:
		if 'META-INF' in file:
			apk.extract(file)
			print(file)

	

def get_master_token(email,password):
	deviceID = '0000000000000000'

	data = {'Email':email, 'Passwd':password, 'app':'com.google.android.gms', 'client_sig':'38918a453d07199354f8b19af05ec6562ced5788', 'parentAndroidId':deviceID}

	#r = requests.post('https://android.clients.google.com/auth',data = data)

	#response_content = r.text

	response_content = """SID=8QPUuun0r0VQppbiyt4FOda5hz1AAgCnHcR_J448XqR5Q-Tmc2Ce1uPYmaJHy58hKYyTjA.
LSID=8QPUusXc0Y_P3_aAXgx6DIOTfMPnEmqzazgxvFiCF52l-7zqSm4lcmnFbifBY44mMbH6uA.
Token=oauth2rt_1/dxKZv8IybHzK5xapvYBIIBEWDJWIdwI4bTB7W1WwM3c
issueAdvice=auto
services=wise,hist,talk,sitemaps,mail,toolbar,adsense,ig,analytics,sprose,writely,mobile,grandcentral,androiddeveloper,a
ndroid,cl,groups2,androidmarket,doritos,googleme,oz,code,youtube,chromewebstore,friendview,ah,lh2,chromiumsync,cloudprin
t,googleplay,omaha,multilogin,chromeoslogin,lso,admob,gerritcodereview,esmobile,blogger,ahadmin,mymaps,sj,backup"""
	
	#tokenPosition = testString.find('Token=')

	lines = response_content.split('\n')

	token = lines[2].split('=')[1]

	return token