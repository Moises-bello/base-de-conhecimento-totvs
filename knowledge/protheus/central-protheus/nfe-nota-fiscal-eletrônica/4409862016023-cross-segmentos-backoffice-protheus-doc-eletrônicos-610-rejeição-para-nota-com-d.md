---
article_id: 4409862016023
category: NFe - Nota Fiscal Eletrônica
content_hash: a52bb5aa8f049185c95c872d05b73a0567733bbb36836d8805011593a193e7c4
fetched_at: '2026-06-28T22:40:03.245714+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  610  Rejeição para
  nota com desconto
type: support-article
updated_at: '2025-06-13T12:16:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409862016023-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-610-Rejei%C3%A7%C3%A3o-para-nota-com-desconto
---

**Dúvida**Como solucionar a 610  Rejeição para nota com desconto  ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões 

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**1. Atualização do ambiente TSS (repositório e schemas )**

1. Atualizar o **repositório** com o último pacote de**expedição continua do TSS** disponível no link:

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981)

2. Atualizar a pasta **SCHEMAS** presente na estrutura do TSS através do link:

<https://suporte.totvs.com/portal/p/10098/download?e=761857>

**Saiba Mais:**[TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552)

**2. Atualização do ambiente Protheus:**

1. Aplicar o **Pacote Acumulado Documentos eletrônicos:**

[Clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=525010692)

1. **Compilar RDMAKE NFESEFAZ** (se emitir NF-e) presente no link abaixo:

[https://suporte.totvs.com/portal/p/10098/download?e=1083729](https://suporte.totvs.com/portal/p/10098/download?e=1152113)

* **Saiba mais:**

Lembrando que **RDMAKE não possui Release** sendo assim, pode ser aplicada em qualquer uma todos os pacotes.

2. Após isso **exclua a nota e gere** novamente.

* ***Saiba mais:***

***O desconto é gravado nos campos D2\_DESC ou D2\_DESCON.***

Caso haja um**valor unitário bruto no campo da SD2 "D2\_PRUNIT"** e outro valor no campo do preço **de lista "D2\_PRCVEN"** será levada na TAG **vUnCom** o valor bruto e gerado desconto com a diferença dos dois campos:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16666804376343)
