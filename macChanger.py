import subprocess

print("[+] .. Your MAC add is changing... -------")
print('....................')
print('....................')

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
subprocess.call("ifconfig", shell=True)
print('[+]   MAC has been changed  ')

n= raw_input("Enter y to change the mac back to normal... n to not \n> ")


if (n=='y'):
    print('[+] Backing the Mac ')
    print('........')

''' HERE the subprocess commands are given in a list way... its much secure than previous one .    	This type of listing need each command in a single quote.
'''
    subprocess.call(["ifconfig", "eth0", "down"])
    subprocess.call(["ifconfig", "eth0", "hw", "ether", "08:00:27:89:03:db"])
    subprocess.call(["ifconfig", "eth0", "up"])
    subprocess.call(["ifconfig"])
    print("YOUR MAC address has been changed to the Normal one.")

else:
    print("Your MAC is not changed")
    subprocess.call("ifconfig",shell=True)
