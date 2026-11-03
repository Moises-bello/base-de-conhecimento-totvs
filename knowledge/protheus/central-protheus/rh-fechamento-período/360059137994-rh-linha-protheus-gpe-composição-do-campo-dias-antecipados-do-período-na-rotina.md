---
article_id: 360059137994
category: RH - Fechamento Período
content_hash: cb586e1f7c51e049f0117628dc13a8e697d2fd66162c658de9d44f366e12ce8f
fetched_at: '2026-06-28T22:43:24.446518+00:00'
product: protheus
section_id: 360011909793
source: central-protheus
title: RH - Linha Protheus - GPE - Composição do campo Dias Antecipados do Período
  na rotina Controle Dias de Direito
type: support-article
updated_at: '2025-04-16T12:14:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059137994-RH-Linha-Protheus-GPE-Composi%C3%A7%C3%A3o-do-campo-Dias-Antecipados-do-Per%C3%ADodo-na-rotina-Controle-Dias-de-Direito
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24909859025943) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como é feita a composição do campo Dias Antecipados do Período (RF\_DIASANT) na rotina Controle Dias de Direito quando ocorre duas férias dentro do mesmo mês?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12  
  
**Solução**O conceito deste campo é abater os dias de Férias Antecipadas com o que foi antecipado nos cálculos.

**Exemplo:**

1º Período de Férias: Rotina Cálculo das férias (GPEM030) (cabeçalho das férias)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000770761)

Campo Dias Férias + Dias Ab. Pec - Dias Fer Venc  
15 + 0 - 5 = **10**

2º Período de Férias: Rotina Cálculo das férias (GPEM030) (cabeçalho das férias)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101841573)

Campo Dias Férias + Dias Ab. Pec - Dias Fer Venc

15 + 0 - 7,5 = **7,5**

Controle dos dias de direito após o fechamento da folha

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000771201)

10 + 7,5 = **17,5**

O campo D. Fer. Prop. (RF\_DFERAAT) congela em 7,5 pois ao final do mês da geração das férias o funcionário tinha direito a esta quantidade de dias de férias, como os dias já foram pagos essa informação não mudará conforme os fechamentos da folha.

**Saiba mais:**

[RH - Fechamento Período](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909793-RH-Fechamento-Per%C3%ADodo)
