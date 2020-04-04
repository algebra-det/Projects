import time
from datetime import datetime as dt

host_temp = "hosts"
host_path = r"C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","dub119.mail.com","www.hotmail.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 2) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 20):
        print("Working Hours")
        with open(host_temp, "r+") as file:     # r+ is used to have both read and write functionality
        # or file = open(host_temp, "r+")
            content = file.read()           # read stores the data letter by letter as a single string
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website +"\n")

    else:
        with open(host_temp, "r+") as file:
            content=file.readlines()        # readlines stores data line by line in a list
            file.seek(0)                    # to put the pointer at 0 otherwise the pointer will get to the end of the file
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun Hours")
    time.sleep(5)
