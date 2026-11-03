---
article_id: 360050033254
category: Faturamento - Integrações
content_hash: 71ab7f71f4fcd1101c7f9598a8a77066f865cffb35fded356d01d60dad3f8cc4
fetched_at: '2026-06-28T22:38:26.411334+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Gravação do
  campo GW8_PESOR na Integração GFE
type: support-article
updated_at: '2022-12-22T16:35:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050033254-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Grava%C3%A7%C3%A3o-do-campo-GW8-PESOR-na-Integra%C3%A7%C3%A3o-GFE
---

**Dúvida**

Gravação do campo **GW8\_PESOR** na Integração GFE.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Segue como é realizada a gravação do campo:

***GW8\_PESOR  ==>  B1\_PESBRU (Peso Bruto do Produto) x D2\_QUANT (Quantidade do item da Nota).***  
  
O sistema verifica também o parâmetro ***MV\_GFERPB*** antes de gerar o ***GW8\_PESOR***.  
  
***MV\_GFERPB*** => permite definir o tipo de cálculo para o peso bruto dos itens da nota de saída - Rateio do Peso Bruto da NF.  
  
O parâmetro ***MV\_GFERPB*** pode ser preenchido com:  
  
**\* 0  (default)** : Não Rateia - Cálculo padrão do Sistema, ou seja, Peso Bruto do Produto (***B1\_PESBRU***) x Quantidade do item da Nota (***D2\_QUANT***).  
  
**\* 1** : Rateia por item - Rateia o peso bruto do cabeçalho da Nota (***F2\_PBRUTO***) entre os itens da nota.  
Quando no pedido é lançado o peso líquido (***C5\_PBRUTO***)  e o mesmo só possui um item (produto), o sistema envia este peso para o ***GW8\_PESOR***.  
  
Cálculo utilizado no rateio :  
  
Produto 000001  (Peso Produto x Qtde do Produto)  = 50 \* 10 = 500  
Produto 000002  (Peso Produto x Qtde do Produto)  = 80 \* 10 = 800  
Total do Peso dos Itens = 1300  
  
Total do Peso no Cabeçalho da Nota (***F2\_PBRUTO***) = 110  
  
Rateio por Item x Nota  
Produto 000001 = ((500 / 1300) \* 110)  =  42,30770  
Produto 000002 = ((800 / 1300) \* 110)  =  67,69230  
  
--------------------------------------------------------------------------------------  
  
Caso deseje utilizar os campos com outras informações, pode utilizar o ponto de entrada ***OMSM0113***.  
***OMSM0113*** - Manipula a tabela ***GW8*** na geração do documento de saída.  
[**https://tdn.totvs.com/x/OhpFCg**](https://tdn.totvs.com/x/OhpFCg)  
Veja mais informações sobre a integração no link abaixo:

[**https://tdn.totvs.com/x/RbMbF**](https://tdn.totvs.com/x/RbMbF)
