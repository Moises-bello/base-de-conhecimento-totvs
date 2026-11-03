---
article_id: 360025370391
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: e74255c5af952ffed3dcf35a86a885b2cb67cf61d4a7db26ab5ce8f73d6493ea
fetched_at: '2026-06-28T22:39:58.506852+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - São Paulo:
  MunicipioPrestacao_This_element_is_not_expected'
type: support-article
updated_at: '2025-06-20T11:59:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025370391-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-S%C3%A3o-Paulo-MunicipioPrestacao-This-element-is-not-expected
---

**Dúvida**Schema inválido ao transmitir um RPS para prefeitura de São Paulo-SP:  
Element '{http://www.prefeitura.sp.gov.br/nfe}MunicipioPrestacao': This element is not expected.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**Esse erro ocorre porque a versão da nota está diferente de 2.00.  
Refaça o wizard. Config da rotina FISA022 e informe no campo Versão o conteúdo 2.00, em seguida retransmita e monitore a nota em questão.
