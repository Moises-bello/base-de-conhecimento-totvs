---
article_id: 12074850441111
category: Folha Mensal
content_hash: ef890588d8ef2aa9fa345f2c2daf36f1c72a22e90ce507958ca2b5b133094227
fetched_at: '2026-06-28T22:46:58.277830+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Como estonar faltas lançadas em meses anteriores
type: support-article
updated_at: '2024-09-16T18:55:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12074850441111-RH-RM-FOP-Como-estonar-faltas-lan%C3%A7adas-em-meses-anteriores
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:36 min  
  
Dúvida**  
Como estornar faltas lançadas em meses anteriores e no mês para não contabilizar em férias e 13 salario?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**1.Utilizar dois eventos:  
  
Um para o pagamento no mês atual ( [2 - Dias Trabalhados](https://tdn.totvs.com/pages/viewpage.action?pageId=452718353) ou [1 - Horas Normais](https://tdn.totvs.com/pages/viewpage.action?pageId=452718302) )  e outro com [código de calculo 128.](https://tdn.totvs.com/pages/viewpage.action?pageId=452718655)  
  
O evento com [código de calculo 128.](https://tdn.totvs.com/pages/viewpage.action?pageId=452718655) precisa dos seguintes parâmetros:  
  
Evento do tipo Base de Cálculo com características que deverão ser iguais ao evento de Código de Cálculo [8 - Faltas](https://tdn.totvs.com/pages/viewpage.action?pageId=452718542). Este evento será utilizado para estornar faltas lançadas e descontadas em períodos anteriores que posteriormente foram justificadas pelo funcionário.  
  
Exemplo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12074636959767)  
  
2. Deverá inserir o evento de CC128 via ficha financeira no mês em que a falta ocorreu. Assim o estorno anula a falta daquele mês e o período aquisitivo de férias do funcionário não é prejudicado.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12074790287383)  
  
Neste caso, estas faltas não serão consideradas para o cálculo das férias e do 13º salário.
