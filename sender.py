import csv
import html2text
from letter import *


def save_email_to_file(filename, content):
    file = open(filename, "w")
    file.write(content)
    file.close()


def send_letters(subject, body, company_index, name_index, email_index, filename):
    letters = []
    i = 0
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        company = ""
        for row in reader:
            try:
                curr_subject = subject
                curr_body = body
                if row[company_index] != '':
                    company = row[company_index].strip()
                name = row[name_index].strip()
                email = row[email_index].strip()
                curr_subject = curr_subject.format(company)
                curr_body = curr_body.format(name, company, company)
                if (curr_subject, curr_body, email) not in letters:
                    letters.append((curr_subject, curr_body, email))
                    next_letter = Letter(curr_subject, curr_body, email)
                    # next_letter.send_mail()
                    i += 1
                    file_to_save = "emails_to_send\\emails\\" + filename.split(".")[0] + " " + str(i) + ".txt"
                    save_email_to_file(file_to_save, html2text.html2text(next_letter.__str__()))
            except:
                continue
    print("Emails amount from " + filename + " - " + str(i))
