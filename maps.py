# game_maps.py - generates game_maps for each game location

import common

"""
melbourne
[ = X

--------------------------------------------
coastal route
--------------------------------------------

geelong
] = X
z = _
a = _
1 = /

lorne
{ = X
b = _
2 = /

apollo
} = X
k = _
y = /

apostles
$ = X
c = _
3 = \

warrnambool
% = X
d = _
4 = \

portland
^ = X
5 = \
6 = /

sa_coastal
< = X
f = _
7 = \
--------------------------------------------
inland route
--------------------------------------------
ballarat
& = X
z = _
f = _
8 = \

ararat
* = X
g = _
9 = \

halls gap
( = X
h = _
0 = \

horsham
) = X
i = _
o = |

sa_inland
> = X
j = _
--------------------------------------------
"""

# ---------------------- character generators - coastal route ----------------------

def geelongchars():
    """generates list of characters to convert for the geelong game_map"""
    chars = ["z", "1", "a"]
    return chars

def lornechars():
    """generates list of characters to convert for the lorne game_map"""
    chars = geelongchars()
    newchars = ["b", "2"]
    for char in newchars:
        chars.append(char)
    return chars

def apollochars():
    """generates list of characters to convert for the apollo game_map"""
    chars = lornechars()
    newchars = ["k", "y"]
    for char in newchars:
        chars.append(char)
    return chars

def apostlechars():
    """generates list of characters to convert for the apostle game_map"""
    chars = apollochars()
    newchars = ["c", "3"]
    for char in newchars:
        chars.append(char)
    return chars

def warrnamboolchars():
    """generates list of characters to convert for the warrnambool game_map"""
    chars = apostlechars()
    newchars = ["d", "4"]
    for char in newchars:
        chars.append(char)
    return chars

def portlandchars():
    """generates list of characters to convert for the portland game_map"""
    chars = warrnamboolchars()
    newchars = ["e", "5", "6"]
    for char in newchars:
        chars.append(char)
    return chars

def sa_coastalchars():
    """generates list of characters to convert for the sa_coastal game_map"""
    chars = portlandchars()
    newchars = ["w", "7"]
    for char in newchars:
        chars.append(char)
    return chars

# ---------------------- character generators - inland route ----------------------

def ballaratchars():
    """generates list of characters to convert for the ballarat game_map"""
    chars = ["z", "8", "f"]
    return chars

def araratchars():
    """generates list of characters to convert for the ararat game_map"""
    chars =  ballaratchars()
    newchars = ["g", "9"]
    for char in newchars:
        chars.append(char)
    return chars


# noinspection SpellCheckingInspection
def hallsgapchars():
    """generates list of characters to convert for the halls gap game_map"""
    chars = araratchars()
    newchars = ["h", "0"]
    for char in newchars:
        chars.append(char)
    return chars

def horshamchars():
    """generates list of characters to convert for the horsham game_map"""
    chars = hallsgapchars()
    newchars = ["i", "o"]
    for char in newchars:
        chars.append(char)
    return chars

def sa_inlandchars():
    """generates list of characters to convert for the sa_inland game_map"""
    chars = horshamchars()
    newchars = ["j"]
    for char in newchars:
        chars.append(char)
    return chars

# ---------------------- character replacement ----------------------

def replacechars(chars, game_map):
    """replaces given characters in a game_map with the correct path characters"""
    for character in chars:
        # underscores
        if character in ["w", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]:
            game_map = game_map.replace(character, "_")
        # backslashes
        elif character in ["3", "4", "5", "7", "8", "9", "0"]:
            game_map = game_map.replace(character, "\\")
        # forward slashes
        elif character in ["y", "1", "2", "6"]:
            game_map = game_map.replace(character, "/")
        # pipes
        elif character in ["o"]:
            game_map = game_map.replace(character, "|")
        else:
            print("error: the", character, "character has not been included in the replacechars() function")

    return game_map

# ---------------------- main ----------------------

