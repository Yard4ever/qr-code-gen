from flask import Flask, request, render_template, send_file, jsonify
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate_qr", methods=["POST"])
def generate_qr():
    data = request.json
    qr_type = data.get("type", "text")
    content = data.get("content", "")
    ssid = data.get("ssid", "")
    password = data.get("password", "")

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )

        # Generate different types of QR codes
        if qr_type == "text" or qr_type == "https":
            qr.add_data(content)
        elif qr_type == "wifi":
            wifi_data = f"WIFI:T:WPA;S:{ssid};P:{password};;"
            qr.add_data(wifi_data)
        else:
            return jsonify({"error": "Invalid QR type."}), 400

        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Convert image to byte stream
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        return send_file(buffer, mimetype="image/png", as_attachment=False)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="000.000.000", port=5000, debug=True)
