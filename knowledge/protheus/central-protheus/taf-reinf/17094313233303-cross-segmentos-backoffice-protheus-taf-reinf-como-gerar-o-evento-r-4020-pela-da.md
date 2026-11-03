---
article_id: 17094313233303
category: TAF - REINF
content_hash: 1047f03f31e39b13210a814c3bf527b16e500644d69a3bfc30c8105b636f5c7d
fetched_at: '2026-06-28T22:41:33.666674+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como gerar o evento R-4020
  pela data de lançamento
type: support-article
updated_at: '2025-01-27T11:23:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17094313233303-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-gerar-o-evento-R-4020-pela-data-de-lan%C3%A7amento
---

**Dúvida** Como gerar no Painel REINF o evento R-4020 por data de lançamento do documento.    
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Automação Fiscal  - A parti da release 33  
  
**Solução**   Para geração do evento R-4020 pela data de lançamento é necessário que o titulo integrado no TAF ou lançado manualmente na rotina **TAFA448** esteja com campo **LEM\_DTEMIS**, preenchido com a data do lançamento do seu documento fiscal.

![LEM Data.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17094322114199)

  A rotina **TAFA552B**(Painel REINF), vai considerar como mês de competência da geração, à informação lançado no seu titulo.

Importante: Para ambientes aonde essa rotina é populada via integração é preciso que o seu ERP de origem integre os dados conforme descrito, para correta geração do seu evento.

Documentação adicional cliente Protheus(**Duvidas na geração do T154 contatar suporte financeiro**):

<https://tdn.totvs.com/display/public/PROT/DT+Extrator+Financeiro+para+o+TAF+-+REINF>

<https://tdn.totvs.com/pages/releaseview.action?pageId=737543501>
