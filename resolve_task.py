#!/usr/bin/python
# -*- coding: utf-8 -*-
# Para usar la librería Unicode hay que ejecutar en la terminal el comando: pip install Unidecode.
from unidecode import unidecode
import json
#########################################################

def self(args):
    pass


class eventwebinar:

    def list_contact(self):

        data_contact = {}
        data_contact['contact'] = [{'name': 'Alice Brown','email': 'None','phone': '1231112223'},
                                   {"name": "Bob Crown","email": "bob@crowns.com","phone": "None"},
                                   {"name": "Carlos Drew","email": "carl@drewess.com","phone": "3453334445"},
                                   {"name": "Doug Emerty","email": "None","phone": "4564445556"},
                                   {"name": "Egan Fair","email": "eg@fairness.com","phone": "5675556667"}]

        data_lead = {}
        data_lead['lead'] =  [{"name": "None","email": "kevin@keith.com","phone": "None"},
                              {"name": "Lucy","email": "lucy@liu.com","phone": "3210001112"},
                              {"name": "Mary Middle","email": "mary@middle.com","phone": "3331112223"},
                              {"name": "None","email": "None","phone": "4442223334"},
                              {"name": "None","email": "ole@olson.com","phone": "None"}]

        data_registrant = {}
        data_registrant['registrant'] = [{"name": "Lucy Liu","email": "lucy@liu.com","phone": "None"},
                                         {"name": "Doug","email": "doug@emmy.com","phone": "4564445556"},
                                         {"name": "Uma Thurman","email": "uma@thurs.com","phone": "None"}]

        with open('data.json','w') as file:
            json.dump(data_registrant,file,indent=4)

        with open('data.json') as file:
            register_contact = json.load(file)

        i = 0
        for registrant in register_contact['registrant']:
            name =  registrant['name']
            email = registrant['email']
            phone = registrant['phone']
            check = False
            for contact in data_contact['contact']:
                if (email in contact['email']) or (phone != 'None' and phone in contact['phone']):
                    check = True
            if not check:
                data_contact['contact'].append({"name":name,"email":email,"phone":phone})

        for lead in data_lead['lead']:
            email_lead = lead['email']
            check_lead = False
            for contact_lead in data_contact['contact']:
                if (email_lead != 'None' and email_lead in contact_lead['email']):
                    check_lead = True
            if check_lead:
                del data_lead['lead'][i]
            i += 1

        return data_contact

    if __name__ == "__main__":
        print(list_contact(self))










