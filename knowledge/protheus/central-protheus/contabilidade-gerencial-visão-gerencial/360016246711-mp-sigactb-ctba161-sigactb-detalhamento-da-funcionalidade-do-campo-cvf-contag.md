---
article_id: 360016246711
category: Contabilidade Gerencial - Visão Gerencial
content_hash: 82460b1324beeea6506f7887f0960d7673f3b01c1b2e06cedc2d9afaa1596f9d
fetched_at: '2026-06-28T22:40:50.695152+00:00'
product: protheus
section_id: 1500001548642
source: central-protheus
title: MP - SIGACTB - CTBA161- SIGACTB - Detalhamento da funcionalidade do campo CVF_CONTAG
type: support-article
updated_at: '2021-04-28T15:23:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016246711-MP-SIGACTB-CTBA161-SIGACTB-Detalhamento-da-funcionalidade-do-campo-CVF-CONTAG
---

**Ocorrência**

* Solicitação de detalhamento da funcionalidade do campo CVF\_CONTAG.
* Ao emitir relatório com Visão gerencial não é apresentada em Ordem

**Ambiente**

Protheus – Contabilidade – A partir da versão P12.1.17.

**Causa**

Ao emitir o relatório o sistema considera o campo Ordem informada na visão gerencial

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016055852/mceclip0.png)

**Solução**

Para intercalar uma nova linha no arquivo (Visão Gerencial), é necessário alterar os campos CVF\_CONTAG e CVF\_ORDEM, das linhas posteriores para poder assim incluir uma nova linha.

Exemplo: Necessário incluir uma linha entre a linha 2 e 3.

01 – Linha 1

02 – Linha 2

03 – Linha 3

**1º Passo:**

Alterar os campos CVF\_CONTAG e CVF\_ORDEM da linha 03 para 04.        

**2º Passo:**

Incluir a linha 03 – Nova linha com os campos CVF\_CONTAG e CVF\_ORDEM preenchidos  com 04 e CVF\_ORDEM preenchidos com 04.

**3º Passo (Novo Layout)**

01 – Linha 1

02 – Linha 2

03 – Nova Linha

04 – Linha 4

**Para maiores detalhes, consulte o link abaixo:**

<http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/mata975_registrosgerados.htm>

<http://tdn.totvs.com/display/PROT/Alter.Valid.Campo_CVF_CONTAG_TGWIZI>
