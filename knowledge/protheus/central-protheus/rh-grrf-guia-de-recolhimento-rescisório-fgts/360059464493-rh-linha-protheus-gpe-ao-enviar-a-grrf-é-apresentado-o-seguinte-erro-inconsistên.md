---
article_id: 360059464493
category: RH - GRRF (Guia de Recolhimento Rescisório - FGTS)
content_hash: 9227e12f6640ade80421b6574dbf511ee307d3007de30cd392e6eac3c913505d
fetched_at: '2026-06-28T22:43:32.300638+00:00'
product: protheus
section_id: 360010781714
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao enviar a GRRF é apresentado o seguinte erro
  : Inconsistência 391 valor do Aviso Prévio deve ser diferente de zeros para indicativo
  de Aviso Prévio igual a 2 - Indenizado'
type: support-article
updated_at: '2025-10-20T12:36:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059464493-RH-Linha-Protheus-GPE-Ao-enviar-a-GRRF-%C3%A9-apresentado-o-seguinte-erro-Inconsist%C3%AAncia-391-valor-do-Aviso-Pr%C3%A9vio-deve-ser-diferente-de-zeros-para-indicativo-de-Aviso-Pr%C3%A9vio-igual-a-2-Indenizado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33069725111319) Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência** Ao enviar a GRRF é apresentado o seguinte erro : Inconsistência 391 valor do Aviso Prévio deve ser diferente de zeros para indicativo de Aviso Prévio igual a 2 - Indenizado

![](https://totvssuporte.zendesk.com/attachments/token/63Nrl7G3AMHosNxpdN47Ox3Tm/?name=inline1876399846.png)  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão Pessoal -  A partir da Versão 12.1.17.  
  
**Causa**Esse erro ocorre  porque a rescisão original do funcionário teve aviso prévio indenizado, desta forma, na rescisão complementar deve também existir valor para o evento de aviso prévio indenizado

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Verifique no arquivo o > Registro Tipo 40 > posição 239 a 253 se consta o valor do aviso.

![](https://totvssuporte.zendesk.com/attachments/token/BDfke0XPQ1CycNTXKSRGZPHBY/?name=inline603661386.png)  
  
2. Verifique se não existir o valor no arquivo , verifique o porque não está trazendo o valor na rescisão.

**Saiba Mais:**

<https://tdn.totvs.com/display/public/PROT/FGTS>

[RH GRRF (Guia de Recolhimento Rescisório FGTS)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010781714-RH-GRRF-Guia-de-Recolhimento-Rescis%C3%B3rio-FGTS)
