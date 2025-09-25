# ♻️ Garbage Classification Web App

An intelligent web application for automated waste classification using *deep learning*. Users can upload images of waste items, and the system will predict their category (plastic, glass, metal, trash, etc.). The app also provides interactive statistics and downloadable reports to streamline waste management and support environmental sustainability.

---

## 🚀 Features

- *Image Classification:* Upload an image to predict its waste category.  
- *Statistics Dashboard:* Visualize predictions with interactive charts.  
- *Downloadable Reports:* Export results in *CSV* or *PDF* format.  
- *Modern UI:* Clean, responsive interface built with *Bootstrap*.  

---

## 🏗️ How It Works

The system is powered by:
- *Random Forest Model:* Best-performing ML model for classification.  
- *Flask Web Server:* Handles requests and serves the application.  
- *Matplotlib & ReportLab:* For generating charts and exporting PDF reports.  
- *Pandas:* For handling CSV logs and analysis.  

Waste categories are classified into recyclable (plastic, glass, metal, paper) and non-recyclable (trash, organic, etc.) classes.  

---

## 📦 Installation

1. *Clone the repository:*
   bash
   git clone https://github.com/sasinduchanaka/Garbage-Classiffication.git
   cd Garbage-Classiffication/waste detection app
   

2. *Install dependencies:*
   > Create and activate a virtual environment for best results.
   bash
   pip install -r requirements.txt
   

3. *Model Files:*
   - Ensure the trained model (Random Forest .pkl file) is located in the model/ folder.  
   - Update the model path in app.py if needed.  

---

## 🖥️ Usage

1. *Run the Flask app:*
   bash
   python app.py
   

2. *Open your browser:*
   
   http://127.0.0.1:5000/
   

3. *Main Features:*
   - *Upload Image:* Classify waste by uploading an image.  
   - *View Statistics:* Check cumulative classification stats.  
   - *Download Reports:* Export results in CSV/PDF formats.  

---

## 📁 Project Structure


waste detection app/
│
├── app.py                  # Flask backend
├── requirements.txt        # Python dependencies
├── model/                  # Trained ML model (Random Forest .pkl)
├── templates/              # HTML templates
│   ├── index.html
│   ├── result.html
│   └── report.html
├── static/
│   ├── uploads/            # Uploaded images
│   └── stats_chart.png     # Generated statistics chart
├── waste_log.csv           # Classification log (generated)
├── waste_report.pdf        # PDF report (generated)


---

## 🛠️ Requirements

- Python 3.9+  
- See [requirements.txt](./requirements.txt) for all dependencies.  

*Major libraries:*
- Flask  
- Pandas  
- Matplotlib  
- ReportLab  
- Scikit-learn  

---

## 📷 Screenshots

Home Page  

![Home](assets/home.png)  

Classification Result  

![Result](assets/result.png)  

Statistics Dashboard  

![Stats](assets/stats.png)  

(Note: Add screenshots to an assets/ folder for README display.)  

---





## 🤝 Contributing

Pull requests and suggestions are welcome! For major changes, open an issue first to discuss what you would like to change.  

---

## ⚠️ Notes

- *Model file is not included due to size.* You must train or provide your own .pkl model and update the path in app.py.  
- For deployment, set debug=False in app.py.  

---

## 📬 Contact

For questions, reach out via [GitHub Issues](https://github.com/sasinduchanaka/Garbage-Classiffication/issues).
