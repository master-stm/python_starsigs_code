#determains the user's horoscope

#takes the user's birthdate and split the inputby / into a list
birthDate = input("Enter Date of Birth (d/m/yyyy) : ").split("/")
#print(birthDate)
#compares the birth date with the horoscope signs

#this statement checks the given month
if birthDate[1] == '1':
#this statement checks the given day
    if birthDate[0] <= '19':
        fh = open("starsigns\capricorn.txt", "r")
        print(fh.read())
    else:
        fh = open("starsigns\\aquarius.txt", "r")
        print(fh.read())
elif birthDate[1] == '2':
    if birthDate[0] <= '18':
        fh = open("starsigns\\aquarius.txt", "r")
        print(fh.read())
    else:
        fh = open("starsigns\pisces.txt", "r")
        print(fh.read())
elif birthDate[1] == '3':
    if birthDate[0] <= '20':
        fh = open("starsigns\pisces.txt", "r")
        print(fh.read())
    else:
        fh = open("starsigns\\aries.txt", "r")
        print(fh.read())
elif birthDate[1] == '4':
    if birthDate[0] <= '19':
        fh = open("starsigns\\aries.txt", "r")
        print(fh.read())
    else:
        fh = open("starsigns\\taurus.txt", "r")
        print(fh.read())
elif birthDate[1] == '5':
    if birthDate[0] <= '20':
        fh = open("starsigns\\taurus.txt", "r")
        print(fh.read())
    else:
        fh = open("starsigns\gemini.txt", "r")
        print(fh.read())
elif birthDate[1] == '6':
    if birthDate[0] <= '20':
        fh = open("starsigns\gemini.txt", "r")
        print(fh.read())
    else:
        fh = open("starsigns\cancer.txt", "r")
        print(fh.read())
elif birthDate[1] == '7':
    if birthDate[0] <= '22':
        fh = open("starsigns\cancer.txt", "r")
        print(fh.read())
    else:
        fh = open("starsigns\leo.txt", "r")
        print(fh.read())
elif birthDate[1] == '8':
    if birthDate[0] <= '22':
        fh = open("starsigns\leo.txt", "r")
        print(fh.read())
    else:
        fh = open("starsigns\\virgo.txt", "r")
        print(fh.read())
elif birthDate[1] == '9':
    if birthDate[0] <= '22':
        fh = open("starsigns\\virgo.txt", "r")
        print(fh.read())
    else:
        fh = open("starsigns\libra.txt", "r")
        print(fh.read())
elif birthDate[1] == '10':
    if birthDate[0] <= '22':
        fh = open("starsigns\libra.txt", "r")
        print(fh.read())
    else:
        fh = open("starsigns\scorpio.txt", "r")
        print(fh.read())
elif birthDate[1] == '11':
    if birthDate[0] <= '21':
        fh = open("starsigns\scorpio.txt", "r")
        print(fh.read())
    else:
        fh = open("starsigns\sagittarious.txt", "r")
        print(fh.read())
elif birthDate[1] == '12':
    if birthDate[0] <= '21':
        fh = open("starsigns\sagittarious.txt", "r")
        print(fh.read())
    else:
        fh = open("starsigns\capricorn.txt", "r")
        print(fh.read())
else:
    print("out of range")
