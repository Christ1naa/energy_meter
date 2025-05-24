from flask import Flask, request, render_template_string
from app.meter_logic import process_meter_data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        data = {
            "id": request.form["id"],
            "date": request.form["date"],
            "readings": {
                "day": int(request.form["day"]),
                "night": int(request.form["night"])
            }
        }
        result = process_meter_data(data)
    return render_template_string("""
    <form method="post">
        <input name="id" placeholder="Meter ID"><br>
        <input name="date" placeholder="YYYY-MM-DD"><br>
        <input name="day" placeholder="Day kWh"><br>
        <input name="night" placeholder="Night kWh"><br>
        <button>Submit</button>
    </form>
    <pre>{{ result }}</pre>
    """, result=result)

if __name__ == "__main__":
    app.run(debug=True)
