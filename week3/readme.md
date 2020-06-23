TODO: Reflect on what you learned this week and what is still unclear.

not_number_rejector - fix

old format:
("OK then, a number between {}".format(lowerBound) + " and {} ?".format(upperBound))

new format:
(f"OK then, a number between {lowerBound}" + f" and {upperBound} ?"

if upperBound <= 5:
        print("This number is lower or equal to 5!")

if lowerBound >= upperBound:
    print("Range needs to be lower!")