---
article_id: 4416749976599
category: Escrita Fiscal - CIAP
content_hash: 69715bacd1b3eeca8447356e3b651564127fae847987e1ef01f198fd98f7b906
fetched_at: '2026-06-28T22:39:33.976922+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Por qual razão ao
  gerar a rotina ATUALIZA SF9 (M906SF9) as parcelas não são deduzidas com base na
  tabela M906SF9SFA (Estorno CIAP)? '
type: support-article
updated_at: '2021-12-22T16:33:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416749976599-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Por-qual-raz%C3%A3o-ao-gerar-a-rotina-ATUALIZA-SF9-M906SF9-as-parcelas-n%C3%A3o-s%C3%A3o-deduzidas-com-base-na-tabela-M906SF9SFA-Estorno-CIAP
---

**Dúvida**Por qual razão ao gerar a rotina ATUALIZA SF9 (M906SF9) as parcelas não são deduzidas com base na tabela M906SF9SFA (Estorno CIAP)?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Se gerada a rotina **ATUALIZA SF9 (M906SF9),** será verificada a quantidade de meses da inclusão do item até a data base e deduzidas deste campo.

Por exemplo:

**ATIVO 001 - CADASTRADO EM 01/12/2012**

**QTD PARCELAS = 48**

**SLD PARCELAS = 48**

Ao rodar rotina ATUALIZA SF9 é aplicada a alteração:

**DATA BASE = 28/02/2013**

**QTD PARCELAS = 48**

**SLD PARCELAS = 45**

Mesmo que não haja apropriação na SFA, será aplicada esta regra, uma vez que a legislação determina que o crédito deve ser calculado mês a mês e caso a empresa não tenha saídas tributadas esse valor é perdido, não sendo possível desconsiderar um mês, para utilizar o crédito posteriormente.
