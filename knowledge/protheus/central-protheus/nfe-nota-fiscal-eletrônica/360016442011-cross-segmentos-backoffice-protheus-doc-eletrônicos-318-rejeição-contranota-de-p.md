---
article_id: 360016442011
category: NFe - Nota Fiscal Eletrônica
content_hash: 80653119661c0f1a1dba12883831de55f7966fcf61c1a10fe0f7884fd895de91
fetched_at: '2026-06-28T22:40:03.867764+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 318 Rejeição :
  Contranota de Produtor sem Nota Fiscal referenciada'
type: support-article
updated_at: '2025-06-30T19:25:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016442011-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-318-Rejei%C3%A7%C3%A3o-Contranota-de-Produtor-sem-Nota-Fiscal-referenciada
---

**Dúvida**Como solucionar a 318 Rejeição : Contranota de Produtor sem Nota Fiscal referenciada ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A SEFAZ está validando se o IE é de produtor rural e, caso seja, é necessário gerar a TAG referenciando a nota.

Para isso, quando é feita a nota de entrada, se o IE do destinatário for de produtor rural, tem que haver a tag referenciando a contranota.

* **Caso seja NFP (Nota fiscal de produtor rural) será gerada a TAG refNFP:**

1- Primeiro, é feita uma nota de Entrada com formulário próprio = Não Espécie = NFP ***(Esta não é transmitida).***

![20220401_141509.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5173363118615)

2- Depois, é feita uma nota de Entrada com formulário próprio = Sim Espécie = SPED ***(Esta é transmitida).***Esta nota deve ser referenciada à anterior que não foi transmitida. E, para referenciar a de origem, os três campos a seguir precisam estar preenchidos:

***D1\_ITEMORI, D1\_SERIORI, D1\_NFORI*** (nota de entrada).

![20220401_142404.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5173562781975)

3- Quando é feita uma nota complementar ou de devolução, elas devem ter formulário próprio = Sim Espécie = SPED e essa nota **deve ser referenciada à que foi transmitida** e não à primeira, com formulário próprio = Não.

E, para referenciar a de origem, os três campos precisam estar preenchidos:

***D1\_ITEMORI, D1\_SERIORI, D1\_NFORI***(nota de entrada)

* **Caso seja NFPe (Nota fiscal de produtor rural eletrônica) será gerada a TAG refNFe:**

1- Primeiro, é feita uma nota de Entrada com formulário próprio = Não Espécie = SPED é preenchido o campo F1\_CHVNFE = com a chave da nota ***(Esta não é transmitida).***

![20220401_142758.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5173659031063)

2- Depois, é feita uma nota de Entrada com formulário próprio = Sim Espécie = SPED ***(Esta é transmitida).*** Esta nota deve ser referenciada à anterior que não foi transmitida. E, para referenciar a de origem, os três campos a seguir precisam estar preenchidos:

***D1\_ITEMORI, D1\_SERIORI, D1\_NFORI*** (nota de entrada).

![20220401_142404.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5173562781975)

3- Quando é feita uma nota complementar ou de devolução, elas devem ter formulário próprio = Sim Espécie = SPED e essa nota deve ser referenciada à que foi transmitida e não à primeira, com formulário próprio = Não.

E, para referenciar a de origem, os três campos precisam estar preenchidos:

***D1\_ITEMORI, D1\_SERIORI, D1\_NFORI (nota de entrada)***

***Observação: Importante que ao incluir a nota do produtor rural a TES esteja configurada para gerar os registros na tabela SF3, pois sem esse registro não é possível  referenciar a nota do produtor na******contra nota pela tag refnfe.***
