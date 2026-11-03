---
article_id: 360044659994
category: ADVPL - Classe e Função
content_hash: d64602bfcf50cf39a271ca71a5eb047181b46d1961d9692004eb709482d4a812
fetched_at: '2026-06-28T22:40:18.116286+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - TMSGraphic via Job
type: support-article
updated_at: '2022-06-14T17:25:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044659994-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-TMSGraphic-via-Job
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura:**00:01:00 min  
  
Dúvida**Ao executar a classe TMSGraphic via job ocorre o erro:

```
"Invalid new interface control without window/dialog in the file"
```

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Conforme documentação da Classe **[TCrontrol](https://tdn.totvs.com/display/tec/TControl)** todos os componentes visuais necessitam de um janela principal criada e caso não exista a seguinte exceção será disparada no SmartClient **"*Invalid new interface control without window/dialog*"**.
