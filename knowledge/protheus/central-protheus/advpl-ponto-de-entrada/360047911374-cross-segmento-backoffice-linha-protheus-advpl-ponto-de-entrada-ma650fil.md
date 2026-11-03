---
article_id: 360047911374
category: ADVPL - Ponto de Entrada
content_hash: 2a2b85a847eaad07cc6fefb9389e789ea7bdd21ece64f2cb1c6b65ed5348cf76
fetched_at: '2026-06-28T22:40:11.577147+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Ponto de entrada MA650FIL
type: support-article
updated_at: '2021-12-21T17:03:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047911374-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MA650FIL
---

**Dúvida**Teriam um exemplo para o ponto de entrada **MA650FIL**?  
  
**Ambiente**Cross Segmento - BackOffice (Linha Protheus) - ADVPL– Todas versões  
  
**Solução**Esse ponto de entrada precisa retornar uma expressão que será usado no **indregua** para a tabela **SC6**. Exemplo, retornar para pegar os pedidos que tem armazém do 01  ao 10, ficaria dessa forma: **"C6\_LOCAL>='01'.And.C6\_LOCAL<='10'".**

```
#include 'totvs.ch'  
  
user function MA650FIL ()  
Local cRet :=''  
    alert ("ponto de entrada >>MA650FIL<<")  
    cRet := "C6_LOCAL >='01' .And. C6_LOCAL <= '10'"  
Return cRet
```

**Saiba mais**  
[MA650FIL - Selecionará pedidos a serem transformados em OP's](https://tdn.totvs.com/pages/releaseview.action?pageId=6087649)
