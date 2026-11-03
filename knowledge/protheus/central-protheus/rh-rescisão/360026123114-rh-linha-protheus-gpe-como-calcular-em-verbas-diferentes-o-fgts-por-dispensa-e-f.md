---
article_id: 360026123114
category: RH - Rescisão
content_hash: 45b9d3bd8b4a087d87221a2a769f1b6ab87193615cc9b5fecd10a77b94e38391
fetched_at: '2026-06-28T22:43:51.963864+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular em verbas diferentes o FGTS por Dispensa
  e FGTS por pedido de demissão na Rescisão e assim levar corretamente para Sefip
  ou GRRF
type: support-article
updated_at: '2024-10-03T21:20:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026123114-RH-Linha-Protheus-GPE-Como-calcular-em-verbas-diferentes-o-FGTS-por-Dispensa-e-FGTS-por-pedido-de-demiss%C3%A3o-na-Rescis%C3%A3o-e-assim-levar-corretamente-para-Sefip-ou-GRRF
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26823239676311)***Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Ao calcular uma rescisão, como fazer com que o sistema calcule o FGTS por dispensa em uma verba e o FGTS por pedido de demissão em outra verba e assim carregar corretamente para a Sefip ou GRRF?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Para que o FGTS por dispensa e o FGTS por pedido de demissão sejam calculados em verbas separadas, é necessário parametrizar na Tabela S043-Manutenção Tabela:  
  
1. **Rescisão por dispensa** **e/ou rescisões onde o FGTS tem que ser recolhidos na GRRF** - Na Tabela S043, deixe a coluna **FGTS Mes Resc.** com **S**, assim a verba BASE FGTS será calculada na verba de ID 0293 e o Recolhimento do FGTS será calculado na verba de ID 0119, e a Base do FGTS 13º será calculada no ID 0294 e o recolhimento do FGTS 13º será calculado no ID 0214:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041557433)

2. **Rescisão por Pedido de Demissão e/ou rescisões onde o FGTS será recolhido na Sefip** - Na Tabela S043, deixar a coluna **FGTS Mes Resc.** com **N,** assim a verba BASE FGTS será calculada na verba de ID 0017 e o Recolhimento do FGTS será calculado na verba de ID 0018, e a verba de Base FGTS 13º será calculada na verba de ID 0108 e o recolhimento do FGTS 13º será na verba de ID 0109:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040727434)

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
