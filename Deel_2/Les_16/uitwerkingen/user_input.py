# def get():
#     user_input = input('voer een waarde in :')
#     return user_input
#
# def get_letter (prompt):
#     while True:
#         user_input = input(prompt)
#         if len(user_input) == 1  :
#             return user_input.upper()
#         else:
#             print('ongeldige invoer. voer een enkele letter in ')
#
# def get_integer (prompt):
#     while True:
#         try:
#             user_input = input(prompt)
#             integer_value = int(user_input)
#             return integer_value
#         except ValueError:
#             print('ongeldige in voer !! ,', prompt)
# def get_float (prompt):
#     while True:
#         try:
#             user_input = input(prompt)
#             float_value = float(user_input)
#             return float_value
#         except ValueError:
#             print('ongeldige in voer !! ,', prompt)
#
# def get_string(prompt):
#     user_input = str(input(prompt))
#     return user_input





def get_integer(prompt):
    while True:
        try:
            user_input = int(input(prompt))
        # integer_value = user_input
            return user_input
        except ValueError:
            print('ongeldige invoer', prompt)

def get_float(prompt):
    try:
        user_input = float(input(prompt))
        return user_input

    except ValueError:
        print('ongeldige invoer ', prompt)