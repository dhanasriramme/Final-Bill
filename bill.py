fy = input()
quantity = int(input())
distance = int(input())

if (food_type == 'V' or fy == 'N') and quantity >= 1 and distance > 0:
    if fy == 'V':
        cc = 120
    else:
        cc = 150

    delivery_charge = 0
    if distance <= 3:
        delivery_charge = 0
    elif distance <= 6:
        delivery_charge = 3 * (distance - 3)
    else:
        delivery_charge = 3 * 3 + 6 * (distance - 6)

    final_bill = cc * quantity + delivery_charge

    print(final_bill)
else:
    final_bill = -1
    print(final_bill)
