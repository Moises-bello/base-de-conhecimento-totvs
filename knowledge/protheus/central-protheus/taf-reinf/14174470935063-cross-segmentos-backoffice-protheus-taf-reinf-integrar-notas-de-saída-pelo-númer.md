---
article_id: 14174470935063
category: TAF - REINF
content_hash: 2df6470a8670c94ebe8c856302a65e2b6a0d2dc66141adf80e9486122e1cd85a
fetched_at: '2026-06-28T22:41:34.696038+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Integrar Notas de Saída
  pelo número do documento ao invés do número do RPS.
type: support-article
updated_at: '2023-12-01T16:51:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14174470935063-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Integrar-Notas-de-Sa%C3%ADda-pelo-n%C3%BAmero-do-documento-ao-inv%C3%A9s-do-n%C3%BAmero-do-RPS
---

**Dúvida**Notas fiscais de saída não integram no TAF, mesmo estando escrituradas corretamente.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Linha Protheus - TOTVS Automação Fiscal - Todas as versões

**Solução**

 Ao integrar notas fiscais de saída do tipo RPS que foram transmitidas, está sendo levado para o TAF o número do RPS ao invés do número da nota fiscal.

Informe no parâmetro **MV\_ESPNFEL** a espécie das notas.

O extrator fiscal irá varrer o parâmetro **MV\_ESPNFEL** (preencher com | quando houver mais espécies) e irá comparar se o **FT\_ESPECIE** está preenchido com a mesma informação do parâmetro para considerar o campo **FT\_NFELETR,** ao invés do campo FT\_NFISCAL.

Observação: O TSI já efetua esse processo de forma automática, se o Extrator Fiscal não possuir a mesma configuração e for executado em conjunto com o TSI, poderá ocorrer duplicidade de documentos no TAF (1 com número de RPS e o outro com o número da prefeitura).

Documentação complementar: <https://tdn.totvs.com/pages/releaseview.action?pageId=423932342>
