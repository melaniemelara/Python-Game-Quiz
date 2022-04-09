from components import quizVars
from PIL import Image

def total(points):


    if points == 0:
        quizVars.character = quizVars.characters
        print("Whoops! I have no idea who you are!")

    elif points == 85:
       quizVars.character = quizVars.characters[0]

       print("It's " + quizVars.character)
       hulk = Image.open("images/hulk.jpg")
       hulk.show()

    elif points == 80:
        quizVars.character = quizVars.characters[1]

        print("It's " + quizVars.character)
        thor = Image.open("images/thor.jpg")
        thor.show()
    
    elif points == 105:
        quizVars.character = quizVars.characters[2]

        print("It's " + quizVars.character)
        natasha = Image.open("images/black-widow.jpg")
        natasha.show()

    elif points == 95:
        quizVars.character = quizVars.characters[3]

        print("It's " + quizVars.character)
        cap = Image.open("images/captain-america.jpg")
        cap.show()

    elif points == 65:
        quizVars.character = quizVars.characters[4]

        print("It's " + quizVars.character)
        tony = Image.open("images/iron-man.jpg")
        tony.show()
    
    elif points == 115:
        quizVars.character = quizVars.characters[5]

        print("It's " + quizVars.character)
        wanda = Image.open("images/wanda.jpg")
        wanda.show()

    elif points == 90:
        quizVars.character = quizVars.characters[6]

        print("It's " + quizVars.character)
        loki = Image.open("images/loki.jpg")
        loki.show()