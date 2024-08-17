import pandas as pd
users_data = {
    "user_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "username": ["JohnDoe", "JaneSmith", "MikeBrown", "SarahJones", "AlexGreen", 
                 "EmilyWhite", "DavidBlack", "LauraGray", "KevinBrown", "NinaBlue"],
    "email": ["john@example.com", "jane@example.com", "mike@example.com", 
              "sarah@example.com", "alex@example.com", "emily@example.com", 
              "david@example.com", "laura@example.com", "kevin@example.com", "nina@example.com"],
    "password_hash": ["hash1", "hash2", "hash3", "hash4", "hash5", "hash6", 
                      "hash7", "hash8", "hash9", "hash10"],
    "phone_number": ["1234567890", "0987654321", "5551234567", "6669876543", 
                     "7771239876", "8883216549", "9997894561", "1112223333", 
                     "2223334444", "3334445555"],
    "address": ["123 Main St, NY", "456 Elm St, CA", "789 Oak St, TX", 
                "101 Pine St, FL", "202 Birch St, NV", "303 Cedar St, IL", 
                "404 Spruce St, OH", "505 Maple St, MI", "606 Willow St, PA", "707 Ash St, AZ"],
    "created_at": ["2024-08-01 12:00:00", "2024-08-02 13:00:00", "2024-08-03 14:00:00", 
                   "2024-08-04 15:00:00", "2024-08-05 16:00:00", "2024-08-06 17:00:00", 
                   "2024-08-07 18:00:00", "2024-08-08 19:00:00", "2024-08-09 20:00:00", "2024-08-10 21:00:00"],
    "updated_at": ["2024-08-10 14:00:00", "2024-08-11 15:00:00", "2024-08-12 16:00:00", 
                   "2024-08-13 17:00:00", "2024-08-14 18:00:00", "2024-08-15 19:00:00", 
                   "2024-08-16 20:00:00", "2024-08-17 21:00:00", "2024-08-18 22:00:00", "2024-08-19 23:00:00"]
}
users_df = pd.DataFrame(users_data)
products_data = {
    "product_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "product_name": ["T-Shirt", "Jeans", "Sneakers", "Jacket", "Watch", "Sunglasses", 
                     "Hat", "Backpack", "Belt", "Gloves"],
    "description": ["Cotton T-shirt, Red", "Denim jeans, Blue", "Running shoes, White", 
                    "Leather jacket, Black", "Analog watch, Silver", "Polarized sunglasses, Black", 
                    "Baseball cap, Blue", "Hiking backpack, Green", "Leather belt, Brown", "Winter gloves, Black"],
    "price": [19.99, 49.99, 69.99, 99.99, 149.99, 39.99, 15.99, 79.99, 29.99, 24.99],
    "category_id": [1, 1, 2, 1, 3, 4, 4, 5, 3, 5],
    "stock_quantity": [50, 40, 30, 20, 15, 60, 70, 25, 55, 35],
    "created_at": ["2024-08-01 12:00:00", "2024-08-02 13:00:00", "2024-08-03 14:00:00", 
                   "2024-08-04 15:00:00", "2024-08-05 16:00:00", "2024-08-06 17:00:00", 
                   "2024-08-07 18:00:00", "2024-08-08 19:00:00", "2024-08-09 20:00:00", "2024-08-10 21:00:00"],
    "updated_at": ["2024-08-10 14:00:00", "2024-08-11 15:00:00", "2024-08-12 16:00:00", 
                   "2024-08-13 17:00:00", "2024-08-14 18:00:00", "2024-08-15 19:00:00", 
                   "2024-08-16 20:00:00", "2024-08-17 21:00:00", "2024-08-18 22:00:00", "2024-08-19 23:00:00"]
}
products_df = pd.DataFrame(products_data)
categories_data = {
    "category_id": [1, 2, 3, 4, 5],
    "category_name": ["Clothing", "Footwear", "Accessories", "Eyewear", "Bags"]
}
categories_df = pd.DataFrame(categories_data)
ar_models_data = {
    "ar_model_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "product_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "model_url": ["/models/tshirt_red.glb", "/models/jeans_blue.glb", "/models/sneakers_white.glb", 
                  "/models/jacket_black.glb", "/models/watch_silver.glb", "/models/sunglasses_black.glb", 
                  "/models/hat_blue.glb", "/models/backpack_green.glb", "/models/belt_brown.glb", "/models/gloves_black.glb"],
    "model_type": ["3D"] * 10,
    "created_at": ["2024-08-01 12:00:00", "2024-08-02 13:00:00", "2024-08-03 14:00:00", 
                   "2024-08-04 15:00:00", "2024-08-05 16:00:00", "2024-08-06 17:00:00", 
                   "2024-08-07 18:00:00", "2024-08-08 19:00:00", "2024-08-09 20:00:00", "2024-08-10 21:00:00"],
    "updated_at": ["2024-08-10 14:00:00", "2024-08-11 15:00:00", "2024-08-12 16:00:00", 
                   "2024-08-13 17:00:00", "2024-08-14 18:00:00", "2024-08-15 19:00:00", 
                   "2024-08-16 20:00:00", "2024-08-17 21:00:00", "2024-08-18 22:00:00", "2024-08-19 23:00:00"]
}
ar_models_df = pd.DataFrame(ar_models_data)
shopping_sessions_data = {
    "session_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "user_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "session_start": ["2024-08-01 12:00:00", "2024-08-02 13:00:00", "2024-08-03 14:00:00", 
                      "2024-08-04 15:00:00", "2024-08-05 16:00:00", "2024-08-06 17:00:00", 
                      "2024-08-07 18:00:00",]}

print(products_df)

products_with_category = pd.merge(products_df, categories_df, on="category_id")

clothing_products = products_with_category[products_with_category['category_name'] == 'Clothing']
print(clothing_products)


products_ar_models = pd.merge(products_df, ar_models_df, on="product_id")
products_ar_models_with_category = pd.merge(products_ar_models, categories_df, on="category_id")

footwear_ar_models = products_ar_models_with_category[products_ar_models_with_category['category_name'] == 'Footwear']
print(footwear_ar_models[['product_name', 'model_url']])
