import os
import sys
import time
import urllib
import json
import requests


def login():
    try:
        token = open("token.txt", "r")
        informasi()
        
    except IOError:
        print " Login Dulu Bos..."
        user = raw_input(" Masukkan Username: ")
        password = raw_input(" Masukkan Password: ")
        url = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+user+"&locale=en_US&password="+password+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
        dev = url.content
        jsl = json.loads(dev)
        if "session_key" in dev:
            print " Login Sukses.."
            open("token.txt", "w").write(jsl["access_token"])
            informasi()
        
        elif "www.facebook.com" in jsl["error_msg"]:
            print " Akun Kena Cekpoint.."
            os.system("rm -rf token.txt")
        else:
            print " Gagal Login.."
            
    except KeyboardInterrupt:
        sys.exit()
        
def informasi():
    try:
        token = open("token.txt", "r").read()
    except IOError:
        print " Tidak Ada Token ..."
    else:
        try:
            target = raw_input(" Masukkan ID Target: ")
            url = requests.get("https://graph.facebook.com/" + target + "?access_token=" + token)
            dev = json.loads(url.text)
            try:
                print " Mama: " + dev['name']
            except KeyError:
                print " Nama Tidak Ada"
           
            try:
                print " Email : " + dev['email']
            except KeyError:
                print " Emai Tidak Ada"
                
            try:
                print " No HP: " + dev["mobile_phone"]
            except KeyError:
                print " NO hp Tidak Ada"
                   
            try:
                print " Tanggal Lahir: " + dev["birthday"]
            except KeyError:
                print " Tanggal Tidak Ada"
        
        except KeyboardInterrupt:
            sys.exit()
    word()
    
def word():
    try:
        token = open("token.txt", "r").read()
    except IOError:
        print " Tidak Ada Token ..."
    else:
        try:
            target = raw_input(" Masukkan ID Target: ")
            url = requests.get("https://graph.facebook.com/" + target + "?access_token=" + token)
            dev = json.loads(url.text)
            nama1 = dev["first_name"] + "123\n"
            nama2 = dev["last_name"] + "123\n"
            nama3 = dev["first_name"] + "12345\n"
            nama4 = dev["last_name"] + "12345\n"
            birth = dev["birthday"]
            tgl = birth.replace("/", "")  
            print nama1 + nama2 + nama3 + tgl     
        except KeyboardInterrupt:
            sys.exit()

def main():
    login()

if __name__=="__main__":
    main()
