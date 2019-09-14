import re

def validasiusername():
    pattern = '^[a-zA-Z0-9]{5,9}$'
    result = re.match(pattern, test_string)
    if result:
        print("Search successful.")
        return True
    else:
        print("Search unsuccessful.")
        return False
    	
def validasipassword():
    pattern = '^[a-zA-Z0-9@]{8,}$'
    result = re.match(pattern, test_string)
    if result:
        print("Search successful.")
        return True
    else:
        print("Search unsuccessful.")
        return False

test_string=str(input('Username : '))
validasiusername()
test_string=str(input('Password : '))
validasipassword()


