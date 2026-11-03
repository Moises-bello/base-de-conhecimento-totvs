---
content_hash: 4422b79a523197529b72b695b14ddf1d0d11c4af73e4f0ade17e0df431170b62
fetched_at: '2026-06-29T00:12:08.454046+00:00'
page_id: '934635869'
product: rm
source: tdn-rm
title: Registro online Sicredi
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+online+Sicredi
version: 18
---

# Conteúdo:

Conteúdo:

# 1. Registro online

Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online de cobrança registrada do Sicredi.  
procedimentoparaconfiguracao

# 2. Procedimento para configuração modeloderegistro

Através do cadastro do Convênio, localizado no menu 'Movimentações Bancárias', é necessário habilitar a opção "Permite registro de boleto online" e definir os parâmetros de acordo com os dados fornecidos pelo Sicredi. O TOTVS Gestão Financeira disponibiliza dois modelos de registro:

Cards2Modelo de Registro Online v1 (descontinuado)Modelo descontinuado de registro online

* **Permite registro de boleto online:**Define se o convênio permite utilizar o registro de boleto online.
* **Ambiente**: Define o ambiente que será feito o registro do boleto na instituição financeira.
* **Modelo de Registro Online:**Define o modelo do registro online: "v1".
* **URL do serviço de registro de cobrança**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pela instituição financeira.
* **URL do sistema de autenticação**: Deve ser informada a URL do sistema de autenticação conforme manual disponibilizado pela instituição financeira.
* **Código de acesso:** Deve ser informado o código de acesso (token master) ao sistema de autenticação disponibilizado pela instituição financeira.

Conforme detalhado no  deste documento, é possível customizar o dado a ser enviado no registro online. Abaixo, seguem alguns exemplos de cadastro de campo no layout do registro online:

* informativo
* mensagem
* valordesconto1

* multas
true3Modelo de Registro Online v2Modelo atual de registro online

* **Permite registro de boleto online*:***Define se o convênio permite utilizar o registro de boleto online.
* **Ambiente**: Define o ambiente que será feito o registro do boleto na instituição financeira.
* **Modelo de Registro Online:**Define o modelo do registro online: "v2".
* **URL do serviço de registro de cobrança**: Deve ser informada a URL do serviço de registro de cobrança disponibilizada pela instituição financeira (<https://api-parceiro.sicredi.com.br/cobranca/boleto/v1>).
* **URL do sistema autenticação**: Deve ser informado a URL do sistema de autenticação conforme manual disponibilizado pela instituição financeira (<https://api-parceiro.sicredi.com.br/auth/openapi/token>).
* **URL do serviço de registro de cobrança - Homologação**: Deve ser informada a URL do serviço de registro de cobrança - Homologação conforme manual disponibilizado pela instituição financeira (<https://api-parceiro.sicredi.com.br/sb/cobranca/boleto/v1>).
* **URL do sistema autenticação - Homologação**: Deve ser informado a URL do sistema de autenticação - Homologação conforme manual disponibilizado pela instituição financeira (<https://api-parceiro.sicredi.com.br/sb/auth/openapi/token>).
* **Usuário**: Deve ser informado o usuário disponibilizado pela instituição financeira.
* **Senha**: Deve ser informada a senha disponibilizada pela instituição financeira.
* **Chave de API (x-api-key)**: Deve ser informado a chave API disponibilizado pela instituição financeira.
* **Chave de API (x-api-key) - Homologação**: Deve ser informado a chave API de homologação disponibilizado pela instituição financeira.

Conforme detalhado no  deste documento, é possível customizar o dado a ser enviado no registro online. Abaixo, seguem alguns exemplos de cadastro de campo no layout do registro online:

* informativo
* mensagem
* valordesconto1
* pagador.nome
* diasProtestoAuto

* diasNegativacaoAuto

* pagador.tipoPessoa
* pagador.endereco
* pagador.endereco
* multa
* Juros
* tipoDesconto
* valordesconto1
* dataDesconto1
* valorDesconto2
* dataDesconto2
* valorDesconto3
* dataDesconto3  
    
  **IMPORTANTE**:
* Para o campo 'Espécie Cnab' do boleto, deve ser informado os seguintes valores definidos conforme o manual da instituição financeira:

  A - DUPLICATA MERCANTILINDICACAO  
  B - DUPLICATA RURAL  
  C - NOTA PROMISSORIA  
  D - NOTA PROMISSORIA RURAL  
  E - NOTA SEGUROS  
  G - RECIBO  
  H - LETRA CAMBIO  
  I - NOTA DEBITO  
  J - DUPLICATA SERVICO INDICACAO  
  K - OUTROS  
  O - BOLETO PROPOSTA  
  P - CARTAO CREDITO
* Para a correta transmissão das instruções de protesto e negativação automática via API v2 do Sicredi, é imprescindível a utilização das tags específicas que atendam ao esquema de dados (*payload*) exigido pela instituição financeira.
  + **diasProtestoAuto**: Utilizada para definir a quantidade de dias corridos após o vencimento para o envio automático do título a protesto.
  + **diasNegativacaoAuto**: Utilizada para definir a quantidade de dias corridos após o vencimento para o envio automático do título para negativação.
* Apesar do Sicredi possuir um serviço que permite alteração da data de vencimento do boleto, a funcionalidade ainda não está disponível no TOTVS Gestão Financeira e será implementada futuramente.

# 3. Customização de dados no registro online

Pode ser utilizado o [Cadastro de Layout do Registro Online](https://tdn.totvs.com/display/LRM/Layout+Registro+Online), para enviar dados de forma flexível para o registro online dos boletos para a instituição financeira. Para isso deve ser feito o [Cadastro de associação de fórmulas e campos do registro online](https://tdn.totvs.com/pages/viewpage.action?pageId=421388759) no cadastro do convênio.

O cadastro do layout do registro online do Sicredi deve ser realizado de acordo com o manual de cobrança online da instituição financeira. Demonstramos alguns exemplos de campos, nas guias referentes a cada modelo de registro online ().
