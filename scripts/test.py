from src import pred
prediction1 = pred("Hi how are you doing?")
print("SMS - *Hi how are you doing?*, Prediction - "+prediction1)

prediction2 = pred("Buy 3 pillows at the rate of 1. Visit www.walmart.com")
print("SMS - *Buy 3 pillows at the rate of 1!! HurryUp!! Visit https://www.walmart.com*, Prediction - "+prediction2)

prediction3 = pred("You won $150000 lottery. Claim now!!!! call 1800180180")
print("SMS - *You won $150000 lottery. Claim now!!!! call 1800180180*, Prediction - "+prediction3)