# def computepay(h,r):
#     regpay = h*r
#     overpay = (h-40)*r*1.5
#     if h <= 40:
#         return regpay
#     else:
#         return regpay+overpay-(h-40)*r # "(h-40)*r" stands for the
#         # excess hour paid in regular rate
#
# hrs = input("Enter Hours:")
# h = float(hrs)
# rate = input("Enter Rate:")
# r = float(rate)
# p = computepay(h,r)
# print("Pay",p)

def computepay(h,r):
    if h <= 40:
        return h*r
    else:
        return 40*r+(h-40)*r*1.5

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
p = computepay(h,r)
print("Pay",p)
