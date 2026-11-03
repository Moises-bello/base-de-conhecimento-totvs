---
article_id: 360020379512
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 3fc8169af615bf1dc924167a22846cb51549e480532ce2b36363b3c936932f9e
fetched_at: '2026-06-28T22:42:01.123528+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - C170 - Valor negativo no campo 8-VL_DESC
type: support-article
updated_at: '2025-02-11T20:56:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020379512-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-C170-Valor-negativo-no-campo-8-VL-DESC
---

**Ocorrência**Campo 8- VL\_DESC do registro registro C170 está sendo gerado com valor negativo.

**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80.   
   
 **Causa**Esta situação está sendo apresentada pelo fato do valor lançado no campo **FT\_DESCONT** possuir valor menor do que o valor lançado no campo **FT\_DESCZFR**, e quando o programa **SPEDFISCAL** realiza a subtração destes valores o resultado é o valor negativo.

**Solução**Será necessário avaliar a escrituração do documento fiscal, pois não é permitido que o valor do desconto seja maior que o desconto da Zona Franca **FT\_DESCZFR**.
