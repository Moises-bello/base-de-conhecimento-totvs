---
article_id: 360025310894
category: NFe - Nota Fiscal Eletrônica
content_hash: 1f7fe4c87a61b11301cb8752dcc3bb00e32231be09c0ee3c8b81c9c0ca91844f
fetched_at: '2026-06-28T22:40:03.600436+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Como gerar mensagem
  em informações complementares do Danfe com mais de 250 caracteres ?
type: support-article
updated_at: '2025-06-25T12:17:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025310894-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-mensagem-em-informa%C3%A7%C3%B5es-complementares-do-Danfe-com-mais-de-250-caracteres
---

**Dúvida**Como gerar mensagem em informações complementares do Danfe com mais de 250 caracteres ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para que seja informada uma mensagem em informações complementares do Danfe com **mais de 250 caracteres:**

1- Crie um campo do tipo **MEMO no configurador** na tabela **SC5** ( para nota de saída) ou na **SF1** (para nota de entrada).

2- Informe no parâmetro **MV\_CMPUSR=** (Informar o nome do campo criado na tabela **SC5** ou na **SF1** com o tipo **MEMO**).

Obs: Para utilizar os campos criados na SF1 é necessário usar o ponto de entrada MT103DCF para habilitar botão Mais Inf. e acrescenta campos na aba DANFE. Caso tenha duvidas com esse processo entre em contato com equipe Protheus Compras.

3- Neste campo **MEMO** deve ser digitado a mensagem que deseja gerar no XML e no DANFE em informações complementares.

**Para NF-e nota de modelo 55 parâmetro****MV\_CMPUSR:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050644694)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050644754)**

* **Saiba mais:**

Caso seja necessário informar, mais de um campo conforme o fonte do **NFESEFAZ** abaixo separar por **PIPE "| "**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404644208919)**

IF GetNewPar("MV\_CMPUSR","")  <>  ""

**aCMPUSR****:= StrTokArr( GetNewPar("MV\_CMPUSR",""), "|" )**
