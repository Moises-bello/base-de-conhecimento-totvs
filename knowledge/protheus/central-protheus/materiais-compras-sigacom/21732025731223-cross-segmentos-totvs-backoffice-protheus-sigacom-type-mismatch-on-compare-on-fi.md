---
article_id: 21732025731223
category: Materiais - Compras (SIGACOM)
content_hash: affe2d5fb44ff2053d9efa22a6ab508cecd0c7b11fb9a9d2dc62a070a1df48a1
fetched_at: '2026-06-28T22:41:25.398984+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - type mismatch on compare  on
  FILLGETDADOS(APLIB171.PRW) 16/01/2024 16:37:17 line : 137'
type: support-article
updated_at: '2024-03-01T14:51:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21732025731223-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-type-mismatch-on-compare-on-FILLGETDADOS-APLIB171-PRW-16-01-2024-16-37-17-line-137
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21732055494423) Tempo aproximado para leitura: **00:01:00min****Ocorrência**Ao utilizar um ponto de entrada é apresentada a ocorrência "type mismatch on compare on FILLGETDADOS(APLIB171.PRW) 16/01/2024 16:37:17 line : 137"  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Totvs Compras - Todas as versões  
  
**Causa**Não declaração de variáveis cNivel, cAliasLoop, aYesUsado, aNoFields. Utilizadas internamente em fontes de lib.  
  
**Solução**Declarar a variável como local na função customizada, seguindo exemplo abaixo:

```
User Function WFW120P()  
Local cNivel = ""
```

**Saiba Mais:**

**[Centralizadora de Compras](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)**