def game_maps(location):

    game_map = r"""
        .....                                                                                                 
        :    :..........                                                                                      
        :              :.                                                                                     
        :                :                                                                                    
        :                 :........                                                                           
        :                          :                                                                          
        :                          :                                                                          
        :                           :.                                                                        
        :                             :....                                                                   
        :                                  :.                                                                  
        :                                    :.                                                               
        :                                      :.    .........                   ....                         
        :                                        :...:        :.............. .:     :..                      
        :                                                                    :         :                      
        :                                                                               :                     
        :                                                                                :                    
        :                                                                                :                    
        >jjjjjjjjjjjjjjj)                                                                 :....               
        :               o                                                                      :...           
        :               oi(hh                                                                      :....      
        :                    0h*gggggg                                                                  :.... 
        :                             9g&fffffff                                                          ..: 
        <www                                    8zz[                                     ................:    
        :   7                                 aa1 ...                                ...:                     
        :... 7   eeeeeeeee                   1 ..:   :                           ...:                         
            : 7^6....   . 5%dd             ]1 .:  :  :.  ..                    .:                             
             :..:    :.: :... 4$cc     {bb2..:     :   :: :                  .:                               
                             :... 3}kky ..:               :..            ...:                                 
                                 :.....:                     :.       ..:                                     
                                                               :....  :                                       
                                                                    :.:"""

    characters = ["w", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "o",
                  "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    landmarks = ["[", "]", "{", "}", "$", "%", "%", "^", "<", "&", "*", "(", ")", ">"]

    if location == "melbourne":
        temp_game_map = game_map
        tempchars = []
        temp_game_map = replacechars(tempchars, temp_game_map)
        temp_game_map = temp_game_map.replace("[", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "geelong":
        temp_game_map = game_map
        tempchars = geelongchars()
        temp_game_map = replacechars(tempchars, temp_game_map)
        temp_game_map = temp_game_map.replace("]", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "lorne":
        temp_game_map = game_map
        tempchars = lornechars()
        temp_game_map = replacechars(tempchars, temp_game_map)
        temp_game_map = temp_game_map.replace("{", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "apollo":
        temp_game_map = game_map
        tempchars = apollochars()
        temp_game_map = replacechars(tempchars, temp_game_map)
        temp_game_map = temp_game_map.replace("}", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "apostle":
        temp_game_map = game_map
        tempchars = apostlechars()
        temp_game_map = replacechars(tempchars, temp_game_map)
        temp_game_map = temp_game_map.replace("$", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "warrnambool":
        temp_game_map = game_map
        tempchars = warrnamboolchars()
        temp_game_map = replacechars(tempchars, temp_game_map)
        temp_game_map = temp_game_map.replace("%", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "portland":
        temp_game_map = game_map
        tempchars = portlandchars()
        temp_game_map = replacechars(tempchars, temp_game_map)
        temp_game_map = temp_game_map.replace("^", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "sa_coastal":
        temp_game_map = game_map
        tempchars = sa_coastalchars()
        temp_game_map = replacechars(tempchars, temp_game_map)
        temp_game_map = temp_game_map.replace("<", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "ballarat":
        temp_game_map = game_map
        tempchars = ballaratchars()
        temp_game_map = replacechars(tempchars, temp_game_map)
        temp_game_map = temp_game_map.replace("&", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "ararat":
        temp_game_map = game_map
        tempchars = araratchars()
        temp_game_map = replacechars(tempchars, temp_game_map)
        temp_game_map = temp_game_map.replace("*", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "hallsgap":
        temp_game_map = game_map
        tempchars = hallsgapchars()
        temp_game_map = replacechars(tempchars, temp_game_map)
        temp_game_map = temp_game_map.replace("(", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "horsham":
        temp_game_map = game_map
        tempchars = horshamchars()
        temp_game_map = replacechars(tempchars, temp_game_map)
        temp_game_map = temp_game_map.replace(")", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "sa_inland":
        temp_game_map = game_map
        tempchars = sa_inlandchars()
        temp_game_map = replacechars(tempchars, temp_game_map)
        temp_game_map = temp_game_map.replace(">", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    else:
        temp_game_map = "error: game_map has not been coded yet"

    print(temp_game_map)