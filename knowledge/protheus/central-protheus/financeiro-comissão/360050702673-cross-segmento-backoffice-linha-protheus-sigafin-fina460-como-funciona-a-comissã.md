---
article_id: 360050702673
category: Financeiro - Comissão
content_hash: 4ee9268121bbfbc330846c6c0cd4985aecae3bf5b516a54fb5f3c0fc729c55c2
fetched_at: '2026-06-28T22:37:50.857071+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA460 - Como funciona
  a comissão para títulos liquidados
type: support-article
updated_at: '2026-03-12T14:15:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050702673-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA460-Como-funciona-a-comiss%C3%A3o-para-t%C3%ADtulos-liquidados
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26670289851543)** Tempo aproximado para leitura: **00:05 min**

Dúvida  
Como funciona a comissão para títulos liquidados?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.

**Solução**

Quando se realiza a liquidação do título, a comissão não será gerada com base no título liquidado, mas sim com base no título "pai". No entanto, o comportamento para a geração da comissão pode ser configurado de duas formas distintas.

**1º Cenário**

**MV\_COMILIQ = 1** - O cálculo da comissão na liquidação do título a receber será feito **na liquidação do título original**.

**Exemplo**

Título no valor de R$ 5 mil, liquidado em 2x; ao concluir a liquidação, será gerada a comissão no valor total do título.

![Gravar_2024_07_10_14_13_20_607.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24794039208343)

**2º Cenário**

**MV\_COMILIQ = 2** - O cálculo da comissão na liquidação do título a receber será feito **na baixa dos títulos gerados pela liquidação**.

**Exemplo**

Título no valor de R$ 10 mil, liquidado em 2x. Ao realizar a baixa do título liquidado, é gerada a comissão apenas para o título baixado, ou seja, comissão com base no valor de R$ 5 mil. 

![Gravar_2024_07_10_14_05_16_864.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24794039210263)

**Importante**  
A comissão é gerada com base no título pai, e não no título gerado pela liquidação.  
![](https://totvssuporte.zendesk.com/attachments/token/TY6KLEBVwQrRMs2ZV58vWD4kh/?name=image.png)

**Saiba Mais**  
[Liquidação Receber - FINA460](https://tdn.totvs.com/pages/releaseview.action?pageId=545236275)

[Recalculo de comissão - FINA440](https://tdn.totvs.com/pages/releaseview.action?pageId=312162528)
