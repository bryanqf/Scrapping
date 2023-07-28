from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import sessionmaker, backref
from src.model.Database import Database

class Model:
    database = Database()
    engine = database.connecta_database()
    def cria_sessao(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
    def fecha_sessao(self, session):
        session.commit()
        session.close()
        
    class Base(DeclarativeBase):
        pass
    class Local(Base):
        __tablename__ = 'local'
        idlocal = Column(Integer, primary_key=True, autoincrement=True)
        local = Column(String(100))
        empresas = relationship('Empresas', backref='local')

    class Empresas(Base):
        __tablename__ = 'empresas'
        idempresa = Column(Integer, primary_key=True, autoincrement=True)
        empresa = Column(String(100))
        local_idlocal = Column(Integer, ForeignKey('local.idlocal'))
        vagas = relationship('Vagas', backref='empresa')

    class Vagas(Base):
        __tablename__ = 'vagas'
        idvaga = Column(Integer, primary_key=True, autoincrement=True)
        vaga = Column(String(200))
        contrato = Column(String(50))
        site = Column(String(200))
        empresa_idempresa = Column(Integer, ForeignKey('empresas.idempresa'))

    Base.metadata.create_all(engine)