---
article_id: 7080826711319
category: Financeiro - Contas a Pagar
content_hash: 1ecca3d33f2b17376e9065c5a37b2861ff088f9da72af9ae557309a70f7c7b42
fetched_at: '2026-06-28T22:38:08.561911+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - HELP NOCPOSX3
type: support-article
updated_at: '2023-01-25T23:25:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7080826711319-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-HELP-NOCPOSX3
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:05:00 min****Ocorrência**Ao incluir um contas a pagar aparece o seguinte HELP:NOCPOSX

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7080733569815/mceclip0.png)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**A mensagem de HELP está relacionado ocorre, pois os campos estão criados dentro das tabelas no banco de dados e não no dicionário de dados(SX3) 

**Solução**Como trata-se de campo que não são padrão do PROTHEUS, o Administrador do PROTHEUS, deve validar no sistema, esses campos que foram criados e possuem nessas tabelas e criá-los na SX3.
