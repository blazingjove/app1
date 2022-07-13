from datetime import date
 
def age(birthdate):
    today = date.today()
    realAge = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return realAge

