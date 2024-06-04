import sys
import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

inp=sys.argv[1]
outp=sys.argv[2]

#pobrac dane do raportu
n=[]
try:
    file=open(inp,"r")
    lines=file.readlines()
    for line in lines:
        n.append(line.replace("\n",""))
    file.close()
    os.remove(inp)

except Exception as e:
    print(e)
    sys.exit()

for i in range(0,len(n)):
    n[i]=n[i].split(";")

inp=inp.split("\\")
inp=inp[len(inp)-1]

#utworzenie raportu w formie tabeli w pliku pdf
pdf=FPDF('P','mm','A4')
pdf.add_font("Arial",'',"C:\\Windows\\Fonts\\arial.ttf")
pdf.add_font("Arial",'B',"C:\\Windows\\Fonts\\arialbd.ttf")
pdf.add_page()

pdf.set_font('Arial','B',16)
pdf.cell(0,7,inp[:-4],new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.set_font('Arial','B',6)
pdf.cell(7, 4, "nr.", border=True)
pdf.cell(80, 4, "wejscie", border=True)
pdf.cell(80, 4, "wyjscie", border=True)
pdf.cell(0, 4, "czas wykonania", new_x=XPos.LMARGIN, new_y=YPos.NEXT, border=True)

pdf.set_font('Arial','',4)
for i in range(0,len(n)):
    pdf.cell(7, 4, (str(i + 1) + "."), border=True)
    pdf.cell(80, 4, n[i][0],border=True)
    pdf.cell(80, 4, n[i][1], border=True)
    pdf.cell(0, 4, n[i][2], new_x=XPos.LMARGIN, new_y=YPos.NEXT, border=True)


pdf.output(outp+"\\"+inp[:-4]+".pdf")
