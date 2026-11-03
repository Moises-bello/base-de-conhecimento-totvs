---
article_id: 24504352369303
category: Financeiro - Movimentação Bancária
content_hash: 98ad17b4e1f496788f708bb8b94294b1371b472b495270bd11e73cf8b36d186c
fetched_at: '2026-06-28T22:38:19.506901+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA380 - Pontos de
  entrada da rotina Conciliação Manual
type: support-article
updated_at: '2024-06-28T21:00:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24504352369303-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA380-Pontos-de-entrada-da-rotina-Concilia%C3%A7%C3%A3o-Manual
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24504368995479) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Quais são os pontos de entrada disponíveis para a rotina FINA380?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

|  |  |  |
| --- | --- | --- |
| **Pontos** **d****e Entrada** | **Observações** | **Link** |
| F380BUT | Inclui botão de usuário | <https://tdn.totvs.com/pages/releaseview.action?pageId=656636092> |
| F380BTCUST | Inclui botão customizado | <https://tdn.totvs.com/pages/releaseview.action?pageId=669607632> |
| F380ALDT | Define se é permitida ou não a alteração da data de disponibilidade | <https://tdn.totvs.com/pages/releaseview.action?pageId=641462024> |
| F380CPOS | Ponto de Entrada responsável por ordenar campos no browse de Conciliação Bancária. | <https://tdn.totvs.com/pages/releaseview.action?pageId=568923443> |
| F380DTC | Validação da data de digitação | <https://tdn.totvs.com/pages/releaseview.action?pageId=641462980> |
| F380DTD | Define se é permitida conciliação bancária com data de crédito anterior à data de inclusão no sistema | <https://tdn.totvs.com/pages/releaseview.action?pageId=641463739> |
| F380ATR | Ponto de entrada para manipular/gravar dados complementares antes do carregamento dos registro para conciliação | <https://tdn.totvs.com/pages/viewpage.action?pageId=805983225> |
| F380MTR | Ponto de Entrada manipula dados após checagem da conciliação bancária | <https://tdn.totvs.com/pages/viewpage.action?pageId=805981533> |
| F380FIL | Complemento de filtro do usuário na seleção de registros para conciliação bancária. | <https://tdn.totvs.com/pages/releaseview.action?pageId=546265001> |
| FA380CHV | Ordena dados | <https://tdn.totvs.com/display/public/PROT/FA380CHV+-+Ordena+dados> |

**Saiba mais**[Conciliadores Bancários Manual e Automático (FINA380 e FINA473)](https://tdn.totvs.com/pages/releaseview.action?pageId=754946735)
