from google.cloud import translate_v2 as translate
from bs4 import BeautifulSoup, SoupStrainer
import os


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/My Web Sites/Try_Translator/my-google-cloud-key.json'
translate_client = translate.Client()


def WebPages(file_name, target_lang):
    with open(file_name, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    for text in soup.find_all(text=True):
        translated_text = ''
        if text.parent.name in ['script', 'style']:
            continue  
        for i in range(0, len(text.string), 5000):
            chunk = text.string[i:i+5000]
            translation = translate_client.translate(chunk, target_lang=target_lang)['translatedText']
            translated_text += translation
        text.replace_with(translated_text)
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(str(soup))


target_lang = 'hi'  
Main_Folder = 'C:\My Web Sites\ClassCentra\FINAL'

for root, dirs, files in os.walk(Main_Folder):
    for file_name in files:
        if file_name.endswith('.html') or file_name.endswith('.htm'):
            full_path = os.path.join(root, file_name)
            if os.access(full_path, os.R_OK):
                WebPages(full_path, target_lang)
                print(f'The Translating file Now is: {file_name}')
            else:
                print(f'Error: {file_name} Cannot be translated.')
