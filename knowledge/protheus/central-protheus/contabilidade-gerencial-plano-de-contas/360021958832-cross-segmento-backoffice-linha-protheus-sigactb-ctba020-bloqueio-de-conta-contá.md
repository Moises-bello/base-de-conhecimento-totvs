---
article_id: 360021958832
category: Contabilidade Gerencial - Plano de Contas
content_hash: 0a1761d313f0df349e11aaf49065a84d5aff52b64cf0ca5750ff0b18056b2d18
fetched_at: '2026-06-28T22:40:33.341928+00:00'
product: protheus
section_id: 1500001549022
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA020 - Bloqueio de
  Conta Contábil
type: support-article
updated_at: '2024-03-25T11:41:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021958832-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA020-Bloqueio-de-Conta-Cont%C3%A1bil
---

**Dúvida**Qual o conceito do bloqueio de Conta Contábil?

**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial - 12.1.17  
  
  
**Solução**O bloqueio de Conta Contábil tem por objetivo impedir que tenham **novas movimentações** para a Conta estipulada por um período que o usuário determinar, para bloquear uma conta, basta que ela exista no Plano de Contas, independentemente de possuir saldo ou não.

Para bloquear uma conta no sistema:  
  
Acesse a rotina **CTBA020(Plano de Contas)**e escolha a opção alterar posicionado na conta de bloqueio.

O bloqueio de Conta Contábil pode ser realizado de duas formas:

**1) Por período determinado:** Os **Dt Ini Bloq** (CT1\_DTBLIN) e **Dt Fim Bloq** (CT1\_DTBLFI) devem ser preenchidos com as datas na qual a conta ficará bloqueada, desde que o campo **Cta Bloq** (CT1\_BlOQ) esteja como Não Bloqueada.

**2) Por período Indeterminado:** O campo **Cta Bloq** (CT1\_BLOQ) deve estar com opção de Bloqueado. Este campo ficará bloqueado até que o usuário realize a alteração para a opção de Não Bloqueada.

Após isso caso tente efetuar um lançamento contábil para a conta bloqueada, será apresentado o

**Help :**CTA\_BLOQ

**Problema:** Esta entidade está bloqueada .CT1 :001

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360018982511)
