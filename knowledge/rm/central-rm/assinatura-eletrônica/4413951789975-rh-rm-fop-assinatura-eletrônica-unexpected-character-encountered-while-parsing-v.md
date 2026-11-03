---
article_id: 4413951789975
category: Assinatura Eletrônica
content_hash: 880832f4d8445f4c4ea1559a656fa72f55264d031b0a1e7bf798cd08d7f0f86f
fetched_at: '2026-06-28T22:46:44.086648+00:00'
product: rm
section_id: 4403549405207
source: central-rm
title: 'RH - RM - FOP - Assinatura Eletrônica: Unexpected character encountered while
  parsing value: d. Path ",line 0, position 0.'
type: support-article
updated_at: '2025-02-03T14:52:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413951789975-RH-RM-FOP-Assinatura-Eletr%C3%B4nica-Unexpected-character-encountered-while-parsing-value-d-Path-line-0-position-0
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao executar o **Processo de Integração de relatórios** do menu Assinatura Eletrônica, o processo é finalizado com o seguinte erro: Unexpected character encountered while parsing value: d. Path ",line 0, position 0. Além disso, no **Monitor de relatórios** apresenta o registro como **Falha na API**.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**O erro ocorre porque a URL da API de integração está informada com algum caractere a mais e indevido.  
  
**Solução**Acesse Ambiente | Parâmetros | Parâmetros Globais | Integração com Totvs Assinatura Eletrônica e verifique se há algum caractere indevido no campo **URL da API de integração**: **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413934227223/mceclip0.png)**Após a correção da URL, salve a parametrização e o erro descrito acima deverá parar de acontecer.
