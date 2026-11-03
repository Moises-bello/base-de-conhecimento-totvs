---
content_hash: 23c7ec05fe907b2962154365b523cc282ed503b92d897742fed8978e09c37b5d
fetched_at: '2026-06-29T00:10:21.705300+00:00'
page_id: '492708295'
product: rm
source: tdn-rm
title: FISCAL01-9195 DT Geração de Guias - Alterar a geração de guias para FUNRural
  e Senar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=492708295
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Fiscal |
| Função: | Geração de Guias |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-9195 |

## **02. SITUAÇÃO/REQUISITO**

Cliente entrou em contato informando que no sistema, a guia no tributo Funrual, Gilrat e Senar, estão sendo geradas separadamente. Uma guia, está sendo levado o valor do tributo Funrural e Gilrat, e outra guia sendo gerada somente com o valor do Senar.  
O mesmo informa que no próprio site do Senar, existe o embasamento legal, demonstrando que para os tributos (Funrural, Gilrat e Senar), deve ser gerado uma unica guia, sendo que na guia, existe o campo separado para levar os valores dos tributos.

## **03. SOLUÇÃO**

Foram realizadas as seguintes alterações:

1. Alterar a geração de guia do Funrural para passar a gerar o campo "**Código de Pagamento**" com o "Código da Retenção" informado no Cadastro do INSS/PJ.
2. Alterar a geração de guia do Senar para passar a gerar o campo "**Código de Pagamento**" com o "Código da Receita - SENAR" informado no Cadastro do INSS/PJ.
3. Gerar a guia SENAR separado **somente** quando houver código de receita informado para ele no Cadastro do INSS/PJ. Caso contrário o valor do SENAR deve ser somado à guia do Funrural.
4. Quando o "Código da Retenção"  não for informado, a guia será gerada com ressalvas. O Log informará em qual  Lançamento o Código do Pagamento foi gerado em branco.
