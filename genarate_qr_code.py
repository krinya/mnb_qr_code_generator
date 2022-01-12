import pyqrcode
#import png
from PIL import Image

def create_qr_code(content = "www.444.hu", filename = "qr_code.png", scale = 5):
    
    qr_code = pyqrcode.create(content)
    qr_code.png(filename, scale = scale)
    im = Image.open(filename)
    
    return(im)

def genarete_white_space_character_at_end(string = "abc", length = -1, characther = " ", add_end = '\n'):
    
    if length == -1:
        length = len(string)
    
    length_of_string = len(string)
    strings_to_add = length - len(string)
    
    new_string = string
    
    for i in range(strings_to_add):
        new_string = new_string + characther
    
    new_string = new_string + add_end
    
    new_string = str(new_string)
    
    return(new_string)


def generate_transfer_request(
    fogado_fel_neve = "Menyhért Zoltán",
    bankszamlaszam = "HU65107000245550868756100000",
    bic_kod = "GNBAHUHBXXX",
    osszeg_huf = 1000,
    scale = 3):
    
    azonosito_kod = "HCT\n"
    verzioszam = "001\n"
    karakterkeszlet = "1\n"

    fizeto_fel_kedvezmenyzett_bic_bei = genarete_white_space_character_at_end(string=bic_kod)
    fizeto_fel_kedvezmenyzett_neve = genarete_white_space_character_at_end(string = fogado_fel_neve)
    fizeto_fel_kedvezmenyzett_IBAN = genarete_white_space_character_at_end(string = bankszamlaszam)
    osszeg = str("HUF"+ str(osszeg_huf) + "\n")
    ervenyessegi_ido = "20220108235959+1\n"
    fizetesi_helyzet_azonosito = genarete_white_space_character_at_end("")
    kozlemeny = genarete_white_space_character_at_end("kozlemeny test string")


    kereskedelmi_egyseg_bolt_azonosito = genarete_white_space_character_at_end("bolt azonosito string")
    kereskedoi_eszkoz_azonosito = genarete_white_space_character_at_end("")
    szamla_vagy_nyugta_azonosito = genarete_white_space_character_at_end("")
    ugyfelazonosito = genarete_white_space_character_at_end("")
    kedvezmenyezett_belso_azonositoja = genarete_white_space_character_at_end("")
    torzsvasarlo_vagy_kedvezmenyezett_azonositoja = genarete_white_space_character_at_end("")
    nav_ellenorzokod = genarete_white_space_character_at_end("")


    qr_code_content_all = azonosito_kod + verzioszam + karakterkeszlet + fizeto_fel_kedvezmenyzett_bic_bei + fizeto_fel_kedvezmenyzett_neve + fizeto_fel_kedvezmenyzett_IBAN + osszeg + ervenyessegi_ido + fizetesi_helyzet_azonosito + kozlemeny + kereskedelmi_egyseg_bolt_azonosito + kereskedoi_eszkoz_azonosito + szamla_vagy_nyugta_azonosito + ugyfelazonosito + kedvezmenyezett_belso_azonositoja + torzsvasarlo_vagy_kedvezmenyezett_azonositoja + nav_ellenorzokod
    qr_code_return = create_qr_code(content = qr_code_content_all, scale = scale)
    
    return(qr_code_return)