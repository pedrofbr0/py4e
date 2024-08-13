# hrs = input("Enter Hours:")
# h = float(hrs)
# rate = input("Enter Rate Per Hour:")
# r = float(rate)
#
# if h <= 40:
#     #pay of <= 40 hrs:
#     print("Regular")
#     print(h*r)
# else:
#     #pay of > 40 hrs:
#     print("Overtime")
#     print(40*r+1.5*r*(h-40)) # 40 hrs will be paid regularly and "h-40" will be paid 1.5 times greate than the regular rate

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate Per Hour:")
r = float(rate)

regpay = h*r
overpay = (h-40)*(1.5-1)*r

if h <= 40:
    print(regpay)
else:
    print(regpay+overpay)
