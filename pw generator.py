import pandas as pd
import string
import MyRNG as generator

rng = generator.MyRNG()

length = int(input("Password length: "))

""" upper_pool = 'ABCDEFGHJKLMNOPQRSTUVWXYZ' # Allowed characters
lower_pool = 'abcdefghijkmnopqrstuvwxyz'
num_pool = '1234567890'
char_pool = lower_pool + upper_pool + num_pool """

char_pool = string.ascii_letters + string.digits + string.punctuation

def generate_password(characters, length):
    output = ''
    characters = str(characters)

    for i in range(length):
        random = rng.gen_index(characters)
        output += random
    return output

passwords = []

for i in range(int(input("How many passwords? "))):
    passwords.append(generate_password(char_pool, length))

print(passwords)
#df = pd.DataFrame(passwords, columns=['Passwords'])
#df.to_excel(f'excel/output/{input("Choose the name of the output file: ")}.xlsx')