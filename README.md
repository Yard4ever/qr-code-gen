# 🔳 QR Code Generator (Flask + HTML)

This is a simple yet powerful web-based QR Code Generator built with Flask (Python) for the backend and a responsive HTML/CSS/JS interface for the frontend. You can generate QR codes for Text, URLs, Wi-Fi networks, and MeCard contact information.

---

## 🚀 Features

- Generate QR Codes for:
  - 📃 Text
  - 🌐 URLs (HTTPS)
  - 📶 Wi-Fi Networks
  - 👤 MeCard Contacts
- Download generated QR codes as PNG images
- Responsive and stylish user interface
- Password toggle for Wi-Fi field (Show/Hide)
- Dynamic form fields based on QR code type

---

## 📁 Project Structure

qr-code-generator/
│
├── app.py              # Flask backend server
├── templates/
│   └── index.html      # Frontend HTML page

---

## ⚙️ Requirements

Install dependencies using pip:

pip install flask qrcode[pil]

---

## ▶️ How to Run

1. Clone or download the project folder.
2. Open a terminal in the project directory.
3. Run the Flask server:

python app.py

4. 
📢 **IMPORTANT:**  
Make sure to **change the IP address** in `app.py` to your **own local IP address**, or use `127.0.0.1` (localhost) if you're testing only on your own computer.

Example:
```python
app.run(host="127.0.0.1", port=5000, debug=True)
---
## 📸 Example QR Types

| Type     | Description                                  |
|----------|----------------------------------------------|
| text     | Plain text QR code                           |
| https    | URL that opens a website                     |
| wifi     | Connects to a Wi-Fi network (WPA only)       |
| mecard   | Contact info with name, phone, email, etc.   |

---

## 🛠 Backend Logic (app.py)

- Handles /generate_qr POST requests with JSON data.
- Generates QR images using the qrcode library.
- Returns the image as a PNG stream via send_file().

---

## 🌐 Frontend Interface (index.html)

- HTML form dynamically switches based on selected QR type.
- JavaScript creates the appropriate QR data format (e.g., WIFI:S:SSID;T:WPA;P:Password;;).
- Uses qrcode.min.js to generate QR previews.
- Option to download QR code after it's generated.

---

## ✨ To-Do / Ideas for Improvement

- Add support for other QR types (Email, SMS, vCard, etc.)
- Improve form validation
- Add QR code history
- Allow image customization (color, size, etc.)

---

## 👨‍💻 Author

Ethan Belov-Fishelevich  
Coder & Creator | Dog Lover | Artist  
Made with love from Israel ❤️

---

## 📬 Contact

Email: yard4ik@gmail.com

---

## 📜 License

This project is open-source and free to use. ✨
