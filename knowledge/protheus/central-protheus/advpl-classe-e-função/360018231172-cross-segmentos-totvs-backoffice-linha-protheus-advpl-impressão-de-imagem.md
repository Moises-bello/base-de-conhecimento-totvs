---
article_id: 360018231172
category: ADVPL - Classe e Função
content_hash: 20aa66fcb5e49396ef70b022b208c679f9bc65c05760c5621f5c219b6c3824f8
fetched_at: '2026-06-28T22:40:20.421596+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Impressão de imagem
type: support-article
updated_at: '2022-01-11T18:44:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018231172-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Impress%C3%A3o-de-imagem
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Quais as classes de impressão e funções para impressão de imagens em relatório customizado? É possível utilizar a TMSprinter?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Classe de impressão 

1. [**FWMsPrinter**](http://tdn.totvs.com/display/PROT/FWMsPrinter)

Repositório de Imagem

1. **[LoadBitmap - Nome da imagem do repositório](http://tdn.totvs.com/pages/releaseview.action?pageId=6815071)**
2. **[RepExtract - Extração de arquivo do repositório imagens](http://tdn.totvs.com/pages/releaseview.action?pageId=6815070)**

```
OBS.: A Classe TMSprinter foi descontinuada sendo aasim deve se utilizar a FWMsPrinter
```
