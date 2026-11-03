---
article_id: 18209814144535
category: TAF - REINF
content_hash: 965b82571e2180e08286bf57dd27e215fdb0d5e0c29fd14eb2dcc2735744efe9
fetched_at: '2026-06-28T22:41:34.734562+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - O campo Valor Bruto (XXX_VLRTOT/XXX_VLRBRU)
  não foi preenchido
type: support-article
updated_at: '2023-10-12T01:34:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18209814144535-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-O-campo-Valor-Bruto-XXX-VLRTOT-XXX-VLRBRU-n%C3%A3o-foi-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18209790614167) Tempo aproximado para leitura: 00:05:00**min****Ocorrência**

**Ao apurar o R-4010 ou R-4020 ocorre um alerta de valor bruto não preenchido:**

Item.......................: [0]  
Id do formulário de origem.: [MODEL\_V4SA]  
Id do campo de origem......: [VLDDATA\_OBRIGAT]  
Id do formulário de erro...: [MODEL\_V4SA]  
Id do campo de erro........: [V4S\_VLRTOT]  
Id do erro.................: [OBRIGAT]  
Mensagem do erro...........: [O campo Valor Bruto (XXX\_VLRTOT/XXX\_VLRBRU) não foi preenchido]  
Mensagem da solução........: []  
Valor atribuido............: [ ]  
Valor anterior.............: [ ]

----------------------------------------

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Automação Fiscal - Todas as versões  
  
**Causa**  
Esse incidente ocorre pois o campo Valor da linha da Natureza de Rendimento está zerado.

**Solução**  
Deve ser preenchido nas rotinas TAFA448 (Faturas/Recibos) e TAFA535 (Pagamentos)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18209721507095)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18209746326807)
