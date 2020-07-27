from datetime import datetime

host_path="C:/Windows/System32/drivers/etc/hosts"
redirect='127.0.0.1'

website_list=["facebook.com","www.facebook.com","www.instagram.com"]

start_date= datetime(2020,7,27)
end_date= datetime(2020,7,26)
today_date= datetime(datetime.now().year,datetime.now().month,datetime.now().day)

while True:
    if start_date <=today_date <end_date:
        with open(host_path,"r+") as file: #r+-->read and write mode
            content=file.read()
            for site in website_list:
                if site not in content:
                    file.write(redirect+" "+site+"\n")
        print('all sites bloclked')
        break
    else:#end_date <=today date
        with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in website_list):
                    file.write(line)
                file.truncate()#to save the file
        print('all sites unblocked')
        break
