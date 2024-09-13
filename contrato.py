from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from datetime import datetime
from enum import Enum


class ProdutoEnum(str,Enum):   
    produto1 = "Curso Basico"
    produto2 = "Curso de Qualificação Profissional"
    produto3 = "Serviço de Academia"
    produto4 = "Clube de Esporte e Lazer"
    produto5 = "Atendimento de Saúde"
    produto6 = "Atendimento Odontologico"


class Vendas(BaseModel):
    """
    Modelo de dados para as vendas.

    Args:
        email (EmailStr): email do comprador
        data (datetime): data da venda
        valor (PositiveFloat): valor da venda
        quantidade (PositiveInt): quantidade de produtos
        produto (ProdutoEnum): nome do produto
    """
    
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum

