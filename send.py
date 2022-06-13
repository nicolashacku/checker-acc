import requests

from colorama import Fore, init

init()

v = Fore.LIGHTGREEN_EX

r = Fore.LIGHTRED_EX

w = Fore.LIGHTWHITE_EX

c = Fore.LIGHTCYAN_EX

texto = str(input(f"{c}Digite el mensaje a publicar: "))

cookies = {

    'MoodleSessionmain': 'j241dsjbosbcu1mpiv1ro95tn6',

    '__utma': '67520969.1098916040.1654453410.1654453410.1655089064.2',

    '__utmb': '67520969.10.10.1655092544',

    '__utmc': '67520969',

    '__utmz': '67520969.1654453410.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',

    '_ga': 'GA1.2.1098916040.1654453410',

    '_gid': 'GA1.2.1634541792.1655089076',

    'MoodleSessionTestmain': 'twD50uJNGf',

    'MOODLEID_main': '%25F0%25DE%251F%251F%25E3-%25E0%255C%25B2',

}

headers = {

    'Host': 'c.ingeniat.com',

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',

    'Accept': 'application/json, text/javascript, */*; q=0.01',

    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',

    # 'Accept-Encoding': 'gzip, deflate',

    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',

    'X-Requested-With': 'XMLHttpRequest',

    # 'Content-Length': '806',

    'Origin': 'https://c.ingeniat.com',

    'Referer': 'https://c.ingeniat.com/mod/filtros/index.php?content=10',

    'Sec-Fetch-Dest': 'empty',

    'Sec-Fetch-Mode': 'cors',

    'Sec-Fetch-Site': 'same-origin',

    # Requests doesn't support trailers

    # 'Te': 'trailers',

    # Requests sorts cookies= alphabetically

    # 'Cookie': 'MoodleSessionmain=j241dsjbosbcu1mpiv1ro95tn6; __utma=67520969.1098916040.1654453410.1654453410.1655089064.2; __utmb=67520969.10.10.1655092544; __utmc=67520969; __utmz=67520969.1654453410.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.2.1098916040.1654453410; _gid=GA1.2.1634541792.1655089076; MoodleSessionTestmain=twD50uJNGf; MOODLEID_main=%25F0%25DE%251F%251F%25E3-%25E0%255C%25B2',

}

data = f'u_id=428411&message_publish={texto}&title_publish_parent=&message_publish_parent=&title_publish_communique=%3Ctextarea+class%3D\'materialize-textarea\'+id%3D\'message_publish_communique\'+name%3D\'message_publish_communique\'%3E&circle=2&grado=-1&cursos%5B93429%5D%5B%5D=-1&cursos%5B93435%5D%5B%5D=-1&cursos%5B93440%5D%5B%5D=-1&cursos%5B93443%5D%5B%5D=-1&cursos%5B93445%5D%5B%5D=-1&cursos%5B93447%5D%5B%5D=-1&cursos%5B93449%5D%5B%5D=-1&cursos%5B93452%5D%5B%5D=-1&cursos%5B93454%5D%5B%5D=-1&cursos%5B93455%5D%5B%5D=-1&cursos%5B93457%5D%5B%5D=-1&cursos%5B95635%5D%5B%5D=-1&cursos%5B95636%5D%5B%5D=-1&cursos%5B95637%5D%5B%5D=-1&cursos%5B95638%5D%5B%5D=-1&cursos%5B95639%5D%5B%5D=-1&cursos%5B95640%5D%5B%5D=-1&cursos%5B95641%5D%5B%5D=-1&cursos%5B95642%5D%5B%5D=-1&cursos%5B95643%5D%5B%5D=-1&id_folder_popup=0'

response = requests.post('https://c.ingeniat.com/mod/filtros/comunicaciones/acciones.php', cookies=cookies, headers=headers, data=data)

if "true" in response.text:

  print(f"{r}an error has been ocurred")

  print(response.text)

else:

  print(f"{v}Sended")

  

