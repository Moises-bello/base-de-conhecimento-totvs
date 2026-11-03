---
article_id: 1500011923502
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: a1e11a66f585d2e62ffcc3ff55cf683f6eba6758d1482624b6d703c1b774f582
fetched_at: '2026-06-28T22:42:44.434096+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem B1_BASE FWNOWIDTH
type: support-article
updated_at: '2021-05-24T12:14:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011923502-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-B1-BASE-FWNOWIDTH
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:40 min**  
**Ocorrência**Ao incluir um produto utilizando o **Configurador de produtos**, o usuário recebe a mensagem **B1\_BASE - FWNOWIDTH - Valor atribuído difere do tamanho do campo Cod Familia**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12.  
  
**Causa**Essa mensagem surge quando o tamanho do campo **BP\_BASE - Conteúdo** é maior do que o **B1\_BASE -Código da Família.**  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Através do **SIGACFG - Configurador** ajuste o tamanho do campo **B1\_BASE** para o mesmo tamanho do campo **BP\_BASE**.
