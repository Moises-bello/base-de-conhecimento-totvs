---
article_id: 360045799793
category: RH - Folha de Pagamento
content_hash: 748125280be6df1c31f9abb294fb002da04c47652940d3844a1c6376e9ea0949
fetched_at: '2026-06-28T22:44:14.692011+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como proporcionalizar o DSR na folha de pagamento
type: support-article
updated_at: '2025-12-03T12:23:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045799793-RH-Linha-Protheus-GPE-Como-proporcionalizar-o-DSR-na-folha-de-pagamento
---

#### time.png Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**Como proporcionalizar o cálculo de DSR na folha nos meses de admissão, afastamento ou férias, fazendo com que o sistema considere apenas os dias trabalhados para o cálculo do DSR?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para proporcionalizar o DSR em meses de admissão, afastamento ou férias temos os mnemônicos abaixo:

**P\_CPROPDSR** - Proporcionalizar DSR HE:0=Não /1-Adm /2-Dem /3-Afast /4-Férias  
**P\_LPROPDSR** -  Proporcionalizar DSR de HE na Admissão, demissão e afastamento.     
  
Caso queira proporcionalizar o DSR na folha nas situações de admissão, ferias ou afastamento, o mnemônico **P\_LPROPDSR** deverá ser parametrizado com **.T.**, e o mnemônico **P\_CPROPDSR** deverá ser parametrizado de acordo com a proporcionalização a ser realizada, por exemplo, caso queira proporcionalizar o DSR nas férias, deverá ser preenchido com **"4"** ou caso queira proporcionalizar o DSR nas férias e na demissão, deverá ser preenchido com **"24"**.  
  
**Observação.:** O sistema só acata a proporcionalização do DSR na folha se o cadastro de calendário do período for analítico (parâmetro MV\_TPCALEN=1), caso contrário o sistema não tem de onde buscar um DSR proporcional uma vez que não há o calendário analítico.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22320009029271)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26079741501079)

**Saiba Mais**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
