from jinja2 import Template 
import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
import password_container

sender_email = 'sarthaksarthaktalukdar@gmail.com'
receiver_email = 'commanderparakeet@gmail.com'
password = password_container.password

with open('index.html','r') as file:
    template = Template(file.read())

html_content = template.render(name = 'John', email = 'john@example.com')

#Create the email message
msg = MIMEMultipart('alternative')
msg['From'] = sender_email
msg['To'] = receiver_email 
msg['Subject'] = 'Welcome to the team!'

#Add the html template
msg.attach(MIMEText(html_content,'html'))

#sending emails

try:
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,msg.as_string())
    print("Email sent successfully")
except Exception as error:
    print(f"Error:{error}")
finally:
    server.quit()

