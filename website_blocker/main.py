import time
from datetime import datetime as dt

host_temp = r"C:\Users\wiki\PycharmProjects\MyProject\website_Blocker\hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","www.hotmail.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 0) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 20):
        print("Working Hours")
        with open(host_path, "r+") as file:     # r+ is used to have both read and write functionality
        # or file = open(host_temp, "r+")
            content = file.read()           # read stores the data letter by letter as a single string
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n" + redirect + " " + website)

    else:
        with open(host_path, "r+") as file:
            content=file.readlines()        # readlines stores data line by line in a list
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun Hours")
    time.sleep(5)

# there's also a feature of running a script in background
# at C:\Users\wiki\AppData\Local\Programs\Python\Python37-32
# there is a exe file by the name pythonw.exe
# we have to run our program through this
# in order to do that we have to change the extension to main.pyw
# and then just "DOUBLE CLICK" the main.pyw file, it will start and run in the background
# after that if we want this script to run on startup and automatically than we have to go to the "task scheduler"
# and then create task for the script
