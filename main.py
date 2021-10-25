from kivy.config import Config

Config.set("graphics", "resizable", "1")
Config.set("graphics", "width", "450")
Config.set("graphics", "height", "700")

import urllib
import certifi as cfi
from kivymd.app import MDApp
from kivymd.toast import toast
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
                    text="KANSELAHIN",
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
                    text="KANSELAHIN",
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
            "PATALASTAS!": "bullhorn-outline",
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
        else:
            Window.close()

    def ipakita_ang_tungkol_sa_aplikasyon(self):
        self.dayalogo_ng_tungkol_sa_aplikasyon = MDDialog(
            title="PILI-BALITA: DETEKTOR NG MALING BALITA",
            text="    Ang Pili-Balita ay isang machine learning application software na maaaring makatulong "
            + "sa pagtukoy kung ang isang balita ba ay naglalaman ng maling impormasyon o hindi. \n\nVersion 1.0.0",
            radius=[10],
        )
        self.dayalogo_ng_tungkol_sa_aplikasyon.open()

    def ipakita_ang_gabay_sa_aplikasyon(self):
        self.dayalogo_ng_gabay_sa_aplikasyon = MDDialog(
            type="custom",
            title="GABAY SA PAGGAMIT NG PILI-BALITA",
            text="1. Humanap ng mga balitang kumakalat sa sosyal midya. Kapag nagdadalawang-isip ka sa balitang iyong nabasa. Maaari mong kopyahin ang kabuuang balita.\n"
            + "2. Matapos kopyahin ang balita, ilagay ito sa TEXT FIELD. Maaari mo ring pindutin ang PINDUTAN NG PASTE para mailagay ng awtomatiko ang iyong kinopyang balita.\n"
            + "3. Pindutin ang  PINDUTAN NG TUKLASIN! para maproseso ng aplikasyon ang iyong nailagay na balita.\n"
            + "4. Pagkatapos iproseso ang datos, ipapakita ng aplikasyon ang porsyento ng kawastuhan ng balita, pati na rin ang husga nito ukol dito.\n"
            + "5. Maaari mo ring pindutin ang PINDUTAN NG KABUUANG RESULTA upang makita ang kabuuang detalye ng resulta.\n",
            radius=[10],
        )
        self.dayalogo_ng_gabay_sa_aplikasyon.open()

    # Link ng google form
    def ipakita_ang_patalastas(self):
        self.dayalogo_ng_gabay_sa_aplikasyon = MDDialog(
            type="custom",
            title="PATALASTAS",
            text="    Isang magandang araw! Maaari ba kaming makahingi ng kaunting oras para ikaw ay aming "
            + "makapanayam? Maaari ninyong pindutin ang lunsaran sa baba para idirekta sa mismong talatanungan. "
            + "Kami ay nangangako na ang mga datos na makakalap sa pag-aaral na ito ay mamamagitan lamang sa mga nagsagot, "
            + "at ng mga mananaliksik at sa mga may kauganayan sa pag-aaral na ito. Maraming salamat! "
            + " - Mga mananaliksik mula sa Departamento ng Inhinyerong Pang-Kompyuter, COE3104",
            radius=[10],
            buttons=[
                MDFlatButton(
                    text="LINK",
                    theme_text_color="Custom",
                    text_color=(126 / 255, 84 / 255, 36 / 255, 255 / 255),
                    # on_press=self.isara_ang_dayalogo_ng_mali,
                ),
            ],
        )
        self.dayalogo_ng_gabay_sa_aplikasyon.open()

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
            ca_file=cfi.where(),
            verify=True,
        )
    
    def iulat_ang_resulta(self, urlrequest, result):
        self.resulta = result
        self.dayalogo_ng_resulta.content_cls.ids.paikot.active = False
        self.kabuuang_resulta_pindutan.disabled = False
        self.kabuuang_resulta_pindutan.md_bg_color = (126/255, 84/255, 36/255, 255/255)
        self.dayalogo_ng_resulta.content_cls.ids.resulta_progressbar.value = result["Average "]
        self.dayalogo_ng_resulta.content_cls.ids.resulta_porsyento.text = str(result["Average "]) + "%"

        if result["Husga"] == "TUNAY":
            self.dayalogo_ng_resulta.content_cls.ids.resulta.text = "TUNAY ANG NILALAMAN"
            self.dayalogo_ng_resulta.content_cls.ids.prediksyon_unang_icon.icon = "check-circle"
            self.dayalogo_ng_resulta.content_cls.ids.prediksyon_pangalawang_icon.icon = "check-circle"
        else:
            self.dayalogo_ng_resulta.content_cls.ids.resulta.text = "PEKENG BALITA"
            self.dayalogo_ng_resulta.content_cls.ids.prediksyon_unang_icon.icon = "alert-octagon"
            self.dayalogo_ng_resulta.content_cls.ids.prediksyon_pangalawang_icon.icon = "alert-octagon"

    def iulat_ang_mali(self, urlrequest, result):
        self.dayalogo_ng_resulta.dismiss()
        toast("Nabigong kuhanin ang resulta. Siguraduhing konektado ka sa Internet o may sapat na alokasyon ng datos para dito")

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
        self.theme_cls.primary_palette = "Brown"


Pangunahin().run()
