def main():
    price=50

    while True:
        amount=int(input("Insert Coin:"))
        if amount in [5,10,25]:
            price=price-amount
            if price>0:
                print("Amount Due:",price)

            elif price<0:
                print("Change Owed:",abs(price))

                break
            elif price==0:
                print("Change Owed:",0)
                break
        elif amount>=50:

            print("Change Owed:",amount-price)
            break
        else:
            print("Amount Due:",price)


if __name__=="__main__":
    main()