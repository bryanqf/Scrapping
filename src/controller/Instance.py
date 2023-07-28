from ..model.model import Model

class Intance:
    model = Model()
    Local = model.Local
    Empresas = model.Empresas
    Vagas = model.Vagas
   

    def local(self, set_local) -> Local:
        local_dict = dict()
        session = self.model.cria_sessao()
        for item in set_local:
            local_temp = self.Local(local=item)
            session.add(local_temp)
            session.flush()
            local_dict[item] = local_temp.idlocal
        self.model.fecha_sessao(session)
        return local_dict
       
    def empresa(self, set_empresa, local_dict) -> Empresas:
        empresa_dict = dict()
        session = self.model.cria_sessao()
        for empresa, local_empresa in set_empresa:
            local_id = local_dict.get(local_empresa)
            empresa_temp = self.Empresas(empresa=empresa, local_idlocal=local_id)
            session.add(empresa_temp)
            session.flush()
            empresa_dict[empresa] = empresa_temp.idempresa
        self.model.fecha_sessao(session)
        return empresa_dict
    
    def vagas(self, lista_vagas, empresa_dict) -> Vagas:
        session = self.model.cria_sessao()
        for cargo, contrato, site, empresa in lista_vagas:
            empresa_id = empresa_dict[empresa]
            vagas_temp = self.Vagas(vaga=cargo, contrato=contrato, site=site, empresa_idempresa=empresa_id)
            session.add(vagas_temp)
        self.model.fecha_sessao(session)


