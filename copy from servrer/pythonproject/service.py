from flask import Flask, request, redirect, session, render_template
from twilio.twiml.messaging_response import MessagingResponse
from scrapeParking import getLot, getParking

app = Flask(__name__, static_folder="static")


info = "Welcome to Parking Pro!\nEnter campus building code or name for parking info."

@app.route("/sms", methods=["GET", "POST"])
def incomingSMS():
    body = request.values.get("Body", None)

    resp = MessagingResponse()

    print(type(body))
    if body is None:
        resp.message(info)
    else:
        result = getLot(body.lower())
        if result:
            response = result[1] + "\nAvailable Slots: " + result[0] + " (" + str(round(int(100 * int(result[0]) / int(result[2])), 0)) + "%)" + "\nTotal Capacity: " + result[2]
            resp.message(response)
        else:
            resp.message(info)
    
    return str(resp)


@app.route("/", methods=["GET"])
def home():
    lots = getParking()

    return render_template("index.html", barnhill=lots[0]['Barnhill Garage'], gateway=lots[0]['Gateway Garage'], blackford=lots[0]['Blackford Garage'], riverwalk=lots[0]['Riverwalk Garage'], sports_garage=lots[0]['Sports Garage'])


if __name__ == "__main__":
    app.run(debug=True, port=5000)