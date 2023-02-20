import datetime as dt
import pandas
import random
import smtplib

PLACEHOLDER = "[NAME]"
SENDER = "enoch260@gmail.com"
PASSWORD = "zoibcqvcutkchrsv"

# TODO: 1. Update the birthdays.csv

# TODO: 2. Check if today matches a birthday in the birthdays.csv

date = dt.datetime.now()

todays_date = (date.month, date.day)

bd_file = pandas.read_csv("birthdays.csv")
name_list = bd_file.name.tolist()

# TODO: 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the
#  person's actual name from birthdays.csv

birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in bd_file.iterrows()}
if todays_date in birthday_dict:
    birthday_person = birthday_dict[todays_date]
    FILE_PATH = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(FILE_PATH) as letter:
        picked_letter = letter.read()
        birthday_letter = picked_letter.replace(PLACEHOLDER, birthday_person["name"])
        print(birthday_letter)

        # TODO: 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connecton:
            connecton.starttls()
            connecton.login(user=SENDER, password=PASSWORD)
            connecton.sendmail(from_addr=SENDER, to_addrs=birthday_person["email"],
                               msg=f"Subject: Birthday Wish\n\n{birthday_letter}")
            print("Message sent")
