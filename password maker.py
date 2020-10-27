
#import string and random module
import string
import random
if __name__ == '__main__':
    #using ascii function of string module 
    s1=string.ascii_letters
    s2=string.digits
    s3=string.punctuation
    #name of the site for which you are creating password
    site=input("enter the name of site")
    #length of password
    passlen=int(input("Enter the number of length of your password:\n"))
    s=[]
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    
    #suffling the password 
    random.shuffle(s)
    print("".join(s[0:passlen]))

    #creating a file
    with open ("passcreator.txt","a") as f:
        #writing in a file
        f.write(f'\n{site} :'+"".join(s[0:passlen]))
        f.close()
