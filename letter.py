from sendgrid.helpers.mail import Email, Mail, Content
import sendgrid


class Letter:
    # using SendGrid's Python Library
    # https://github.com/sendgrid/sendgrid-python
    mykey = "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"


    from_email = Email("charlie.f@trendyrhino.com")
    # from_email = Email("kachmar@ucu.edu.ua")

    def __init__(self, subject, content, to_email):
        self.subject = subject
        self.content = content
        self.to_email = to_email

    def send_mail(self):
        # sending an email
        print("Sending email to " + self.to_email)
        sg = sendgrid.SendGridAPIClient(apikey=self.mykey)
        content = Content("text/html", self.content)
        mail = Mail(self.from_email, str(self.subject), Email(self.to_email), content)
        response = sg.client.mail.send.post(request_body=mail.get())
        return response, self.subject, content.value

    def __str__(self, *args, **kwargs):
        return "Subject: {},\n Adress: {},\n {}".format(self.subject, self.to_email, self.content)
        # letter = Letter("test", "test body", "pavlokach@gmail.com")
        # print(letter.__str__())

# l = Letter('test', "test content", "pavlokach@gmail.com")
# l.send_mail()
