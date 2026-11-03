---
article_id: 29221749711767
category: ADVPL - Classe e Função
content_hash: 902b119d2849ce3e719d56cde0110066c1ced55df001fa2736f477ffe95b3d01
fetched_at: '2026-06-28T22:40:20.729923+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Função Escape
type: support-article
updated_at: '2025-01-22T10:43:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29221749711767-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-Escape
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29221690183319) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como formatar parâmetros enviados inseridos em uma URL em uma requisição?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**Quando passamos parâmetros via url , devemos tomar o cuidado de não utilizar caracteres reservados e especiais nos nomes e conteúdos de parâmetros. Para realizar estas conversões, utilizamos a função **Escape**()

A função Escape() deve ser utilizada para realizar conversões de caracteres especiais e reservados quando da necessidade de passagem de parâmetros via URL .  
  
**Por exemplo:**

```
cUrl := 'http://localhost/webinfo.apw'  
cPAram1 := 'Teste de Parametro 01-02'  
cPAram2 := '#reserva#'  
cPAram3 := '1+2+3'  
cUrl += '?Par01=' + escape(cPAram1) + '&PAr02=' + escape(cPAram2) + '&Par03=' + escape(cPAram3)  
  
  
// O conteudo de cUrl deverá ser:  
// "http://localhost/webinfo.apw?Par01=Teste%20de%20Parametro%2001-02&PAr02=%23reserva%23&Par03=1%2B2%2B3"  
// próprio para a montagem de um link.
```

**Saiba mais**[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Onde posso tirar dúvidas sobre ADVPL?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4984257614615-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Onde-posso-tirar-d%C3%BAvidas-sobre-ADVPL)
