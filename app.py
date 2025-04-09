from flask import Flask

app = Flask(__name__)

@app.route("/contact")

def create_contact():
    return "you created a contact!"

if __name__ == '__main__':
    app.run(debug=True)

