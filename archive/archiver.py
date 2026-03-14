import os
import sys
import re

try:
    from fpdf import FPDF
    from fpdf.enums import XPos, YPos
except ImportError:
    print("\n[!] fpdf2 eksik. 'pip install fpdf2' yapın.")
    sys.exit()

class MathLabHighContrastPDF(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.set_margins(20, 20, 20)
        self.set_auto_page_break(auto=True, margin=20)
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.font_p = os.path.join(current_dir, "DejaVuSans.ttf")
        self.font_b = os.path.join(current_dir, "DejaVuSans-Bold.ttf")
        self.add_font('DejaVu', '', self.font_p)
        self.add_font('DejaVu', 'B', self.font_b)
        self.m_font = 'DejaVu'

    def header(self):
        if self.page_no() > 0:
            self.set_font(self.m_font, 'B', 8)
            self.set_text_color(100, 100, 100) # Sayfa numarası ve üst bilgi hafif gri kalabilir
            self.cell(0, 10, f'Dr. Ozhan Akdag - Sayfa {self.page_no()}', align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def bolum_basligi_at(self, metin, r, g, b):
        """Bölüm geçişleri için şık ve renkli bir başlık oluşturur."""
        self.ln(5)
        self.set_font(self.m_font, 'B', 12)
        self.set_text_color(r, g, b)
        self.cell(0, 8, metin, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        # Başlığın altına ince bir çizgi çekelim
        self.set_draw_color(r, g, b)
        self.line(self.get_x(), self.get_y(), self.w - 20, self.get_y())
        self.ln(3)

    def formatli_metin_bas(self, metin):
        paragraflar = metin.split('\n')
        eff_width = self.w - 40 
        for par in paragraflar:
            par = par.strip()
            if not par:
                self.ln(3); continue
            
            self.set_x(20)
            if par.startswith('#'):
                level = par.count('#')
                size = 14 - (level) if level < 4 else 11
                self.set_font(self.m_font, 'B', size)
                self.set_text_color(20, 20, 20) # Çok koyu gri/siyah başlık
                self.multi_cell(eff_width, 8, par.replace('#', '').strip(), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            else:
                self.set_font(self.m_font, '', 10)
                self.set_text_color(0, 0, 0) # TAM SİYAH GÖVDE METNİ
                temiz_par = re.sub(r'!\[.*?\]\(.*?\)', '', par)
                if temiz_par.strip():
                    self.multi_cell(eff_width, 6, temiz_par, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def ders_islee(self, ders_adi, lesson_path, md_content, py_content):
        # --- SAYFA 1: DERS NOTU (READABLE) ---
        self.add_page()
        self.set_font(self.m_font, 'B', 20)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 15, ders_adi, align='L', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        self.bolum_basligi_at("I. DERS DÖKÜMANTASYONU", 0, 51, 102) # Koyu Lacivert
        self.formatli_metin_bas(md_content)

        # --- SAYFA 2: HAM METİN VE KOD ---
        self.add_page()
        self.bolum_basligi_at("II. HAM README VERİSİ", 102, 0, 102) # Mor
        self.set_font(self.m_font, '', 8)
        self.set_text_color(0, 0, 0) # TAM SİYAH
        self.multi_cell(self.w-40, 4.5, md_content, border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        self.ln(10)
        self.bolum_basligi_at("III. PYTHON KAYNAK KODU", 0, 102, 51) # Koyu Yeşil
        self.set_font(self.m_font, '', 7)
        self.set_text_color(0, 0, 0) # TAM SİYAH
        self.set_fill_color(245, 245, 245)
        self.multi_cell(self.w-40, 4, py_content, border=1, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # --- SAYFA 3: GÖRSELLER ---
        images = re.findall(r'!\[(.*?)\]\((.*?)\)', md_content)
        if images:
            self.add_page()
            self.bolum_basligi_at("IV. GÖRSEL LABORATUVAR ANALİZİ", 204, 0, 0) # Koyu Kırmızı
            for alt, rel_path in images:
                img_path = os.path.normpath(os.path.join(lesson_path, rel_path))
                if os.path.exists(img_path):
                    self.ln(2)
                    self.set_font(self.m_font, 'B', 10)
                    self.set_text_color(0, 0, 0)
                    self.cell(0, 8, f"🔍 Şekil: {alt}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                    self.image(img_path, x=25, w=160)
                    self.ln(10)

def start_archiving():
    pdf = MathLabHighContrastPDF()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.abspath(os.path.join(current_dir, "..", "modules"))
    
    print(f"--- YÜKSEK KONTRASTLI ARŞİVLEME BAŞLADI ---")

    for sub in sorted(os.listdir(base_path)):
        sub_p = os.path.join(base_path, sub)
        if os.path.isdir(sub_p):
            print(f"📂 Modül: {sub}")
            for lesson in sorted(os.listdir(sub_p)):
                l_p = os.path.join(sub_p, lesson)
                if os.path.isdir(l_p):
                    md_c, py_c = "", ""
                    for f in os.listdir(l_p):
                        if f.lower() == "readme.md":
                            with open(os.path.join(l_p, f), "r", encoding="utf-8") as file:
                                md_c = file.read()
                        elif f.endswith(".py") and f != "__init__.py":
                            with open(os.path.join(l_p, f), "r", encoding="utf-8") as file:
                                py_c = file.read()
                    
                    if md_c or py_c:
                        print(f"   + {lesson}")
                        pdf.ders_islee(lesson.upper(), l_p, md_c, py_c)

    output_file = "The_Mathematical_Lab_High_Contrast.pdf"
    pdf.output(output_file)
    print(f"\n🚀 TAMAMLANDI! Yazılar jilet gibi siyah oldu: {output_file}")

if __name__ == "__main__":
    start_archiving()
