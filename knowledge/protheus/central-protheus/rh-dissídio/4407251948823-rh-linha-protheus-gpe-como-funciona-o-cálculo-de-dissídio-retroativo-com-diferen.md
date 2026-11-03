---
article_id: 4407251948823
category: RH - Dissídio
content_hash: d3ad9a30d203e862d9b4cb24e7df7c4a81f38b00cf2247b55ea2c8d1a32f7c72
fetched_at: '2026-06-28T22:43:43.304816+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona o cálculo de dissídio retroativo
  com Diferença de Férias
type: support-article
updated_at: '2025-10-20T12:15:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407251948823-RH-Linha-Protheus-GPE-Como-funciona-o-c%C3%A1lculo-de-diss%C3%ADdio-retroativo-com-Diferen%C3%A7a-de-F%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34314629722263) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**Como funciona o cálculo de dissídio retroativo com Diferença de Férias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para o cálculo do dissídio retroativo para períodos que tiveram cálculos de verbas de diferença de férias envolvidas, deve seguir as orientações de configuração de verbas de férias conforme explicado no manual do Dissídio Retroativo, disponibilizado no link abaixo:  
  
[RH - Linha Protheus - GPE - Manual dissídio retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034578653-RH-Linha-Protheus-GPE-Manual-diss%C3%ADdio-retroativo-?source=search)  
  
A única particularidade na configuração é que na versão 12 não são mais necessário configurar as verbas de Diferença de férias (como por exemplo os Ids 0088 – Diferença de Férias\*, 0089 – Diferença de Férias Mês Seguinte\*, 0090 – Diferença de 1/3 Férias\*, 0091 – Diferença de 1/3 Férias Mês Seguinte\*).

Sendo assim, configurando as próprias verbas de férias, no cálculo do dissidio retroativo o sistema somará as verbas de Diferença de Férias com as verbas de Férias efetivamente, trazendo no cálculo do dissídio retroativo a diferença a ser pago, em cima da verba de férias já com o valor somado.

Segue exemplo de cálculo:

\* Folha de pagamento da época 06/2021 - com verbas de de férias e diferença de férias envolvidas

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407251690391)

Cálculo do dissídio retroativo em 07/2021, considerando a folha 06/2021 para pagar a diferença

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407251753879)  
  
Memória de cálculo:

Verba 129 Férias = 500,00 + 100,00 = 600,00 (campo Valor Origem)  
1320,00 / 30 \* 15 = 660,00 (campo Valor Calculado)  
  
Verba 134 1/3 Férias = 166,67 + 33,33 = 200,00 (campo Valor Origem)  
660,00 / 3 = 220,00 (campo Valor Calculado)

Saiba Mais:  
[Página Centralizadora do Dissídio (GPEM690)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
