---
content_hash: 0c5954681ebae2cd89a619abeb0079ca1127aabbc229f235c0fc2c70691d1369
fetched_at: '2026-06-29T00:12:07.277499+00:00'
page_id: '922683758'
product: rm
source: tdn-rm
title: Registro online Santander
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+online+Santander
version: 27
---

# Conteúdo:

Conteúdo:

# 1. Registro online

Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online da carteira de cobrança registrada do Banco Santander.

procedimentoparaconfiguracao

# 2. Procedimento para configuração

Através do cadastro do Convênio, localizado no menu 'Movimentações Bancárias', é necessário habilitar a opção "Permite registro de boleto online" e definir os parâmetros de acordo com os dados fornecidos pelo Santander. Obs: A partir dos patchs 12.1.2410.222 e 12.1.2502.138 o sistema dispõe do modelo 'v2' do registro online.

CardstrueModelo de Registro Online v1

* **Ambiente**: Define o ambiente que será feito o registro do boleto no banco.
* **URL do serviço de registro do boleto**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo banco. Para o banco Santander é a URL do serviço de cobrança. (<https://ymbcash.santander.com.br/ymbsrv/CobrancaV3EndpointService>)
* **URL do serviço do ticket de segurança**: Deve ser informada a URL do serviço do ticket de segurança disponibilizado pelo banco.  (<https://ymbdlb.santander.com.br/dl-ticket-services/TicketEndpointService>)
* **Cód. Estação**: Deve ser informado o código da estação do convênio gerada pelo banco.
* **Certificado digital**: Deve ser informado o certificado digital que foi cadastrado junto ao banco.

**Importante**: **Conforme manual disponibilizado pelo banco, o cliente deverá adquirir um certificado digital junto a uma empresa certificadora, e efetuar o cadastramento no ambiente de segurança do banco enviando o arquivo no formato ".CER" referente ao certificado adquirido. Requisitos: Certificado tipo Client de 2048 bits.**

Modelo de Registro Online v2

* **Ambiente**: Define o ambiente que será feito o registro do boleto no banco.
* **URL do serviço de registro de cobrança**: Deve ser informada a URL (disponibilizada pelo banco) do serviço de registro do boleto. (<https://trust-open.api.santander.com.br/collection_bill_management/v2/workspaces/{WORKSPACE_ID}/bank_slips>)
* **URL de homologação do serviço de registro de cobrança**: Deve ser informada a URL (disponibilizada pelo banco) de homologação do serviço de registro do boleto. (<https://trust-sandbox.api.santander.com.br/collection_bill_management/v2/workspaces/{WORKSPACE_ID}/bank_slips>)
* **URL do sistema autorizador**: Deve ser informada a URL (disponibilizada pelo banco) do sistema autorizador. (<https://trust-open.api.santander.com.br/auth/oauth/v2/token>)
* **URL de homologação do sistema autorizador**: Deve ser informada a URL (disponibilizada pelo banco) de homologação do sistema autorizador. (<https://trust-sandbox.api.santander.com.br/auth/oauth/v2/token>)
* **URL para criação do Workspace**: Deve ser informada a URL (disponibilizada pelo banco) para criação do Workspace. (<https://trust-open.api.santander.com.br/collection_bill_management/v2/workspaces>)
* **URL de homologação para criação do Workspace**: Deve ser informada a URL (disponibilizada pelo banco) de homologação para criação do Workspace. (<https://trust-sandbox.api.santander.com.br/collection_bill_management/v2/workspaces>)
* **Client Id**: Deve ser informado o código de acesso ao sistema autorizador fornecido pelo banco.
* **Client Secret**: Deve ser informada a senha de acesso ao sistema autorizador fornecido pelo banco.
* **Certificado não auto assinado**: Deve ser informado o certificado digital obtido pela empresa.
* **Código do workspace**: Código gerado ao clicar no botão "Obter workspace" quando o ambiente definido é "Produção".
* **Código do workspace de homologação:** Código gerado ao clicar no botão "Obter workspace" quando o ambiente definido é "Teste".

Conforme detalhado no  deste documento, é possível customizar o dado a ser enviado no registro online. Abaixo, seguem alguns exemplos de cadastro de campo no layout do registro online:

**Campo da seção** "**documentKind":** Deve ser **obrigatoriamente** informado com o tipo de espécie do documento, conforme uma das opções válidas indicadas pelo manual do banco:

Exemplo de preenchimento do campo do layout do registro online na associação do layout nos anexos do cadastro do convênio:

Outras opções que podem ser usadas no valor fixo:

* DUPLICATA\_MERCANTIL
* DUPLICATA\_SERVICO
* NOTA\_PROMISSORIA
* NOTA\_PROMISSORIA\_RURAL
* RECIBO
* APOLICE\_SEGURO
* BOLETO\_CARTAO\_CREDITO
* BOLETO\_PROPOSTA
* BOLETO\_DEPOSITO\_APORTE
* CHEQUE
* OUTROS

**Campo da seção "payer"**:

* dados.payer.name
* dados.payer.city

**Campo da seção "beneficiary"**:

* dados.beneficiary.name
* dados.beneficiary.documentType
* dados.beneficiary.documentNumber

**Campo da seção "discount"**:

* dados.discount.type
* dados.discount.discountOne.limitDate
* dados.discount.discountOne.value

**Campo da seção "sharing"**:

* dados.sharing.code
* dados.sharing.value

**IMPORTANTE**:

* De acordo com o layout do banco podem ocorrer 3 (três) descontos, portanto o nome do campo deverá ser 'discount/discountOne.', 'discount/discountTwo.' e 'discount.discountThree.'.
* Os campos de desconto "limitDate" e "value" são pares, se um deles for informado, obrigatoriamente o outro também deve ser para o tipo "VALOR\_DATA\_FIXA". Para os descontos por antecipação "VALOR\_DIA\_CORRIDO" e "VALOR\_DIA\_UTIL" é obrigatório informar somente o valor de desconto ao dia a ser concedido "value", a data limite será a própria data de vencimento do boleto.

# 3. Customização de dados no registro online

customizacao

Pode ser utilizado o [Cadastro de Layout do Registro Online](https://tdn.totvs.com/display/LRM/Layout+Registro+Online), para enviar dados de forma flexível para o registro online dos boletos para o banco. Para isso deve ser feito o [Cadastro de associação de fórmulas e campos do registro online](https://tdn.totvs.com/pages/viewpage.action?pageId=421388759) no cadastro do convênio.

O cadastro do layout do registro online do Santander deve ser realizado de acordo com o manual de cobrança online do banco. Demonstramos alguns exemplos de campos na guia referente ao modelo de registro online 'v2' ().
