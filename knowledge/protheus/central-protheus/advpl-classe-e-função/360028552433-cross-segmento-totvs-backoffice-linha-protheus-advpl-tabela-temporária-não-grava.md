---
article_id: 360028552433
category: ADVPL - Classe e Função
content_hash: e8658058225e2d579b3a5ccd8fa650b723a85a4d0a8b2ef02cbf76d52a43184d
fetched_at: '2026-06-28T22:40:18.064390+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Tabela temporária
  não grava profile
type: support-article
updated_at: '2022-03-23T11:05:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028552433-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Tabela-tempor%C3%A1ria-n%C3%A3o-grava-profile
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Quando criado um filtro ao utilizar um navegador (*browser*) utilizando tabelas temporárias, o mesmo não é armazenado no arquivo de preferências (*profile*) do usuário.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Causa**As informações não são persistidas nas preferências do usuário por motivo da não geração de vínculo entre tabela (mesmo com nomeação fixa) e usuário.  
  
**Solução**Adicionar uma operação personalizada (opção no vetor aRotina) para realização dos filtros desejados e armazenamento em um arquivo texto.
