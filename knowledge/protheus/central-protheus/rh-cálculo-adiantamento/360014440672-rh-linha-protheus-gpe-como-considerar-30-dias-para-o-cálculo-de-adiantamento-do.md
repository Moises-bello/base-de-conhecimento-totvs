---
article_id: 360014440672
category: RH - Cálculo Adiantamento
content_hash: badb575e8656068ca0ca363c3e15fedf7d02cf2290c08ef4e789dd65f4b48c29
fetched_at: '2026-06-28T22:43:14.248131+00:00'
product: protheus
section_id: 360011983213
source: central-protheus
title: RH - Linha Protheus - GPE - Como considerar 30 dias para o cálculo de adiantamento
  do funcionário horista
type: support-article
updated_at: '2025-04-14T20:15:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014440672-RH-Linha-Protheus-GPE-Como-considerar-30-dias-para-o-c%C3%A1lculo-de-adiantamento-do-funcion%C3%A1rio-horista
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24787376263063) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como configurar o sistema para que considere sempre 30 dias, no cálculo do adiantamento para funcionários horistas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Foi criado o mnemônico **P\_ADIHOR** para que, caso o **funcionário seja horista** o cadastro de períodos esteja configurado para cálculo sobre os dias do mês, e o mnemônico esteja configurado com **.T.**, considerar 30 dias para o cálculo do **adiantamento**.  
Caso o **mnemônico** esteja com conteúdo **.F.** o sistema irá considerar os dias do mês para cálculo do adiantamento.

Será considerado 30 dias para cálculo do adiantamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31411011539095)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31411023824535)

Será considerado os dias do mês para cálculo do adiantamento..

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31411011555735)  
  
**Saiba Mais**Acesse o *link* a seguir para maiores informações sobre a criação do mnemônico: [DRHPAG-13343 DT Adiantamento para horistas, considerando salario de 30 dias, mesmo quando o mês possuir 31 dias.](http://tdn.totvs.com/pages/viewpage.action?pageId=337354384)

<https://tdn.totvs.com/pages/releaseview.action?pageId=286732427>

[RH - Cálculo Adiantamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983213-RH-C%C3%A1lculo-Adiantamento)
