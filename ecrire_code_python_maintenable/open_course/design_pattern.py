"""Sert un groupe de clients"""

GUESTS_NUMBER = 15
WATER_PER_GUEST = 400
WATER_LEVEL = GUESTS_NUMBER * WATER_PER_GUEST
TIME_TO_WAIT = GUESTS_NUMBER * 2
SPOONS_NUMBER = 2
MUSIC_LEVEL = 10








def serve_group_of_two():
    """Sert un groupe de deux clients affamés.
 
    S'assure d'une expérience inoubliable !
    """
    greet_guests()
    table_number = prepare_table(GUESTS_NUMBER)
    for guest in range(GUESTS_NUMBER):
        lay_spoons_on_table(SPOONS_NUMBER)
 
    lead_customers_to_table(table_number)
    fill_water_carafe(WATER_LEVEL)
    adjust_music_volume(MUSIC_LEVEL)
    present_menus(GUESTS_NUMBER)
 
    wait_minutes(TIME_TO_WAIT)
 
    drinks_order = take_order(table_number)
    process_order(drinks_order)
    # ...
    present_bill()
    thank_guests()

def greet_guests():
    print("Bienvenue !")

def prepare_table(guests):
    print(f"prepare une table pour {guests} personnes")
    return 10
    

def lay_spoons_on_table(spoons_number):
    print(f"dispose {spoons_number} cuillères sur la table")

def lead_customers_to_table(table_number):
    print(f"Venez à la table {table_number}")

def fill_water_carafe(water_level):
    print(f"nous vous servons {water_level} ml d'eau ")

def adjust_music_volume(music_level):
    print(f"nous ajustons le volume pour {music_level}")

def present_menus(number_menu):
    print(f"Nous présentons {number_menu} menus à la table")

def wait_minutes(minutes):
    print(f"---  Il y a une attente de {minutes} minutes ---")


def take_order(number):
    print(f"Nous prenons la commande de la table {number}.")
    return "Bouteille de vin"


def process_order(drinks_order):
    print("Nous allons chercher les boissons !")

def present_bill():
    print("here your bill")

def thank_guests():
    print("Merci d'être passé")


if __name__ == "__main__":
    serve_group_of_two()





