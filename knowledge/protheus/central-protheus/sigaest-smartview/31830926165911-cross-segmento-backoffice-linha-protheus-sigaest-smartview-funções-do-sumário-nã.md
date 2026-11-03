---
article_id: 31830926165911
category: SIGAEST - SMARTVIEW
content_hash: 4b5f569c7eee47c8692787f371707b67c5f5dad972e6d515bee6e3667420170b
fetched_at: '2026-06-28T22:38:47.164910+00:00'
product: protheus
section_id: 16108365627287
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - SMARTVIEW - Funções
  do sumário não são respeitadas
type: support-article
updated_at: '2026-03-06T19:21:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31830926165911-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-SMARTVIEW-Fun%C3%A7%C3%B5es-do-sum%C3%A1rio-n%C3%A3o-s%C3%A3o-respeitadas
---

Ao criar sumários em relatórios Smartview com funções como soma, média, contagem, mínimo e máximo, os cálculos podem não aparecer corretamente se não houver um agrupador por filial definido. Para resolver, é necessário arrastar a coluna "Filial" para o cabeçalho do relatório antes de criar o sumário, permitindo que as informações sejam apresentadas corretamente no rodapé.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31830911606551) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Por que ao criar um sumário em relatórios Smartview com as funções soma/média/contagem/mínimo/máximo não são calculadas/apresentadas devidamente?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.2310 ou Superior  
  
**Solução**

Este comportamento geralmente ocorre, quando o relatório não possui um agrupador por filial já definido. Como alguns relatórios do Smartview não foram desenvolvidos para ter agrupador, então há a necessidade de antes de criar o sumário, criar um agrupador pela coluna filial, conforme demonstrado abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31830926129431)

Para isso, basta arrastar a coluna "Filial" para o cabeçalho do relatório:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31830926130071)

Após isso, podemos criar o sumário com a função desejada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31830911619351)

E assim, a informação passsa a ser apresentada no rodapé:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31830926132887)

Saiba mais:

[Configuração do SmartView](https://tdn.totvs.com/x/8WTCMQ)

[Como configurar o Smart View?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22260770294551-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-configurar-o-Smart-View)
