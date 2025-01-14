def demo():
    try:
        a = int(input("Enter a number: "))
        print(float(a))
        return

    except Exception as e:
        print(e)
        return

    finally:              # finally runs even if try doesnt throw any error
        print("The end")  # and even after return 

demo()