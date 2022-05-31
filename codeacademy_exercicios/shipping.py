# Sal's shippers shipping calculation

print("Welcome to Sal's shipping calculator!")
pckg_weight = float(input('Insert your package weight, in pounds: '))

# if shipped by ground:

if pckg_weight <= 2:
    g_price = 1.5 * pckg_weight + 20
elif pckg_weight <= 6:
    g_price = 3 * pckg_weight + 20
elif pckg_weight <= 10:
    g_price = 4 * pckg_weight + 20
else:
    g_price = 4.75 * pckg_weight + 20

# if shipped by ground premium:

flt_chrg = 125.0

# if shipped by drone:

if pckg_weight <= 2:
    d_price = 4.5 * pckg_weight
elif pckg_weight <= 6:
    d_price = 9 * pckg_weight
elif pckg_weight <= 10:
    d_price = 12 * pckg_weight
else:
    d_price = 14.25 * pckg_weight

# Calculating the min price for shipping:

min_price = min(g_price, flt_chrg, d_price)
if min_price == g_price:
    print("The cheapest shipping method is Ground, costing " + '$' + "{:.2f}".format(g_price) + ".")
elif min_price == flt_chrg:
    print("The cheapest shipping method is Ground Shipping Premium, costing " + '$' + "{:.2f}".format(flt_chrg) + ".")
else:
    print("The cheapest shipping method is Drone Shipping, costing " + '$' + "{:.2f}".format(d_price) + ".")
