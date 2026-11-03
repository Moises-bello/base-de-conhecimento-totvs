---
article_id: 360046324813
category: NFe - Nota Fiscal Eletrônica
content_hash: 33a725e4ec8c8112b1bce0ac55b0e8563d00e20ac2d63d11ee99af65c672ea93
fetched_at: '2026-06-28T22:40:01.989500+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -331 Rejeição: Informar
  o CNPJ do adquirente ou do encomendante nesta forma de importação'
type: support-article
updated_at: '2021-10-11T17:44:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046324813--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-331-Rejei%C3%A7%C3%A3o-Informar-o-CNPJ-do-adquirente-ou-do-encomendante-nesta-forma-de-importa%C3%A7%C3%A3o
---

**Dúvida**Como solucionar a rejeição abaixo:

331 Rejeição: Informar o CNPJ do adquirente ou do encomendante nesta forma de importação?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**1-** Quando**não usa integração**com o**módulo SIGAEIC é necessário que o parâmetro MV\_EASY= N**

**![20201201_145829.gif](https://totvssuporte.zendesk.com/hc/article_attachments/360101037393/20201201_145829.gif)**

**2-**Acesse a rotina **Livros Fiscais-> Atualizações->Movimentos->NF manual de Saída->Outras ações->Complementos->Importação:**

**![20201201_145142.gif](https://totvssuporte.zendesk.com/hc/article_attachments/360101036933/20201201_145142.gif)**

3 - Quando é informado a TAG **tpIntermedio=2 ou 3** informação  preenchida no campo **CD5\_INTERM.**

4 - É necessário ser preenchida a TAG **CNPJ** o campo que leva o conteúdo dessa TAG é  **CD5\_CNPJAE podendo ser preenchida uma das opções abaixo:**

**1=**Importação por conta própria;

**2=**Importação por conta e ordem;

**3=**Importação por encomenda;

5- Se informar tpIntermedio  **CD5\_INTERM= 1** o campo **CD5\_CNPJAE** poderá ficar em branco.

6- Exclua a nota e preencha os Livros fiscais conforme acima, após isso transmita a nota.

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065404593/mceclip0.png)
