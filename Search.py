#importing the libraries
import imaplib
import email
import getpass

#making the connction with the server
m = imaplib.IMAP4_SSL('imap.gmail.com')

#email = getpass.getpass('Email: ')
#password = getpass.getpass('Password: ')
emailid = ''
password = ''

#loggin into the server
m.login(emailid,password)

#selecting inbox labeled emails from the email ID
m.select('INBOX')

#searching for Trading View emails in Inbox label
status, data = m.search(None,'UNSEEN FROM','TradingView')

#selecting the email ID of Trading View mails
email_ids = data[0]
id_list = email_ids.split()

#fetching the binary code of the mail and capturing the same in raw_email variable
result, email_data = m.fetch(id_list[0],'(RFC822)')
raw_email = email_data[0][1]

#decoding the binary mail body into normal language
raw_email_string = raw_email.decode('utf-8')

email_message = email.message_from_string(raw_email_string)
email_message_subject = email_message['Subject'].split()
print(email_message_subject)
