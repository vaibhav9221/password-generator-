# import string
# import random
#
# if __name__ == '__main__':
#
#     # Letter Sets
#     s1 = string.ascii_letters
#     s2 = string.digits
#     s3 = string.punctuation
#     service_name = input("Enter the site: ")
#     plen = int(input("Enter the password length: "))
#
#     # Combining all the sets
#     s = []
#     s.extend(list(s1))
#     s.extend(list(s2))
#     s.extend(list(s3))
#     # print(s)
#     random.shuffle(s)
#     # print (s)
#
#     print("Your password is: ")
#     print("".join(s[0:plen]))
#
#
#     # Saving the password in the file
#     file = open("pass.txt" , "a")
#     file.write(f"\n{service_name} ; ")
#     file.write("".join(s[0:plen]))
#     file.close()
#
#     print("Password has been saved in the file.")
#
import string
import random
if __name__ == '__main__':
    s1=string.ascii_letters
    s2=string.digits
    s3=string.punctuation
    site=input("enter the name of site")
    passlen=int(input("Enter the number of length of your password:\n"))
    s=[]
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)

    random.shuffle(s)
    print("".join(s[0:passlen]))


    with open ("passcreator.txt","a") as f:
        f.write(f'\n{site} :'+"".join(s[0:passlen]))
        f.close()