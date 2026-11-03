---
article_id: 360040115794
category: ADVPL - Classe e Função
content_hash: 3db7b43cd155eb279a1ad73aa47bd7e7ac130e103cb3765af011d91bca725179
fetched_at: '2026-06-28T22:40:19.293762+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - ExecInDLLOpen
  está sempre retornando -1
type: support-article
updated_at: '2024-05-09T11:28:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040115794-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-ExecInDLLOpen-est%C3%A1-sempre-retornando-1
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:03:00 min****Ocorrência**ExecInDLLOpen está sempre retornando -1 na release 12.1.25.

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.25  
  
**Causa**Qualquer DLL que esteja coma a versão 32 bits, que não é compatível com Lobo Guara.  
  
**Solução**A DLL utilizada (readexcel.dll) é uma versão 32bits, DLLs precisam ter a mesma arquitetura do binário para serem carregadas (com a ExecInDLLOpen por exemplo). Isso não é uma limitação do Protheus e sim uma questão de arquitetura/sistema operacional.

Para utilizar a readexcel.dll é necessário utilizar a versão 32bits do Smartclient disponível em nossa central de downloads.

**Saiba Mais**[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - DLL corrompida ou divergente para arquitetura da aplicação smartclient](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033957453)  
[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Funções tratamento de DLLs](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027616111)
