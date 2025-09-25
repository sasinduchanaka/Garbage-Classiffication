import matplotlib
matplotlib.use('Agg')  # Non-GUI backend for plotting

import os
import cv2
import numpy as np
from flask import Flask, render_template, request, redirect, send_file
from tensorflow.keras.models import load_model
from fpdf import FPDF
import matplotlib.pyplot as plt

# -----------------------------
# Flask Config
# -----------------------------
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# -----------------------------
# Load your classification model
MODEL_PATH = os.path.join("model", "mobilenetv2_garbage_best.keras")
best_model = load_model(MODEL_PATH, compile=False)
IMG_SIZE = 128  # 👈 Match your training image size!

# -----------------------------
# Class labels (10 waste categories)
CLASS_LABELS = [
    "battery", "biological", "brown-glass", "cardboard",
    "clothes", "metal", "paper", "shoes",
    "trash", "white-glass"
]

RECYCLABLE = ["brown-glass", "white-glass", "metal", "paper", "cardboard"]
NON_RECYCLABLE = ["trash", "biological", "shoes", "clothes", "battery"]

stats = {}

# -----------------------------
# Preprocess image for classification
def preprocess_image(file_path):
    img = cv2.imread(file_path)
    img_rgb = cv2.cvtColor(cv2.resize(img, (IMG_SIZE, IMG_SIZE)), cv2.COLOR_BGR2RGB)
    img_rgb = img_rgb.astype("float32") / 255.0
    img_input = np.expand_dims(img_rgb, axis=0)  # shape (1, 128, 128, 3)
    return img_rgb, img_input

# -----------------------------
# Log predictions
def log_prediction(class_label):
    stats[class_label] = stats.get(class_label, 0) + 1
    total_items = sum(stats.values())
    with open("waste_log.csv", "w") as f:
        f.write("Waste Classification Report\n")
        f.write(f"Total Items Processed: {total_items}\n")
        for category, count in stats.items():
            f.write(f"{category}: {count}\n")

# -----------------------------
# Generate PDF report
def generate_pdf_report():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="Waste Classification Report", ln=True, align="C")
    pdf.ln(10)

    total_items = sum(stats.values())
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, txt=f"Total Items Processed: {total_items}", ln=True)

    for category, count in stats.items():
        pdf.cell(0, 10, txt=f"{category}: {count}", ln=True)

    pdf_file = "waste_report.pdf"
    pdf.output(pdf_file)
    return pdf_file

# -----------------------------
# Home & Upload route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("file")
        if not file or file.filename == "":
            return redirect(request.url)

        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)

        img_rgb, img_input = preprocess_image(file_path)
        preds = best_model.predict(img_input)
        class_idx = np.argmax(preds, axis=1)[0]
        class_label = CLASS_LABELS[class_idx]
        confidence = preds[0][class_idx]

        log_prediction(class_label)

        if class_label in RECYCLABLE:
            bin_type = "Recyclable ♻️"
        elif class_label in NON_RECYCLABLE:
            bin_type = "Non-Recyclable 🗑️"
        else:
            bin_type = "Unknown ⚠️"

        return render_template(
            "result.html",
            image=file.filename,
            label=class_label,
            confidence=f"{confidence*100:.2f}%",
            bin_type=bin_type
        )

    return render_template("index.html")

# -----------------------------
# Stats route
@app.route("/stats")
def show_stats():
    if stats:
        categories = list(stats.keys())
        counts = list(stats.values())
        plt.figure(figsize=(6, 4))
        plt.bar(categories, counts, color="green")
        plt.xlabel("Category")
        plt.ylabel("Count")
        plt.title("Waste Classification Statistics")
        plt.tight_layout()
        plt.savefig("static/stats_chart.png")
        plt.close()
    return render_template("report.html", stats=stats)

# -----------------------------
# Download routes
@app.route("/download_pdf")
def download_pdf():
    pdf_path = generate_pdf_report()
    return send_file(pdf_path, as_attachment=True)

@app.route("/download_csv")
def download_csv():
    return send_file("waste_log.csv", as_attachment=True)

# -----------------------------
# Run Flask
if __name__ == "__main__":
    app.run(debug=True)
