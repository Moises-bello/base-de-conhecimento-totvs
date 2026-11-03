---
article_id: 4421391500055
category: Financeiro
content_hash: 37b4ab3277284b2b4f9efda45da77e3de9c0d2cd3a088dde24fdc4dfaec86367
fetched_at: '2026-06-28T22:38:01.141528+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmento - Backoffice Protheus  - FINA022- Qual a diferença em preencher
  o campo FRV_BANCO = SIM ou NÃO
type: support-article
updated_at: '2022-02-04T12:08:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421391500055-Cross-Segmento-Backoffice-Protheus-FINA022-Qual-a-diferen%C3%A7a-em-preencher-o-campo-FRV-BANCO-SIM-ou-N%C3%83O
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Qual a diferença em preencher o campo FRV\_BANCO = SIM ou NÃO?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA022- A partir da versão 12  
  
**Solução**O preenchimento como **SIM** será movimentado Banco, significa que será feito uma **movimentação** **bancária** na tabela **SE5** e consequentemente movimenta saldo na tabela **SE8,** no momento da baixa.  
  
Se preencher como **NÃO**, o comportamento será como um título **baixado** por **Dação** (sem **movimentação bancária**).

Os impactos  e as diferentes irão, depender das movimentações  e do cadastro dos campos que preencheu na **Situação de Cobrança**, segue abaixo:![](https://totvssuporte.zendesk.com/attachments/token/elwryWFF5fAN1kewwfMXHLBjE/?name=inline2018444484.png)

**Saiba mais:**

[MP - SIGAFIN - Como incluir novas situações de cobranças](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021885651-MP-SIGAFIN-Como-incluir-novas-situa%C3%A7%C3%B5es-de-cobran%C3%A7as?source=search)
