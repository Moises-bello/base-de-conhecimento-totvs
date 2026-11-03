---
content_hash: a1f17be6db22594e317d40f09289419b5f487f2a9f19cbbc78398a56a47077e2
fetched_at: '2026-06-29T00:12:15.299498+00:00'
page_id: '976133710'
product: rm
source: tdn-rm
title: Registro online Grafeno
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+online+Grafeno
version: 1
---

# Conteúdo:

Conteúdo:

# 1. Registro online

Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online de cobrança registrada do banco Grafeno.

# 2. Procedimento para configuração

Através do cadastro do Convênio, localizado no menu 'Movimentações Bancárias', é necessário habilitar a opção "Permite registro de boleto online" e definir os parâmetros de acordo com os dados fornecidos pelo banco Grafeno.

Cards2Modelo de Registro Online v1

* **Permite registro de boleto online:**Define se o convênio permite utilizar o registro de boleto online.
* **Integração com os serviços da AutBank:**Define que o banco utiliza o padrão da AutBank para o registro online de boletos.
* **Ambiente**: Define o ambiente que será feito o registro do boleto no banco.
* **URL do serviço de registro de cobrança**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo banco.
* **URL de homologação do serviço de registro de cobrança**: Deve ser informada a URL de homologação do serviço de registro do boleto disponibilizada pelo banco. Veja mais em [COBRANÇA GRAFENO](https://docs.grafeno.digital/reference/cria%C3%A7%C3%A3o-de-cobran%C3%A7as)
* **Token**: A autenticação na API Grafeno Pagamento é feita através de um token enviado por header. Veja mais em [TOKENS GRAFENO](https://docs.grafeno.digital/reference/autentica%C3%A7%C3%A3o)

Conforme detalhado no item 3 deste documento, é possível enviar os dados de forma flexível para o banco ao registrar online os boletos. O cadastro do layout do registro online do Grafeno deve ser feito conforme o manual de cobrança online do banco, onde contempla a descrição de cada campo. Alguns campos obrigatórios devem ser informados no Layout do Registro Online do convênio. Os valores de multa e juros precisam ser informados no layout devido ao TOTVS Gestão Financeira não trabalhar com estes valores mês.

Multa: Valor informado em percentual

Tipo de Juros: Tipo de juros (Percentual ou Valor)

Régua de Cobrança no Cadastro: Obter o ID da regra de cobrança no URL da regra de cobrança no site pelo menu Cobranças => Réguas de Cobranças => Editar, exemplo "<https://pagamentos.grafeno.be/messaging_rules/>b398da13.../edit"

Juros Mês: Valor informado em percentual

**Exemplos** para os campos da seção principal:

* applicableFine = 0.01
* interestType = (Escolher um opção abaixo para colocar no valor fixo)
  + percentage
  + fixed
* messagingRuleUuid = "b398da13..."
* monthlyInterest = 0.01

# 3. Customização de dados no registro online

Pode ser utilizado o [Cadastro de Layout do Registro Online](https://tdn.totvs.com/display/LRM/Layout+Registro+Online), para enviar dados de forma flexível para o registro online dos boletos para o banco. Para isso deve ser feito o [Cadastro de associação de fórmulas e campos do registro online](https://tdn.totvs.com/pages/viewpage.action?pageId=421388759) de acordo com o manual de cobrança online do Grafeno.

**IMPORTANTE**:

* O número da conta e dígito informada no convênio será utilizada para o registro da cobrança online. Mais detalhes em [CRIAÇÃO DE COBRANÇAS GRAFENO](https://grafeno-sa.github.io/pagamentos-doc/#criacao-de-cobrancas)
