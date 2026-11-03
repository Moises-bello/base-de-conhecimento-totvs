---
article_id: 19143957039895
category: RH - Folha de Pagamento
content_hash: 711f21bc73f24b60c48875035cf56a8f15339325ecace38a03e9ba801a87ee96
fetched_at: '2026-06-28T22:44:11.997291+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Barra de progresso na rotina GPEM020 - Cálculo
  por Roteiros  - Mnemônico P_LOGDEM
type: support-article
updated_at: '2024-09-05T17:57:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19143957039895-RH-Linha-Protheus-GPE-Barra-de-progresso-na-rotina-GPEM020-C%C3%A1lculo-por-Roteiros-Mnem%C3%B4nico-P-LOGDEM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19143964802071) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Barra de progresso na rotina GPEM020 - Cálculo por Roteiros - Mnemônico **P\_LOGDEM**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.  
  
**Solução**Ao efetuar o cálculo de roteiros de um processo que possua funcionários que serão descartados, seja porque estão demitidos ou porque serão admitidos apenas no próximo período, por exemplo. A barra de progresso nunca chega a 100%, pois não é incrementada para estes funcionários, causando a sensação de que algum funcionário possa não ter sido calculado indevidamente.

Efetuado ajuste para que a barra de progresso seja incrementada na situação citada e que, todos os funcionários que não tenham sido calculados sejam exibidos no log de processamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19143972707991)

Devido ao tamanho do log que, em algumas empresas, pode ficar demasiadamente grande devido a quantidade de funcionários demitidos, foi criado o mnemônico **P\_LOGDEM**, que indica se os funcionários demitidos devem ser exibidos no log de cálculo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19143935559447)  
O valor padrão do mnemônico é .F., indicando que os demitidos não serão exibidos no log, para que eles passem a ser exibidos o mnemônico deve ser alterado para .T

**Saiba Mais:**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[DT Cálculo por roteiros - Barra de progresso](https://tdn.totvs.com/pages/releaseview.action?pageId=738235302)
