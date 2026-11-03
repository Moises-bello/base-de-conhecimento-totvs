---
article_id: 235301547
category: Materiais - Compras (SIGACOM)
content_hash: e2ee057c2e08ef5cfb5fafbe0e38cd7d593da53a221ab5933fc71705e1953461
fetched_at: '2026-06-28T22:41:20.201419+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Mensagem: O cliente/fornecedor
  não esta relacionado a esta ou nenhuma filial'
type: support-article
updated_at: '2022-05-18T21:04:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/235301547-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Mensagem-O-cliente-fornecedor-n%C3%A3o-esta-relacionado-a-esta-ou-nenhuma-filial
---

**Dúvida**

Mensagem: O cliente/fornecedor não esta relacionado a esta ou nenhuma filial

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101881513/mceclip0.png)

**Ambiente**

Protheus – Compras – A partir da 12.1.17  
  
**Solução**

Para que não apresente mais a mensagem **O cliente/fornecedor não esta relacionado a esta filial,** verifique se o conteúdo do campo **Trans** **Filial** (**F4\_TRANFIL**) do **TES** está preenchido com **SIM**.

O sistema valida se a nota refere-se a transferência entre filiais e valida o Cadastro do Fornecedor com o CNPJ da filial origem.

Se não for nota de transferência entre filiais, altere o conteúdo do campo para **Não**, ou utilize outro **TES**.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
