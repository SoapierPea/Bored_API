import requests
from colorama import Fore, Style

class Bored():
    def __init__(self):
        self.activity = ""
        self.price = None
        self.type = ""
        self.users = ""
    
    def get_activity(self):
        minprice = print(input("Select your minimum price range: (0 - 1) "))
        maxprice = print(input("Select your maximum price range: (0 - 1) "))

        url = f"http://www.boredapi.com/api/activity?minprice={minprice}&maxprice={maxprice}"
        response = requests.get(url)
        data = response.json()


        if response.ok:
            self.exercise = data["exercise"]
            self.type = data["type"]
            self.price = data["price"]
            self.users = data["users"]
            return True
        else:
            return False

    def data_set(self):
        print(Fore.BLUE, end='')
        print(self.activity)
        print(Fore.GREEN, end='')
        print(self.price)
        print(Fore.RED, end='')
        print(self.type)
        print(Fore.YELLOW, end='')
        print(self.users)
        print(Style.RESET_ALL)

    def app(self):
        bored = Bored()
        while True:
            print(bored.get_activity())
            bored.data_set()
            select = input("Would you like to do anything else? (y/n)")
            if select[0].lower() == "n":
                print("Take care now!")
                break

Bored()