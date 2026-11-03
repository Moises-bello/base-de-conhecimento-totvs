---
article_id: 360026258514
category: NFe - Nota Fiscal Eletrônica
content_hash: 698078797b68547cd25533049ced5c5e6a5b580b42adad3a750f30ef7030fa3c
fetched_at: '2026-06-28T22:40:00.272769+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  924 Rejeição:
  Informado Cupom Fiscal referenciado'
type: support-article
updated_at: '2023-05-24T17:42:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026258514--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-924-Rejei%C3%A7%C3%A3o-Informado-Cupom-Fiscal-referenciado
---

**Dúvida**Como solucionar a rejeição abaixo:

Rejeição: 924 Rejeição: Informado Cupom Fiscal referenciado?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**A critério da UF não poderá mais ser referenciada nota de cupom.**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041744253/mceclip0.png)**

Se informado a TAG  **refECF** no XML:

* **refECF=** Modelo 65 **Espécie =**  NFCE/SATCE

* Verificar se a nota foi **referenciada ao documento**correto:

D2\_ITEMORI, D2\_SERIORI, D2\_NFORI (nota de saída)  
  
D1\_ITEMORI, D1\_SERIORI, D1\_NFORI (nota de entrada)

Se **sim** e a espécie da nota de origem realmente for **NFCE** ou **SATCE** a **UF não** permite mais que seja referenciada a uma **NF-e**

* **Importante:**

Caso esteja errado a espécie da nota de origem, refazer a nota ou alterar nos campos F2 ou F1\_ESPECIE, F3\_ESPECIE e FT\_ESPECIE.

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041740153/mceclip0.png)**
