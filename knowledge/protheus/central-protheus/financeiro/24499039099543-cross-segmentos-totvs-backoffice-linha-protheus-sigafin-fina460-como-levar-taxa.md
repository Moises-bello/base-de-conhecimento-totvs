---
article_id: 24499039099543
category: Financeiro
content_hash: 0480d3c275d8f94f924d6abf12d203644a16919b26bc97d49229e22f931b7629
fetched_at: '2026-06-28T22:38:04.181283+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - SIGAFIN - FINA460 - como
  levar taxa de juros pré-definida de um título para uma liquidação
type: support-article
updated_at: '2026-03-02T20:35:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24499039099543-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA460-como-levar-taxa-de-juros-pr%C3%A9-definida-de-um-t%C3%ADtulo-para-uma-liquida%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24499039087383) Tempo aproximado para leitura: **05:00 min**  
  
**Dúvida**  
Como transferir a taxa de juros pré-definida de um título para o processo de liquidação?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.

**Solução**  
A taxa de juros pré-definida de um título é levada para a liquidação quando informada no campo **E1\_PORCJUR**.

**Exemplo:** Título cadastrado no contas a receber com uma taxa de juros de 0,20% e multa de 0,20%.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38751741922199)

**Processo de liquidação, exemplo:**

Na liquidação, a taxa de **0,20** foi importada, sendo calculados **juros no valor de R$ 1.180,00** e **multa de R$ 20,00**. Esses valores serão incorporados ao título negociado. Caso o título não seja quitado dentro do prazo, o sistema realizará o recálculo de juros e multa considerando a **data de vencimento do título liquidado**.

Caso seja necessário atualizar as taxas de juros, o ajuste deverá ser realizado **no grid da tela de liquidação**, para que a nova condição seja aplicada ao título futuro. Nesse cenário, será considerada a nova taxa informada no campo **Tx. Jur. Ger. = 0,85**.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24498985559447)](https://centraldeatendimento.totvs.com/hc/article_attachments/24498985559447)

Títuloliquidado.o

O título negociado com o juros aplicado.[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24499039089431)](https://centraldeatendimento.totvs.com/hc/article_attachments/24499039089431)

No título liquidado foi importada a nova taxa de juros 0,85 para o campo **Porc.Juros**.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24498985560471)](https://centraldeatendimento.totvs.com/hc/article_attachments/24498985560471)

**Saiba mais**  
[**Juros e Multa na Liquidação**](https://tdn.totvs.com/pages/releaseview.action?pageId=545236275)
