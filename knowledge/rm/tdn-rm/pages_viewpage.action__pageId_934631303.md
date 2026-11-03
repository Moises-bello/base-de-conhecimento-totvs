---
content_hash: c715668ce95e77f728ca2dc3fc6f75b3328d38ab5e5a9b133b6ffd04846140ec
fetched_at: '2026-06-29T00:12:08.439221+00:00'
page_id: '934631303'
product: rm
source: tdn-rm
title: Registro online Caixa Econômica Federal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=934631303
version: 2
---

# Conteúdo:

Conteúdo:

# 1. Registro online

Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online da carteira de cobrança registrada da Caixa Econômica Federal.

procedimentoparaconfiguracao

# 2. Procedimento para configuração

Através do cadastro do Convênio, localizado no menu 'Movimentações Bancárias', é necessário habilitar a opção "Permite registro de boleto online" e definir os parâmetros de acordo com os dados fornecidos pela Caixa Econômica Federal.

CardstrueModelo de Registro Online v1

* **Permite registro de boleto online*:***Define se o convênio permite utilizar o registro de boleto online.
* **URL do serviço de registro do boleto**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo banco.  

  Conforme detalhado no  deste documento, é possível customizar o dado a ser enviado no registro online. Abaixo, seguem alguns exemplos de cadastro de campo no layout do registro online:

**Campos da seção "HEADER"**:

* HEADER.IDPROCESSO
* HEADER.USUARIO

**Campos da seção "TITULO"**:

* TITULO.NUMERO\_DOCUMENTO
* TITULO.JUROS\_MORA.VALOR
* TITULO.POS\_VENCIMENTO.ACAO
* TITULO.POS\_VENCIMENTO.NUMERO\_DIAS
* TITULO.PAGADOR.NOME
* TITULO.PAGADOR.ENDERECO.LOGRADOURO
* TITULO.SACADOR\_AVALISTA.CNPJ
* TITULO.MULTA.VALOR
* TITULO.PAGAMENTO.TIPO
* TITULO.DESCONTOS.DESCONTO1.VALOR
* TITULO.FICHA\_COMPENSACAO.MENSAGEM1
* TITULO.RECIBO\_PAGADOR.MENSAGEM1
* TITULO.JUROS\_MORA.DATA

**Importante**: 

* De acordo com o manual da Caixa Econômica Federal, podem ocorrer 3 vezes o desconto, por isso devem ser cadastrados como DESCONTO1, DESCONTO2 e DESCONTO3. O mesmo acontece para as mensagens da ficha de compensação que devem ser cadastradas como MENSAGEM1 e MENSAGEM2, e do recibo do pagador que devem ser cadastradas como MENSAGEM1, MENSAGEM2, MENSAGEM3 e MENSAGEM4. Para os campos de valores ou percentual deve seguir o formato de acordo com o manual disponibilizado pelo banco. Ao definir um valor fixo ou formula deve ser retornado um string com o separador decimal '.' (ponto). **Exemplo**:   
    
  2.49 (para valores, com duas casas decimais )  
  1.00035 (para percentuais, com cinco casas decimais)
* De acordo com o manual da Caixa Econômica Federal é obrigatório a instrução para Protesto/Devolução, portanto devem ser criados os campos TITULO.POS\_VENCIMENTO.ACAO e TITULO.POS\_VENCIMENTO.NUMERO\_DIAS no layout do registro online (anexo do cadastro do banco) e associado um valor fixo e/ou fórmula. Os valores para o campo TITULO.POS\_VENCIMENTO.ACAO devem ser PROTESTAR ou DEVOLVER.
* O campo Data da Multa será calculado a partir da Data de Vencimento do boleto acrescido do parâmetro "Dias de Atraso" configurado na etapa Valor Líquido do lançamento financeiro.
* Ao utilizar o layout do registro online para customizar o envio dos dados ao banco, ressaltamos a importância de seguir o padrão estabelecido no manual bancário. Ao utilizar algum campo de data, como o campo "TITULO.JUROS\_MORA.DATA" para customizar a data dos juros de mora, ao passar uma data diferente do padrão do banco, como "31/07/2025", será retornada uma mensagem por parte do serviço do banco detalhando tecnicamente o motivo pelo qual o boleto não foi registrado online. Exemplo: "*The value "31/07/2025" is not a valid value for the "date" datatype*.". Para solucionar esta ocorrência, utilize o formato de data '*AAAA-MM-DD*'.

# 3. Customização de dados no registro online

customizacao

Pode ser utilizado o [Cadastro de Layout do Registro Online](https://tdn.totvs.com/display/LRM/Layout+Registro+Online), para enviar dados de forma flexível para o registro online dos boletos para o banco. Para isso deve ser feito o [Cadastro de associação de fórmulas e campos do registro online](https://tdn.totvs.com/pages/viewpage.action?pageId=421388759) no cadastro do convênio.

O cadastro do layout do registro online da Caixa Econômica Federal deve ser realizado de acordo com o manual de cobrança online do banco. Demonstramos alguns exemplos de campos no .
