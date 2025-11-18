from flask import Flask, render_template, request

app = Flask(__name__)

# Prices must match the checkbox values in index.html
prices = {"Biryani": 220, "rice": 50, "chicken": 180, "Soup": 100}

@app.route("/", methods=["GET"])
def home():
    # On GET show the form with no preselected items
    return render_template("index.html", message=None, name="", selected=[])

@app.route("/order", methods=["POST"])
def order():
    name = request.form.get("name", "").strip()
    foods = request.form.getlist("food")        # list of selected food names
    qty_raw = request.form.get("quantity", "1")

    # validate quantity
    try:
        quantity = int(qty_raw)
        if quantity < 1:
            raise ValueError("Quantity must be >= 1")
    except ValueError:
        message = "⚠ Quantity must be a positive integer."
        return render_template("index.html", message=message, name=name, selected=foods)

    if not foods:
        message = "⚠ Please select at least one food item!"
        return render_template("index.html", message=message, name=name, selected=foods)

    # compute total and line items; handle unknown items gracefully
    total = 0
    unknown = []
    line_items = []
    for item in foods:
        if item in prices:
            subtotal = prices[item] * quantity
            line_items.append({
                "name": item,
                "unit_price": prices[item],
                "qty": quantity,
                "subtotal": subtotal
            })
            total += subtotal
        else:
            unknown.append(item)

    if unknown:
        message = f"⚠ Unknown menu items: {', '.join(unknown)}"
        return render_template("index.html", message=message, name=name, selected=foods)

    # Render bill page
    return render_template(
        "bill.html",
        name=name or "Guest",
        line_items=line_items,
        total=total
    )

if __name__ == "__main__":
    app.run(debug=True)