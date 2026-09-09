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

def geelong_chars():
    """generates list of characters to convert for the geelong game_map"""
    chars = ["z", "1", "a"]
    return chars

def lorne_chars():
    """generates list of characters to convert for the lorne game_map"""
    chars = geelong_chars()
    new_chars = ["b", "2"]
    for char in new_chars:
        chars.append(char)
    return chars

def apollo_chars():
    """generates list of characters to convert for the apollo game_map"""
    chars = lorne_chars()
    new_chars = ["k", "y"]
    for char in new_chars:
        chars.append(char)
    return chars

def apostle_chars():
    """generates list of characters to convert for the apostle game_map"""
    chars = apollo_chars()
    new_chars = ["c", "3"]
    for char in new_chars:
        chars.append(char)
    return chars

def warrnambool_chars():
    """generates list of characters to convert for the warrnambool game_map"""
    chars = apostle_chars()
    new_chars = ["d", "4"]
    for char in new_chars:
        chars.append(char)
    return chars

def portland_chars():
    """generates list of characters to convert for the portland game_map"""
    chars = warrnambool_chars()
    new_chars = ["e", "5", "6"]
    for char in new_chars:
        chars.append(char)
    return chars

def sa_coastal_chars():
    """generates list of characters to convert for the sa_coastal game_map"""
    chars = portland_chars()
    new_chars = ["w", "7"]
    for char in new_chars:
        chars.append(char)
    return chars

# ---------------------- character generators - inland route ----------------------

def ballarat_chars():
    """generates list of characters to convert for the ballarat game_map"""
    chars = ["z", "8", "f"]
    return chars

def ararat_chars():
    """generates list of characters to convert for the ararat game_map"""
    chars =  ballarat_chars()
    new_chars = ["g", "9"]
    for char in new_chars:
        chars.append(char)
    return chars


# noinspection SpellCheckingInspection
def halls_gap_chars():
    """generates list of characters to convert for the halls gap game_map"""
    chars = ararat_chars()
    new_chars = ["h", "0"]
    for char in new_chars:
        chars.append(char)
    return chars

def horsham_chars():
    """generates list of characters to convert for the horsham game_map"""
    chars = halls_gap_chars()
    new_chars = ["i", "o"]
    for char in new_chars:
        chars.append(char)
    return chars

def sa_inland_chars():
    """generates list of characters to convert for the sa_inland game_map"""
    chars = horsham_chars()
    new_chars = ["j"]
    for char in new_chars:
        chars.append(char)
    return chars

# ---------------------- character replacement ----------------------

def replace_chars(chars, game_map):
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
            print("error: the", character, "character has not been included in the replace_chars() function")

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
        temp_chars = []
        temp_game_map = replace_chars(temp_chars, temp_game_map)
        temp_game_map = temp_game_map.replace("[", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "geelong":
        temp_game_map = game_map
        temp_chars = geelong_chars()
        temp_game_map = replace_chars(temp_chars, temp_game_map)
        temp_game_map = temp_game_map.replace("]", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "lorne":
        temp_game_map = game_map
        temp_chars = lorne_chars()
        temp_game_map = replace_chars(temp_chars, temp_game_map)
        temp_game_map = temp_game_map.replace("{", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "apollo":
        temp_game_map = game_map
        temp_chars = apollo_chars()
        temp_game_map = replace_chars(temp_chars, temp_game_map)
        temp_game_map = temp_game_map.replace("}", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "apostle":
        temp_game_map = game_map
        temp_chars = apostle_chars()
        temp_game_map = replace_chars(temp_chars, temp_game_map)
        temp_game_map = temp_game_map.replace("$", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "warrnambool":
        temp_game_map = game_map
        temp_chars = warrnambool_chars()
        temp_game_map = replace_chars(temp_chars, temp_game_map)
        temp_game_map = temp_game_map.replace("%", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "portland":
        temp_game_map = game_map
        temp_chars = portland_chars()
        temp_game_map = replace_chars(temp_chars, temp_game_map)
        temp_game_map = temp_game_map.replace("^", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "sa_coastal":
        temp_game_map = game_map
        temp_chars = sa_coastal_chars()
        temp_game_map = replace_chars(temp_chars, temp_game_map)
        temp_game_map = temp_game_map.replace("<", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "ballarat":
        temp_game_map = game_map
        temp_chars = ballarat_chars()
        temp_game_map = replace_chars(temp_chars, temp_game_map)
        temp_game_map = temp_game_map.replace("&", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "ararat":
        temp_game_map = game_map
        temp_chars = ararat_chars()
        temp_game_map = replace_chars(temp_chars, temp_game_map)
        temp_game_map = temp_game_map.replace("*", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "hallsgap":
        temp_game_map = game_map
        temp_chars = halls_gap_chars()
        temp_game_map = replace_chars(temp_chars, temp_game_map)
        temp_game_map = temp_game_map.replace("(", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "horsham":
        temp_game_map = game_map
        temp_chars = horsham_chars()
        temp_game_map = replace_chars(temp_chars, temp_game_map)
        temp_game_map = temp_game_map.replace(")", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    elif location == "sa_inland":
        temp_game_map = game_map
        temp_chars = sa_inland_chars()
        temp_game_map = replace_chars(temp_chars, temp_game_map)
        temp_game_map = temp_game_map.replace(">", "X")
        temp_game_map = common.erase(characters, landmarks, temp_game_map)

    else:
        temp_game_map = "error: game_map has not been coded yet"

    print(temp_game_map)
