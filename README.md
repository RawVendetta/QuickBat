# QuickBat
Quickbat is a python3 script that makes a simple reverse shell quickly with minimal user effort</br>This script is meant to be ran on a linux machine as its functionality includes using commands like `ip` & `msfvenom(part of the metasploit framework)`<br>
<strong><head3><br>Usage:</stong></head3><br>Run the script by typing `python3 QuickBat.py`
<br>Then all you have to do is `specify the name` of the files to be for the reverse shell, as well as the `port` you want to listen on. The script will do the rest.
<br><head3><strong><br>Purpose:</head3></strong><br>This script easily generates a stager, and a reverse shell. A reverse shell gives your machine control over a remote machine. This is called Remote Code Execution(RCE for short). Social Engineering is involved in the stager making it appear as a setup file for whatever you made the name of the script for. The remote machine in which you wish to have RCE on needs to run one of the two files generated by this script.<br>
<br><br>How to install?<br>`git clone https://github.com/RawVendetta/QuickBat/`

<br><br>This script is really easy to use and usaully needs no dependancies to use it. If there are issues, below will solve them.<br>
<br><strong><head3>Dependancies issue fix:</strong></head3><br>Only use these commands if running the script on linux doesn't work first try. This will fix what is missing.<br>`sudo apt-get install iproute2`<br>`curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall`
