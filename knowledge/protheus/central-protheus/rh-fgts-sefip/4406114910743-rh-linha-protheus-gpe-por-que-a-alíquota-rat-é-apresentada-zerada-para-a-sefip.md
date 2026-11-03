---
article_id: 4406114910743
category: RH - FGTS / SEFIP
content_hash: 81d7d01f304fbe0f9c5a4d198f47fb9d2df51a4e5c32fe2133bbae9ea4755033
fetched_at: '2026-06-28T22:43:41.455187+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Por que a alíquota RAT é apresentada zerada para
  a Sefip
type: support-article
updated_at: '2025-08-07T22:01:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406114910743-RH-Linha-Protheus-GPE-Por-que-a-al%C3%ADquota-RAT-%C3%A9-apresentada-zerada-para-a-Sefip
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34028230584599) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Por que a alíquota RAT é carregada zerada para a Sefip?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**A alíquota RAT será enviada zerada para a Sefip se na **Tabela S037** da rotina Manutenção de Tabelas a coluna **%RAT** estiver com percentual maior de 3,9999 ou menor que 1.0000, pois conforme consta na Sefip, para o RAT só existem 3 percentuais, que são 1%, 2% ou 3%:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406114757143)

**Saiba mais:**  
[RH - Linha Protheus - GPE- Onde alterar o % do FAP e como informar o RAT (acidente de trabalho) no sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028194571)
