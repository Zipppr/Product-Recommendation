from product_data import products
print("Product Catalog Preview:")
for product in products[:5:]:
    print(product)


customer_preferences = []

response = ""
while response != "N":
    preference = input("Input a preference: ")
    customer_preferences.append(preference)
    response = input("Do you want to add another preference? (Y/N): ").upper()
  

customer_pref_set = set(customer_preferences)


converted_products = []
for product in products:
    converted_products.append({
        "name": product["name"],
        "tags": set(product["tags"])
    })



def count_matches(product_tags, customer_tags):
    """
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    """
    return len(product_tags & customer_tags)
   




def recommend_products(products, customer_tags):
    """
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    """
    recommendations = []
    for product in products:  
        matches = count_matches(product["tags"], customer_tags)
        if matches > 0:
            recommendations.append((product["name"], matches))
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations

    



recommended = recommend_products(converted_products, customer_pref_set)
print("\nRecommended Products:")
for name, matches in recommended:
    print(f"- {name} ({matches} match(es))")



# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# I set intersections to find matching tags efficiently.
# Added loops to iterate though products and count matches.
# Added lists to store products and preferences, and added sets to remove duplicates.
# 2. How might this code change if you had 1000+ products?
# I would make the recommendation system more scalable by indexing tags using dictionaries, so that each tag is mapped to the product tthat contains it.
