from django.shortcuts import render, redirect
from electronics.models import Product as ElectronicsProduct
from clothing.models import product as ClothingProduct
from grocery.models import Product as GroceryProduct

def add_to_cart(request, product_id, category):
    # Get the correct product model based on category
    if category == "electronics":
        product = ElectronicsProduct.objects.get(id=product_id)
    elif category == "clothing":
        product = ClothingProduct.objects.get(id=product_id)
    elif category == "grocery":
        product = GroceryProduct.objects.get(id=product_id)
    else:
        return redirect("home")

    # Initialize cart in session if not exists
    if "cart" not in request.session:
        request.session["cart"] = {}

    cart = request.session["cart"]

    product_key = f"{category}_{product.id}"

    if product_key in cart:
        cart[product_key]["quantity"] += 1  # Increase quantity
    else:
        cart[product_key] = {
            "id": product.id,
            "name": product.name,
            "price": float(product.price),
            "image": product.image.url if product.image else "",
            "quantity": 1,
            "category": category,
            "total_price": float(product.price),  # Initialize total price
        }

    request.session["cart"] = cart  # Save the cart in session
    request.session.modified = True  # Mark session as modified

    return redirect("view_cart")

def view_cart(request):
    cart = request.session.get("cart", {})

    # Update total price for each item
    for key, item in cart.items():
        item["total_price"] = item["price"] * item["quantity"]

    total_price = sum(item["total_price"] for item in cart.values())

    request.session["cart"] = cart  # Save the updated cart in session
    request.session.modified = True  # Mark session as modified

    return render(request, "cart/cart.html", {"cart_items": cart, "total_price": total_price})

def remove_from_cart(request, product_key):
    cart = request.session.get("cart", {})

    if product_key in cart:
        del cart[product_key]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("view_cart")

def update_cart(request, product_key, action):
    cart = request.session.get("cart", {})

    if product_key in cart:
        if action == "increase":
            cart[product_key]["quantity"] += 1
        elif action == "decrease" and cart[product_key]["quantity"] > 1:
            cart[product_key]["quantity"] -= 1

        # Recalculate total price for the item
        cart[product_key]["total_price"] = cart[product_key]["price"] * cart[product_key]["quantity"]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("view_cart")
