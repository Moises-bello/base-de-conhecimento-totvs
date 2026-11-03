---
article_id: 360051158134
category: RH - Férias
content_hash: 35ce5ddd2482d000a369465a6c663f43d551d233d2817ee5c30c105af56bdfa6
fetched_at: '2026-06-28T22:43:58.128318+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Como excluir o calculo das férias conforme origem
  de cálculo
type: support-article
updated_at: '2025-09-02T17:00:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051158134-RH-Linha-Protheus-GPE-Como-excluir-o-calculo-das-f%C3%A9rias-conforme-origem-de-c%C3%A1lculo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26747543645847)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como excluir o calculo das férias conforme origem de cálculo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

O cancelamento deve ser realizado na rotina em que se originou o calculo.

Se férias **Normais** acessar - **Miscelânea > Calculo > Férias**, selecionar o funcionário - **Outras Ações** e excluir.  
Se férias **Coletivas** acessar **- Miscelânea > Calculo > Férias coletivas/programadas** - **outras ações** - excluir   
Se férias **Programada** acessar - **Miscelânea > Calculo > Férias coletivas/programadas - outras ações - excluir**

O campo **Tipo de Cálculo (RH\_TIPCAL) na tabela SRH,** passa a ser gravado com o seguinte conteúdo:  
• **N** - férias normais  
• **P** - férias programadas -> quando calculadas pela opção **Programada**  
• **C** - férias coletivas -> quando calculada pela opção **Coletiva  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34637787502871)**

**Saiba Mais**

[RH - Férias](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597291-RH-F%C3%A9rias)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[RH - Linha Protheus - GPE - Como verificar qual tipo de Férias foi calculada para o Funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22658839180311-RH-Linha-Protheus-GPE-Como-verificar-qual-tipo-de-F%C3%A9rias-foi-calculada-para-o-Funcion%C3%A1rio)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
