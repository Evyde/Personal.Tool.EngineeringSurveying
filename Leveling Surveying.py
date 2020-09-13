sum = float(input())
while True:
    print("-" * 100)
    tmpS = input().split(' ')
    tmp = []
    for i in tmpS:
        tmp.append(int(i))
    hx, qx, hb, hr = tmp
    tmpS = input().split(' ')
    tmp = []
    for i in tmpS:
        tmp.append(int(i))
    hs, qs, qb, qr = tmp
    # print("后尺|下|上|后距|视距差\t前尺|下|上|前距|ω视距差\t\t黑面")
    print("后下\t%d\t前下\t%d\t后黑%d\t\t红%d" % (hx, qx, hb, hr))
    print("后上\t%d\t前上\t%d\t前黑%d\t\t红%d" % (hs, qs, qb, qr))
    if abs((hr - qr) + 100 - (hb - qb)) < abs((hr - qr) - 100 - (hb - qb)):
        min = (hr - qr) + 100# - (hb - qb)
    else:
        min = (hr - qr) - 100# - (hb - qb)
    print("后距\t%f\t前距\t%f\t后-前黑%d\t红%d\t%d" % ((hs - hx)/10, (qs - qx)/10, hb - qb, hr - qr, (hb - qb) - min))
    sum += ((hs - hx) - (qs - qx)) / 10
    print("视距差d\t%f\t视距差ωd\t%f\t中数\t%f" % (((hs - hx) - (qs - qx)) / 10, sum, (min + hb - qb) / 2))
    print("-" * 100)
