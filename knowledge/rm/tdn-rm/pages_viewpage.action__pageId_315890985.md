---
content_hash: 7544ead7842263362b0aee0c8479c01ab0591449e9ea5afd577f4de739df2a25
fetched_at: '2026-06-29T00:08:45.785183+00:00'
page_id: '315890985'
product: rm
source: tdn-rm
title: DT Registro Boleto Online Caixa Econômica Federal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=315890985
version: 99
---

# REGISTRO ONLINE DE BOLETO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção & Projetos* |
| **Módulo:** | **TOTVS Gestão Financeira** |
| **Requisito/S****tory/Issue:** | *<http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-792>* |

## Descrição

Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online de cobrança registrada da Caixa Econômica Federal.

## Procedimento para Configuração

No TOTVS Gestão Financeira, menu *Movimentações Bancárias | Controle Bancário | Convênio,* devem ser feitas as configurações do convênio para o registro de boleto online:

* **Permite registro de boleto online*:*** Define se o convênio permite utilizar o registro de boleto online.
* **URL do serviço de registro do boleto**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo banco.

Pode ser utilizado o , para enviar dados de forma flexível para o registro online dos boletos para o banco. Para isso deve ser feito o  no cadastro do convênio utilizado para o registro online.

O cadastro do layout do registro online da Caixa deve ser feita de acordo com o manual de cobrança online do banco, da seguinte maneira:

* Exemplos para os campos do HEADER:  
  HEADER.IDPROCESSO  
  HEADER.USUARIO
* Exemplos para os campos do TITULO:  
  TITULO.NUMERO\_DOCUMENTO  
  TITULO.JUROS\_MORA.VALOR  
  TITULO.POS\_VENCIMENTO.ACAO  
  TITULO.POS\_VENCIMENTO.NUMERO\_DIAS  
  TITULO.PAGADOR.NOME  
  TITULO.PAGADOR.ENDERECO.LOGRADOURO  
  TITULO.SACADOR\_AVALISTA.CNPJ  
  TITULO.MULTA.VALOR  
  TITULO.PAGAMENTO.TIPO  
  TITULO.DESCONTOS.DESCONTO1.VALOR  
  TITULO.FICHA\_COMPENSACAO.MENSAGEM1  
  TITULO.RECIBO\_PAGADOR.MENSAGEM1  
    
    
    
    
  **Importante:**
  + De acordo com o manual da Caixa podem ocorrer 3 vezes o desconto, por isso devem ser cadastrados como DESCONTO1, DESCONTO2 e DESCONTO3. O mesmo acontece para as mensagens da ficha de compensação que devem ser cadastradas como MENSAGEM1 e MENSAGEM2, e do recibo do pagador que devem ser cadastradas como MENSAGEM1, MENSAGEM2, MENSAGEM3 e MENSAGEM4.  
      
    Para os campos de valores ou percentual deve seguir o formato de acordo com o manual disponibilizado pela Caixa. Ao definir um valor fixo ou formula deve ser retornado um string com o separador decimal '.' (ponto).   
    Exemplo:   
    2.49 (para valores, com duas casas decimais )  
    1.00035 (para percentuais, com cinco casas decimais)
  + De acordo com o manual da Caixa é obrigatório a instrução para Protesto/Devolução, portanto devem ser criados os campos TITULO.POS\_VENCIMENTO.ACAO e TITULO.POS\_VENCIMENTO.NUMERO\_DIAS no Layout Registro Online no cadastro do Banco e associado um valor fixo e/ou fórmula. Os valores para o campo TITULO.POS\_VENCIMENTO.ACAO devem ser PROTESTAR ou DEVOLVER.
  + O campo Data da Multa será calculado a partir da Data de Vencimento do boleto acrescido do parâmetro *Dias de Atraso* configurado na etapa Valor Líquido do Lançamento Financeiro.

divs
