---
article_id: 360036504053
category: Inspeção de Entradas (SIGAQIE)
content_hash: e6d36b0f2082190853fa3b956a85bae20e76caa9043f33e325dbd8beb33a2730
fetched_at: '2026-06-28T22:42:26.933783+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Conceito do parâmetro MV_QLIBDEV
type: support-article
updated_at: '2021-07-27T14:35:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036504053-Manufatura-Linha-Protheus-SIGAQIE-Conceito-do-par%C3%A2metro-MV-QLIBDEV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:35 min**  
**Dúvida**Qual o conceito do parâmetro **MV\_QLIBDEV - Libera a devolução parcial de entradas que mesmo tendo parte de seu saldo liberado, ainda possui saldo no CQ (98)**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**O parâmetro **MV\_QLIBDEV**quando habilitado, ou seja, com conteúdo igual à **T - True**, permite a devolução de material sem verificar se existe saldo ainda a ser inspecionado. Porém, se o parâmetro estiver configurado como **F - False**, o usuário somente pode devolver o material quando não houver mais saldo dessa nota fiscal no armazém da qualidade.
