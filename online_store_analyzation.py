import codecademylib3
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

#Inspect
print(visits.head(10))
print(cart.head(10))
print(checkout.head(10))
print(purchase.head(10))

#combine visits&cart
visit_cart = pd.merge(visits,cart, how="left")
#print(visit_cart)

#how long is DF
print(len(visit_cart))
#how many null
timestamps_null = visit_cart[visit_cart.cart_time.isnull()]
print(len(timestamps_null))

#percente_not_buy = 
mean = float((len(timestamps_null)/len(visit_cart))*100)
print(str(mean) + "%")

#cart and checkout
catr_checkout = pd.merge(cart,checkout, how="left")
#how many null
catr_checkout_null = catr_checkout[catr_checkout.checkout_time .isnull()]
print(len(catr_checkout_null))
#how many not proceed xheckout
mean = round((len(catr_checkout_null)/len(catr_checkout))*100,2)
print(str(mean) + "%")

#merging all 4
all_data = visits.merge(cart, how="left").merge(checkout, how = "left").merge(purchase, how="left")
print(all_data.head(10))

#weekest funell
#also calculations done
len_all_data = len(all_data)
visit_null = all_data[all_data.visit_time .isnull()]
cart_null = all_data[all_data.cart_time .isnull()]
cart_null_per = round((len(cart_null)/len_all_data)*100,1) 
chechout_null = all_data[all_data.checkout_time .isnull()]
chechout_null_per = round((len(chechout_null)/len_all_data)*100,1) 
purchase_null = all_data[all_data.purchase_time .isnull()]
purchase_null_per = round((len(purchase_null)/len_all_data)*100,1) 

#printing calc out
print("Percentage of users not comleting visit is: " + str(len(visit_null)/len_all_data) + "%")
print("Percentage of users not comleting cart itme: " + str(cart_null_per) + "%")
print("Percentage of users not comleting checkout: " + str(chechout_null_per) + "%")
print("Percentage of users not comleting purchase: " + str(purchase_null_per) + "%")

#average time from visit to final purchase
all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
#print(all_data.time_to_purchase)
avg_time_purchase = all_data.time_to_purchase.mean()
print("Average time to purchase is: " + str(avg_time_purchase))
