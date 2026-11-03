---
content_hash: 92ca0c87d7b8af3080e04de8e09d9de1e530cb28b0f16a08e56e5c03652a48cc
fetched_at: '2026-06-29T00:08:39.367925+00:00'
page_id: '286017432'
product: rm
source: tdn-rm
title: Registro Boleto Online Banco do Brasil
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+Boleto+Online+Banco+do+Brasil
version: 125
---

## **01. VISÃO GERAL**

**Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online de cobrança registrada do Banco do Brasil.**

## **02. CONFIGURAÇÃO**

No TOTVS Gestão Financeira, através do menu *Movimentações Bancárias | Controle Bancário | Convênio,* devem ser feitas as configurações do convênio para o registro de boleto online. Abaixo, destacamos os campos conforme os modelos de registro online disponíveis:  
  
Modelo v1:

* **Permite registro de boleto online*:*** Define se o convênio permite utilizar o registro de boleto online.
* **Ambiente**: Define o ambiente que será feito o registro do boleto no banco.
* **Modelo de Registro Online**: Modelo "v1".
* **URL do serviço de registro de cobrança**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo banco. **[https://cobranca.bb.com.br:7101/registrarBoleto](https://cobranca.homologa.bb.com.br:7101/registrarBoleto)**
* **URL de homologação do serviço de registro de cobrança:**Deve ser informada a URL de homologação do serviço de registro do boleto disponibilizada pelo banco. **<https://cobranca.homologa.bb.com.br:7101/registrarBoleto>**
* **URL do sistema autorizador**: Deve ser informado a URL do sistema autorizador que retornará o token de acesso ao serviço de registro de cobrança. **<https://oauth.bb.com.br/oauth/token>**
* **URL de homologação do sistema autorizador:**Deve ser informado a URL de homologação do sistema autorizador que retornará o token de acesso ao serviço de homologação de registro de cobrança. **<https://oauth.hm.bb.com.br/oauth/token>**
* **Client Id**: Código de acesso ao sistema autorizador fornecido pelo banco.
* **Client Secret**: Senha de acesso ao sistema autorizador fornecido pelo banco.

Segue os dados que podem ser utilizados para teste no ambiente de homologação para o modelo 'v1':

* Client Id: eyJpZCI6IjgwNDNiNTMtZjQ5Mi00YyIsImNvZGlnb1B1YmxpY2Fkb3IiOjEwOSwiY29kaWdvU29mdHdhcmUiOjEsInNlcXVlbmNpYWxJbnN0YWxhY2FvIjoxfQ
* Client Secret: eyJpZCI6IjBjZDFlMGQtN2UyNC00MGQyLWI0YSIsImNvZGlnb1B1YmxpY2Fkb3IiOjEwOSwiY29kaWdvU29mdHdhcmUiOjEsInNlcXVlbmNpYWxJbnN0YWxhY2FvIjoxLCJzZXF1ZW5jaWFsQ3JlZGVuY2lhbCI6MX0
* Numero do convênio: 2625444
* Carteira: 17
* Tipo (variação) da carteira: 19
* CPF do pagador: 00000000191

Modelo v2:

* **Permite registro de boleto online*:*** Define se o convênio permite utilizar o registro de boleto online.
* **Ambiente**: Define o ambiente que será feito o registro do boleto no banco.
* **Modelo de Registro Online**: Modelo "v2".
* **URL do serviço de registro de cobrança**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo banco. **https://api.bb.com.br/cobrancas/v2**
* **URL de homologação do serviço de registro de cobrança:**Deve ser informada a URL de homologação do serviço de registro do boleto disponibilizada pelo banco. **https://api.hm.bb.com.br/cobrancas/v2**
* **URL do sistema autorizador**: Deve ser informado a URL do sistema autorizador que retornará o token de acesso ao serviço de registro de cobrança. **https://oauth.bb.com.br/oauth/token**
* **URL de homologação do sistema autorizador:**Deve ser informado a URL de homologação do sistema autorizador que retornará o token de acesso ao serviço de homologação de registro de cobrança. **https://oauth.hm.bb.com.br/oauth/token**
* **Client Id**: Código de acesso ao sistema autorizador fornecido pelo banco.
* **Client Secret**: Senha de acesso ao sistema autorizador fornecido pelo banco.
* **App-Key:** Chave secreta (produção) de validação do cliente disponibilizada pelo banco
* **App-Key de Homologação:** Chave secreta (homologação) de validação de disponibilizada pelo banco

Segue os dados que podem ser utilizados para teste no ambiente de homologação para o modelo 'v2':

* Client Id: eyJpZCI6ImZkODk1MTItZTQyMi00YjVkLWFhIiwiY29kaWdvUHVibGljYWRvciI6MCwiY29kaWdvU29mdHdhcmUiOjc1NDI4LCJzZXF1ZW5jaWFsSW5zdGFsYWNhbyI6MX0
* Client Secret: eyJpZCI6ImI5NWZjMDAtODUzZS00ZDU2LTg4OTktNTBiMGJlMjZlODQxYjUiLCJjb2RpZ29QdWJsaWNhZG9yIjowLCJjb2RpZ29Tb2Z0d2FyZSI6NzU0MjgsInNlcXVlbmNpYWxJbnN0YWxhY2FvIjoxLCJzZXF1ZW5jaWFsQ3JlZGVuY2lhbCI6MSwiYW1iaWVudGUiOiJob21vbG9nYWNhbyIsImlhdCI6MTY5NjAxNjk0NDcyN30
* App-Key de Homologação: 3f85582a484043a38e04fe28a9beb190
* Numero do convênio: 3128557
* Carteira: 17
* Tipo (variação) da carteira: 35
* CPF do pagador: 96050176876

Importante: É possível realizar o cancelamento da remessa dos boletos gerados com um convênio configurado para o modelo v2. Mais informações, confira o processo [Cancelamento de Registro online](https://tdn.totvs.com/display/public/LRM/Cancelamento+de+Registro+online).

Pode ser utilizado o [Cadastro de Layout do Registro Online](http://tdn.totvs.com/pages/viewpage.action?pageId=311625508), para enviar dados de forma flexível para o registro online dos boletos para o banco. Para isso deve ser feito o [Cadastro de associação de fórmulas e campos do registro online](http://tdn.totvs.com/pages/viewpage.action?pageId=307835775) no cadastro do convênio utilizado para o registro online.

O cadastro do layout do registro online do Banco do Brasil deve ser feita de acordo com o manual de cobrança online do banco, da seguinte maneira:

* Exemplos:  
    
  + API v1  

    codigoTipoDesconto  
    dataDescontoTitulo  
    percentualDescontoTitulo  
    valorDescontoTitulo  
    valorAbatimentoTitulo  
    quantidadeDiaProtesto  
    codigoTipoJuroMora  
    percentualJuroMoraTitulo  
    valorJuroMoraTitulo  
    codigoTipoMulta  
    dataMultaTitulo  
    percentualMultaTitulo  
    valorMultaTitulo  
    textoDescricaoTipoTitulo  
    indicadorPermissaoRecebimentoParcial  
    textoMensagemBloquetoOcorrencia

* + API v2

dataEmissao

dataVencimento

quantidadeDiasNegativacao

orgaoNegativador

quantidadeDiasProtesto

indicadorAceiteTituloVencido

dados.Desconto.tipo (*opcional)*  
dados.Desconto.dataExpiracao *(opcional)*  
dados.Desconto.porcentagem *(opcional)*  
dados.Desconto.valor *(opcional)*

dados.segundoDesconto.dataExpiracao  
dados.segundoDesconto.porcentagem  
dados.segundoDesconto.valor

dados.terceiroDesconto.dataExpiracao  
dados.terceiroDesconto.porcentagem  
dados.terceiroDesconto.valor

dados.jurosMora.tipo

dados.jurosMora.porcentagem

dados.jurosMora.valor

dados.multa.tipo

dados.multa.data

dados.multa.porcentagem

dados.multa.valor

**Observações**

* O primeiro desconto (grupo "desconto") já é enviado nativamente no JSON gerado pelo sistema, buscando o valor de desconto do Boleto. Somente se desejar customizar o valor do primeiro desconto (utilizando fórmula, por exemplo) que será necessário inserir os campos do primeiro desconto no layout do registro online e associa-los no cadastro do Convênio.
* Para os campos de valores ou percentual deve seguir o formato de acordo com o manual disponibilizado pelo banco. Ao definir um valor fixo ou formula deve ser retornado um string com o separador decimal '.' (ponto).   
  Exemplo:   
  2.49 (com duas casas decimais )  
  30.03.2018 (data no formato DD.MM.YYYY)
* O campo Data da Multa será calculado a partir da Data de Vencimento do boleto acrescido do parâmetro *Dias de Atraso* configurado na etapa Valor Líquido do Lançamento Financeiro.

divs
