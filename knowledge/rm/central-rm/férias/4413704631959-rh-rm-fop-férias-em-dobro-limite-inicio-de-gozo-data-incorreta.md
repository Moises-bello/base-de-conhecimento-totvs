---
article_id: 4413704631959
category: Férias
content_hash: d9bfd9c4a9d36918c961917ffeea6b0ce36f28fcf67ebf5d5b02ea1645aa9dc3
fetched_at: '2026-06-28T22:46:56.342666+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias em dobro: Limite inicio de gozo data incorreta'
type: support-article
updated_at: '2025-01-22T18:11:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413704631959-RH-RM-FOP-F%C3%A9rias-em-dobro-Limite-inicio-de-gozo-data-incorreta
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29424531781911)** Tempo aproximado para leitura: **00:01:42 min  
  
Ocorrência**No módulo **Folha de pagamento**, ao tentar realizar o Cálculo de férias é apresentada uma mensagem informando que o funcionários tem direito ao pagamento de férias em dobro, porém ao calcular o recibo de férias, não é lançado eventos para pagamento férias em dobro do período aquisitivo atual.   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esse incidente ocorre, pois a parametrização do sistema está incorreta para a contagem do Limite inicio de gozo.  
  
![](https://atendimento.totvs.com/attachments/token/0RfWbSHXkmH4k8vkolgALzZG6/?name=image001.png)  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse: **Configurações | Parametrizador | Férias | Férias em Dobro** e desmarque a flag **Interrompe contagem do período para pagto de férias em dobro nos afastamentos I - L - M - P - T.****![](https://centraldeatendimento.totvs.com/hc/article_attachments/29424544512535)**  
  
Quando o funcionário está afastado por Licença Maternidade (tipo E), é interrompido o período de afastamento na contagem de período para pagamento de férias em dobro. Com este parâmetro marcado, será considerado este período na contagem do período para pagamento de férias em dobro.  
  
**Exemplo:**

* **Parâmetro desmarcado**  
  Período aquisitivo em aberto: 13/06/2015 a 12/06/2016  
  Limite para início de gozo: 14/05/2017  
  Funcionário afastado pelo tipo 'E' de 01/01/2017 a 30/04/2017  
  O Limite para início de gozo passa a ser 14/09/2017  
  Caso o funcionário inicie o gozo de férias 01/06/2017´, o sistema não irá calcular férias em dobro para o mesmo.
* **Parâmetro marcado**  
  Período aquisitivo em aberto: 13/06/2015 a 12/06/2016  
  Limite para início de gozo: 14/05/2017  
  Funcionário afastado pelo tipo 'E' de 01/01/2017 a 30/04/2017  
  O Limite para início de gozo passa a ser 14/05/2017  
  Caso o funcionário inicie o gozo de férias 01/06/2017´, o sistema irá calcular férias em dobro para o mesmo do período do dia 15/05 a 31/05.

**Saiba mais**[RH - RM - FOP - Férias em dobro: Parametrização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015821812-RH-RM-FOP-F%C3%A9rias-em-dobro-Parametriza%C3%A7%C3%A3o)
