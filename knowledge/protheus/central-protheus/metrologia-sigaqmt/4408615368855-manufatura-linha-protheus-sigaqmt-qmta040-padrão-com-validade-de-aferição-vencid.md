---
article_id: 4408615368855
category: Metrologia (SIGAQMT)
content_hash: 683291ad47861a2cfb19ba531961cbb226b8ef6162aeefd84b35d35c89d89248
fetched_at: '2026-06-28T22:42:24.841620+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - QMTA040 - Padrão com validade de aferição
  vencida
type: support-article
updated_at: '2021-09-15T13:55:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408615368855-Manufatura-Linha-Protheus-SIGAQMT-QMTA040-Padr%C3%A3o-com-validade-de-aferi%C3%A7%C3%A3o-vencida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:50 min****Ocorrência**No módulo **SIGAQMT - Metrologia**, ao realizar a associação do padrão com a faixa por meio da opção **Outras Ações > PaDrões** na rotina **QMTA040 - Faixas**, ocorre a mensagem **Padrão com validade de aferição vencida**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Causa**Esta mensagem ocorre quando o padrão selecionado está vencido, ou seja, na rotina **QMTA070 - Padrões** o campo **Valid. Calib.** é menor do que a data atual.  
  
**Solução**Para solucionar essa mensagem, realize os seguintes passos:  
1. Verifique se a data de validade da calibração deste padrão na rotina **QMTA070** está correta e válida. Esta data é calculada com base no conteúdo dos campos **Data Calib.** e **Freq. Calib.**;  
2. Ou informe um padrão em que a data de calibração ainda não esteja vencida.
