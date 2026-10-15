total =0

while True:

    user_input=(input("enter your expense and to close the program write exit:"))

    if user_input=="exit":
        print(f" your total expense is {total} and the program has been closed successfully.")
        break

   
    expense=int(user_input)
    total +=expense
    print(f"your total expense is {total}")



    