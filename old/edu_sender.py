import csv
from letter import *


def send_edu_letters():
    letters = []
    i = 0
    with open('EduProviders.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                company = row[0].strip()
                name = row[2].strip()
                email = row[4].strip()
                subject = "120,000+ students wanting guidance on joining {}".format(company)
                body = """<p style="background-color: tran<p style="line-height: 1.656; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 9.5pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Hi</span><strong><span style="font-size: 9.5pt; font-family: Arial; color: #000000; background-color: transparent; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"> {}</span></strong><span style="font-size: 9.5pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">,</span></p>
<p style="line-height: 1.38; margin-top: 0pt; margin-bottom: 0pt;">&nbsp;</p>
<p style="line-height: 1.656; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 9.5pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">I&rsquo;m reaching out to</span><strong><span style="font-size: 9.5pt; font-family: Arial; color: #000000; background-color: transparent; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"> {}</span></strong><span style="font-size: 9.5pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;"> as I run a Facebook Group with 120,000+ current year 11 and 12 students and these students are looking for an educational provider to directly engage and educate them in this group.</span></p>
<p style="line-height: 1.38; margin-top: 0pt; margin-bottom: 0pt;">&nbsp;</p>
<p style="line-height: 1.656; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 9.5pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Having run this group for the last four years, I&rsquo;ve noticed a pattern in the enormous amount of student discussion and questions about how to effectively make the transition to university, and at the moment - these questions are answered by other students who share various articles and resources.</span></p>
<p style="line-height: 1.38; margin-top: 0pt; margin-bottom: 0pt;">&nbsp;</p>
<p style="line-height: 1.656; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 9.5pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">In Victoria and NSW, we&rsquo;ve already had Latrobe University &amp; University of Wollongong step in and become trusted advisors for their state&rsquo;s students - and we thought that you could be interested in stepping up and becoming the trusted advisor for year 11 and 12 students in applying for university.</span></p>
<p style="line-height: 1.38; margin-top: 0pt; margin-bottom: 0pt;">&nbsp;</p>
<p style="line-height: 1.656; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 9.5pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">We&rsquo;re currently having a chat with all the main educational providers in Australia to see who could provide value to these students and we&rsquo;d love to have a chat with you.</span></p>
<p style="line-height: 1.38; margin-top: 0pt; margin-bottom: 0pt;">&nbsp;</p>
<p style="line-height: 1.656; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 9.5pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Please feel free to schedule a time that you&rsquo;d be free to chat at this link: </span><a style="text-decoration: none;" href="https://calendly.com/charlie-f"><span style="font-size: 9.5pt; font-family: Arial; color: #1155cc; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: underline; -webkit-text-decoration-skip: none; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">https://calendly.com/charlie-f</span></a><span style="font-size: 9.5pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">. It would be great to see a educational provider join this group as a trusted advisor for the students.</span></p>
<p style="line-height: 1.38; margin-top: 0pt; margin-bottom: 0pt;">&nbsp;</p>
<p style="line-height: 1.656; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 9.5pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Look forward to chatting soon,</span></p>
<p style="line-height: 1.38; margin-top: 0pt; margin-bottom: 0pt;">&nbsp;</p>
<p style="line-height: 1.656; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-size: 9.5pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Charlie</span></p>""".format(name, company)
                if (subject, body, email) not in letters:
                    letters.append((subject, body, email))
                    next_letter = Letter(subject, body, email)
                    if i == 0:
                        next_letter.send_mail()
                    i += 1
            except:
                continue
    print("EDU - " + str(i))
