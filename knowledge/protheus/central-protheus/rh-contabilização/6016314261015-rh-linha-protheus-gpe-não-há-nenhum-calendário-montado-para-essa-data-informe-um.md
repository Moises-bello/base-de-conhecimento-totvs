---
article_id: 6016314261015
category: RH - Contabilização
content_hash: 9e9e5231f3ab4cfb98bd3433d2b244e4eb099f2aa9af5ebc71b0a3ebd16eab49
fetched_at: '2026-06-28T22:43:46.149185+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Não há nenhum calendário montado para essa data
  informe um calendário válido ou informe uma data válida (GPEM110)
type: support-article
updated_at: '2025-07-31T05:15:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6016314261015-RH-Linha-Protheus-GPE-N%C3%A3o-h%C3%A1-nenhum-calend%C3%A1rio-montado-para-essa-data-informe-um-calend%C3%A1rio-v%C3%A1lido-ou-informe-uma-data-v%C3%A1lida-GPEM110
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**GPEM110 - Ao tentar gerar a contabilização ocorre a mensagem: "Não há nenhum calendário montado para essa data informe um calendário válido ou informe uma data válida".

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões.  
  
**Causa**Não há calendário para a competência contabilizada ou o calendário está bloqueado.   
  
**Solução**1) É necessário incluir o calendário e moedas x calendário no módulo SIGACTB na rotina **Atualizações / Cadastros /Calendários Contábeis** **(CTBA010):**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6016454094103/mceclip0.png)

**Obs:** O calendário pode ser criado referente ao ano todo ou mensal.

2) Cadastrar uma moeda contábil em **Atualizações / Cadastros /Moedas Contábeis:**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6016679490071/mceclip1.png)

3) Relacionar o calendário criado a moeda no cadastro de **Moedas x Calendário** (**CTBA200):**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6017012538647/mceclip2.png)

4) Após os cadastros , feche as rotinas e gere novamente a contabilização no **GPEM110.**

Saiba Mais:  
[Página Centralizadora da Contabilização (GPEM110)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109092-RH-Contabiliza%C3%A7%C3%A3o)
