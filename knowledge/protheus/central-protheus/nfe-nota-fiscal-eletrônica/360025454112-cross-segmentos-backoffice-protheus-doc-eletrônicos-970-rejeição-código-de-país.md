---
article_id: 360025454112
category: NFe - Nota Fiscal Eletrônica
content_hash: f7eb4328fd061f3d6105b03ca7a4570b22724c83f61351f993c1cad4e9e81917
fetched_at: '2026-06-28T22:40:01.608617+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 970 Rejeição:
  Código de País inexistente [local de retirada/entrega]'
type: support-article
updated_at: '2021-10-11T18:13:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025454112--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-970-Rejei%C3%A7%C3%A3o-C%C3%B3digo-de-Pa%C3%ADs-inexistente-local-de-retirada-entrega
---

**Dúvida**

Como solucionar a rejeição 970 Rejeição: Código de País inexistente [local de retirada/entrega] ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* **Será necessário realizar atualização do link abaixo:**

**[NT 2018.005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021996291/preview/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzYwMDIxOTk2MjkxLCJleHAiOjE1NTQyMTEzNTN9.pLWryvNhKK9lOxZH2tG29r-vIboZBbJVEUhpnWVBPww)**

**Caso seja informado o cliente de entrega ou retirado, será necessário verificar se é nota de entrada ou de saída.**

Se nota de entrada fornecedor o campo A2\_PAIS.

Se nota de saída cliente o campo A1\_PAIS.

De acordo com o país informado no campo acima:

Será  necessário entrar na APSDU na tabela SYA alterar o campo YA\_SISEXP, se estiver em branco deverá preencher o campo em branco ou se tiver mais de 4 números  
desconsiderar o zero a esquerda que o Protheus só valida 4 números.

Poderá verificar no site:

<http://www.bcb.gov.br/rex/Censo2000/port/manual/pais.asp?idpai=CENSOCE>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024533591/mceclip0.png)
