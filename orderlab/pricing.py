def subtotal(unit_price: int, quantity: int) -> int:
    if unit_price < 0 or quantity < 0:
        raise ValueError("negative input")

    return unit_price * quantity


def final_total(price: int, qty: int, discount: int) -> int:
    if not 0 <= discount <= 100:
        raise ValueError("invalid discount")

    amount = subtotal(price, qty)

    amount -= amount * discount / 100

    if 0 < amount < 50000:
        shipping = 3000
    else:
        shipping = 0

    return amount + shipping
