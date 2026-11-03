---
article_id: 360049426554
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 3d86526d393675f06e85dd8e5c7b99d0d101c6bfded05d0e45faf200dcc5089b
fetched_at: '2026-06-28T22:38:45.125017+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT-O sistema está abrindo
  o lançamento contábil  na preparação da nota (MATA461) pelo pedido de venda(MATA410),
  mesmo informando no parâmetro para não contabilizar on line.
type: support-article
updated_at: '2022-09-30T20:22:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049426554-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-O-sistema-est%C3%A1-abrindo-o-lan%C3%A7amento-cont%C3%A1bil-na-prepara%C3%A7%C3%A3o-da-nota-MATA461-pelo-pedido-de-venda-MATA410-mesmo-informando-no-par%C3%A2metro-para-n%C3%A3o-contabilizar-on-line
---

**Dúvida**

O sistema está abrindo o lançamento contábil  na preparação da nota (**MATA461**) pelo pedido de venda(**MATA410**), mesmo informando no parâmetro para não contabilizar on line.  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT-  a partir da versão 11.

**Solução**

Nos parâmetros de preparação da nota, deixe a configuração das perguntas ***Mostra lanc. Contab***, ***Aglut. lançamentos***, ***Lanç Contab on-line*** e ***Contab. Custo On- line*** como **Não**, conforme a imagem abaixo:   
  
![](https://totvssuporte.zendesk.com/attachments/token/qkyBbDR8qnBo7udWUwUrO0cHj/?name=inline-1631536956.png)

Desta forma, não abrirá o lançamento padrão e não será contabilizado a nota on line.

O que pode gerar confusão é que  no browser do pedido, pode ser chamado o ***menu F12***, clicando na tecla **F12** do teclado, e neste menu também há a informação de ***Contabiliza on line***, ***Aglutina lan. Contábil*** e ***Mostra lançamento***, conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075238133/mceclip0.png)

Porém, o menu F12 do pedido, ***as pergunta de contabilização são para tratamento de contabilização do pedido de venda e não para a  geração da nota de saída***.

Para tratar a contabilização da nota de saída, a alteração do perguntes são nos parâmetros de preparação do documento de saída, após a seleção do número da nota fiscal, e neste parâmetros que devem ser configurados para não demonstrar o lançamento e não contabilizar on line.

![](https://totvssuporte.zendesk.com/attachments/token/mAyjEw4J1x0IdFU3ILGCPZGRm/?name=inline-573483338.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/9AqVQoY7G62HMX0fjpb8PBeUJ/?name=inline1566934414.png)​
