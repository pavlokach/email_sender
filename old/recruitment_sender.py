import csv
from letter import *


def save_email_to_file(filename, content):
    file = open(filename, "w")
    file.write(content)
    file.close()


def send_recruitment_letters():
    letters = []
    i = 0
    with open('CompanyList2.csv', newline='') as f:
        reader = csv.reader(f)
        company = ""
        for row in reader:
            try:
                if row[0] != "":
                    company = row[0]
                name = row[2]
                email = row[4]
                subject = "120,000+ students wanting guidance on joining {}".format(company)
                body = """<p style="background-color: transparent; color: #000000; font-family: Times New Roman; font-size: 16px; font-variant: normal; font-weight: 400; letter-spacing: normal; line-height: 26.49px; margin-bottom: 0px; margin-top: 0px; orphans: 2; text-align: left; text-decoration: none; text-indent: 0px; text-transform: none; -webkit-text-stroke-width: 0px; white-space: normal; word-spacing: 0px;"><span style="background-color: transparent; color: #000000; font-family: Arial; font-size: 12.66px; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Hi</span><strong><span style="background-color: transparent; color: #000000; font-family: Arial; font-size: 12.66px; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"> {}</span></strong><span style="background-color: transparent; color: #000000; font-family: Arial; font-size: 12.66px; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">,</span></p>
<p style="background-color: transparent; color: #000000; font-family: Times New Roman; font-size: 16px; font-variant: normal; font-weight: 400; letter-spacing: normal; line-height: 26.49px; margin-bottom: 0px; margin-top: 0px; orphans: 2; text-align: left; text-decoration: none; text-indent: 0px; text-transform: none; -webkit-text-stroke-width: 0px; white-space: normal; word-spacing: 0px;">&nbsp;</p>
<p style="background-color: transparent; color: #000000; font-family: Times New Roman; font-size: 16px; font-variant: normal; font-weight: 400; letter-spacing: normal; line-height: 26.49px; margin-bottom: 0px; margin-top: 0px; orphans: 2; text-align: left; text-decoration: none; text-indent: 0px; text-transform: none; -webkit-text-stroke-width: 0px; white-space: normal; word-spacing: 0px;"><span style="background-color: transparent; color: #000000; font-family: Arial; font-size: 12.66px; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">I&rsquo;m reaching out to</span><strong><span style="background-color: transparent; color: #000000; font-family: Arial; font-size: 12.66px; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"> {}</span></strong><span style="background-color: transparent; color: #000000; font-family: Arial; font-size: 12.66px; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"> as I run a Facebook Group with 120,000+ current high achieving Australian students and these students are looking for </span><strong><span style="background-color: transparent; color: #000000; font-family: Arial; font-size: 12.66px; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">{} </span></strong><span style="background-color: transparent; color: #000000; font-family: Arial; font-size: 12.66px; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">to directly engage and educate them about future career opportunities with you.</span></p>
<p style="background-color: transparent; color: #000000; font-family: Times New Roman; font-size: 16px; font-variant: normal; font-weight: 400; letter-spacing: normal; line-height: 26.49px; margin-bottom: 0px; margin-top: 0px; orphans: 2; text-align: left; text-decoration: none; text-indent: 0px; text-transform: none; -webkit-text-stroke-width: 0px; white-space: normal; word-spacing: 0px;">&nbsp;</p>
<p style="background-color: transparent; color: #000000; font-family: Times New Roman; font-size: 16px; font-variant: normal; font-weight: 400; letter-spacing: normal; line-height: 26.49px; margin-bottom: 0px; margin-top: 0px; orphans: 2; text-align: left; text-decoration: none; text-indent: 0px; text-transform: none; -webkit-text-stroke-width: 0px; white-space: normal; word-spacing: 0px;"><span style="background-color: transparent; color: #000000; font-family: Arial; font-size: 12.66px; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Having run this group for the last four years, I&rsquo;ve noticed a pattern in the enormous amount of student discussion and questions about how to effectively make the transition to full time employment, and at the moment - these questions are answered by other students who share various articles and resources.</span></p>
<p style="background-color: transparent; color: #000000; font-family: Times New Roman; font-size: 16px; font-variant: normal; font-weight: 400; letter-spacing: normal; line-height: 26.49px; margin-bottom: 0px; margin-top: 0px; orphans: 2; text-align: left; text-decoration: none; text-indent: 0px; text-transform: none; -webkit-text-stroke-width: 0px; white-space: normal; word-spacing: 0px;">&nbsp;</p>
<p style="background-color: transparent; color: #000000; font-family: Times New Roman; font-size: 16px; font-variant: normal; font-weight: 400; letter-spacing: normal; line-height: 26.49px; margin-bottom: 0px; margin-top: 0px; orphans: 2; text-align: left; text-decoration: none; text-indent: 0px; text-transform: none; -webkit-text-stroke-width: 0px; white-space: normal; word-spacing: 0px;"><span style="background-color: transparent; color: #000000; font-family: Arial; font-size: 12.66px; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">We&rsquo;ve already partnered with companies like RMIT, Bank of Melbourne and Latrobe University in assisting students make the transition to employment - and we thought that you could be interested in stepping up and becoming the trusted advisor for students in applying for, and receiving graduate positions. </span></p>
<p style="background-color: transparent; color: #000000; font-family: Times New Roman; font-size: 16px; font-variant: normal; font-weight: 400; letter-spacing: normal; line-height: 26.49px; margin-bottom: 0px; margin-top: 0px; orphans: 2; text-align: left; text-decoration: none; text-indent: 0px; text-transform: none; -webkit-text-stroke-width: 0px; white-space: normal; word-spacing: 0px;">&nbsp;</p>
<p style="background-color: transparent; color: #000000; font-family: Times New Roman; font-size: 16px; font-variant: normal; font-weight: 400; letter-spacing: normal; line-height: 26.49px; margin-bottom: 0px; margin-top: 0px; orphans: 2; text-align: left; text-decoration: none; text-indent: 0px; text-transform: none; -webkit-text-stroke-width: 0px; white-space: normal; word-spacing: 0px;"><span style="background-color: transparent; color: #000000; font-family: Arial; font-size: 12.66px; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">We&rsquo;re currently having a chat with all the main graduate employers in Australia to see who could provide the most assistance to these students, and we&rsquo;d love to have a chat with you.</span></p>
<p style="background-color: transparent; color: #000000; font-family: Times New Roman; font-size: 16px; font-variant: normal; font-weight: 400; letter-spacing: normal; line-height: 26.49px; margin-bottom: 0px; margin-top: 0px; orphans: 2; text-align: left; text-decoration: none; text-indent: 0px; text-transform: none; -webkit-text-stroke-width: 0px; white-space: normal; word-spacing: 0px;">&nbsp;</p>
<p style="background-color: transparent; color: #000000; font-family: Times New Roman; font-size: 16px; font-variant: normal; font-weight: 400; letter-spacing: normal; line-height: 26.49px; margin-bottom: 0px; margin-top: 0px; orphans: 2; text-align: left; text-decoration: none; text-indent: 0px; text-transform: none; -webkit-text-stroke-width: 0px; white-space: normal; word-spacing: 0px;"><span style="background-color: transparent; color: #000000; font-family: Arial; font-size: 12.66px; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Please feel free to schedule a time that you&rsquo;d be free to chat at this link: </span><a style="text-decoration: none;" href="https://calendly.com/charlie-f"><span style="background-color: transparent; color: #1155cc; font-family: Arial; font-size: 12.66px; font-variant: normal; font-weight: 400; text-decoration: underline; vertical-align: baseline; white-space: pre-wrap;">https://calendly.com/charlie-f</span></a><span style="background-color: transparent; color: #000000; font-family: Arial; font-size: 12.66px; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">, or reply by email.</span></p>
<p style="background-color: transparent; color: #000000; font-family: Times New Roman; font-size: 16px; font-variant: normal; font-weight: 400; letter-spacing: normal; line-height: 26.49px; margin-bottom: 0px; margin-top: 0px; orphans: 2; text-align: left; text-decoration: none; text-indent: 0px; text-transform: none; -webkit-text-stroke-width: 0px; white-space: normal; word-spacing: 0px;">&nbsp;</p>
<p style="background-color: transparent; color: #000000; font-family: Times New Roman; font-size: 16px; font-variant: normal; font-weight: 400; letter-spacing: normal; line-height: 26.49px; margin-bottom: 0px; margin-top: 0px; orphans: 2; text-align: left; text-decoration: none; text-indent: 0px; text-transform: none; -webkit-text-stroke-width: 0px; white-space: normal; word-spacing: 0px;"><span style="background-color: transparent; color: #000000; font-family: Arial; font-size: 12.66px; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Look forward to chatting soon,</span></p>
<p style="background-color: transparent; color: #000000; font-family: Times New Roman; font-size: 16px; font-variant: normal; font-weight: 400; letter-spacing: normal; line-height: 26.49px; margin-bottom: 0px; margin-top: 0px; orphans: 2; text-align: left; text-decoration: none; text-indent: 0px; text-transform: none; -webkit-text-stroke-width: 0px; white-space: normal; word-spacing: 0px;">&nbsp;</p>
<p style="background-color: transparent; color: #000000; font-family: Times New Roman; font-size: 16px; font-variant: normal; font-weight: 400; letter-spacing: normal; line-height: 26.49px; margin-bottom: 0px; margin-top: 0px; orphans: 2; text-align: left; text-decoration: none; text-indent: 0px; text-transform: none; -webkit-text-stroke-width: 0px; white-space: normal; word-spacing: 0px;"><span style="background-color: transparent; color: #000000; font-family: Arial; font-size: 12.66px; font-variant: normal; font-weight: 400; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Charlie</span></p>""".format(
                    name, company, company)
                if (subject, body, email) not in letters:
                    letters.append((subject, body, email))
                    if i <= 98:
                        key = "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"
                    elif i > 98 and i <= 197:
                        key = "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"
                    elif i > 197 and i <= 296:
                        key = "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"
                    elif i > 296 and i <= 395:
                        key = "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"
                    elif i > 395 and i <= 494:
                        key = "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"
                    elif i > 494:
                        key = "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"
                    next_letter = Letter(subject, body, email, key)
                    next_letter.send_mail()
                    i += 1
                    filename = "emails_to_send\\recruitment\\" + str(i) + ".txt"
                    save_email_to_file(filename, next_letter.__str__())
            except:
                print(row)
                print(i)
    print("RECRUITMENT - " + str(i))