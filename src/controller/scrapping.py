from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
class Scrapping:
    ##utils 
    def espera_elemento_aparecer(self, driver: webdriver.Chrome, tipo: str, elemento: str) -> None:
        wait = WebDriverWait(driver, 10)
        elemento = wait.until(EC.visibility_of_element_located([tipo,elemento]))
        return 
    
    def elementos(self) -> list:
        classe = By.CLASS_NAME
        article =  'listing-item__jobs'
        carrega_vagas_botao = 'load-more'
        vagas_encontradas = 'search-results__title'
        return [classe, article, carrega_vagas_botao, vagas_encontradas]
    
        
    def abre_navegador(self) -> webdriver.Chrome:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://hipsters.jobs/jobs/')
        return driver
    
    def encontra_todas_vagas(self, driver:webdriver.Chrome) -> None:
        classe, article, botao, vagas_encontradas = self.elementos()
        vagas_totais = int()
        print(classe)
        print(vagas_totais)
        print(vagas_encontradas)
        self.espera_elemento_aparecer(driver, classe, vagas_encontradas)
        vagas = driver.find_element(classe, vagas_encontradas).text.split(' ')[0]
        print(vagas)
        while vagas_totais < int(vagas):
            print(vagas_totais)
            self.espera_elemento_aparecer(driver, classe, article)
            elements = driver.find_elements(classe, article)
            vagas_totais = len(elements)
            try: 
                self.espera_elemento_aparecer(driver, classe, botao)
                botao_vagas = driver.find_element(classe, botao).click()
            except:
                pass
            
    def cria_lista_vagas(self, driver:webdriver.Chrome) -> list:
            classe, article, _, _ = self.elementos()
            vagas = list()
            self.espera_elemento_aparecer(driver, classe, article)
            elements = driver.find_elements(classe, article)
            for index, element in enumerate(elements):
                vaga = dict()
                html = element.get_attribute('outerHTML')
                soap = BeautifulSoup(html, 'html.parser')
                link = soap.find('a', class_='link')
                spans = soap.find_all('span')
                contrato = spans[0].text.strip()
                empresa = spans[1].text.strip() if len(spans) >= 2 else 'Não especifica a empresa'
                local = spans[2].text.strip() if len(spans) >= 3 else 'Não especifica o local'
                cargo = link.text
                url = link['href']
                vaga = {'empresa': empresa, 'contrato': contrato, 'cargo': cargo, 'local': local, 'site': url}
                vagas.append(vaga)
            return vagas
    
    def controller(self):
        driver = self.abre_navegador()
        self.encontra_todas_vagas(driver)
        lista = self.cria_lista_vagas(driver)
        df = pd.DataFrame(lista)
        return df