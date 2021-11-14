import certifi as cfi
import urllib, webbrowser
from kivymd.app import MDApp
from kivymd.toast import toast
from patalastas import anunsyo
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.uix.button import MDFlatButton, MDRaisedButton


class KabuuangResulta(FloatLayout):
    pass


class Resulta(FloatLayout):
    pass


class BoxLayoutScreen(BoxLayout):
    pass


class DeskripsyonAlgoritmo(BoxLayout):
    pass


class TungkolSaAplikasyon(BoxLayout):
    pass


class GabaySaAplikasyon(BoxLayout):
    pass


class Katawan(BoxLayout):
    def tuklasin(self):
        # kukunin ang mga salitang inilagay sa text field
        nilagay_na_balita = self.ids.balita.text
        if not (nilagay_na_balita and not nilagay_na_balita.isspace()):
            toast("Punan muna ang lagayan ng balita.")
        else:
            self.iproseso_ang_datos()
            self.ipakita_ang_resulta()

    def ipakita_ang_resulta(self):
        self.kabuuang_resulta_pindutan = MDRaisedButton(
                    text="KABUUANG RESULTA",
                    disabled=True,
                    md_bg_color=(197/255, 130/255, 51/255, 0),
                    on_press=self.ipakita_ang_kabuuang_resulta,
        )

        self.dayalogo_ng_resulta = MDDialog(
            type="custom",
            title="RESULTA",
            radius=[10],
            auto_dismiss=False,
            content_cls=Resulta(),
            buttons=[
                self.kabuuang_resulta_pindutan,
                MDFlatButton(
                    text="ISARA",
                    theme_text_color="Custom",
                    text_color=(126 / 255, 84 / 255, 36 / 255, 255 / 255),
                    on_press=self.isara_ang_dayalogo_ng_resulta,
                ),
            ],
        )
        self.dayalogo_ng_resulta.open()

    def ipakita_ang_kabuuang_resulta(self, obj):
        self.dayalogo_ng_kabuuang_resulta = MDDialog(
            type="custom",
            title="KABUUANG RESULTA",
            radius=[10],
            auto_dismiss=False,
            content_cls=KabuuangResulta(),
            buttons=[
                MDFlatButton(
                    text="ISARA",
                    theme_text_color="Custom",
                    text_color=(126 / 255, 84 / 255, 36 / 255, 255 / 255),
                    on_press=self.isara_ang_dayalogo_ng_kabuuang_resulta,
                ),
            ],
        )
        self.dayalogo_ng_resulta.dismiss()
        self.dayalogo_ng_kabuuang_resulta.open()
        self.iproseso_ang_kabuuang_resulta()

    def ipakita_ang_iba_pang_kagamitan(self):
        self.iba_pang_kagamitan = MDGridBottomSheet(
            radius_from="top", bg_color=(208 / 255, 167 / 255, 106 / 255, 255 / 255)
        )
        datos = {
            "TUNGKOL": "information-variant",
            "GABAY": "help",
            "ISARA": "exit-to-app",
            "DESKRIPSYON NG MGA ALGORITMO": "book-information-variant",
            "PATALASTAS!": "bullhorn-outline"   
        }

        for aytem in datos.items():
            self.iba_pang_kagamitan.add_item(
                aytem[0],
                lambda x, y=aytem[0]: self.buksan_ang_aytem(y),
                icon_src=aytem[1],
            )

        self.iba_pang_kagamitan.open()

    def buksan_ang_aytem(self, *args):
        if args[0] == "TUNGKOL":
            self.ipakita_ang_tungkol_sa_aplikasyon()

        elif args[0] == "GABAY":
            self.ipakita_ang_gabay_sa_aplikasyon()

        elif args[0] == "PATALASTAS!":
            self.ipakita_ang_patalastas()

        elif args[0] == "DESKRIPSYON NG MGA ALGORITMO":
            self.ipakita_ang_deskripsyon_ng_mga_algoritmo()

        else:
            Window.close()

    def ipakita_ang_deskripsyon_ng_mga_algoritmo(self):
        self.dayalogo_ng_deskripsyon_ng_mga_algoritmo = MDDialog(
            type="custom",
            title="DESKRIPSYON NG MGA ALGORITMO",
            content_cls=DeskripsyonAlgoritmo(),
            radius=[10],
        )
        self.dayalogo_ng_deskripsyon_ng_mga_algoritmo.open()

    def ipakita_ang_tungkol_sa_aplikasyon(self):
        self.dayalogo_ng_tungkol_sa_aplikasyon = MDDialog(
            type="custom",
            title="PILI-BALITA: DETEKTOR NG MALING BALITA",
            content_cls=TungkolSaAplikasyon(),
            radius=[10],
        )
        self.dayalogo_ng_tungkol_sa_aplikasyon.open()

    def ipakita_ang_gabay_sa_aplikasyon(self):
        self.dayalogo_ng_gabay_sa_aplikasyon = MDDialog(
            type="custom",
            title="GABAY SA PAGGAMIT NG PILI-BALITA",
            content_cls=GabaySaAplikasyon(),
            radius=[10],
        )
        self.dayalogo_ng_gabay_sa_aplikasyon.open()

    def ipakita_ang_patalastas(self):
        self.dayalogo_ng_gabay_sa_aplikasyon = MDDialog(
            type="custom",
            title="PATALASTAS",
            text=anunsyo(),
            radius=[10],
            buttons=[
                MDRaisedButton(
                    text="SURBEY-PANAYAM LUNSARAN",
                    on_press=self.buksan_ang_surbey_panayam
            )],
        )
        self.dayalogo_ng_gabay_sa_aplikasyon.open()
    
    def buksan_ang_surbey_panayam(self, obj):
        self.dayalogo_ng_gabay_sa_aplikasyon.dismiss()
        webbrowser.open("https://forms.gle/FYA2wgJQ2n2hFEW99")

    def isara_ang_dayalogo_ng_resulta(self, obj):
        self.dayalogo_ng_resulta.dismiss()

    def isara_ang_dayalogo_ng_kabuuang_resulta(self, obj):
        self.dayalogo_ng_kabuuang_resulta.dismiss()

    def isara_ang_dayalogo_ng_gabay_sa_aplikasyon(self, obj):
        self.dayalogo_ng_gabay_sa_aplikasyon.dismiss()

    def alisin(self):
        self.ids.balita.text = ""

    def iproseso_ang_datos(self):
        balita = urllib.parse.quote(self.ids.balita.text, safe='')
        URLRequest = f"https://pilibalita-api.herokuapp.com/hula?balita={balita}"
        UrlRequest(
            url=URLRequest,
            on_success=self.iulat_ang_resulta,
            on_failure=self.iulat_ang_mali,
            on_error=self.iulat_ang_error,
            ca_file=cfi.where(),
            verify=True,
        )
    
    def iulat_ang_resulta(self, urlrequest, result):
        self.resulta = result
        self.dayalogo_ng_resulta.content_cls.ids.paikot.active = False
        self.dayalogo_ng_resulta.content_cls.ids.kawastuhan.text = "KAWASTUHAN"
        self.kabuuang_resulta_pindutan.disabled = False
        self.kabuuang_resulta_pindutan.md_bg_color = (126/255, 84/255, 36/255, 255/255)
        self.dayalogo_ng_resulta.content_cls.ids.resulta_porsyento.text = str(result["Average "]) + "%"

        if result["Husga"] == "TUNAY":
            self.dayalogo_ng_resulta.content_cls.ids.resulta.text = "TUNAY ANG NILALAMAN"
            self.dayalogo_ng_resulta.content_cls.ids.resulta.text_color =  (126/255, 84/255, 36/255, 255/255)
            self.dayalogo_ng_resulta.content_cls.ids.prediksyon_unang_icon.icon = ""
            self.dayalogo_ng_resulta.content_cls.ids.prediksyon_pangalawang_icon.icon = ""
        else:
            self.dayalogo_ng_resulta.content_cls.ids.resulta.text = "PEKENG BALITA"
            self.dayalogo_ng_resulta.content_cls.ids.resulta.text_color = (1, 0, 0, 1)
            self.dayalogo_ng_resulta.content_cls.ids.prediksyon_unang_icon.icon = "alert-octagon"
            self.dayalogo_ng_resulta.content_cls.ids.prediksyon_pangalawang_icon.icon = "alert-octagon"

    def iulat_ang_mali(self, urlrequest, result):
        self.dayalogo_ng_resulta.dismiss()
        toast("Nabigong kuhanin ang resulta. Siguraduhing konektado ka sa Internet \no may sapat na alokasyon ng datos para dito")

    def iulat_ang_error(self, urlrequest, result):
        self.dayalogo_ng_resulta.dismiss()
        toast("Nabigong kuhanin ang resulta. Ulitin muli o i-refresh ang aplikasyon.")

    def iproseso_ang_kabuuang_resulta(self):
        self.dayalogo_ng_kabuuang_resulta.content_cls.ids.lr_porsyento.text = str(self.resulta["LR Porsyento"])
        self.dayalogo_ng_kabuuang_resulta.content_cls.ids.lr_kategorya.text = self.resulta["LR Prediksyon"]
        self.dayalogo_ng_kabuuang_resulta.content_cls.ids.dt_porsyento.text = str(self.resulta["DT Porsyento"])
        self.dayalogo_ng_kabuuang_resulta.content_cls.ids.dt_kategorya.text = self.resulta["DT Prediksyon"]
        self.dayalogo_ng_kabuuang_resulta.content_cls.ids.rfc_porsyento.text = str(self.resulta["RFC Porsyento"])
        self.dayalogo_ng_kabuuang_resulta.content_cls.ids.rfc_kategorya.text = self.resulta["RFC Prediksyon"]


class Pangunahin(MDApp):
    def build(self):
        self.title = "Pili-Balita"
        self.icon = "larawan/pili-balita-icon.png"
        self.theme_cls.primary_palette = "Brown"

Pangunahin().run()