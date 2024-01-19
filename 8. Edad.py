import time

def calculate_age(birth_year, birth_month, birth_day):
    # Get the current date
    current_time = time.localtime()

    # Calculate the user's age
    age = current_time.tm_year - birth_year - 1

    # Check if the user has already had their birthday this year
    if current_time.tm_mon > birth_month or (current_time.tm_mon == birth_month and current_time.tm_mday >= birth_day):
        age += 1

    return age

# Get the user's birthdate
birth_day = int(input("Ingrese el dia de su nacimiento: "))
birth_month = int(input("Ingrese el mes de su nacimiento: "))
birth_year = int(input("Ingrese el año de su nacimiento: "))

# Calculate the user's age
age = calculate_age(birth_year, birth_month, birth_day)

print(f"Usted tiene {age} años.")
