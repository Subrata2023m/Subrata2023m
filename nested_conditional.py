

name = "subrata mishra"
phone = "07001952675"
email = "s"

if(len(name)==0 or len(phone)==0): #name=0,phone=1} name or phone
    print("failed")
else:
    if(len(name)<2 or len(name)>6):
         print("the minimum name length must be between 2 and 6")
    elif(len(phone)!=10):
        print("phone number size must be 10")
       
    else:
        print("success")