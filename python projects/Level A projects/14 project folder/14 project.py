from contestants import data
from ascii_art import logo
from ascii_art import vs
from random import randint



print(input("Welcome to the Higer or Lower game. Press enter to start: "))
print("\n" * 10)


def the_game():



    

    celeb_1 = randint(0, 49)
    celeb_2 = randint(0, 49)

    person_A = data[celeb_1]["name"]
    person_B = data[celeb_2]["name"]
    profession_A = data[celeb_1]["description"]
    profession_B = data[celeb_2]["description"]
    country_A = data[celeb_1]["country"]
    country_B = data[celeb_2]["country"]
    follow_A = data[celeb_1]["follower_count"]
    follow_B = data[celeb_2]["follower_count"]







    print("".join(logo))
    print(f"Celeb A: {person_A}, {profession_A}, {country_A}\n")



    print("".join(vs))
    print(f"Celeb B: {person_B}, {profession_B}, {country_B}\n")
    print(input("Who has more Followers? Type 'A' or 'B': ").lower())

    







the_game()