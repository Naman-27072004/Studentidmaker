import os
import pandas as pd
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
import qrcode

# Directories setup
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "id_cards"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Constants for ID Card
CARD_WIDTH, CARD_HEIGHT = 600, 1000  # Adjusted for better resolution
FONT_PATH = "arial.ttf"  # Ensure this font exists
SIMS_LOGO_PATH = "sims_logo.png"  # Replace with actual SIMS logo
DAZZLE_LOGO_PATH = "dazzle_logo.png"  # Replace with actual Dazzle logo

# Streamlit UI
st.title("🎨 ID Card Generator")

uploaded_file = st.file_uploader("📂 Upload Excel file", type=["xlsx"])

if uploaded_file:
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)

    # Save the uploaded file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ File uploaded successfully!")

    # Load and process Excel file
    try:
        df = pd.read_excel(file_path, dtype=str)  # Read everything as string to preserve format
        df.columns = df.columns.str.strip()  # Remove accidental spaces

        required_columns = ["Name", "Course", "Year", "Team"]
        if not all(col in df.columns for col in required_columns):
            st.error(f"❌ Missing required columns. Ensure Excel contains: {', '.join(required_columns)}")
        else:
            st.write("📌 **Data Preview:**", df.head())

            # PDF Setup
            pdf_path = os.path.join(OUTPUT_FOLDER, "student_id_cards.pdf")
            c = canvas.Canvas(pdf_path)
            c.setPageSize((CARD_WIDTH, CARD_HEIGHT))

            # Load font safely
            try:
                font_large = ImageFont.truetype(FONT_PATH, 40)  # Large font for student details
                font_small = ImageFont.truetype(FONT_PATH, 28)  # Smaller font for institute name
            except IOError:
                st.warning("⚠️ Font not found! Using default font.")
                font_large = ImageFont.load_default()
                font_small = ImageFont.load_default()

            # Load logos safely
            try:
                sims_logo = Image.open(SIMS_LOGO_PATH).convert("RGBA").resize((150, 50))
            except IOError:
                st.warning("⚠️ SIMS Logo missing! Proceeding without it.")
                sims_logo = None

            try:
                dazzle_logo = Image.open(DAZZLE_LOGO_PATH).convert("RGBA").resize((400, 120))
            except IOError:
                st.warning("⚠️ Dazzle Logo missing! Proceeding without it.")
                dazzle_logo = None

            for _, row in df.iterrows():
                name, course, year, team = row["Name"], row["Course"], row["Year"], row["Team"]

                # Ensure Year is displayed as it is in Excel
                formatted_year = str(year)

                # Create ID card
                id_card = Image.new("RGB", (CARD_WIDTH, CARD_HEIGHT), "white")
                draw = ImageDraw.Draw(id_card)

                # Position SIMS Logo
                logo_y_position = 30  # Fixed position at the top
                if sims_logo:
                    id_card.paste(sims_logo, (30, logo_y_position), mask=sims_logo)

                # Add Institute Name **below the SIMS logo**
                text_y_position = logo_y_position + 60  # Leaves space below the logo
                institute_text = "sirifort institute of management studies"
                text_width = draw.textlength(institute_text, font=font_small)
                text_x_position = (CARD_WIDTH - text_width) // 2  # Center align
                draw.text((text_x_position, text_y_position), institute_text, fill="black", font=font_small)

                # Position Dazzle Logo **below the institute name**
                dazzle_y_position = text_y_position + 50  # Add space before Dazzle logo
                if dazzle_logo:
                    id_card.paste(dazzle_logo, (100, dazzle_y_position), mask=dazzle_logo)

                # Add Student Details
                text_x, text_y = 50, dazzle_y_position + 180  # Ensures proper spacing
                draw.text((text_x, text_y), f"Name: {name}", fill="black", font=font_large)
                draw.text((text_x, text_y + 60), f"Course: {course}", fill="black", font=font_large)
                draw.text((text_x, text_y + 120), f"Year: {formatted_year}", fill="black", font=font_large)
                draw.text((text_x, text_y + 180), f"Team: {team}", fill="black", font=font_large)

                # Generate QR Code
                qr_data = f"Name: {name}\nCourse: {course}\nYear: {formatted_year}\nTeam: {team}"
                qr = qrcode.make(qr_data).resize((200, 200))
                id_card.paste(qr, (50, CARD_HEIGHT - 250))

                # Draw Empty Box for Signature
                draw.rectangle([300, CARD_HEIGHT - 250, 550, CARD_HEIGHT - 200], outline="black", width=3)

                # Save ID card image
                img_path = os.path.join(OUTPUT_FOLDER, f"{name}.png")
                id_card.save(img_path)

                # Add to PDF
                c.drawImage(img_path, 0, 0, width=CARD_WIDTH, height=CARD_HEIGHT)
                c.showPage()

            c.save()
            st.success("✅ ID cards generated successfully!")

            # Download button for the generated PDF
            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="📥 Download ID Cards PDF",
                    data=f,
                    file_name="student_id_cards.pdf",
                    mime="application/pdf"
                )

    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")
