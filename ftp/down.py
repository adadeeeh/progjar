from ftplib import FTP

f = FTP('127.0.0.1')
f.login('Hana', 'tes')

fd = open('grafkom.pdf', 'wb')
f.retrbinary('RETR grafkom.pdf', fd.write)

fd.close()
f.quit()
