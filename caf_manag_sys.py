import streamlit as st

menu = {
    "HOT BEVERAGES": {
        "Espresso": 300,
        "Americano": 350,
        "Cappuccino": 450,
        "Latte (Vanilla)": 500,
        "Latte (Caramel)": 500,
        "Latte (Hazelnut)": 500,
        "Latte (Almond)": 500,
        "Mocha": 550,
        "Macchiato": 400,
        "Flat White": 450,
        "Chai Latte": 400,
        "Hot Chocolate": 500,
        "Matcha Green Tea": 600
    },
    "COLD BEVERAGES": {
        "Iced Coffee (Black)": 300,
        "Iced Coffee (Latte)": 300,
        "Iced Coffee (Mocha)": 300,
        "Cold Brew Coffee": 400,
        "Iced Tea (Lemon, Peach, Green)": 300,
        "Milkshakes (Chocolate, Strawberry, Oreo, Banana)": 450,
        "Smoothies (Berry Blast, Mango, Avocado, Green Detox)": 500,
        "Fresh Lemonade": 280,
        "Iced Matcha Latte": 550,
        "Frappe (Coffee)": 480,
        "Coconut Water": 220,
        "Kombucha": 600
    },
    "PASTRIES AND BAKERY": {
        "Croissant (Plain)": 300,
        "Croissant (Almond)": 350,
        "Croissant (Chocolate)": 380,
        "Muffin (Blueberry)": 280,
        "Muffin (Chocolate)": 300,
        "Danish Pastry": 320,
        "Cinnamon Roll": 350,
        "Scone (Raisin)": 280,
        "Scone with Cream Cheese": 400,
        "Brownie": 350,
        "Cheesecake Slice": 500,
        "Doughnut (Glazed)": 250
    },
    "SANDWICHES AND LIGHT BITES": {
        "Classic Club Sandwich": 550,
        "Grilled Cheese Sandwich": 450,
        "Tuna Melt Sandwich": 500,
        "Egg & Avocado Toast": 480,
        "BLT Sandwich (Bacon, Lettuce, Tomato)": 550,
        "Caprese Sandwich": 500,
        "Turkey & Swiss Sandwich": 600,
        "Ham & Cheese Croissant": 580,
        "Veggie Wrap": 480,
        "Chicken Pesto Panini": 650
    },
    "DESSERTS AND SWEET TREATS": {
        "Tiramisu": 600,
        "Chocolate Lava Cake": 650,
        "Apple Pie": 500,
        "Red Velvet Cake Slice": 550,
        "Ice Cream (1 Scoop)": 250,
        "Ice Cream (2 Scoops)": 400,
        "Eclairs": 380,
        "Waffles with Maple Syrup": 500,
        "Panna Cotta": 550,
        "Churros with Chocolate Dip": 450,
        "Crepes (Nutella)": 600,
        "Crepes (Strawberry)": 600
    }
}

st.title("Welcome to Our Cafe!")

order = []
amount = []

# Display menu and category-specific selection
for category, items in menu.items():
    st.subheader(category)
    selected_items = st.multiselect(f"Select items from {category}", list(items.keys()), key=category)
    for item in selected_items:
        order.append(item)
        amount.append(items[item])

if order:
    st.success("Items added to your order.")

if st.button("Show Order Summary"):
    st.subheader("Your Order:")
    for i, itm in enumerate(order, 1):
        st.write(f"{i}- {itm}")

if st.button("Show Bill"):
    st.subheader("Bill Summary:")
    for itm, price in zip(order, amount):
        st.write(f"{itm}: Rs.{price}")
    
    st.subheader("Total Bill:")
    total_cost = sum(amount)
    st.write(f"Your total bill is Rs.{total_cost}")
