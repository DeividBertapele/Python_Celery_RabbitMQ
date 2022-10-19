from dataclasses import dataclass
from celery import chain
from tasks import ocr_documento, validar_cpf_no_governo


@dataclass
class Pessoa:
    nome: str
    telefone: str
    documento: str


def cadastro(pessoa: Pessoa):

    chain(
        ocr_documento.s(pessoa.documento),
        validar_cpf_no_governo.s(),
        # enviar_email
    )
    return 'Cadastro em avaliação, você recebera um email em breve'


p = Pessoa(
    'Teste',
    '44111111111',
    'images/documento_certo.png'
)

print(cadastro(p))




# from tasks import ola_mundo

# ola_mundo.delay()