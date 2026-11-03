---
article_id: 4415768235031
category: RH - Rescisão
content_hash: 4a5e43ec6e34126642f90ec111fa96f9898d33c6b309f4151fd960f89b244ace
fetched_at: '2026-06-28T22:43:53.492413+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE - Por que ao calcular rescisão por pedido de demissão
  onde há cadastro de aviso prévio GPEA925, sistema emite mensagem: Atenção Código
  de Afastamento de FGTS informado no Tipo de Rescisão é incompatível com o tipo de
  Aviso Prévio'
type: support-article
updated_at: '2025-04-16T18:37:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415768235031-RH-Linha-Protheus-GPE-Por-que-ao-calcular-rescis%C3%A3o-por-pedido-de-demiss%C3%A3o-onde-h%C3%A1-cadastro-de-aviso-pr%C3%A9vio-GPEA925-sistema-emite-mensagem-Aten%C3%A7%C3%A3o-C%C3%B3digo-de-Afastamento-de-FGTS-informado-no-Tipo-de-Rescis%C3%A3o-%C3%A9-incompat%C3%ADvel-com-o-tipo-de-Aviso-Pr%C3%A9vio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Por que ao calcular rescisão por pedido de demissão onde há cadastro de aviso prévio GPEA925, sistema emite mensagem: Atenção Código de Afastamento de FGTS informado no Tipo de Rescisão é incompatível com o tipo de Aviso Prévio.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415768097303/mceclip0.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**O cálculo de rescisão emite a mensagem porque o campo Tip. Av Prev na rotina cadastro de aviso GPEA925 foi preenchido incorretamente.. Para pedido de demissão deve ser informado o código 4.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415760458903/mceclip1.png)

**Saiba mais**  
Para adquirir mais conhecimento acesse o *link* abaixo:

[MP - GPE - Cadastro de Aviso Prévio - (Aviso trabalhado)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038464054-MP-GPE-Cadastro-de-Aviso-Pr%C3%A9vio-Aviso-trabalhado-?source=search)
