from src.controller.scrapping import Scrapping
from src.controller.Instance import Intance
def semeia_database():
    instance = Intance()
    scrap = Scrapping()
    #Dados 
    set_local = set()
    set_empresa = set()
    lista_vagas = list()
    df = scrap.controller()
    for index, row in df.iterrows():
        local = row['local']
        set_local.add(local)
        empresa = (row['empresa'], row['local'])
        set_empresa.add(empresa)
        vaga = [row['cargo'], row['contrato'], row['site'], row['empresa']]
        lista_vagas.append(vaga)

    local_dict = instance.local(set_local)
    empresa_dict = instance.empresa(set_empresa, local_dict)
    instance.vagas(lista_vagas, empresa_dict)

semeia_database()