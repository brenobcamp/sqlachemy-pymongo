from sqlalchemy import (
    create_engine, Column, Integer, String, inspect
    )
from sqlalchemy.orm import (
    declarative_base, relationship, Session
)

Base = declarative_base()
engine = create_engine('sqlite:///memory')


class Cliente(Base):
    """
        Cria a tabela Cliente com o sqlalchemy
    """
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(9))


class Endereco(Base):
    """
        Cria a tabela endereço com o sqlalchemy
    """
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = relationship("Cliente", back_populates="id")

def cria_tabelas():
    """
        Cria as tabelas no sqlite
    """
    Base.metadata.create_all(engine)


cria_tabelas()

insp = inspect(engine)
print(insp.get_table_names())

with Session(engine) as session:
    breno = Cliente(
        nome="Breno",
        fullname="Breno Campos",
        address=[Address(email_address='brenobcampos@gmail.com')]
    )
    sandy = User(
        name="Sandy",
        fullname="Sandy Alves",
        address=[Address(email_address="sandyalves@gmail.com"), Address(email_address="sandy@gmail.com")]
    )
    pedro = User(
        name="Pedro",
        fullname="Pedro Lucas")