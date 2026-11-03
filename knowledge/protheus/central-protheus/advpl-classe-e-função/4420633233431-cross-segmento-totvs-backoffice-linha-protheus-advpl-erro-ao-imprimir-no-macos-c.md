---
article_id: 4420633233431
category: ADVPL - Classe e Função
content_hash: b929dea7bcb7a1a791fa74a9cd3385ada4c7bf60d324893891a84d6522e98380
fetched_at: '2026-06-28T22:40:15.800808+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro ao imprimir
  no MacOS com FWMsPrinter
type: support-article
updated_at: '2023-02-03T19:43:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420633233431-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-ao-imprimir-no-MacOS-com-FWMsPrinter
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Erro ao imprimir no MacOS com FWMsPrinter  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – ADVPL – A partir da versão 12.1.27  
  
**Solução**Para versões anteriores ao *MacOS Catalina* é possível imprimir normalmente, a partir do *MacOS Catalina* a *Apple* retirou o suporte a aplicativos 32-bits, para *MacOS* hoje possui somente o **printer** 32-bits.

Desta maneira para relatórios customizados utilizando a classe **FWMsPrinter**, será necessário gerar o pdf no server e não local pois o **printer** não é compatível e caso seja feito local ira gerar apenas o arquivo .rel.  
  
**Saiba Mais:**

[Totvs Printer](https://tdn.totvs.com/display/tec/Agente+TOTVS+Printer)

[FWMsPrinter](https://tdn.totvs.com/display/framework/FWMsPrinter)
