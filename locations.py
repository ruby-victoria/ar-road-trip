# locations.py - game loops for each location
import common
import maps
import sys

# ----------------------------------------- MELBOURNE -----------------------------------------
def melbourne(time_period, weather):
    common.clear()
    maps.game_maps("melbourne")
    print()
    print("welcome to beautiful melbourne! it is a", weather, time_period)
    print("melbourne is the capital city of victoria and has a population of approximately 5 million people")
    print()
    choice = common.stay_continue()
    if choice == "STAY":
        # write activities to do in melbourne
        common.clear()
        maps.game_maps("melbourne")
        print()
        print("TO BE COMPLETED - ACTIVITIES TO DO IN MELBOURNE ")
        print()
        print("sorryyy, not done yet, continuing on!!")
        print()
        input("press enter to continue >:) ")
        choice = "CONTINUE"
    if choice == "CONTINUE":
        common.clear()
        valid_choice = False

        while not valid_choice:
            print("the road from melbourne to south australia splits into two main routes:")
            print()
            print("the first is the INLAND route.")
            print("this route goes through ballarat and past the mountains of ararat.")
            print("it continues through the lovely grampian mountain range and then enters south australia through"
                  "the large town of horsham and rural farmland.")
            print()
            print("the second is the COASTAL route.")
            print("this route follows the famous great ocean road. it begins in the nearby coastal city of geelong,")
            print("and then continues to the popular surfing destination of lorne.")
            print("the great ocean road then winds through scenic beach towns such as apollo bay and warrnambool,")
            print("before heading inland towards portland and finally entering south australia through pine forests.")
            print()
            choice = input("would you like to take the INLAND route or the COASTAL route?: ")

            if choice.lower() == "inland":
                return "ballarat"
            elif choice.lower() == "coastal":
                return "geelong"
            else:
                common.clear()

# ----------------------------------------- BALLARAT -----------------------------------------
def ballarat(time_period, weather):
    common.clear()
    maps.game_maps("ballarat")
    print()
    print("WTF YOUR GPS IS GOING ROGUE AND REDIRECTING YOU TO GEELONG (sorry inland isn't done yet)")
    print()
    input("press enter to continue TO COASTAL ROUTE >:) ")
    return "geelong"

# ----------------------------------------- GEELONG -----------------------------------------
def geelong(time_period, weather):
    common.clear()
    maps.game_maps("geelong")
    print()
    print("welcome to geelong! it is a", weather, time_period)
    print()
    print("geelong is a popular coastal city about 1 hour south of melbourne "
          "and has a population of approximately 300k")
    print()
    print(r"""it has several attractions, including:
          a beautiful foreshore BOARDWALK,
          a coastal FERRIS WHEEL, and
          a large sandy BEACH""")
    print()
    choice = common.stay_continue()
    if choice == "STAY":
        # TO DO - add different text if it is different weather
        # TO DO - add different text for different times (e.g., cant walk on beach if it's dark but ferris wheel is lit up)
        common.clear()
        maps.game_maps("geelong")
        print()
        print("you decide to spend some time exploring geelong!")
        print()
        print("first, you walk past the gardens to reach the boardwalk on the foreshore.")
        print()
        print("you walk down the jetty and try to spot some sea life!!")
        print("you hear a splash - could it be a seal??")
        print("you quickly turn to look, but only see ripples fading in the water")
        print()
        input("press enter to continue: ")

        common.clear()
        maps.game_maps("geelong")
        print()
        print("you return to the boardwalk and start walking towards the ferris wheel")
        print("as you walk, you enjoy the cool breeze and fresh sea air")
        print()
        print("you stroll past the pavilion containing the historic victorian-era carousel")
        print("you take a moment to watch the painted wooden horses dance hypnotically as they spin")
        print()
        input("press enter to continue: ")

        common.clear()
        maps.game_maps("geelong")
        print()
        print("you're startled by a nearby toot-toot!!")
        print()
        print("you turn around and see none other than thomas the tank engine himself charging at you!!")
        print("your fight or flight instincts engage and you are milliseconds away from committing a federal crime "
              "when you realise that it isn't the real thomas")
        print("instead, it's an adorable and most likely "
              "copyright-infringing children's car that regularly drives kids down the boardwalk for a small fee")
        print()
        input("press enter to continue: ")

        common.clear()
        maps.game_maps("geelong")
        print()
        print("after your heart recovers, you continue towards the ferris wheel")
        print()
        print("you walk alongside the water and take a shortcut past the seafood paella boat")
        print()
        print("the ferris wheel is in sight!!")
        print("unfortunately, disaster strikes...")
        print()
        print("just as you are walking across to the ticket stand, "
              "a large and rowdy extended family cuts in front of you")
        print("there must be at least 200 of them :(")
        print()
        input("press enter to continue: ")

        common.clear()
        maps.game_maps("geelong")
        print()
        print("you take a deep breath and decide to walk to the nearby beach to kill time until they have finished "
              "lining up at the ferris wheel")
        print()
        print("as you reach the beach, you take your shoes off and enjoy the feeling of the soft, warm sand on your feet")
        print("you stroll along the beach and allow the rhythmic lapping of the waves to soothe you")
        print("you step towards the water and feel the cool, fresh seawater contrast against the warmth of the sand")
        print()
        print("before you know it, half an hour of blissful serenity has passed!! you decide to return to the ferris wheel")
        print()
        input("press enter to continue: ")

        common.clear()
        maps.game_maps("geelong")
        print()
        print("this time, the ferris wheel is free. you buy a ticket and move to the entry line")
        print()
        print("you try not to think about the creaking of the joints, or the severe rusting, or the careless attitude of the workers, or...")
        print()
        print("the sound of the entry gate opening in front of you mercifully stops the thoughts from spiralling")
        print("before you know it, you're in your own ferris car and you feel yourself rising")
        print("you enjoy the views of the sea, beach, parks, and township as you rise")
        print()
        print("thankfully, the ferris wheel does not seem like it will be collapsing today")
        print("you have a lovely time until the wheel stops and you are escorted off")
        print()
        input("press enter to continue: ")

        common.clear()
        maps.game_maps("geelong")
        print()
        print("what a wonderful time spent in geelong!!")
        print()
        print("the town has more attractions to offer, but you are eager to continue on your road trip :)")
        print()
        input("press enter to continue: ")

    common.clear()
    return "lorne"

def lorne(time_period, weather):
    common.clear()
    maps.game_maps("lorne")
    print()
    print("you return to the car and begin driving towards the surf town of lorne")
    print()
    print("LORNE - TO BE COMPLETED")
    print()
    input("press enter to exit: ")
    sys.exit()

