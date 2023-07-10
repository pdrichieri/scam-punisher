import requests
import random
import json

emails = json.loads(open('emails.json').read())
passwords = json.loads(open('passwords.json').read())

url = 'https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1'

for i in range(0, 3):
    randEmailIndex = random.randint(0,499)
    randPasswordIndex = random.randint(0,499)

    print ('Sending user %s with password %s' % (emails[randEmailIndex], passwords[randPasswordIndex]))

data = {
    
    }

pato = requests.post(url, allow_redirects= False)

print('Response: %s' % (pato.content))

