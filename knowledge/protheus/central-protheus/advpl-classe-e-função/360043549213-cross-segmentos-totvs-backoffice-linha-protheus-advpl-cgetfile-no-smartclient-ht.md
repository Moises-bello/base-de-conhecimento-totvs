---
article_id: 360043549213
category: ADVPL - Classe e Função
content_hash: 8f6833d3540d176a011e78025d68058006e9e3fd21f548b98d44bbf21db389f4
fetched_at: '2026-06-28T22:40:18.276682+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - cGetFile no SmartClient
  HTML
type: support-article
updated_at: '2022-01-03T22:10:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043549213-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-cGetFile-no-SmartClient-HTML
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**É possível efetuar abertura de pastas locais utilizando a função cGetFile através do SmartClient HTML?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**A função **cGetFile** no SmartClient HTML somente terá acesso ao root path (diretório abaixo do protheus\_data), não é possível ter acesso a diretórios locais.  
Como o acesso é via Web não tem como  enxergar arquivos locais.
