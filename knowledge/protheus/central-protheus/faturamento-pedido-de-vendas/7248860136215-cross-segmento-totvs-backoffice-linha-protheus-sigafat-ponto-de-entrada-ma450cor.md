---
article_id: 7248860136215
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 504e8f048c51cec784cb3a95c48317c18e28e0d92b4a432016e66ea228b97cb9
fetched_at: '2026-06-28T22:38:42.408277+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  MA450COR
type: support-article
updated_at: '2022-07-25T12:28:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7248860136215-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-MA450COR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00****min****Dúvida**Exemplo de utilização do Ponto de Entrada **MA450COR - Alterar textos da legenda de status do pedido.**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**Ponto de entrada que pertence à rotina de **Liberação de Crédito (MATA450)**, usado em conjunto com o ponto **MA455LEG**, para alterar os textos da legenda, que representam o status do pedido.  
  
**Obs.:** As rotinas abaixo utilizam a **mesma legenda**, caso utilize o Ponto de Entrada **MA450COR** as alterações irão refletir em todas elas.

* Análise de Crédito de Pedido de Venda (**MATA450**)
* Liberação de Estoque (**MATA455**)
* Liberação de Crédito e Estoque (**MATA456**)

**Exemplo**

```
User Function MA450COR()  
  
    Local aLegenda := {}  
  
    //Formato do item da legenda {'cor', 'texto legenda'}  
    aLegenda := {  {'ENABLE' ,'Item Liberado'           },; //Verde  
                   {'DISABLE','Item Faturado'           },; //Vermelho  
                   {'BR_PINK','Item Bloqueado - Credito'} } //Rosa  
  
Return(aLegenda)
```

**Saiba Mais**

**[MA450COR - Alterar textos da legenda de status do pedido](https://tdn.totvs.com/x/IIVn)**
