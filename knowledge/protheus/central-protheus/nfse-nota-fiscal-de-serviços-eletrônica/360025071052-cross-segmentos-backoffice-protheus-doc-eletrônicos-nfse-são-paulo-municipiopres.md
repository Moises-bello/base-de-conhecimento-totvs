---
article_id: 360025071052
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: bc7fd71847426ac1e048346dca4f1ecbe746a54243b433c7ad85a9ca3db39eb4
fetched_at: '2026-06-28T22:39:58.509181+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - São Paulo:
  MunicipioPrestacao_This_element_is_not_expected'
type: support-article
updated_at: '2025-07-18T13:48:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025071052-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-S%C3%A3o-Paulo-MunicipioPrestacao-This-element-is-not-expected
---

**Dúvida**

Schema inválido ao transmitir um RPS para prefeitura de São Paulo-SP:

Element '{http://www.prefeitura.sp.gov.br/nfe}MunicipioPrestacao': This element is not expected.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

Esse erro ocorre porque a versão da nota está diferente de 2.00.

Refaça o wizard. Config da rotina FISA022 e informe no campo Versão o conteúdo 2.00, em seguida retransmita e monitore a nota em questão.
