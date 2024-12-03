available_products = set(input("Въведете наличните продукти: ").split())

recipe_name = input("Въведете името на рецептата: ")

needed_products = set()
n = int(input("Въведете брой продукти за рецептата: "))
print("Въведете продуктите за рецептата: ")
for i in range(n):
    product = input()
    needed_products.add(product)

matching_products = available_products & needed_products
products_to_buy = needed_products - available_products
unnecessary_products = available_products - needed_products

print(f"There are {len(matching_products)} products for {recipe_name}: {', '.join(matching_products)}")
print(f"You need to buy {len(products_to_buy)} products: {', '.join(products_to_buy)}")
print(f"Unnecessary products: {', '.join(unnecessary_products)}")