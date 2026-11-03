---
content_hash: fa5f1cffce89a8245a26cc0084cc063a8876472b547281733eacc5baf5c60cbc
fetched_at: '2026-06-29T00:11:21.253009+00:00'
page_id: '689880562'
product: rm
source: tdn-rm
title: DT Registro Online Grafeno
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Registro+Online+Grafeno
version: 10
---

# Registro Online Grafeno

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção & Projetos* |
| **Módulo:** | **TOTVS Gestão Financeira** |
| **Requisito/S****tory/Issue:** | *TINPAD001-13398* |

## Descrição

Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online de cobrança registrada do Banco Grafeno.

## Procedimento para Configuração

No TOTVS Gestão Financeira, menu *Movimentações Bancárias | Controle Bancário | Convênio,* devem ser feitas as configurações do convênio para o registro de cobrança online:

* **Permite registro online*:*** Define se o convênio permite utilizar o registro de cobrança online.
* **Ambiente**: Define o ambiente que será feito o registro de cobrança no banco.
* **URL do serviço de registro de cobrança**: Deve ser informada a URL do serviço de registro de cobrança disponibilizada pelo banco.
* **URL de homologação do serviço de registro de cobrança**: Deve ser informada a URL de homologação do serviço de registro de cobrança disponibilizada pelo banco.  Veja mais em [COBRANÇA GRAFENO](https://docs.grafeno.digital/reference/cria%C3%A7%C3%A3o-de-cobran%C3%A7as)
* **Token**: A autenticação na API Grafeno Pagamento é feita através de um token enviado por header. Veja mais em [TOKENS GRAFENO](https://docs.grafeno.digital/reference/autentica%C3%A7%C3%A3o)

Pode ser utilizado o [Cadastro de Layout do Registro Online](http://tdn.totvs.com/pages/viewpage.action?pageId=311625508), para enviar dados de forma flexível para o registro online de cobrança para o banco. Para isso deve ser feito o [Cadastro de associação de fórmulas e campos do registro online](http://tdn.totvs.com/pages/viewpage.action?pageId=307835775) no cadastro do convênio.

O cadastro do layout do registro online do Grafeno deve ser feita de acordo com o manual de cobrança online do banco, da seguinte maneira:

No cadasto de Banco, anexo e Layout Registro Online, realize o cadastros dos campos abaixo e depois associe no convênio com seus valores.

**Atenção**: Alguns campos obrigatórios devem ser informados no Layout do Registro Online do convênio. Os valores de multa e juros precisam ser informados no layout devido ao RM não trabalhar com estes valores mês.

Multa: Valor informado em percentual

Tipo de Juros: Tipo de juros (Percentual ou Valor)

Régua de Cobrança no Cadastro: Obter o ID da regra de cobrança no URL da regra de cobrança no site pelo menu Cobranças => Réguas de Cobranças => Editar, exemplo "https://pagamentos.grafeno.be/messaging\_rules/b398da13.../edit"

Juros Mês: Valor informado em percentual

Exemplos para os campos da seção principal:

* applicableFine = 0.01
* interestType = (Escolher um opção abaixo para colocar no valor fixo)
  + percentage
  + fixed
* messagingRuleUuid = "b398da13..."
* monthlyInterest = 0.01

* **IMPORTANTE:** O número da conta e dígito informada no convênio será utilizada para o registro da cobrança online. Mais detalhes em [CRIAÇÃO DE COBRANÇAS GRAFENO](https://grafeno-sa.github.io/pagamentos-doc/#criacao-de-cobrancas)
