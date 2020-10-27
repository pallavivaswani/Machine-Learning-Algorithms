#importing libraries and dataset
import pandas as pd
import numpy as np
data = pd.read_csv("dataset.csv")

#converting columns to list
color = list(data['Colour'].values)
brand = list(data['Brand'].values)
month = list(data['Month'].values)
price = list(data['Price'].values)
buy = list(data['Purchased?'].values)

#making manipulation
month_count = len(month)
yes= buy.count('yes')
no= buy.count('no')

#colour
red_y, red_n = 0,0
yellow_y, yellow_n = 0,0
#brand
levi_y, levi_n = 0,0
reebok_y, reebok_n = 0,0
#month
q1_y, q1_n = 0,0
q2_y, q2_n = 0,0
q3_y, q3_n = 0,0
q4_y, q4_n = 0,0

for l in range(month_count):
    if buy[l] == 'Yes':
        if color[l] == 'Red' : red_y +=1
        if color[l] == 'Yellow' : yellow_y +=1
        if brand[l] == 'Levi' : levi_y +=1
        if brand[l] == 'Reebok' : reebok_y +=1
        if month[l] == 'Q1' : q1_y +=1
        if month[l] == 'Q2' : q2_y +=1
        if month[l] == 'Q3' : q3_y +=1
        if month[l] == 'Q4' : q4_y +=1
    if buy[l] == 'No':
        if color[l] == 'Red' : red_n +=1
        if color[l] == 'Yellow' : yellow_n +=1
        if brand[l] == 'Levi' : levi_n +=1
        if brand[l] == 'Reebok' : reebok_n +=1
        if month[l] == 'Q1' : q1_n +=1
        if month[l] == 'Q2' : q2_n +=1
        if month[l] == 'Q3' : q3_n +=1
        if month[l] == 'Q4' : q4_n +=1
            
red_y /= yes
red_n /= no
yellow_y /= yes
yellow_n /= no 
levi_y /= yes
levi_n /= no
reebok_y /= yes
reebok_n = no
q1_y /= yes
q1_n /= no
q2_y /= yes
q2_n /= no
q3_y /= yes
q3_n /= no
q4_y /= yes
q4_n /= no

#taking input
colour_i = input("Enter the Colour of product: ")
brand_i = input("Enter the Brand of product: ")
month_i = input("Enter the Month of purchase: ")
if (month_i =='January' or month_i =='February' or month_i =='March'):
	month_i='Q1'
elif (month_i =='April' or month_i =='May' or month_i =='June'):
	month_i='Q2'
elif (month_i =='July' or month_i =='August' or month_i =='September'):
	month_i='Q3'
else:
	month_i='Q4'
print("Quarter =",month_i)
y,n = 0,0
if(colour_i == 'Red'):
    if(brand_i == 'Levi'):
        if(month_i == 'Q1'):
                y = red_y * levi_y * q1_y * (yes/month_count)
                n = red_n * levi_n * q1_n * (no/month_count)
        elif(month_i == 'Q2'):
                y = red_y * levi_y * q2_y * (yes/month_count)
                n = red_n * levi_n * q2_n * (no/month_count)
        elif(month_i == 'Q3'):
                y = red_y * levi_y * q3_y * (yes/month_count)
                n = red_n * levi_n * q3_n * (no/month_count)
        elif(month_i == 'Q4'):
                y = red_y * levi_y * q4_y * (yes/month_count)
                n = red_n * levi_n * q4_n * (no/month_count)
                
    elif(brand_i == 'Reebok'):
        if(month_i == 'Q1'):
                y = red_y * reebok_y * q1_y * (yes/month_count)
                n = red_n * reebok_n * q1_n * (no/month_count)
        elif(month_i == 'Q2'):
                y = red_y * reebok_y * q2_y * (yes/month_count)
                n = red_n * reebok_n * q2_n * (no/month_count)
        elif(month_i == 'Q3'):
                y = red_y * reebok_y * q3_y * (yes/month_count)
                n = red_n * reebok_n * q3_n * (no/month_count)
        elif(month_i == 'Q4'):
                y = red_y * reebok_y * q4_y * (yes/month_count)
                n = red_n * reebok_n * q4_n * (no/month_count)
                
elif(colour_i == 'Yellow'):
    if(brand_i == 'Levi'):
        if(month_i == 'Q1'):
                y = yellow_y * levi_y * q1_y * (yes/month_count)
                n = yellow_n * levi_n * q1_n * (no/month_count)
        elif(month_i == 'Q2'):
                y = yellow_y * levi_y * q2_y * (yes/month_count)
                n = yellow_n * levi_n * q2_n * (no/month_count)
        elif(month_i == 'Q3'):
                y = yellow_y * levi_y * q3_y * (yes/month_count)
                n = yellow_n * levi_n * q3_n * (no/month_count)
        elif(month_i == 'Q4'):
                y = yellow_y * levi_y * q4_y * (yes/month_count)
                n = yellow_n * levi_n * q4_n * (no/month_count)
                
    elif(brand_i == 'Reebok'):
        if(month_i == 'Q1'):
                y = yellow_y * reebok_y * q1_y * (yes/month_count)
                n = yellow_n * reebok_n * q1_n * (no/month_count)
        elif(month_i == 'Q2'):
                y = yellow_y * reebok_y * q2_y * (yes/month_count)
                n = yellow_n * reebok_n * q2_n * (no/month_count)
        elif(month_i == 'Q3'):
                y = yellow_y * reebok_y * q3_y * (yes/month_count)
                n = yellow_n * reebok_n * q3_n * (no/month_count)
        elif(month_i == 'Q4'):
                y = yellow_y * reebok_y * q4_y * (yes/month_count)
                n = yellow_n * reebok_n * q4_n * (no/month_count)
                
if ( y > n ):
    print("Yes")
else:
    print("No")            

