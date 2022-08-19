import os
import random
import pyautogui


# ------------------------------------------------------------------------------------------------------------#
# Functions
# ------------------------------------------------------------------------------------------------------------#


# OS


def abrir(directory: str):
    os.startfile(directory)


def obter_arquivos_em(directory: str):
    for root, dirs, files in os.walk(directory):
        return files


def clickar(image: str, need_click=True, right=False, time: int = 20, confidense=True, move=False, x: int = 0,
            y: int = 0):
    for i in range(time):
        try:
            if confidense:
                button = pyautogui.locateCenterOnScreen(image, confidence=0.9)
            else:
                button = pyautogui.locateCenterOnScreen(image)

            assert button is not None

            if move:
                if need_click:
                    if right:
                        pyautogui.rightClick(button[0] + x, button[1] + y)
                    else:
                        pyautogui.click(button[0] + x, button[1] + y)
                else:
                    pyautogui.moveTo(button[0] + x, button[1] + y)
            else:
                if need_click:
                    if right:
                        pyautogui.rightClick(button)
                    else:
                        pyautogui.click(button)
            break
        except:
            time -= 1
        if time == 0:
            print('Infelizmente não foi possivel clickar no botão especificado.\n')


# Others


def get_musics(pasta_das_musicas):
    # Adicionando em uma lista as musicas obtidas
    lista_de_musicas = obter_arquivos_em(pasta_das_musicas)
    print(lista_de_musicas)
    lista_de_musicas.sort(key=len)
    print('\nMusicas obtidas:{}.\n'.format(lista_de_musicas))
    return lista_de_musicas


def filtering(pasta_das_musicas: str, musicas_renomeadas: list, musicas_para_renomear: list):
    # Filtrando
    for musica in get_musics(pasta_das_musicas):
        if 'track' in musica and '.ogg' in musica and not '-' in musica:
            musicas_renomeadas.append(musica)
        if '.ogg' in musica and not 'track' in musica:
            musicas_para_renomear.append(musica)
    print('Musicas renomeadas:{}\n'.format(musicas_renomeadas))
    print('Musicas para renomear:{}\n'.format(musicas_para_renomear))


def renaming(pasta_das_musicas, musicas_renomeadas: list, musicas_para_renomear: list):
    # Renomeando musicas não renomeadas
    for musica in musicas_para_renomear:
        num = 1
        while True:
            try:
                os.rename(r'{}\{}'.format(pasta_das_musicas, musica), r'{}\track{}.ogg'.format(pasta_das_musicas, num))
                break
            except:
                num += 1

    print('Musicas atuais:{}\n'.format(musicas_renomeadas))


def renaming_for_test(pasta_das_musicas):
    # Renomeando todas as musicas para "test{num}.ogg"
    for musica in get_musics(pasta_das_musicas):
        os.rename(r'{}\{}'.format(pasta_das_musicas, musica), r'{}\{}'.format(pasta_das_musicas, musica.replace('track', 'test')))


def renaming_for_track(pasta_das_musicas):
    # Renomeando todas as musicas para "track{num_random}.ogg"
    count = 1
    ultima_musica = get_musics(pasta_das_musicas)[-1].replace('test', '').replace('.ogg', '')
    for musica in get_musics(pasta_das_musicas):
        while True:
            print(musica)
            nova_musica = musica.replace('test', 'track').replace(str(count), str(random.randint(1, int(ultima_musica))))
            try:
                os.rename(r'{}\{}'.format(pasta_das_musicas, musica), r'{}\{}'.format(pasta_das_musicas, nova_musica))
                count += 1
                break
            except:
                print('Deu ruim')


# ------------------------------------------------------------------------------------------------------------#
# Variables
# ------------------------------------------------------------------------------------------------------------#


# Mudando para pasta raiz
loc = os.getcwd()
new_loc = loc.split('\\')
os.chdir(loc.replace(fr'\{new_loc[-2]}\{new_loc[-1]}', ''))

# Locates
jogo = r'.\mysummercar.exe'
pasta_das_musicas = r'.\Radio'
pasta_das_imagens = r'.\assets\img'

# Imagens
play_button = r'{}\play.png'.format(pasta_das_imagens)
white_button = r'{}\white.png'.format(pasta_das_imagens)
import_button = r'{}\import.png'.format(pasta_das_imagens)
anderstand_button = r'{}\anderstand.png'.format(pasta_das_imagens)


# ------------------------------------------------------------------------------------------------------------#
# Source
# ------------------------------------------------------------------------------------------------------------#


def Start():
    RenomearMusicas()
    AbrirJogo()


def RenomearMusicas():
    musicas_renomeadas = []
    musicas_para_renomear = get_musics(pasta_das_musicas)
    filtering(pasta_das_musicas, musicas_renomeadas, musicas_para_renomear)
    renaming(pasta_das_musicas, musicas_renomeadas, musicas_para_renomear)
    renaming_for_test(pasta_das_musicas)
    renaming_for_track(pasta_das_musicas)

def AbrirJogo():
    abrir(jogo)
    os.chdir(loc.replace(fr'\{new_loc[-1]}', ''))
    clickar(play_button)
    clickar(anderstand_button)
    clickar(white_button, confidense=False)
    clickar(import_button)


# ------------------------------------------------------------------------------------------------------------#
# Init
# ------------------------------------------------------------------------------------------------------------#


Start()
