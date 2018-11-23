import firebase as firebase
from firebase.firebase import FirebaseApplication
import click
import json
import time
fire = FirebaseApplication("https://smart4brno.firebaseio.com/", None)

@click.command()
@click.option('--file', help='Name of the JSON file', type=click.File('r'))






def JsonParse(file):
    global fire
    FILE = json.loads(file.read())
    print("ID: " + str(FILE["id"]))
    print("Jméno: " + FILE["name"])
    print("Adresa: "+ FILE["address"])
    print("Volných míst: "+ str(FILE["free"]["now"]))
    print("Celkem míst: "+ str(FILE["total"]))
    print("GPS Souřadnice: "+ str(FILE["gps"][0]) + " "+str(FILE["gps"][1]))
    
    print(fire.get('/', None))
    fire.patch(str(FILE["id"]), FILE)    
    time.sleep(1)
    print("Done")
if __name__ == '__main__':
    JsonParse()
    
