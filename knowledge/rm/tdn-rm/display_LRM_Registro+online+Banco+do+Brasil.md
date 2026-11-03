---
content_hash: 61ad23e7ada34b574b8fe3ab4d0055c37657b83effbf9da59f1c7d1c0f067cbd
fetched_at: '2026-06-29T00:12:08.418345+00:00'
page_id: '934622172'
product: rm
source: tdn-rm
title: Registro online Banco do Brasil
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+online+Banco+do+Brasil
version: 4
---

# Conteúdo:

Conteúdo:

# 1. Registro online

Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online da carteira de cobrança registrada do Banco do Brasil.

procedimentoparaconfiguracao

# 2. Procedimento para configuração

Através do cadastro do Convênio, localizado no menu 'Movimentações Bancárias', é necessário habilitar a opção "Permite registro de boleto online" e definir os parâmetros de acordo com os dados fornecidos pelo Banco do Brasil.

CardstrueModelo de Registro Online v1

* **Permite registro de boleto online*:***Define se o convênio permite utilizar o registro de boleto online.
* **Ambiente**: Define o ambiente que será feito o registro do boleto no banco.
* **URL do serviço de registro de cobrança**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo banco. **[https://cobranca.bb.com.br:7101/registrarBoleto](https://cobranca.homologa.bb.com.br:7101/registrarBoleto)**
* **URL de homologação do serviço de registro de cobrança:**Deve ser informada a URL de homologação do serviço de registro do boleto disponibilizada pelo banco. **<https://cobranca.homologa.bb.com.br:7101/registrarBoleto>**
* **URL do sistema autorizador**: Deve ser informado a URL do sistema autorizador que retornará o token de acesso ao serviço de registro de cobrança. **<https://oauth.bb.com.br/oauth/token>**
* **URL de homologação do sistema autorizador:**Deve ser informado a URL de homologação do sistema autorizador que retornará o token de acesso ao serviço de homologação de registro de cobrança. **<https://oauth.hm.bb.com.br/oauth/token>**
* **Client Id**: Código de acesso ao sistema autorizador fornecido pelo banco.
* **Client Secret**: Senha de acesso ao sistema autorizador fornecido pelo banco.

Segue os dados que podem ser utilizados para teste no ambiente de homologação para o modelo 'v1':

* Client Id: eyJpZCI6IjgwNDNiNTMtZjQ5Mi00YyIsImNvZGlnb1B1YmxpY2Fkb3IiOjEwOSwiY29kaWdvU29mdHdhcmUiOjEsInNlcXVlbmNpYWxJbnN0YWxhY2FvIjoxfQ
* Client Secret: eyJpZCI6IjBjZDFlMGQtN2UyNC00MGQyLWI0YSIsImNvZGlnb1B1YmxpY2Fkb3IiOjEwOSwiY29kaWdvU29mdHdhcmUiOjEsInNlcXVlbmNpYWxJbnN0YWxhY2FvIjoxLCJzZXF1ZW5jaWFsQ3JlZGVuY2lhbCI6MX0
* Numero do convênio: 2625444
* Carteira: 17
* Tipo (variação) da carteira: 19
* CPF do pagador: 00000000191

Conforme detalhado no  deste documento, é possível customizar o dado a ser enviado no registro online. Abaixo, seguem alguns exemplos de cadastro de campo no layout do registro online:

Outros exemplos de campos:

codigoTipoDesconto  
dataDescontoTitulo  
percentualDescontoTitulo  
valorDescontoTitulo  
valorAbatimentoTitulo  
quantidadeDiaProtesto  
codigoTipoJuroMora  
percentualJuroMoraTitulo  
valorJuroMoraTitulo  
valorMultaTitulo  
textoDescricaoTipoTitulo  
indicadorPermissaoRecebimentoParcial

**Observações**

* O primeiro desconto (grupo "desconto") já é enviado nativamente no JSON gerado pelo sistema, buscando o valor de desconto do Boleto. Somente se desejar customizar o valor do primeiro desconto (utilizando fórmula, por exemplo) que será necessário inserir os campos do primeiro desconto no layout do registro online e associa-los no cadastro do Convênio.
* Para os campos de valores ou percentual deve seguir o formato de acordo com o manual disponibilizado pelo banco. Ao definir um valor fixo ou formula deve ser retornado um string com o separador decimal '.' (ponto).   
  **Exemplo**:   
  2.49 (com duas casas decimais )  
  30.03.2018 (data no formato DD.MM.YYYY)
* O campo Data da Multa será calculado a partir da Data de Vencimento do boleto acrescido do parâmetro *Dias de Atraso* configurado na etapa Valor Líquido do Lançamento Financeiro.
Modelo de Registro Online v2

* **Permite registro de boleto online*:***Define se o convênio permite utilizar o registro de boleto online.
* **Ambiente**: Define o ambiente que será feito o registro do boleto no banco.
* **URL do serviço de registro de cobrança**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo banco. **<https://api.bb.com.br/cobrancas/v2>**
* **URL de homologação do serviço de registro de cobrança:**Deve ser informada a URL de homologação do serviço de registro do boleto disponibilizada pelo banco. **<https://api.hm.bb.com.br/cobrancas/v2>**
* **URL do sistema autorizador**: Deve ser informado a URL do sistema autorizador que retornará o token de acesso ao serviço de registro de cobrança. **<https://oauth.bb.com.br/oauth/token>**
* **URL de homologação do sistema autorizador:**Deve ser informado a URL de homologação do sistema autorizador que retornará o token de acesso ao serviço de homologação de registro de cobrança. **<https://oauth.hm.bb.com.br/oauth/token>**
* **Client Id**: Código de acesso ao sistema autorizador fornecido pelo banco.
* **Client Secret**: Senha de acesso ao sistema autorizador fornecido pelo banco.
* **App-Key:** Chave secreta (produção) de validação do cliente disponibilizada pelo banco
* **App-Key de Homologação:** Chave secreta (homologação) de validação de disponibilizada pelo banco.

Segue os dados que podem ser utilizados para teste no ambiente de homologação para o modelo 'v2':

* Client Id: eyJpZCI6ImZkODk1MTItZTQyMi00YjVkLWFhIiwiY29kaWdvUHVibGljYWRvciI6MCwiY29kaWdvU29mdHdhcmUiOjc1NDI4LCJzZXF1ZW5jaWFsSW5zdGFsYWNhbyI6MX0
* Client Secret: eyJpZCI6ImI5NWZjMDAtODUzZS00ZDU2LTg4OTktNTBiMGJlMjZlODQxYjUiLCJjb2RpZ29QdWJsaWNhZG9yIjowLCJjb2RpZ29Tb2Z0d2FyZSI6NzU0MjgsInNlcXVlbmNpYWxJbnN0YWxhY2FvIjoxLCJzZXF1ZW5jaWFsQ3JlZGVuY2lhbCI6MSwiYW1iaWVudGUiOiJob21vbG9nYWNhbyIsImlhdCI6MTY5NjAxNjk0NDcyN30
* App-Key de Homologação: 3f85582a484043a38e04fe28a9beb190
* Numero do convênio: 3128557
* Carteira: 17
* Tipo (variação) da carteira: 35
* CPF do pagador: 96050176876

Conforme detalhado no  deste documento, é possível customizar o dado a ser enviado no registro online. Abaixo, seguem alguns exemplos de cadastro de campo no layout do registro online:

Outros exemplos de campos:

dataEmissao

dataVencimento

quantidadeDiasProtesto

indicadorAceiteTituloVencido

dados.Desconto.tipo (opcional)  
dados.Desconto.dataExpiracao (opcional)  
dados.Desconto.porcentagem (opcional)  
dados.Desconto.valor (opcional)

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
  **Exemplo**:   
  2.49 (com duas casas decimais )  
  30.03.2018 (data no formato DD.MM.YYYY)
* O campo Data da Multa será calculado a partir da Data de Vencimento do boleto acrescido do parâmetro *Dias de Atraso* configurado na etapa Valor Líquido do Lançamento Financeiro.
* É possível realizar o cancelamento da remessa dos boletos gerados com um convênio configurado para o modelo v2. Entretanto, o cancelamento do registro poderá ser realizado após 30min do registro do boleto junto ao Banco. Caso tente cancelar antes deste prazo, o Banco poderá retornar uma mensagem com este aviso. Mais informações, confira o processo [Cancelamento de Registro online](https://tdn.totvs.com/display/public/LRM/Cancelamento+de+Registro+online).

# 3. Customização de dados no registro online

customizacao

Pode ser utilizado o [Cadastro de Layout do Registro Online](https://tdn.totvs.com/display/LRM/Layout+Registro+Online), para enviar dados de forma flexível para o registro online dos boletos para o banco. Para isso deve ser feito o [Cadastro de associação de fórmulas e campos do registro online](https://tdn.totvs.com/pages/viewpage.action?pageId=421388759) no cadastro do convênio.

O cadastro do layout do registro online do Banco do Brasil deve ser realizado de acordo com o manual de cobrança online do banco. Demonstramos alguns exemplos de campos em cada modelo de registro online ().
