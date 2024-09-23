import json
import requests as r
from urllib.parse import quote
import sys
from wikitextparser import remove_markup

pagina = sys.argv[1].capitalize()

def r_page(page):
  url = f"http://pt.wikipedia.org/w/api.php" + \
      f"?action=query&prop=revisions&rvprop=content" + \
      f"&format=json&titles={quote(page)}"
  request = r.get(url)
  content = json.loads(request.text)['query']
  page_content = content['pages'][list(content['pages'].keys())[0]]['revisions'][0]['*']

  if page_content.startswith('#REDIRECT'):
    return r_page(page_content[page_content.find('[[')+2:page_content.find(']]')])
  return page_content

    
try:
  page_content = r_page(pagina)

  with open(f'{pagina.replace(" ","_")}.wiki', 'w') as txt:
    txt.write(remove_markup(page_content))

except KeyError:
  print("Página não encontrada")


except Exception:
  print("Erro na requisição")