---
article_id: 7399161181335
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: eafaeec48344ea9841559a77a9884b08e9f28ff69ce2b628026ff2e755c4f43b
fetched_at: '2026-06-28T22:38:45.276151+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  M460QRY
type: support-article
updated_at: '2022-07-25T12:28:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7399161181335-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M460QRY
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **M460QRY - Adição de elementos**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**Ponto de entrada executado antes da exibição da tela de seleção de itens para a geração de **Doc. de Saída** (**Markbrowse**), ao realizar o cálculo dos **rateios de Despesas Acessórias** (**Frete**/**Seguro**/**Despesa**) e de **Desconto** entre os itens do pedido a ser faturado.

O ponto de entrada é **executado duas vezes** para cada um desses cálculos (rateio de despesas acessórias e rateio de desconto) quando for necessário.

Ao utilizar o ponto de entrada **M460QRY** é necessário utilizar o ponto de entrada **M460FIL****.****Exemplo**

```
#INCLUDE "RWMAKE.CH"  
  
User Function M460QRY()  
  
    Local _volta  := " and C9_CODISS = ' '"  
    Local cQuery  := paramixb[1]  
    Local cCodQry := paramixb[2]  
  
    If cCodQry == 1  
       cQuery += _volta  
    EndIf  
  
    Alert("Passou pelo PE M460QRY")  
  
Return(cQuery)
```

**Saiba Mais**

**[M460QRY - Adição de elementos](https://tdn.totvs.com/x/xYRn)**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada M460FIL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7399404638743-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M460FIL)**
