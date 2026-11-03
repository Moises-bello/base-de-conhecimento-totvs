---
article_id: 360015821812
category: Férias
content_hash: afc367ce7026fba8e2d75f42cd7c313d431510e16fe750bfa123d4fc8d0fdb01
fetched_at: '2026-06-28T22:46:56.469687+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias em dobro: parametrização'
type: support-article
updated_at: '2025-01-20T21:47:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015821812-RH-RM-FOP-F%C3%A9rias-em-dobro-parametriza%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:44 min  
  
Ocorrência** No módulo **Folha de pagamento**, ao tentar realizar o cálculo de férias é apresentada uma mensagem informando que o funcionários tem direito ao pagamento de férias em dobro, porém ao calcular o recibo de férias, é lançado somente o valor referente às férias proporcionais do período aquisitivo atual. Isso acontece, pois a parametrização das férias em dobro não foram realizadas no sistema. Veja a solução abaixo.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**   
Esse incidente ocorre devido à ausência da parametrização para o pagamento de férias em dobro no lançamento do recibo de férias.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse a aba **Administração de pessoal | Eventos | Eventos** e faça o cadastro dos eventos com os códigos de cálculo abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5117530772887/mceclip0.png)  
  
[Código de Cálculo 309 - Férias em Dobro](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452718557)  
[Código de Cálculo 310 - Adicional 1/3 de Férias em Dobro](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719770)  
[Código de Cálculo 311 - Abono de Férias em Dobro](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719256)  
[Código de Cálculo 312 - Adicional 1/3 de Abono de Férias em Dobro](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719754)  
  
2. Acesse a aba **Configurações | Parametrizador | Férias | Férias em dobro.**  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5117540628375/mceclip1.png)  
  
3. Habilite o parâmetro **Paga férias em dobro.**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5103403667991/mceclip1.png)  
  
**Saiba mais**[Férias em Dobro](https://tdn.totvs.com/pages/releaseview.action?pageId=452719558)
