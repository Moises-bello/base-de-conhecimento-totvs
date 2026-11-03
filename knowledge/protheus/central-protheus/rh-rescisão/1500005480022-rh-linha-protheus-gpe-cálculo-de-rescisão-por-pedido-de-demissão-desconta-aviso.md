---
article_id: 1500005480022
category: RH - Rescisão
content_hash: c2762c8374726d5f30fd77e2091dd9ddf173f85680ee8829927694b1d26a126d
fetched_at: '2026-06-28T22:43:51.942652+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de rescisão por pedido de demissão, desconta
  aviso prévio 30 dias mais a projeção de 3 dias adquiridos ao ano
type: support-article
updated_at: '2025-09-08T17:06:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005480022-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-rescis%C3%A3o-por-pedido-de-demiss%C3%A3o-desconta-aviso-pr%C3%A9vio-30-dias-mais-a-proje%C3%A7%C3%A3o-de-3-dias-adquiridos-ao-ano
---

**Dúvida**Por que cálculo de rescisão por pedido de demissão, desconta aviso prévio 30 dias mais a projeção de 3 dias adquiridos ao ano?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal  - Versão 12.1.17  
  
**Solução**Na tabela S043 da rotina Manutenção de Tabelas, pelo caminho >Atualizações >Definições de cálculo >Manutenção Tabela, são definidos os critérios de cálculo da rescisão.   
Para que seja descontado somente os 30 dias de aviso prévio quanto a rescisão por pedido, a coluna Aviso Prévio deve ser configurada com D e a coluna Projeta Aviso com N.

**Tabela S043**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007401161)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007401661)**

**Saber Mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
