---
article_id: 7235560259991
category: Comércio Exterior - Easy Export Control - Financeiro
content_hash: 09d37eb8e45b3d147e61dc27da5ee69737f1215d2cc91a2ce051debd7cc49a74
fetched_at: '2026-06-28T22:36:58.170986+00:00'
product: protheus
section_id: 1500001538221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Como limpar a
  data do campo Solic. Cambio (EEQ_SOL), ao fazer o estorno da liquidação e do recebimento
  no exterior?
type: support-article
updated_at: '2022-07-05T12:22:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7235560259991-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Como-limpar-a-data-do-campo-Solic-Cambio-EEQ-SOL-ao-fazer-o-estorno-da-liquida%C3%A7%C3%A3o-e-do-recebimento-no-exterior
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como limpar a data do campo **Solic. Cambio (EEQ\_SOL)**, ao fazer o estorno da liquidação e do recebimento no exterior?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Export Control - Todas as versões.  
  
**Solução**Ao estornar a liquidação e a movimentação no exterior, o sistema por padrão não apaga automaticamente a data do campo **Solic. Cambio (EEQ\_SOL)**.  Para o processo, trata-se de momentos distintos - em algum momento da operação é solicitada a negociação do câmbio, em outro é realizada a liquidação. Ainda que para o cliente este momento seja o mesmo, não o podemos considerar padrão para o produto, neste caso deve ser tratado via ponto de entrada pelo painel de câmbio ([<https://tdn.totvs.com/pages/releaseview.action?pageId=419546074>)], ou pela rotina de controle de câmbio ([<https://tdn.totvs.com/pages/releaseview.action?pageId=266980321>)] para que se possa adequar o sistema às necessidades reportadas.
