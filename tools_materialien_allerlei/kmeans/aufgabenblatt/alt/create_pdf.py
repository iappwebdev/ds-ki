from fpdf import FPDF
import os

# Initialisiere das PDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'K-Means Clustering Aufgabe', align='C', ln=True)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Seite {self.page_no()}', align='C')

# Erstelle PDF
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Titel
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'K-Means Clustering - Iterationsdetails', ln=True)
pdf.ln(10)

# Log-Daten hinzufügen
logs = [
    "Plot für Iteration 1 gespeichert als cluster_plot_iteration_1.png",
    "Punkt a zu Cluster 1 (Distanzen: [0, 5, 9])",
    # Verkürztes Beispiel - füge hier den gesamten Log ein
    "Algorithmus konvergierte nach 4 Iterationen.",
    "Finale Zentroiden: [[4, 9], [7, 5], [2, 3]]"
]

pdf.set_font('Arial', '', 12)
for log in logs:
    pdf.multi_cell(0, 10, log)
    pdf.ln(2)

# Plots einfügen
plot_folder = '.'  # Ordner, in dem die Plots gespeichert sind
plot_files = sorted([f for f in os.listdir(plot_folder) if f.startswith('cluster_plot_iteration') and f.endswith('.png')])

for plot_file in plot_files:
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, f'Iteration: {plot_file.split("_")[-1].split(".")[0]}', ln=True)
    pdf.ln(5)
    pdf.image(os.path.join(plot_folder, plot_file), x=10, y=None, w=180)  # Bildbreite anpassen

# PDF speichern
pdf_output = 'k_means_aufgabe.pdf'
pdf.output(pdf_output)
print(f'PDF gespeichert als {pdf_output}')
