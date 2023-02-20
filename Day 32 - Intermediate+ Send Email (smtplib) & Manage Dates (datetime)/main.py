import datetime as dt
import random, smtplib
    
now = dt.datetime.now()
day_of_the_week = now.weekday()


if day_of_the_week == 4:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        rand_num = random.choice(quotes)
    
    sender = "enoch260@gmail.com"
    receiver = "enochamanor@yahoo.com"
    password = "Jesus26298#21"
    message = f"Subject: Monday Motivation\n\n{quotes[rand_num]}"
        
    with smtplib.SMTP(host="smtp.office365.com", port=587) as connecton:
        connecton.starttls()
        connecton.login(user=sender, password=password)
        connecton.sendmail(from_addr=sender, to_addrs=receiver, msg=message)
        print("Message sent")