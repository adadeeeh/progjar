from ftplib import FTP

f = FTP('127.0.0.1')
print "Welcome:", f.getwelcome()

f.login('Hana', 'tes')
print "Current working directory:", f.pwd()
names = f.nlst()
print 'List of directory: ', names
f.quit()