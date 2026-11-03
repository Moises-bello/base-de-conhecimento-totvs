---
article_id: 360027664131
category: Gestão de Distribuição (SIGAOMS)
content_hash: f791c55958133900dbf825f43d722be8b36fc67c161211f310877ddd1b41db32
fetched_at: '2026-06-28T22:45:49.829424+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Faturamento por carga no TOTVS OMS
type: support-article
updated_at: '2021-08-09T17:35:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027664131-Log%C3%ADstica-Linha-Protheus-OMS-Faturamento-por-carga-no-TOTVS-OMS
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:54 min****Dúvida**O **Faturamento por Carga no TOTVS OMS - Order Management System** é composto por quais **rotinas**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**O processo de **Faturamento por Carga** é composto por duas rotinas:

* **Documentos de saída - carga - MATA460B - OMSA460B**
* **Exclusão documentos de saída - carga -  MATA521B - OMSA521B**

Estas rotinas nada mais são do que facilitadores, para que o usuário possa de uma única vez  **gerar ou excluir as notas fiscais relacionadas a uma carga**, garantindo assim agilidade na operação e a consistência das informações.  
 **Importante**Caso a **TES - Tipo de Entrada e Saída**, informada no Pedido de Venda esteja configurada para gerar duplicata, é na criação dos documentos de saída que serão gerados os **títulos a receber** no financeiro.
