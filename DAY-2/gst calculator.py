# GST calculator
amt = float(input('enter amount (in ₹): '))
gst = float(input('enter gst %: '))
gst_amt = (amt*(gst/100))
net_gst = amt + gst_amt 
print(f'''Gst Amount = ₹ {gst_amt}
Net Amount = ₹ {net_gst}
''')