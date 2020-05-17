
class a:
    
    def adding():
        import Account_Saver
    def values():
        f = open('Accounts.txt','r')
        f_values = f.read()
        print(f_values)
    def checking():
        what = input("Search the account: ")
        f = open('Accounts.txt','r')
        if what in "Accounts.txt":
            print("exists")
        else:
            print("can't locate the account :(")

exit_var = 1
while exit_var:
    checkup = input("Check , Add, View : ")
    if checkup == "view":
        a.values()
        
        
    if checkup == "check":
        a.checking()
    if checkup == "add":
        a.adding()
if exit_var == "q":
    exit_var = 0
