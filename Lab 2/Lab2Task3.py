cover_price=25.00
discount_perc=40
fixed_delivery_cost=5.50
unit_delivery_cost=0.55
order_qty=350

calculate_delivery_cost=fixed_delivery_cost+(unit_delivery_cost*order_qty)

bookprice = cover_price*order_qty

costof_books = bookprice-(bookprice*discount_perc/100)

print("final cost of books is: ", costof_books+calculate_delivery_cost)
print("cost of books is: ", bookprice-(bookprice*discount_perc/100))
print("delivery cost is: ", calculate_delivery_cost)