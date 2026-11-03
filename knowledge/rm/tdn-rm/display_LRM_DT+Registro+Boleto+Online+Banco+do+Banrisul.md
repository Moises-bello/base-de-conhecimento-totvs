---
content_hash: a8be88025e3e798ce8664cae7d1d4f89c0e6cf7ca3bd15de6d02799f3003d8a0
fetched_at: '2026-06-29T00:08:56.590345+00:00'
page_id: '351384062'
product: rm
source: tdn-rm
title: DT Registro Boleto Online Banco do Banrisul
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Registro+Boleto+Online+Banco+do+Banrisul
version: 91
---

# REGISTRO ONLINE DE BOLETO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Backoffice RM* |
| **Módulo:** | **TOTVS Gestão Financeira** |
| **Requisito/S****tory/Issue:** | **<http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-2252>** |

## Descrição

Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online de cobrança registrada do Banco do Banrisul.

## Procedimento para Configuração

No TOTVS Gestão Financeira, menu *Movimentações Bancárias | Controle Bancário | Convênio,* devem ser feitas as configurações do convênio para o registro de boleto online:

* **Permite registro de boleto online*:*** Define se o convênio permite utilizar o registro de boleto online.
* **Ambiente**: Define o ambiente que será feito o registro do boleto no banco.
* **URL do serviço de registro do boleto**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo banco.
* **URL de homologação do serviço de registro de cobrança:**Deve ser informada a URL de homologação do serviço de registro do boleto disponibilizada pelo banco.
* **Certificado digital**: Certificado digital cadastrado junto ao banco para o registro de boleto online.

Pode ser utilizado o [Cadastro de Layout do Registro Online](http://tdn.totvs.com/pages/viewpage.action?pageId=311625508), para enviar dados de forma flexível para o registro online dos boletos para o banco. Para isso deve ser feito o [Cadastro de associação de fórmulas e campos do registro online](http://tdn.totvs.com/pages/viewpage.action?pageId=307835775) no cadastro do convênio utilizado para o registro online.

O cadastro do layout do registro online do Banco do Banrisul deve ser feita de acordo com o manual de cobrança online do banco, da seguinte maneira:

Exemplos:

* titulo.nosso\_numero
* titulo.seu\_numero
* titulo.data\_vencimento
* titulo.valor\_nominal
* titulo.especie
* titulo.data\_emissao
* titulo.valor\_iof
* titulo.beneficiario.codigo
* titulo.pagador.aceite
* titulo.instrucoes.juros.codigo
* titulo.instrucoes.juros.data
* titulo.instrucoes.juros.taxa
* titulo.instrucoes.juros.valor
* titulo.instrucoes.multa.codigo
* titulo.instrucoes.multa.data
* titulo.instrucoes.multa.valor
* titulo.instrucoes.multa.taxa
* titulo.instrucoes.desconto.codigo
* titulo.instrucoes.desconto.data
* titulo.instrucoes.desconto.valor
* titulo.instrucoes.desconto.taxa
* titulo.instrucoes.protesto.codigo
* titulo.instrucoes.protesto.prazo
* titulo.instrucoes.baixa.codigo
* titulo.instrucoes.baixa.prazo
* titulo.pag\_parcial.autoriza
* titulo.pag\_parcial.codigo
* titulo.pag\_parcial.quantidade
* titulo.pag\_parcial.tipo
* titulo.pag\_parcial.valor\_min
* titulo.pag\_parcial.valor\_max
* titulo.pag\_parcial.percentual\_min
* titulo.pag\_parcial.percentual\_max
* titulo.mensagem[1 a 9].linha
* titulo.mensagem[1 a 9].texto

**Importante:**

* Para os campos de valores ou percentual deve seguir o formato de acordo com o manual disponibilizado pelo banco. Ao definir um valor fixo ou formula deve ser retornado um string com o separador decimal '.' (ponto).   
  Exemplo:   
  2.49 (com duas casas decimais )  
  2018-03-30 (data no formato AAAA-MM-DD)
* O campo Data da Multa será calculado a partir da Data de Vencimento do boleto acrescido do parâmetro *Dias de Atraso* configurado na etapa Valor Líquido do Lançamento Financeiro.
* No registro do boleto será gravado no campo Json/XML o valor completo da requisição, além do conteúdo do Json/XML, também incluídos os dados da requisição SOAP. Os mesmos são necessários no processo de validação da rotina junto ao banco.

divs
