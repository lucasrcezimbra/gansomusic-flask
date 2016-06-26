#coding: utf-8

import yagmail
import os

#fix encoding
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Mailer:
    def __init__(self, to, subject, attach_path):
        self.to = to
        self.subject = subject
        self.attch_path = attach_path
        self.contents = [self.attch_path]

    def send(self):
        login = os.environ['GANSO-EMAIL-LOGIN']
        password = os.environ['GANSO-EMAIL-PASSWORD']
        yag = yagmail.SMTP(login, password)
        yag.send(self.to, self.subject, self.contents)
