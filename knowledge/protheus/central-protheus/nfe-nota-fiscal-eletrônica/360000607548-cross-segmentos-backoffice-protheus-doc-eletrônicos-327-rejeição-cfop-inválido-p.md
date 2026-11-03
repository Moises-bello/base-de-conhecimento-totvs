---
article_id: 360000607548
category: NFe - Nota Fiscal Eletrônica
content_hash: 512fb6ec30c294f1855754355ed51c2e781f6cd04b39c0334cb2c9d27c48cf34
fetched_at: '2026-06-28T22:40:03.894222+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 327 Rejeição :
  CFOP inválido para NF-e com finalidade de devolução de mercadoria.'
type: support-article
updated_at: '2025-07-25T18:34:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000607548-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-327-Rejei%C3%A7%C3%A3o-CFOP-inv%C3%A1lido-para-NF-e-com-finalidade-de-devolu%C3%A7%C3%A3o-de-mercadoria
---

**Ocorrência**Como solucionar a 327 Rejeição : CFOP inválido para NF-e com finalidade de devolução de mercadoria ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todos as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Ao fazer **nota de devolução** ou **retorno** no sistema é gerada a TAG **FINNFE= 4 (devolução)** para qualquer **CFOP.**

Porém, quando o **CFOP** não possui a **finalidade de devolução** é necessário gerar a TAG **FINNFE = 1 (normal).**

Para **esses CFOPS é necessário** incluir no parâmetro **MV\_DEVCFOP** no configurador.

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **editar**  **MV\_DEVCFOP:** 6910;5910;6211;5211; ***(ponto e vírgula sem espaço) com CFOPS da nota fiscal eletrônica;***

![20220418_113611.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5519295562007)

2. Após isso, ***r****etransmita NF-e.***

**Saiba mais:**

É possível consultar a **nota técnica 2013.005\_v\_1.22** página 130 para saber quais são os CFOPs com finalidade de devolução.

<http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=tW+YMyk/50s=>

 Para a Sefaz não existe operações no qual conste um **CFOP com finalidade de devolução** e outro **CFOP com finalidade normal**. Para esses casos se os **CFOPs da nota estiverem corretos**, será necessário fazer duas notas.

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074785174)
