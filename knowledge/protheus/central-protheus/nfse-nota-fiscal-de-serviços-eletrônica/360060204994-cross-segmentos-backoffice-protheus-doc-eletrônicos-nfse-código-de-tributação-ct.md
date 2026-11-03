---
article_id: 360060204994
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: d2a1072c6d365fc9a045acb8a88a84385ca86122416169c55eb04c1fc4c0b4e9
fetched_at: '2026-06-28T22:39:56.365424+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Código de
  Tributação / CTISS de Salvador - BA
type: support-article
updated_at: '2025-07-14T21:35:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060204994-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-C%C3%B3digo-de-Tributa%C3%A7%C3%A3o-CTISS-de-Salvador-BA
---

**Dúvida**Envio da tag CodigoTributacaoMunicipio no xml do RPS de Salvador-BA, conforme DECRETO Nº 33.434 de 11 janeiro de 2021.  
<http://www.sefaz.salvador.ba.gov.br/Documento/ObterArquivo/1812>

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**O TSS já está preparado para gerar a tag CodigoTributacaoMunicipio no xml do RPS de Salvador-BA.  
Basta informar o código de tributação (CTISS) conforme "TABELA DE CÓDIGOS DE TRIBUTAÇÃO DO IMPOSTO SOBRE SERVIÇOS DE QUALQUER NATUREZA – CTISS" no campo **C. Trib. Mun (B1\_TRIBMUN)**.

**Veja exemplo:**  
Código extraído da "TABELA DE CÓDIGOS DE TRIBUTAÇÃO DO IMPOSTO SOBRE SERVIÇOS DE QUALQUER NATUREZA – CTISS":

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001558382/mceclip0.png)**  
Preenchimento do campo **C. Trib. Mun (B1\_TRIBMUN)** no Protheus, **somente números**:

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001610741/mceclip2.png)**  
Geração da tag no **XML**:<CodigoTributacaoMunicipio>0801003</CodigoTributacaoMunicipio>
