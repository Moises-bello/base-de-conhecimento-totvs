---
article_id: 360017786551
category: Ativo Fixo - Relatórios
content_hash: 2af845b0a7d46f21332d5c14a9c71b46259e81d990b3b63726d6c523b6709280
fetched_at: '2026-06-28T22:41:46.711345+00:00'
product: protheus
section_id: 1500001536301
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus  - SIGGAATF : ATFR130 - Razão Auxiliar'
type: support-article
updated_at: '2022-09-16T14:46:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017786551-Cross-Segmento-Backoffice-Linha-Protheus-SIGGAATF-ATFR130-Raz%C3%A3o-Auxiliar
---

**Dúvida**

Quais as opções de configuração do parâmetro MV\_ATFNAT.

**Ambiente**Protheus – Ativo Fixo – A partir da versão 11.80  
  
  
**Solução**

O parâmetro possui duas opções de configuração:

'P' = valor padrão e recomendável para os relatórios do tipo 'movimentação', esta configuração permite que o relatório efetue os cálculos dos valores de acordo com as movimentações realizadas nos bens.

'C' = esta configuração desconsidera os tipos de movimentação ocorridos nos bens, e passa a considerar apenas a natureza da conta, considerando:

* Contas com natureza devedora: Exibe valores positivos.
* Contas com natureza credora: Exibe valores negativos.

**Para maiores detalhes consulte:**

[Relatório Razão do Imobilizado o ATFR130 -- 116626](http://tdn.totvs.com/pages/viewpage.action?pageId=6067636)

[ATF0014 - Tipos de movimentos N4\_OCORR](http://tdn.totvs.com/display/PROT/ATF0014+-+Tipos+de+movimentos+N4_OCORR)
