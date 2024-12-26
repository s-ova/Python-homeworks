import re
import codecs
class HTMLCleaner:
    def __init__(self, html):
        self.html = html
    def clean(self):
        return re.sub(r'<[^>]*>', '', self.html)
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
    cleaner = HTMLCleaner(html)
    cleaned_text = cleaner.clean()
    cleaned_text = '\n'.join(line.strip() for line in cleaned_text.splitlines() if line.strip())
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned_text)