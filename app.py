from flask import Flask, render_template, request
import sqlite3
from dotenv import load_dotenv
import os
from google import genai
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def ask_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text
app = Flask(__name__)
def save_plan(plan_type, budget, details):
    connection = sqlite3.connect("pocketsmart.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO plans (plan_type, budget, details) VALUES (?, ?, ?)",
        (plan_type, budget, details)
    )

    connection.commit()
    connection.close()

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
    details = f"Room: {room}"
    save_plan("Home", budget, details)
    prompt = f"""
    You are a smart home budget planner.

    The user's budget is ₹{budget}.
    The room they want to plan is {room}.
    Create a simple budget-friendly home plan.
    Suggest suitable categories, approximate spending, and useful items.
    Make sure the total suggested spending stays within the user's budget.
    Give the response in a clear and easy-to-read format.
    """
    ai_plan = ask_gemini(prompt)
    save_plan("Home AI", budget, ai_plan)
    return f"""
<h1>AI Home Budget Plan</h1>

<h2>Your Details</h2>
<p><strong>Budget:</strong> ₹{budget}</p>
<p><strong>Room:</strong> {room}</p>

<h2>AI Recommendation</h2>
<p>{ai_plan}</p>
"""
@app.route("/generate-party", methods=["POST"])
def generate_party():
    budget = request.form.get("budget")
    guests = request.form.get("guests")
    event = request.form.get("event")
    venue = request.form.get("venue")
    prompt = f"""
    You are a smart party budget planner.
    The total budget is ₹{budget}.
    There are {guests} guests.
    The event type is {event}.
    The venue is {venue}.
    Create a practical, budget-friendly party plan.
    Suggest approximate spending for catering, decoration,
    entertainment, and other important expenses.
    Make sure the total suggested spending stays within the budget.
    Give the response in a clear and easy-to-read format.
    """

    ai_plan = ask_gemini(prompt)
    save_plan("Party AI", budget, ai_plan)
    details = f"Guests: {guests}, Event: {event}, Venue: {venue}"
    save_plan("Party", budget, details)
    return f"""
<h1>AI Party Budget Plan</h1>

<h2>Your Details</h2>
<p><strong>Budget:</strong> ₹{budget}</p>
<p><strong>Guests:</strong> {guests}</p>
<p><strong>Event:</strong> {event}</p>
<p><strong>Venue:</strong> {venue}</p>

<h2>AI Recommendation</h2>
<p>{ai_plan}</p>
"""
@app.route("/generate-jewelry", methods=["POST"])
def generate_jewelry():
    budget = request.form.get("budget")
    occasion = request.form.get("occasion")
    style = request.form.get("style")
    details = f"Occasion: {occasion}, Style: {style}"
    save_plan("Jewelry", budget, details)
    prompt = f"""
    You are a smart jewelry budget planner.

    The user's jewelry budget is ₹{budget}.
    The occasion is {occasion}.
    The preferred jewelry style is {style}.

    Suggest suitable jewelry options for the occasion and style.
    Include approximate spending for each suggestion.
    Make sure the total suggested spending stays within the user's budget.
    Give the response in a clear and easy-to-read format.
    """

    ai_plan = ask_gemini(prompt)

    save_plan("Jewelry AI", budget, ai_plan)
    return f"""
<h1>AI Jewelry Plan</h1>

<h2>Your Details</h2>
<p><strong>Budget:</strong> ₹{budget}</p>
<p><strong>Occasion:</strong> {occasion}</p>
<p><strong>Style:</strong> {style}</p>

<h2>AI Recommendation</h2>
<pre>{ai_plan}</pre>
"""
if __name__ == "__main__":
    app.run(debug=True)