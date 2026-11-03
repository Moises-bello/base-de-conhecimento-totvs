---
article_id: 7399404638743
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 966bd21ffdc6d7cbeb5ffc9cb994aa06fc88e88c7c1f51f241570876b5fff199
fetched_at: '2026-06-28T22:38:45.250504+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  M460FIL
type: support-article
updated_at: '2022-07-25T12:28:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7399404638743-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M460FIL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **M460FIL - Seleção de Markbrowse**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

Ponto de entrada executado antes da exibição da tela de seleção de itens para a geração de **Doc. de Saída** (**Markbrowse**).

O ponto de entrada **M460FIL** está disponível para filtrar de forma customizada os itens a serem apresentados na tela de seleção de itens (**Markbrowse**) da rotina **Doc. de Saída** (**MATA460A**).

Ao utilizar o ponto de entrada **M460FIL** é necessário utilizar o ponto de entrada **M460QRY****.  
  
Exemplo**

```
#INCLUDE "RWMAKE.CH"  
  
User Function M460FIL()  
  
   Local _volta  := "C9_CODISS = ' '"   //Filtra os itens com (C9_CODISS = ' ')  
   cQuery := _volta  
   Alert("Passou pelo PE M460FIL")  
  
Return(cQuery)
```

**Saiba Mais**

**[M460FIL - Seleção de Markbrowse](https://tdn.totvs.com/x/s4Rn)**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada M460QRY](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7399161181335-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M460QRY)**
