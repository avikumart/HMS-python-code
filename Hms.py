


def getdate():
    import datetime
    return datetime.datetime.now()

var1 = str(input("name of your client:" ))

if var1 == "harry":
    v2=int(input("choose 1 or 2: "))
    if v2 == 1:
        x=open("r1.py" , "rt")
        print(x.read())
    else:
        y=open("r2.py","rt")
        y.read()
else:
    pass






