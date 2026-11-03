---
article_id: 360028640453
category: RH - Provisão
content_hash: e07ae4b059b2a3ede62af9887d4b926ee19839098250f90c61975a3c8531917e
fetched_at: '2026-06-28T22:43:55.883076+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Conferência dos encargos de INSS e FGTS de Provisão
  de Férias com baixas de Férias e Abono Pecuniário
type: support-article
updated_at: '2025-10-24T12:22:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028640453-RH-Linha-Protheus-GPE-Confer%C3%AAncia-dos-encargos-de-INSS-e-FGTS-de-Provis%C3%A3o-de-F%C3%A9rias-com-baixas-de-F%C3%A9rias-e-Abono-Pecuni%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32998661862039)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como conferir o cálculo dos encargos de INSS e FGTS de Provisão de Férias com baixa de Férias e Abono Pecuniário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Quando há Abono Pecuniário no cálculo das Férias, o valor do abono não é considerado para a baixa dos encargos (INSS, FGTS e PIS), visto que o abono não possui incidência para estes encargos.

Segue abaixo exemplo de Cálculo:

Cálculo das Férias:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041926894)

Cálculo da Provisão de Férias:

No mês anterior, foi provisionado de INSS e FGTS referente à 30 dias, contudo o funcionário solicitou 10 dias em abono pecuniário. Nesse caso o sistema realiza a seguinte conta:

Soma todos os proventos relacionados às férias:

Verba 129 Férias - 666,67  
Verba 131 Abono - 333,33  
Verba 134 1/3 Férias - 222,22  
Verba 136 1/3 Abono - 111,11

Total = 1333,33 (Chamaremos de Base Férias).

Logo após, o sistema somará os proventos de Abono Pecuniário que estão com N para INSS e N para FGTS:

Verba 131 - 333,33  
Verba 136 - 111,11

Total = 444,44 (Chamaremos de Base Abono).

Cálculo:

Base Férias - Base Abono = Base Encargos  
1333,33 - 444,44 = 888,89

Sobre a Base Encargos são aplicados os respectivos percentuais para os Impostos, conforme abaixo:

INSS = 888,89 \* 26,8% = 238,22  
FGTS = 888,89 \* 8% = 71,11

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041930014)

Nesse cenário, o valor da linha "No Mês" mês ficará **negativo,** visto que a empresa provisionou mais do que a baixa, pois parte das férias foi convertida em abono pecuniário.

Note também que o valor da linha "Atual" ficou zerado, pois o período aquisitivo foi quitado.

**Saiba Mais**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)

<http://tdn.totvs.com/pages/releaseview.action?pageId=447088971>
