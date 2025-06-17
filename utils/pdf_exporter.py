from fpdf import FPDF

def export_to_pdf(memory, filename="final_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, "🧠 Autonomous Agent Report", align='C')
    pdf.ln(10)

    for step in memory:
        step_title = f"🔹 Step {step['step']}"
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, step_title, ln=True)

        pdf.set_font("Arial", size=11)
        for key, value in step.items():
            if key != "step":
                pdf.multi_cell(0, 8, f"{key.upper()}:\n{value}\n")
        pdf.ln(5)

    pdf.output(filename)
    print(f"\n📄 PDF saved as: {filename}")
