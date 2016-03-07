import imapclient
import pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('labita.leonard@gmail.com', 'BlahBlah')

conn.select_folder('INBOX', readonly=True)

UIDS = conn.search(['Since 20-Aug-2015'])  # returns list of unique ideas for emails

rawMessage = conn.fetch([47474], ['BODY||']), 'FLAGS'])

message = pyzmail.PyzMessage.factory(rawMessage[47474][b'BODY[]'])

message.get_subject() # returns subject of email

message.get_address('from')
