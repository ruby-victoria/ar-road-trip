# game.py - main functions
# alice and ruby road trip game <3
import sys
import common
import locations

vic_locations = [
    "melbourne", "geelong", "lorne", "apollo",
    "apostles", "warrnambool", "portland",
    "ballarat", "ararat", "halls gap", "horsham"
]
sa_locations = []

def main(location, time_period, weather):
    """takes user input and runs game loop"""

    while True:
        # locations
        if location == "melbourne":
            location = locations.melbourne(time_period, weather)
            continue

        if location == "geelong":
            location = locations.geelong(time_period, weather)
            continue

        if location == "ballarat":
            location = locations.ballarat(time_period, weather)
            continue

        if location == "lorne":
            location = locations.lorne(time_period, weather)
            continue

        print()
        action = input("what do u want to do?: ")

        # general actions
        if action.lower() == "help" or action.lower() == "h":
            common.help_text()
        elif action.lower() == "quit" or action.lower() == "exit" or action.lower() == "end":
            sys.exit()

        return


# introduction
common.clear()
print(r"""
       _ _                            _              _           
  __ _│ (_) ___ ___    __ _ _ __   __│ │  _ __ _   _│ │__  _   _ 
 ╱ _` │ │ │╱ __╱ _ ╲  ╱ _` │ '_ ╲ ╱ _` │ │ '__│ │ │ │ '_ ╲│ │ │ │
│ (_│ │ │ │ (_│  __╱ │ (_│ │ │ │ │ (_│ │ │ │  │ │_│ │ │_) │ │_│ │
 ╲__,_│_│_│╲___╲___│  ╲__,_│_│ │_│╲__,_│ │_│   ╲__,_│_.__╱ ╲__, │
                                                           │___╱ 
                       _   _        _             _              
   _ __ ___   __ _  __│ │ │ │_ _ __(_)_ __    ___(_)_ __ ___     
  │ '__╱ _ ╲ ╱ _` │╱ _` │ │ __│ '__│ │ '_ ╲  ╱ __│ │ '_ ` _ ╲    
  │ │ │ (_) │ (_│ │ (_│ │ │ │_│ │  │ │ │_) │ ╲__ ╲ │ │ │ │ │ │   
  │_│  ╲___╱ ╲__,_│╲__,_│  ╲__│_│  │_│ .__╱  │___╱_│_│ │_│ │_│   
                                     │_│                                      


welcome to the alice and ruby road trip sim!

to play the game, just type the action u want to do :)

---------------------------------------------------------------------------
|   the map at the top of the screen shows where u are!                   |
|      - the road trip locations are represented with: @                  |
|      - your current location is represented with: X                     |
|      - as u travel, your route will be represented with lines: _ / \ |  |
---------------------------------------------------------------------------
    
to show this help text again, type 'help' or 'h'

have fun!!""")

# setup
print(r"""
---------------------------------------------------------------------------
|   to-do: make optional different starting locations :)                  |
|   for now u will have to start in melbourne >:)                         |
---------------------------------------------------------------------------
""")

input("press enter to continue: ")

common.clear()

start_location = "melbourne"
start_time_period = "morning"
start_weather = "sunny"

repeat = True

# main game loop
while repeat:
    main(start_location, start_time_period, start_weather)