---
content_hash: 1d97b50a96f56b57fb807fe6db4701cd6fa7b4d121b2bed1487c5f798f818e73
fetched_at: '2026-06-29T00:10:19.302071+00:00'
page_id: '4813226'
product: rm
source: tdn-rm
title: Os Campos de Valor do Material e Valor Sub Empreitada não são apresentados
  na movimentação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813226
version: 4
---

BLOCK

Os Campos de Valor do Material e Valor Sub Empreitada não são apresentados na movimentação

FAQ: **Os Campos de Valor do Material e Valor Sub Empreitada não são apresentados na movimentação**

|  |  |
| --- | --- |
| Produto: | Unspecified |
| Ambiente: | Unspecified |
| Versão: | 11.00 |

Sintoma

* **Sintoma**

Os campos “Valor do Material” e “Valor Sub Empreitada” não são apresentados na movimentação.

Causa

* **Causas**

1- Estes campos são apresentados apenas nas movimentações de saída 2.X.XX.

2- Os parâmetros '***Emite Livro Construção Civil***', ‘***Deduz Materiais***' e '***Deduz SubEmpreitada***' nos parâmetros da Regra de Apuração do ISS por filial do “TOTVS Gestão Fiscal” não estão marcados.

Solução

* **Solução**

1- O tipo de movimento utilizado deverá ser de saída 2.X.XX.

2- Nos parâmetros do “TOTVS Gestão Fiscal”, Apuração de Tributos / Regras de Apuração do ISS, Filial correspondente / etapa Construção Civil e Deduções, marcar os parâmetros '***Emite Livro Construção Civil***', ‘***Deduz Materiais***' e '***Deduz SubEmpreitada***'.

Observações

O documento em questão está postado no blog da Totvs e pode ser consultado através do link : <http://totvsconnect.blogspot.com/2010/10/dica-os-campos-de-valor-do-material-e.html>
