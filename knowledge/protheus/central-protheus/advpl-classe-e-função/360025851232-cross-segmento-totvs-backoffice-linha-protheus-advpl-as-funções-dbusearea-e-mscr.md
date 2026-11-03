---
article_id: 360025851232
category: ADVPL - Classe e Função
content_hash: d4d8d7b8736225d0abf0eaf79ba0ab64b7ac28b33ada1f856df5b11f0407c7f5
fetched_at: '2026-06-28T22:40:14.390461+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - As funções DbUseArea()
  e MsCreate() estão gerando erro na validação do CodeAnalysis
type: support-article
updated_at: '2023-08-01T21:20:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025851232-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-As-fun%C3%A7%C3%B5es-DbUseArea-e-MsCreate-est%C3%A3o-gerando-erro-na-valida%C3%A7%C3%A3o-do-CodeAnalysis
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**As funções DbUseArea() e MsCreate() estão gerando erro na validação do CodeAnalysis. Elas foram/serão descontinuadas?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.23  
  
**Causa**Ambas as funções estão sendo apontadas como erro apenas nos casos onde o usuário está tentando realizar a manipulação de *drivers* ISAM.  
  
**Solução**  
Utilize as funções informando o driver como "TOPCONN" (*Top Connect*), desta forma a geração de arquivos acontecerá no banco e não localmente.  
  
Exemplo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025248591/mceclip0.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025248291/mceclip1.png)
