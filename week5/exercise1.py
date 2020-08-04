# -*- coding: UTF-8 -*-

import math
import requests

"""Refactoring.

This exercise contains a complete and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""


# This is a terrible function. The rest of the functions in this file do a
# much better job of what it's trying to do. Once you've has a little look,
# move on, and eventually delete this function. (And this comment!)
# def do_bunch_of_bad_things():
#     print("Getting ready to start in 9")
#     print("Getting ready to start in 8")
#     print("Getting ready to start in 7")
#     print("Getting ready to start in 6")
#     print("Getting ready to start in 5")
#     print("Getting ready to start in 4")
#     print("Getting ready to start in 3")
#     print("Getting ready to start in 2")
#     print("Getting ready to start in 1")
#     print("Let's go!")

#     triangle = {"base": 3, "height": 4}
#     triangle["hypotenuse"] = triangle["base"] ** 2 + triangle["height"] ** 2
#     print("area = " + str((triangle["base"] * triangle["height"]) / 2))
#     print("side lengths are:")
#     print("base: {}".format(triangle["base"]))
#     print("height: {}".format(triangle["height"]))
#     print("hypotenuse: {}".format(triangle["hypotenuse"]))

#     another_hyp = 5 ** 2 + 6 ** 2
#     print(another_hyp)


#     yet_another_hyp = 40 ** 2 + 30 ** 2
#     print(yet_another_hyp)


# return a list of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    # i = 0
    while start != (stop - 1):
        print(f"{message} {start}")
        start = start - 1
    print(f"{completion_message}")
    
    
    



# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    h = base ** 2 + height ** 2
    hsq = math.sqrt(h)
    return hsq


def calculate_area(base, height):
    a = 0.5 * base * height
    return a


def calculate_perimeter(base, height):
    p = base + height + (math.sqrt(base ** 2 + height ** 2))
    return p


def calculate_aspect(base, height):
    if height > base:
        return "tall"
    if base > height:
        return "wide"
    if base == height:
        return "equal"


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    return {
        "area": calculate_area(base, height),
        "perimeter": calculate_perimeter(base, height),
        "height": height,
        "base": base,
        "hypotenuse": calculate_hypotenuse(base, height),
        "aspect": calculate_aspect(base, height),
        "units": units,
    }


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = (
        "This triangle is {area}{units}²\n"
        "It has a perimeter of {perimeter}{units}\n"
        "This is a {aspect} triangle.\n"
    )


    a = calculate_area
    p = calculate_perimeter
    h = calculate_hypotenuse
    aspect = calculate_aspect
    if facts_dictionary["aspect"] == "tall":
        diagram = tall.format(**facts_dictionary)
    elif facts_dictionary["aspect"] == "wide":
        diagram = wide.format(**facts_dictionary)
    else:
        diagram = equal.format(**facts_dictionary)
    facts = pattern.format(**facts_dictionary)
    return( diagram + "\n" + facts)

    


def triangle_master(base, height, return_diagram=False, return_dictionary=False):
    facts = get_triangle_facts(base, height)
    right = tell_me_about_this_right_triangle(facts)
    if return_diagram and return_dictionary:
        return {"diagram": right,"facts": facts}
    elif return_diagram:
        return right
    elif return_dictionary:
        return facts
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    p = list(range(3, 21, 2))
    p.extend(list(range(20, 3, -2)))
    word_length = p
    words = list_of_words_with_lengths(word_length)
    return words


def get_a_word_of_length_n(length):
    import requests
    baseURL = (f"https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={length}")
    url = baseURL.format(length)
    r = requests.get(url)
    
    try:
        if r.status_code is 200:
            message = r.text
            return message
    except:
        print("failed a request", r.status_code)

def list_of_words_with_lengths(list_of_lengths):
    import requests
    p_list = []
    for i in list_of_lengths:
        p_list.append(get_a_word_of_length_n(i))

    return p_list


if __name__ == "__main__":
    countdown("We're about to start", 9, 1, "we finished, wheeeee!")
    triangle_master(3, 5)
    pyramid = wordy_pyramid()
    for word in pyramid:
        print(word)