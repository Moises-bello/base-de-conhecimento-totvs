---
article_id: 360022499672
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 03b0f03b15e70adc29f30aaeb220e1148588ac9214470227b38572b5c7e39619
fetched_at: '2026-06-28T22:40:32.563244+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBA102 Partida dobrada
  com mesma conta a débito e a crédito é apresentado help: CTAEQUA123'
type: support-article
updated_at: '2023-11-23T11:18:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022499672-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Partida-dobrada-com-mesma-conta-a-d%C3%A9bito-e-a-cr%C3%A9dito-%C3%A9-apresentado-help-CTAEQUA123
---

**Dúvida**Ao efetuar lançamento de partida dobrada com mesma conta a débito e a crédito é apresentado help: CTAEQUA123

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019817811)

**Ambiente**Microsiga Protheus  – Contabilidade Gerencial – A partir da versão 11.80

**Causa**

Esta mensagem ocorre pois é feita Validação Lançamentos com Contas Credito/Debito Iguais, não sendo possível salvar lançamentos com a mesma conta Débito e Credito.

Rotina de lançamentos não permite  incluir um lançamento de partida dobrada informando a mesma conta no debito e credito, exceto se houver centro de custo no debito e credito o lançamento será validado.

**Solução**

Para que a mensagem não seja apresentada não deve ser informada contas de debito e credito iguais ou deve ser informado entidades (centro de custo, item ou classe de valor) a debito ou a credito para diferenciar a operação.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019969412)**

**Obs.:** Verifique todas as entidades (conta contabil, centro de custo, item contabil e classe de valor)

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416546391575)**

**Saiba mais**

* [CTBA105 - Contabilização Off-Line não valida a linha do lançamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059273293-MP-SIGACTB-CTBA105-Contabiliza%C3%A7%C3%A3o-Off-Line-n%C3%A3o-valida-a-linha-do-lan%C3%A7amento?source=search)
* <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018884032--MP-SIGACTB-CTBA102-LAN%C3%87AMENTO-DE-PARTIDA-DOBRADA-E-PARTIDA-SIMPLES-COM-DUAS-CONTAS-INFORMADAS>
