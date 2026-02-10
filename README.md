# 🎨 ID Card Generator (Streamlit App)

This project is a **Streamlit-based ID Card Generator** that creates **custom student ID cards** from an uploaded Excel file.  
It supports **logos, QR codes, student details, and PDF export**, making it ideal for colleges, events, and institutions.

---

## 📌 Overview

The application allows users to:
- Upload an Excel file containing student details
- Automatically generate **individual ID cards**
- Embed **QR codes** for verification
- Export all ID cards into a **single downloadable PDF**

The entire workflow is handled through a clean and interactive **Streamlit web interface**.

---

## ✨ Features

- 📂 Upload student data via Excel (`.xlsx`)
- 🪪 Auto-generate ID cards for each student
- 🖼️ Support for institutional logos
- 🔲 QR code generation for student details
- ✍️ Signature placeholder box
- 📄 Export all ID cards as a single PDF
- ⚡ Fast, automated, and user-friendly

---

## 🛠️ Tech Stack

| Category | Technology |
|--------|-----------|
| Language | Python |
| Web App | Streamlit |
| Data Handling | Pandas |
| Image Processing | Pillow (PIL) |
| PDF Generation | ReportLab |
| QR Code | qrcode |
| File Format | Excel (.xlsx), PDF |

---

## 📂 Project Structure

```text
ID-Card-Generator/
│── app.py                 # Streamlit application
│── uploads/               # Uploaded Excel files
│── id_cards/              # Generated ID card images & PDF
│── sims_logo.png          # Institute logo (optional)
│── dazzle_logo.png        # Event logo (optional)
│── README.md
```

---

## 📄 Excel File Format
The uploaded Excel file must contain the following columns:

|Column Name|
|-----------|
|Name|
|Course|
|Year|
|Team|

Example:

```bash
Name        | Course | Year | Team
----------------------------------
John Doe    | BCA    | 2024 | Alpha
Jane Smith  | MCA    | 2025 | Beta
```

---

## ⚙️ How It Works
1. User uploads an Excel file
2. App validates required columns
3. For each student:
  - An ID card image is generated
  - QR code is embedded
  - Logos and text are placed
4. All ID cards are compiled into a PDF
5. User downloads the final PDF

---

##🚀 How to Run Locally
###1️⃣ Clone the Repository
```bash
git clone https://github.com/Naman-27072004/Studentidmaker.git
cd id-card-generator
```
###2️⃣ Install Dependencies
```bash
pip install streamlit pandas pillow reportlab qrcode openpyxl
```
###3️⃣ Run the App
```bash
streamlit run app.py
```
The app will open at:
```bash
http://localhost:8501
```

---

## ⚠️ Notes
- Ensure arial.ttf exists or update FONT_PATH
- Logos are optional; the app works without them
- All files are generated locally in the project folders

---

## 🔮 Future Improvements
- Upload student photos
- Custom ID card themes
- Live preview before PDF generation
- Role-based access (admin/user)
- Cloud deployment

---

##🧾 License
This project is licensed under the MIT License.

---

## 📬 Author
- Naman Gupta
- MCA @ JIMS Rohini
- Full-Stack Developer | AI & ML Enthusiast


