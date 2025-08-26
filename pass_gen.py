import random
import string
try:
    amount = int(input("Enter the amount of symbols: "))
except:
    print("Not a valid number!")

def generaterandomstring(length):
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def main():
    print(generaterandomstring(amount))

if __name__=="__main__":
    main()