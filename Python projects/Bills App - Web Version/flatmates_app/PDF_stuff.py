from fpdf import FPDF

class PDF(FPDF):
    pass

pdf_obj=PDF(orientation="P",unit="pt",format="A4")
pdf_obj.set_font('Arial', 'B', 16)

pdf_obj.add_page()
pdf_obj.cell(550,50,"Bills",0,0.5,"C")
