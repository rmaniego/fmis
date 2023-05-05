import sample
from modules import inventory

def main():
    print("#"*50)
    print(" Farm Management Information System")
    print("#"*50)
    
    print("")
    print("*"*50)
    username = input("Enter your username: ")
    print("-"*50)
    sample.hello(username)
    print("-"*50)
    
    
    print("")
    print("*"*50)
    farm = input(" What is the name of the farm: ")
    
    fmis = sample.FMIS(farm)
    fmis.welcome()
    
    inventory.inventory()

if __name__ == "__main__":
    main()