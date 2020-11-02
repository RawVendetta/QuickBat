# QuickBat
Quickbat is a python3 script that makes a simple reverse shell quickly with minimal user effort</br>This script is meant to be ran on a linux machine as its functionality includes using commands like `ip` & `msfvenom(part of the metasploit framework)`<br>
<strong><head3><br>Usage:</stong></head3><br>Run the script by typing `python3 QuickBat.py`
<br>Then all you have to do is `specify the name` of the files to be for the reverse shell, as well as the `port` you want to listen on. The script will do the rest.
<br><br>How to install?<br>`git clone https://github.com/RawVendetta/QuickBat/`
<br><br>This script is really easy to use and usaully needs no dependancies to use it.

<br><strong><head3>Dependancies issue fix:</strong></head3><br>Only use these commands if running the script on linux doesn't work first try. This will fix what is missing.<br>`sudo apt-get install iproute2`<br>`curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall`
