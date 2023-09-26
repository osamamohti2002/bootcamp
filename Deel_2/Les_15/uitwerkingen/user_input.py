def get_integer(prompt):
    user_input = int(input(prompt))
    return user_input

def get_float (vraag):
    user_input = float(input(vraag))
    return user_input

def get_sting(prompt):
    user_input = str(input(prompt))
    return user_input

def get_letter (prompt):
    while True:
        user_input = input(prompt)
        if len(user_input) == 1 :
            return user_input.upper()
        else:
            print('ongeldige waarde')





















# def get():
#     user_input = input("Voer een waarde in: ")
#     return user_input
#
# def get_letter(prompt):
#     while True:
#         user_input = input(prompt)
#         if len(user_input) == 1 and user_input.isalpha():
#             return user_input.upper()
#         else:
#             print("Ongeldige invoer. Voer een enkele letter in.")
#
# def get_integer(prompt):
#     while True:
#         user_input = input(prompt)
#         try:
#             integer_value = int(user_input)
#             return integer_value
#         except ValueError:
#             print("Ongeldige invoer. Voer een geheel getal in.")
#
# def get_float(prompt):
#     while True:
#         user_input = input(prompt)
#         try:
#             float_value = float(user_input)
#             return float_value
#         except ValueError:
#             print("Ongeldige invoer. Voer een kommagetal in.")
#
# def get_string(prompt):
#     user_input = input(prompt)
#     return user_input
