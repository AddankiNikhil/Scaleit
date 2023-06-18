def verifier(user):
    spc="!@#$%^&*()-=+_/<>;'"
    spc2 = "!#$%^&*()-=+_/<>;'"
    if user[0]in spc:
         return "The beginning of the given mail.",False

    elif len(user)>64:
        return "Too Long Email.",False

    elif user.count("@")>1:
        return "Can Only have One @ symbol in a Mail",False
    else:
        for i in spc2:
            if i in user:
                return "Invalid Characters Present in the mail. \n",False
        return "",True

user_name=input("Enter The Email : \t")
res=verifier(user_name)
if res[1]:
    user = user_name.split("@")
    print(f"The Username is :{user[0]} \nThe Domain is :{user[1]}")
else:
    print(f"The Given Mail is Invalid .Because Of {res[0]}")

