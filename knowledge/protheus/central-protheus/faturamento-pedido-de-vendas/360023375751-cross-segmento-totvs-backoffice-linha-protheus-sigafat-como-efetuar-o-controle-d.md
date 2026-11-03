---
article_id: 360023375751
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 04738c5d1d0fb24ed54db96cb13e8094812c594d241edc349219d52dda372871
fetched_at: '2026-06-28T22:38:38.482904+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como efetuar
  o controle de poder em terceiros
type: support-article
updated_at: '2022-08-24T18:21:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023375751-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-efetuar-o-controle-de-poder-em-terceiros
---

**Dúvida**

Como efetuar o controle de poder em terceiros?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

**I) Beneficiamento ou remessa a fornecedor**

* **Saída**

1) A saída deve ser efetuada pelo **MATA410** ( **Pedido de Venda** ).

2) O Tipo do Pedido deve ser "**B - Beneficiamento"**, pois é obrigatório a informação do fornecedor.

3) A Pergunta "Poder Terc." (**F4\_PODER3**) deve estar preenchida como "R" ( **Remessa** ).

* **Entrada**

1) A entrada deve ser efetuada pelo **MATA100** (**Nota fiscal de entrada**).

2) O Tipo da Nota deve ser "**N - Normal**", pois é obrigatório a informação do fornecedor.

3) A Pergunta "Poder Terc." (**F4\_PODER3**) deve estar preenchida como "D" (**Devolucao**).

4) Clique em **Outras Ações** na opção **ORIGEM, para localizar a nota de remessa.**

**II) Remessa para Cliente.**

* **Saída**

1) A saída deve ser efetuada pelo **MATA410** ( **Pedido de Venda** ).

2) O Tipo do Pedido deve ser "**N - Normal**", pois é obrigatório a informação do cliente.

3) A Pergunta "Poder Terc." (**F4\_PODER3**) deve estar preenchida como "R" ( **Remessa** ).

* **Entrada**

1) A entrada deve ser efetuada pelo **MATA100** (**Nota fiscal de entrada**).

2) O Tipo da Nota deve ser "**B - Beneficiamento**", pois é obrigatório a informação do cliente

3) A Pergunta "Poder Terc." (**F4\_PODER3**) deve estar preenchida como "D" (**Devolução**).

4) Clique em **Outras Ações** na opção **ORIGEM** **para localizar a nota de remessa.**

**.**
