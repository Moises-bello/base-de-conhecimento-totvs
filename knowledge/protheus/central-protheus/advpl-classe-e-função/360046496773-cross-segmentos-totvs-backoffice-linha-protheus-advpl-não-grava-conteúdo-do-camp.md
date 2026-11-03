---
article_id: 360046496773
category: ADVPL - Classe e Função
content_hash: af5196187250e838fb732359e62e9b6790fe69349d8e2bf30beeb32414f3bf5a
fetched_at: '2026-06-28T22:40:20.535904+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Não grava conteúdo
  do campo C7_TES, quando tem gatilho customizado.
type: support-article
updated_at: '2022-06-01T18:20:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046496773-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-N%C3%A3o-grava-conte%C3%BAdo-do-campo-C7-TES-quando-tem-gatilho-customizado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Não grava conteúdo do campo C7\_TES, quando tem gatilho customizado, qual o motivo?  
  
**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17.  
  
**Solução**O campo **C7\_TES** é preenchido, mas a gravação depende das validações padrão que é  executado no *valid* na lógica do **MATA120** referente ao **MATXFIS** - função **MaFisAlt** para persistência do dado.  
Diante disso apenas passar o gatilho sem executar as validações do Fiscal não garante a integridade da gravação do campo.
