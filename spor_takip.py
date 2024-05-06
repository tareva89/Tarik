import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox


class Sporcu:
    def __init__(self, ad, spor_dali):
        self.ad = ad
        self.spor_dali = spor_dali
        self.antrenmanlar = []

    def program_olustur(self, antrenman):
        self.antrenmanlar.append(antrenman)

    def ilerleme_kaydet(self, antrenman_adi, ilerleme):
        for antrenman in self.antrenmanlar:
            if antrenman.ad == antrenman_adi:
                antrenman.ilerlemeler.append(ilerleme)

    def rapor_al(self):
        rapor = f"{self.ad} adli Sporcunun Antrenman Raporu:\n"
        for antrenman in self.antrenmanlar:
            rapor += f"{antrenman.ad}: "
            for ilerleme in antrenman.ilerlemeler:
                rapor += f"{ilerleme}, "
            rapor = rapor.rstrip(", ") + "\n"
        return rapor

    def __str__(self):
        return self.ad


class Antrenman:
    def __init__(self, ad, detaylar):
        self.ad = ad
        self.detaylar = detaylar
        self.ilerlemeler = []

    def __str__(self):
        return self.ad


class SporTakipUygulamasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Spor Takip Uygulamasi')
        self.setGeometry(100, 100, 400, 300)

        self.label_ad = QLabel('Sporcu Adý:')
        self.input_ad = QLineEdit()
        self.label_spor_dali = QLabel('Spor Dalý:')
        self.input_spor_dali = QLineEdit()

        self.button_kayit = QPushButton('Sporcu Kaydý Oluþtur')
        self.button_kayit.clicked.connect(self.kayit_ol)

        self.button_sporculari_listele = QPushButton('Sporcularý Listele')
        self.button_sporculari_listele.clicked.connect(self.sporculari_listele)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_ad)
        self.layout.addWidget(self.input_ad)
        self.layout.addWidget(self.label_spor_dali)
        self.layout.addWidget(self.input_spor_dali)
        self.layout.addWidget(self.button_kayit)
        self.layout.addWidget(self.button_sporculari_listele)

        self.setLayout(self.layout)

        self.sporcular = []

    def kayit_ol(self):
        ad = self.input_ad.text()
        spor_dali = self.input_spor_dali.text()

        if ad and spor_dali:
            self.sporcular.append(Sporcu(ad, spor_dali))
            QMessageBox.information(self, 'Baþarýlý', 'Sporcu kaydý baþarýyla oluþturuldu.')
            self.clear_input()
        else:
            QMessageBox.warning(self, 'Hata', 'Sporcu adý ve spor dalý alanlarý boþ býrakýlamaz!')

    def sporculari_listele(self):
        if not self.sporcular:
            QMessageBox.information(self, 'Bilgi', 'Henüz sporcu kaydý bulunmamaktadýr.')
        else:
            sporcular_listesi = "Sporcular:\n"
            for sporcu in self.sporcular:
                sporcular_listesi += f"- {sporcu}\n"
            QMessageBox.information(self, 'Sporcular', sporcular_listesi)

    def clear_input(self):
        self.input_ad.clear()
        self.input_spor_dali.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SporTakipUygulamasi()
    window.show()
    sys.exit(app.exec_())
