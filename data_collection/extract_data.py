import requests
from bs4 import BeautifulSoup
def extract_data():

  # URL à scraper
  urls={
      "url_apropos" :'https://concours.ept.sn/a-propos/',
      "url_pres" : 'https://ept.sn/presentation-de-lept/',
      "url_social" : "https://ept.sn/campus-social/",
      "url_org" : "https://ept.sn/organisation/"
  }

  def get_content(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup 
  
  # Extraire les données souhaitées de la page (par exemple, les balises <p>)
  pres_paragraphs = get_content(urls['url_pres']).find("div",{"class":"entry-content"}).find_all('p')
  pres_li_tags = get_content(urls['url_pres']).find("div",{"class":"entry-content"}).find_all('li')
  pres_paragraphs.extend(pres_li_tags)

  # Extraire les données souhaitées de la page (par exemple, les balises <p>)
  paragraphs = get_content(urls['url_apropos']).find_all('p')
  depts = get_content(urls['url_apropos']).find("div",{"class":"about-text-item"}).find_all('li')
  paragraphs.extend(depts)

  # Extraire les données souhaitées de la page (par exemple, les balises <p>)
  social_paragraphs = get_content(urls['url_social']).find("div",{"class":"elementor-widget-container"}).find_all('p')

  # Extraire les données souhaitées de la page (par exemple, les balises <p>)
  org_paragraphs = get_content(urls['url_org']).find("div",{"class":"elementor-widget-container"}).find_all('p')
  li_tags = get_content(urls['url_org']).find("div",{"class":"elementor-widget-container"}).find_all('li')
  org_paragraphs.extend(li_tags)


  filenames={
      "knowledge/social.txt" : social_paragraphs,
      "knowledge/presentation.txt" : pres_paragraphs,
      "knowledge/organisation.txt" : org_paragraphs,
      "knowledge/apropos.txt" : paragraphs
  }

  for filename, data in filenames.items():
    # Écrire les données dans un fichier texte
    with open(filename, 'w') as file:
        for paragraph in data:
            file.write(paragraph.get_text() + '\n')