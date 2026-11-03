---
article_id: 23390169725719
category: RH - Rescisão
content_hash: 876d7f9c2849223bcb531b4c59223e808455ade1aa62c13e8558b0ab1875ff3c
fetched_at: '2026-06-28T22:43:50.886557+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Seguro desemprego com verba acumulado calculada
  em roteiro VEX
type: support-article
updated_at: '2025-08-12T16:31:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23390169725719-RH-Linha-Protheus-GPE-Seguro-desemprego-com-verba-acumulado-calculada-em-roteiro-VEX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23390160734743) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como gerar arquivo seguro desemprego com verba acumulado calculada em roteiro VEX para não ocorrer duplicidade em valor?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

Quando houver integração do roteiro VEX com o roteiro FOL, as verbas pagas no roteiro VEX irão duas vezes para os acumulados (SRD) após o fechamento, deste modo para não gerar duplicidade em arquivo seguro desemprego, no campo verbas acumulado deve ser informada verba de contrapartida cálculo VEX (verba desconto).

**Exemplo:**

Cálculo folha mês anterior rescisão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23390160737303)

Verba comissão 179 e verba contrapartida Y31.

**Geração arquivo seguro desemprego.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23390169710103)

**Arquivo seguro desemprego.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23390160739735)

**1.661,86 + 340,65 + 340,65 = 2.343,16 - 340,65 = 2.002,51.**

**Saiba Mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)

[RH - Linha Protheus - GPE - Como fazer a geração do arquivo de seguro desemprego](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010783602-RH-Linha-Protheus-GPE-Como-fazer-a-gera%C3%A7%C3%A3o-do-arquivo-de-seguro-desemprego?source=search)

<https://tdn.totvs.com/display/public/PROT/TVVSDA_DT_Roteiro_Valores_Extras>
