---
article_id: 360052081154
category: NFe - Nota Fiscal Eletrônica
content_hash: e8f1c9436fd4a6899a3b2dd75e4e076139ee0e322eddaa948f76b19fa275fdd7
fetched_at: '2026-06-28T22:40:06.842999+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Exportação de XML
type: support-article
updated_at: '2025-06-26T14:46:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052081154-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Exporta%C3%A7%C3%A3o-de-XML
---

**Dúvida**

Como exportar o XML de notas transmitidas e autorizadas ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

1. Acessar a rotina  SPEDNFE que fica dentro no modulo **Faturamento > NFESEFAZ (SPEDNFE) > Outras Ações > Exportar.**

![nfesefaz.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11563276656663)

2. Posteriormente é preciso informar na tela de parâmetros os dados para que o sistema ***filtre por numero e série, range, data e outras informações:***

![exportar_XML.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11563445971735)

3. Basta prosseguir com o ***processo e consultar no diretório informado a geração do(s) arquivo(s) gerado(s) após finalização.***

***![DIRETORIO_XML.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11563548520343)***

* ***Saiba mais:***

Informar que o processo só terá êxito quando a filial que será acessada no Protheus,  ***seja a mesma que realizou a transmissão da nota.***

Existe um vinculo entre a filial com a entidade que corresponde a mesma no TSS, ou seja, se a nota foi transmitida pela filial 01 e entidade 000001 no TSS, apenas acessando por essa filial é possível exportar ou imprimir o documento.
