
#TODO. Make a text adventure for walk down a path.
#*             Basic flowchart for text adventure:
#! My solution starts on line 100 for comparison.
#?         Have a welcome statement for your game.
#?         Start point: ask user to pick left or right?
#?                                  |
#?                                  |--------Right------> Game over.
#?                                  V
#?                                  |
#?                                 Left
#?                                  |
#?                                  V
#?                             Jump or sit?
#?                                  |
#?                                  |--------Jump-------> Game over.
#?                                  V
#?                                  |
#?                                 Sit
#?                                  |
#?                                  V
#?                         East, West, or North?
#?                                  |
#?  Game over. <------East----------|-------North-------> Game over.
#?                                  |---------------|
#?                                 West             |
#?                                  V               |
#?                               [Winner]           |
#?                                                  V
#?                                             Anything else.
#?                                                  |
#?                                                  |
#?                                                  V
#?                                              Game over.

































































# print("Welcome To the text trial!")

# pick_direction = input("You are walking on a trail, but come across a fork in the road. What direction do you go, Left or Right? ").lower()

# if pick_direction == "left":
#     print("We start heading down the left path! ")

#     pick_an_action = input("Soon you come across a log in the road. Do you choose to Sit on the log or Jump over it. Please type either Sit or Jump: ").lower()
#     if pick_an_action == "sit":
#         print("It was a good thing we took a break, your feet were pretty sore.")
       
#         which_door = input("After continuing your hike, you soon come across a house with 3 doors on the sides of the house. The doors are located on the East, West and North side of the house. Which door would you like to Enter? PLease type either East, West, or North: ").lower()
#         if which_door == "west":
#             print("We have found the Costco food court! Now we have a happy life!")
#         else:
#             print("You are trampled by a horde of hungry citizens looking for food, better luck next time on the trial.")
        
#     else:
#         print("Your ankles broke, due to the fatigue from the trial. The trial is now over.")
# else:
#     print("You have walked into a hole that was covered in leaves, and broke your leg. The trial is over for you")
