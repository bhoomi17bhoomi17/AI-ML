# app.py
from flask import flask, request, render_template

app = flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chat():
    reply = ""
    if request.method == "POST":
        user_input = request.form["message"].lower()

        if "how are you" in user_input:
            reply = "I am fine."
        elif "what is your name" in user_input:
            reply = "I am a simple AI chatbot."
        elif "who created you" in user_input:
            reply = "I was created using Python and Flask."
        elif "what is python" in user_input:
            reply = "Python is a popular programming language."
        elif "what is ai" in user_input:
            reply = "AI means Artificial Intelligence."
        elif "tell me a joke" in user_input:
            reply = "Why don’t robots get tired? Because they recharge!"
        elif "bye" in user_input or "goodbye" in user_input:
            reply = "Goodbye! Have a nice day."
        elif "what is 2+2" in user_input:
            reply = "2+2 is 4."
        elif "thank you" in user_input:
            reply = "You’re welcome!"
        elif "what is your purpose" in user_input:
            reply = "My purpose is to help answer your questions."
        else:
            reply = "I don’t understand yet."

    return 
    render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)