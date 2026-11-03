---
article_id: 360025477394
category: NFe - Nota Fiscal Eletrônica
content_hash: 8517418d780b3b825c3b77875e209bfbc237125da5cb43ea674e139d0b86b5e6
fetched_at: '2026-06-28T22:40:01.562846+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 922 Rejeição :
  Contranota de Produtor só pode referenciar NF-e ou NF de Produtor Modelo 4'
type: support-article
updated_at: '2021-10-04T11:57:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025477394--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-922-Rejei%C3%A7%C3%A3o-Contranota-de-Produtor-s%C3%B3-pode-referenciar-NF-e-ou-NF-de-Produtor-Modelo-4
---

**Dúvida**Como solucionar a rejeição abaixo:

922 Rejeição : Contranota de Produtor só pode referenciar NF-e ou NF de Produtor Modelo 4 ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**A Sefaz só aceita contranota de produtor rural que seja dos modelos abaixo:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040337673/mceclip1.png)

* **refNFe =** Modelo 55 Espécie = SPED **(quando tem chave)**
* **refNFP=** Modelo 04 Espécie =  NFP **(quando não tem chave)**

**Caso seja NFP (Nota fiscal de produtor rural) será gerada a TAG refNFP:**

Primeiro, é feita uma nota de Entrada com formulário próprio = Não Espécie = NFP **(Esta não é transmitida).**

Depois, é feita uma nota de Entrada com formulário próprio = Sim Espécie = SPED **(Esta é transmitida).** Esta nota deve ser referenciada à anterior que não foi transmitida. E, para referenciar a de origem, os três campos a seguir precisam estar preenchidos:

**D1\_ITEMORI, D1\_SERIORI, D1\_NFORI** (nota de entrada).

Quando é feita uma nota complementar ou de devolução, elas devem ter formulário próprio = Sim Espécie = SPED e essa nota deve ser referenciada à que foi transmitida e não à primeira, com formulário próprio = Não.

E, para referenciar a de origem, os três campos precisam estar preenchidos:

**D1\_ITEMORI, D1\_SERIORI, D1\_NFORI**(nota de entrada)

**Caso seja NFPe (Nota fiscal de produtor rural eletrônica) será gerada a TAG refNFe:**

Primeiro, é feita uma nota de Entrada com formulário próprio = Não Espécie = SPED é preenchido o campo F1\_CHVNFE = com a chave da nota **(Esta não é transmitida).**

Depois, é feita uma nota de Entrada com formulário próprio = Sim Espécie = SPED **(Esta é transmitida).** Esta nota deve ser referenciada à anterior que não foi transmitida. E, para referenciar a de origem, os três campos a seguir precisam estar preenchidos:

**D1\_ITEMORI, D1\_SERIORI, D1\_NFORI** (nota de entrada).

Quando é feita uma nota complementar ou de devolução, elas devem ter formulário próprio = Sim Espécie = SPED e essa nota deve ser referenciada à que foi transmitida e não à primeira, com formulário próprio = Não.

E, para referenciar a de origem, os três campos precisam estar preenchidos:

**D1\_ITEMORI, D1\_SERIORI, D1\_NFORI (nota de entrada)**

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040336753/mceclip0.png)**
