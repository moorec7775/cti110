# CTI-110
# P3HW2 - Shipping Charges
# Colin Moore
# 10/07/2018
#

weightOfPackage = int(input('Please input the weight of the package: '))

if weightOfPackage <= 2:
    shippingCharges = 1.50
elif weightOfPackage < 7:
    shippingCharges = 3.00
elif weightOfPackage < 11:
    shippingCharges = 4.00
else:
    shippingCharges = 4.75
print('\nFor a package weighing ' + str( weightOfPackage )  + \
      ", you'll pay $" + format( shippingCharges, ",.2f" ) + " per pound.")
  

