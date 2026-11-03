---
article_id: 4407698190743
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 224586dc296cc6534d4b71bb0f04ac9e69980d74d804e424815b686d74f75f34
fetched_at: '2026-06-28T22:39:58.530369+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Tag SituacaoEspecial
  para Joinville-SC
type: support-article
updated_at: '2025-07-18T14:44:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407698190743-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Tag-SituacaoEspecial-para-Joinville-SC
---

**Dúvida**Como gerar a tag SituacaoEspecial no XML do RPS de Joinville-SC?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Documentos Eletrônicos - Todas as versões.  
  
**Solução**O conteúdo da tag **SituacaoEspecial** é extraído diretamente do cadastro do cliente, campo A1\_TPNFSE:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407689578263)

O uso dessa tag é muito importante para notas com ISS Retido.

Se o ISS for retido e essa tag não for enviada, o valor do ISS será destacado como devido no portal da prefeitura.

Essa situação foi tratada na issue DSERTSS2-8891
