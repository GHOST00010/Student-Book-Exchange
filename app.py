from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# 🔹 Home page - registration form
@app.route('/')
def register():
    return render_template("regi.html")

# 🔹 Submit route - saves user data to users.db and redirects to index.html
@app.route('/submit', methods=["POST"])
def submit():
    name = request.form['name']
    phone = request.form['phone']
    address = request.form['address']

    # Save to SQLite DB
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, phone, address) VALUES (?, ?, ?)", 
                   (name, phone, address))
    conn.commit()
    conn.close()

    # ✅ Redirect to buy/sell page
    return redirect('/index')

# 🔹 After registration - show Buy/Sell page
@app.route('/index')
def index():
    return render_template("index.html")

# 🔹 Dummy buy route
@app.route('/buy')
def buy():
    return render_template("buy.html")  # Must be inside templates/

# 🔹 Dummy sell route
@app.route('/sell')
def sell():
    return render_template("sell.html")  # Must be inside templates/

if __name__ == '__main__':
    app.run(debug=True)
