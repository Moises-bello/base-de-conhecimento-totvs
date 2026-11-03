---
article_id: 39311943493143
category: Encargos
content_hash: c6c435fbe537adc0dd213793762cf6a69f405d7240390ec9b2b64dd0df172cbb
fetched_at: '2026-06-28T22:46:52.175366+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Lançamento Financeiro Crédito do Trabalhador - Fórmula para
  somar eventos por código de rúbrica 9253
type: support-article
updated_at: '2026-03-26T16:28:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39311943493143-RH-RM-FOP-Lan%C3%A7amento-Financeiro-Cr%C3%A9dito-do-Trabalhador-F%C3%B3rmula-para-somar-eventos-por-c%C3%B3digo-de-r%C3%BAbrica-9253
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39311948800535) Tempo aproximado para leitura: **00:01:38 min**  
  
**Ocorrência**  
Cliente apresentou dúvidas sobre como somar os eventos do envelope de pagamento utilizando o código da rubrica 9253, referente ao empréstimo Crédito do Trabalhador.

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
A causa do problema está na utilização da função MV, que exige ajuste manual da fórmula sempre que há inclusão de novos eventos  
  
**Solução**  
Como solução, recomenda-se a utilização de fórmula para customizar a geração dos Títulos de Lançamentos Financeiros, garantindo o retorno do valor do evento:

Segue abaixo um exemplo, utilizando a função `MVRUBRICA` com os parâmetros (MÊS, ANO, '9253'), sendo “9253” a natureza da rubrica no eSocial.  
  
![image-2025-11-12_10-28-4.png](https://tdn.totvs.com/download/attachments/963025822/image-2025-11-12_10-28-4.png?version=1&modificationDate=1762954084613&api=v2)  
 **Saiba mais:**

Para mais informações e dúvidas sobre o processo, acesse:

* [Lançamento Financeiro do empréstimo Crédito do Trabalhador via formula](https://tdn.totvs.com/pages/releaseview.action?pageId=963025822)
* [Fórmulas / Funções – M](https://tdn.totvs.com/pages/releaseview.action?pageId=452719272)
