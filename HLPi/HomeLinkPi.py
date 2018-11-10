import requests
import os

if os.path.isfile("creds.txt"):
    print("")
else:
    filepath = os.path.dirname(os.path.realpath(__file__))+"/HomeLinkPi.py"
    print("SETSTORM HOMELINK")
    print("-------------------------------------")
    print("Please enter your SetStorm Administrator E-Mail:")
    username = input(">")
    print("-------------------------------------")
    print("Please enter your SetStorm Password:")
    password = input(">")
    print("-------------------------------------")
    print("[SECURE] Contacting server...")
    r = requests.post("https://setstorm.com/homelink/device.php", data={'username': username, 'password':password, 'action':"checkadmin"})
    if r.text == "0VALID":
        print(">>>Credentials valid!<<<")
        print("------------------------")
        print("Do you want to make HomeLinkPi automatically start after the Pi has booted up?")
        c = input("(y/N)")
        if c == "y" or c == "Y":
            print("Installing...")
            os.system("sudo echo python "+filepath+">/etc/init.d/homelinkpi")
            os.system("sudo chmod 755 /etc/init.d/homelinkpi")
            os.system("sudo update-rc.d homelinkpi defaults")
            print("HomeLinkPi Autostart script has successfully been installed into /etc/init.d/")
        else:
            print("HomeLinkPi will not start automatically.")
        print("Registering to account...")
        
    else:
        print("Credentials invalid. Please restart the application to retry.")
        exit()
    