def ispresent(person):
    names = ["Al", "Bo", "Chi", "Ha"]
    if person in names:
        return True
    else:
        return False
    
def nodigit(person):
    if person.isalpha():
        return True
    else:
        return False