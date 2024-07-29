def trycatch():
    try:
        a=5
        b=0
        print(a/b)
    except Exception as error:
        print("Error Occured",error)
    else:
        print("Error not recured")
    finally:
        print("Program Executed Successfully")
trycatch()

print("Hello World")