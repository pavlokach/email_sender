import csv
from letter import *


def send_bar_letters():
    letters = []
    i = 0
    with open('BarsProviders.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                company = row[0].strip()
                name = row[2].strip()
                email = row[4].strip()
                subject = "100k+ students talking about {}".format(company)
                body = """<p style="line-height: 1.38; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 9.5pt; font-family: Arial; color: #222222; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Hi</span><strong><span style="font-size: 9.5pt; font-family: Arial; color: #222222; background-color: transparent; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"> {}</span></strong><span style="font-size: 9.5pt; font-family: Arial; color: #222222; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">,</span></p>
<p style="line-height: 1.38; margin-top: 0pt; margin-bottom: 0pt;">&nbsp;</p>
<p style="line-height: 1.656; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 9.5pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">I&rsquo;m reaching out as I run Facebook Groups with 100,000+ current students and having run this group for the last four years, I&rsquo;ve noticed an enormous amount of student discussion and questions about local clubs and bars, particularly</span><strong><span style="font-size: 9.5pt; font-family: Arial; color: #000000; background-color: transparent; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"> {}</span></strong><span style="font-size: 9.5pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">.</span></p>
<p style="line-height: 1.656; margin-top: 0pt; margin-bottom: 0pt;">&nbsp;</p>
<p style="line-height: 1.656; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 9.5pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">At the moment - these questions are answered by other students who share various articles and resources - however we see an opportunity for a club/bar to jump in and talk to these students directly.</span></p>
<p style="line-height: 1.656; margin-top: 0pt; margin-bottom: 0pt;">&nbsp;</p>
<p style="line-height: 1.656; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 9.5pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">We're already worked alongside large corporates like PWC, Bank of Melbourne and RMIT and thus we're currently having a chat with all the main bars/clubs to see who could provide value to these students. We&rsquo;d love to have a chat with you.</span></p>
<p style="line-height: 1.656; margin-top: 0pt; margin-bottom: 0pt;">&nbsp;</p>
<p style="line-height: 1.656; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 9.5pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Please feel free to suggest a time that you&rsquo;d be free to chat - it would be great to see a bar or club join this group as a source of information and value for the students.</span></p>
<p style="line-height: 1.656; margin-top: 0pt; margin-bottom: 0pt;">&nbsp;</p>
<p style="line-height: 1.656; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 9.5pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Look forward to chatting soon,</span></p>
<p style="line-height: 1.656; margin-top: 0pt; margin-bottom: 0pt;">&nbsp;</p>
<p style="line-height: 1.656; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 9.5pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Charlie</span></p>""".format(name, company)
                if (subject, body, email) not in letters:
                    letters.append((subject, body, email))
                    next_letter = Letter(subject, body, email)
                    if i == 0:
                        next_letter.send_mail()
                    i += 1
            except:
                continue
    print("BAR - " + str(i))
