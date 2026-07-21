#Function-Data cleaning
def clean_ph_no(raw):
    digit=" "
    for item in raw:
        if item.isdigit():
            digit+=item
    return digit[-10:] # -10: means last 10 digits of the number
ph_1="+91-98765 43201"
ph_2="(987) 654-3210"
ph_3="98765.43210"

print(clean_ph_no(ph_1))
print(clean_ph_no(ph_2))
print(clean_ph_no(ph_3))

