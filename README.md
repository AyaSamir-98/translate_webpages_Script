# translate_webpages_Script

The script performs website translation by utilizing the Google Cloud Translate API. It uses the google.cloud.translate_v2 module to access the translation functionality. Additionally, it makes use of the BeautifulSoup library to parse HTML files and extract text for translation.

Here's a breakdown of the script's main components:

    Imports:
        google.cloud.translate_v2: Importing the Google Cloud Translate client for translation operations.
        bs4.BeautifulSoup, bs4.SoupStrainer: Importing the BeautifulSoup library for HTML parsing.
        os: Importing the os module for accessing the operating system.

    Setting Google Cloud credentials:
        The script sets the path to the Google Cloud credentials file (my-google-cloud-key.json) using the os.environ dictionary.

    WebPages function:
        This function takes a file_name and a target_lang as parameters.
        It reads the HTML content of the file specified by file_name.
        It creates a BeautifulSoup object (soup) to parse the HTML.
        It iterates over all text elements within the HTML and translates them using the Google Cloud Translate API.
        The translated text is stored in the translated_text variable.
        The original text is replaced with the translated text in the HTML.
        The modified HTML content is then written back to the file.

    Configuration variables:
        target_lang: Specifies the target language for translation (e.g., 'hi' for Hindi).
        Main_Folder: Specifies the root folder where the script will recursively search for HTML files to translate.

    Translation loop:
        The script traverses the directory tree starting from Main_Folder using os.walk.
        For each file found, it checks if the file has a '.html' or '.htm' extension.
        If the file is readable, it calls the WebPages function to translate the file.
        If the file is not readable, an error message is printed.

Overall, this script automates the translation of HTML files in a given directory to a specified target language using the Google Cloud Translate API.
