---
article_id: 4408233464343
category: NFe - Nota Fiscal Eletrônica
content_hash: e20acca8766eb6adacfd4c64a66a652565af1302dfd6e4c23d029571520b82ad
fetched_at: '2026-06-28T22:40:01.966931+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Tag da UF da Placa
  Opcional '
type: support-article
updated_at: '2023-08-22T17:58:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408233464343--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Tag-da-UF-da-Placa-Opcional
---

**Dúvida**Como configurar para que a TAG da UF da Placa Opcional   
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

O novo modelo de placa adotado no Brasil não possui a informação da UF de registro, por este motivo esta informação foi tornada opcional no Schema **(campos X19 e X23).**

1 - No **cadastro de veículo o campo do Estado Placa  "DA3\_ESTPLA"**, passa a ser opcional na nota técnica 2020.005, sendo assim não é necessário informar conteúdo no campo.

![20210910_121136.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4408228500375/20210910_121136.gif)

2- Para que não apresente falha de Schema na **transmissão é necessário aplicar os pacotes da documentação abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052495714)

* **Exemplo do XML:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409132714391/mceclip0.png)

* Caso gere a **868 Rejeição** temos a documentação do link abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 868 Rejeição : Grupo veículo transporte e reboque não devem ser informados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007158412)
