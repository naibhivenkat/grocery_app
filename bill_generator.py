from fpdf import FPDF
from datetime import datetime
import os
import webbrowser

def generate_pdf_bill(order_data, filename="bill.pdf"):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Super Grocery Mart", ln=True, align="C")

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Customer: {order_data['user']}", ln=True)
    pdf.cell(0, 10, f"Shop: {order_data['shop']}", ln=True)

    now = datetime.now()
    pdf.cell(0, 10, f"Date: {now.strftime('%Y-%m-%d')}", ln=True)
    pdf.cell(0, 10, f"Time: {now.strftime('%H:%M:%S')}", ln=True)
    pdf.cell(0, 10, f"Payment Mode: {order_data.get('payment', 'N/A')}", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(60, 10, "Item", border=1)
    pdf.cell(30, 10, "Qty", border=1)
    pdf.cell(40, 10, "Rate", border=1)
    pdf.cell(40, 10, "Total", border=1)
    pdf.ln()

    pdf.set_font("Arial", size=12)
    grand_total = 0
    for item in order_data['items']:
        name = item['name']
        qty = item['qty']
        rate = item['price']
        total = qty * rate
        grand_total += total
        pdf.cell(60, 10, name, border=1)
        pdf.cell(30, 10, str(qty), border=1)
        pdf.cell(40, 10, f"Rs. {rate}", border=1)
        pdf.cell(40, 10, f"Rs. {total}", border=1)
        pdf.ln()

    pdf.set_font("Arial", "B", 12)
    pdf.cell(130, 10, "Grand Total", border=1)
    pdf.cell(40, 10, f"Rs. {grand_total}", border=1)

    output_path = os.path.join(os.getcwd(), filename)
    pdf.output(output_path)
    webbrowser.open(output_path)
    return output_path
