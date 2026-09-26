from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/home")
def home_planner():
    return render_template("home.html")


@app.route("/party")
def party_planner():
    return render_template("party.html")

@app.route("/jewelry")
def jewelry_planner():
    return render_template("jewelry.html")

@app.route("/generate-home", methods=["POST"])
def generate_home():
    budget = request.form.get("budget")
    room = request.form.get("room")

    return f"""
<h1>Home Budget Plan</h1>
<h2>Your Details</h2>
<p><strong>Budget:</strong> ₹{budget}</p>
<p><strong>Room:</strong> {room}</p>

<h2>Suggested Budget Allocation</h2>
<p>Furniture: ₹{int(budget) * 40 // 100}</p>
<p>Lighting: ₹{int(budget) * 20 // 100}</p>
<p>Decor: ₹{int(budget) * 20 // 100}</p>
<p>Other Expenses: ₹{int(budget) * 20 // 100}</p>
"""
@app.route("/generate-party", methods=["POST"])
def generate_party():
    budget = request.form.get("budget")
    guests = request.form.get("guests")
    event = request.form.get("event")
    venue = request.form.get("venue")

    return f"""
<h1>Party Budget Plan</h1>

<h2>Your Details</h2>
<p><strong>Budget:</strong> ₹{budget}</p>
<p><strong>Guests:</strong> {guests}</p>
<p><strong>Event:</strong> {event}</p>
<p><strong>Venue:</strong> {venue}</p>

<h2>Suggested Budget Allocation</h2>
<p>Catering: ₹{int(budget) * 40 // 100}</p>
<p>Decoration: ₹{int(budget) * 25 // 100}</p>
<p>Entertainment: ₹{int(budget) * 20 // 100}</p>
<p>Other Expenses: ₹{int(budget) * 15 // 100}</p>
"""
@app.route("/generate-jewelry", methods=["POST"])
def generate_jewelry():
    budget = request.form.get("budget")
    occasion = request.form.get("occasion")
    style = request.form.get("style")

    return f"""
    <h1>Jewelry Plan</h1>

    <h2>Your Details</h2>
    <p><strong>Budget:</strong> ₹{budget}</p>
    <p><strong>Occasion:</strong> {occasion}</p>
    <p><strong>Style:</strong> {style}</p>
    """
if __name__ == "__main__":
    app.run(debug=True)