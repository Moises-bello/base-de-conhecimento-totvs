---
article_id: 11592861572759
category: NFe - Nota Fiscal Eletrônica
content_hash: eaacf08c603fc794fc88a08cb8f428f54cc30efadf4d85a33b9c047fbfa2185d
fetched_at: '2026-06-28T22:40:05.473331+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 891 Rejeição: GTIN
  incompatível com a NCM'
type: support-article
updated_at: '2024-09-02T17:34:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11592861572759-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-891-Rejei%C3%A7%C3%A3o-GTIN-incompat%C3%ADvel-com-a-NCM
---

**Dúvida**Como corrigir a 891 Rejeição: GTIN incompatível com a NCM ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe -a partir da versão 12.1.27

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. Acessar o cadastro de CCG-Cadastro Centralizado de GTIN, pode consultar pelo site: <https://cnp.gs1br.org/>

Verificar o NCM vinculado, para confirmar qual o último dígito deve ter no padrão conforme o site:

[www.gs1.org/check-digit-calculator](http://www.gs1.org/check-digit-calculator)

2. Para alterar o NCM diferente  preencha no campo do cadastro de produto ***Pos.IPI/NCM** "**B1\_POSIPI". para um NCM válido pela Sefaz.***

![20220411_141510.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/26078213812375)

* **Validação da Sefaz:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11592612802967)
