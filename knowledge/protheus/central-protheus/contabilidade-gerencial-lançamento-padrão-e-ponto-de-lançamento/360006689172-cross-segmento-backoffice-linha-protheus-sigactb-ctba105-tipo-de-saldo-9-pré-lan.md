---
article_id: 360006689172
category: Contabilidade Gerencial - Lançamento Padrão e Ponto de Lançamento
content_hash: 700cde539deee1b010f2a5aafd3f2eafc400aec45682495c3c3eaf3a452c5777
fetched_at: '2026-06-28T22:40:34.137258+00:00'
product: protheus
section_id: 1500001549002
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA105 Tipo de saldo
  9 Pré-Lançamento
type: support-article
updated_at: '2025-02-19T15:15:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006689172-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA105-Tipo-de-saldo-9-Pr%C3%A9-Lan%C3%A7amento
---

**Dúvida**

Como faço para utilizar o Saldo do tipo 9 Pré-Lançamento?

Com configurar o sistema para que seja gerado CT2\_TPSALD='9'  
  
**Ambiente**

Protheus - Contabilidade Gerencial - 12.1.17  
  
  
**Solução**

* O saldo tipo 9 é utilizado nos lançamentos contábeis juntamente com o parâmetro **MV\_PRELAN.**

Documentação referente ao MV\_PRELAN: <http://tdn.totvs.com/pages/releaseview.action?pageId=284348618>

* [CTBA105 - Contabilização Off-Line não valida a linha do lançamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059273293-MP-SIGACTB-CTBA105-Contabiliza%C3%A7%C3%A3o-Off-Line-n%C3%A3o-valida-a-linha-do-lan%C3%A7amento?source=search)

* Caso o cliente queira efetivar o seu Pré-Lançamento, será necessário utilizar a rotina de Efetivação (CTBA350)

Comentação da rotina de Efetivação: <http://tdn.totvs.com/pages/releaseview.action?pageId=233755553>

* Através do cadastro do lançamento padrão é possível informar o "Tipo do SLD" , para que todos o lançamentos originados desta LP sejam gerado como Pré- Lançamento , desconsiderando assim a configuração do parâmetro descrito inicialmente
* CT5\_TPSALD

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085355934/mceclip0.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009461851/mceclip0.png)

[Verifique os parâmetro](https://tdn.totvs.com/display/public/PROT/SIGACTB+-+Diversos+--+24238)s :

[**MV\_CT105MS :**](https://tdn.totvs.com/pages/releaseview.action?pageId=6068560)

O parâmetro **MV\_CT105MS** é utilizado para indicar se serão exibidas mensagens de alerta ao encontrar inconsistências em lançamentos de integração, caso o o sistema estiver configurado para não permitir a alteração destes lançamentos no momento da contabilização (parâmetro **MV\_ALTLCTO**com conteúdo N)

**MV\_ALTLCTO**

Permite alterar os lançamentos contábeis de integração. No caso de não permitir a alteração de   lançamentos, e se estes tenham alguma inconsistência de valor  ou entidades contábeis não   existentes, o lançamento será obrigatoriamente gravado como pré-lançamento.

 

**MV\_CONTBAT:**

Não permite confirmar a inclusão/alteração de um lançamento

contábil quando o débito não bater com o crédito.

 

**MV\_CONTSB:**

Indica se a contabilização será feita, mesmo que os valores de

débito e crédito não batam. Se estiver com "S", gravará o

lançamento contábil sem verificação de valores. Caso contrário,

dependerá da configuração de MV\_CONTBAT.

 

**MV\_CONTSLD:**

Indica se a validação de débito e crédito do lançamento

contábil será efetuada por tipo de saldo (evitando que sejam

gerados lançamentos à débito e à credito em tipos de saldo

diferentes. Se não for necessário efetuar esta validação,

preencher o conteúdo com “N”.

Documentações relacionadas:

[MP- SIGACTB - Tipos de Saldos Contábeis](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015967548-MP-SIGACTB-Tipos-de-Saldos-Cont%C3%A1beis)

* [CTBA105 - Contabilização Off-Line não valida a linha do lançamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059273293-MP-SIGACTB-CTBA105-Contabiliza%C3%A7%C3%A3o-Off-Line-n%C3%A3o-valida-a-linha-do-lan%C3%A7amento?source=search)
