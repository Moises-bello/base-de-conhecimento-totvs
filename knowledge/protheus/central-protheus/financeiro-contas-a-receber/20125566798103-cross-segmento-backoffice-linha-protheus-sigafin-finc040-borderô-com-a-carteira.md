---
article_id: 20125566798103
category: Financeiro - Contas a Receber
content_hash: 194bf19fb64629b911c6cb71f8e1429f9c47cbc8e9eed682a7a2aeb1a4ac65f3
fetched_at: '2026-06-28T22:38:13.765851+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINC040 - Borderô com
  a carteira descontada sem realizar a baixa não é apresentado na posição de título.
type: support-article
updated_at: '2023-12-28T08:48:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20125566798103-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINC040-Border%C3%B4-com-a-carteira-descontada-sem-realizar-a-baixa-n%C3%A3o-%C3%A9-apresentado-na-posi%C3%A7%C3%A3o-de-t%C3%ADtulo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20125566769047) Tempo aproximado para leitura: **00:00:30 min****Dúvida**Ao realizar um borderô com a carteira descontada na posição do título não cria a linha de movimento.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINC040 - Todas as versões  
  
**Solução**

1. Em **Posição Título Rec.**, selecione o título e clique em **Consultar**.

São exibidos os dados do título selecionado.

Observe que o Titulo que foi transferido para uma cobrança descontada de forma individual através da rotina transferência (**FINA060**) não irá apresentar uma linha com o movimento. (Nesse exemplo há configuração do F12 para não baixar o título no momento da transferência)

Os movimentos oriundos da geração de borderô não geram esse tipo de visualização.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20125582632471)

Só irá apresentar o movimento no FINC040 após realizar a baixa do movimento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20125582634135)

Caso queria visualizar os movimentos pode usar a relatório FINR660 para ver os movimentos transferidos.

**Saiba mais:**

https://tdn.totvs.com/pages/releaseview.action?pageId=312158689
