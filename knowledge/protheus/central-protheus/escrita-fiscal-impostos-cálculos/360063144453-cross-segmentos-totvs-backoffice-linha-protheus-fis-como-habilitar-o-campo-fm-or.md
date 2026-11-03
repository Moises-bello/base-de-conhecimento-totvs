---
article_id: 360063144453
category: Escrita Fiscal - Impostos - Cálculos
content_hash: e23ffc3a26cef22130b191f657faaf23d1dcbaa77227e966c5d2ee52caa03c6b
fetched_at: '2026-06-28T22:39:30.679400+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como habilitar o campo
  FM_ORIGEM?
type: support-article
updated_at: '2021-07-29T13:01:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063144453-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-habilitar-o-campo-FM-ORIGEM
---

**Dúvida:**

Como habilitar o campo FM\_ORIGEM para tratativa do enquadramento da TES inteligente através da origem do produto, quando se tem controle de Lote/Sublote  
  
**Ambiente:**

Microsiga Protheus - A partir  da versão 12.  
  
**Solução:**

O campo **FM\_ORIGEM** ("Origem do produto") no cadastro de TES Inteligente só será habilitado quando o parâmetro **MV\_A410OPE = .T.**  Este por sua vez servirá especificamente para atender ao cenário de utilização de lotes com controle de origem e do preenchimento automático de tipos de operação no pedido de venda habilitados. Essa tratativa depende da habilitação do parâmetro **MV\_ORILOTE** e sua devida configuração.

Informações adicionais:

[TES Inteligente - MATA089 - Fiscal - P12](https://tdn.totvs.com/display/PROT/TES+Inteligente+-+MATA089+-+Fiscal+-+P12)

[DSERFAT-10688 DT Considerar a Origem do Lote/SubLote do Produto dos Documentos de Entrada](https://tdn.totvs.com/x/ddu5HQ)

<https://tdn.totvs.com/pages/releaseview.action?pageId=527855853>
