---
article_id: 7250330018711
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: a8b782177aa6de954ee2ec07e49ada58a3398e18193c442c2626ab95932197ee
fetched_at: '2026-06-28T22:38:42.414054+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  MA455COR
type: support-article
updated_at: '2022-07-25T12:27:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7250330018711-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-MA455COR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **MA455COR - Alterar cores do browse do cadastro.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**Este ponto de entrada pertence à rotina de liberação de credito e estoque e liberação de estoque, MATA455() e MATA450. Usado, em conjunto com os pontos M450LEG e MA450COR, para alterar cores do “browse” do cadastro, que representam o “status” do pedido.  
  
**Exemplo**

```
#INCLUDE "RWMAKE.CH"  
  
User Function MA455COR()  
  
    Local aCores := {}  
  
    //Formato do item do array de cores {"condição", 'cor'}.   
    aCores := { {"C9_BLCRED == '  ' .And. C9_BLEST=='  '",'ENABLE'   },;  //Item Liberado (verde)  
                {"C9_BLCRED == '10' .And. C9_BLEST=='10'",'DISABLE'  },;  //Item Faturado (vermelho)  
                {"C9_BLCRED == '01' .And. C9_BLEST=='  '",'BR_PINK'  },;  //Item Bloqueado - Credito (rosa)  
                {"C9_BLCRED == '  ' .And. C9_BLEST=='02'",'BR_MARROM'} }  //Item Bloqueado - Estoque (marrom)  
  
Return(aCores)
```

**Saiba Mais**

**[MA455COR - Alterar cores do browse do cadastro](https://tdn.totvs.com/x/I4Vn)**
