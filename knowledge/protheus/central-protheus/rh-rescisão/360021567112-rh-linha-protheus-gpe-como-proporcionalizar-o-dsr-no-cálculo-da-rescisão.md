---
article_id: 360021567112
category: RH - Rescisão
content_hash: 6e901043b2657012f33974b66731d79a32137b4b1550efb42910d6279479b3cb
fetched_at: '2026-06-28T22:43:52.113525+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como proporcionalizar o DSR no cálculo da rescisão
type: support-article
updated_at: '2022-07-19T17:51:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021567112-RH-Linha-Protheus-GPE-Como-proporcionalizar-o-DSR-no-c%C3%A1lculo-da-rescis%C3%A3o
---

**Dúvida**No cálculo da rescisão como fazer com que o sistema considere os dias para cálculo de DSR somente até o dia do desligamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**O sistema considera dois mnemônicos para cálculo de DSR na rescisão, o **P\_CPROPDSR**  e o **P\_LPROPDSR**, temos as opções abaixo de configuração:  
  
**P\_CPROPDSR** - Proporcionalizar DSR HE:0=Não /1-Adm /2-Dem /3-Afast /4-Férias  
**P\_LPROPDSR** -  Proporcionalizar DSR de HE na Admissão, demissão e afastamento.  

Configure, conforme abaixo para que o sistema proporcionalize o DSR no cálculo da rescisão:  
**P\_CPROPDSR** - "2"  
**P\_LPROPDSR** - .T.   
  
**Observação:** O sistema só acata a proporcionalização do DSR na rescisão se o cadastro de calendário do período for analítico (parâmetro MV\_TPCALEN=1), caso contrário o sistema não tem de onde buscar um DSR proporcional uma vez que não há o calendário analítico.
