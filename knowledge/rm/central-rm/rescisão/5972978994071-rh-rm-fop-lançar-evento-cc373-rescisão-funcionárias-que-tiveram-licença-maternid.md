---
article_id: 5972978994071
category: Rescisão
content_hash: 508a486cc3e92781bb44fa0537cb62cdbe780b4dae7c151c9cbaab97a17f5674
fetched_at: '2026-06-28T22:46:54.363133+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Lançar evento CC373 rescisão funcionárias que tiveram licença
  maternidade '
type: support-article
updated_at: '2025-02-27T18:11:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5972978994071-RH-RM-FOP-Lan%C3%A7ar-evento-CC373-rescis%C3%A3o-funcion%C3%A1rias-que-tiveram-licen%C3%A7a-maternidade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao realizar rescisão para funcionárias que tiveram licença maternidade durante o ano, o evento CC373 não estar sendo lançado.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Ocorre quando o evento CC373 possui a prioridade informada no cadastro do evento igual ou menor que a prioridade do evento CC48;  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5972824397335/mceclip0.png)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5972832110871/mceclip1.png)  
  
**Solução**  
**01**. Altere a prioridade do evento CC373 para maior que a prioridade do evento CC48;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5972858927383/mceclip2.png)

**Exemplo**A prioridade do evento CC48 e do evento CC373 é 0, altere a prioridade do evento CC373 para 1, assim o evento será lançado no envelope de pagamento.   
  
**Saiba Mais**

**[Código de Cálculo 373 – 13º Rescisão Licença Maternidade Provento](https://tdn.totvs.com/pages/releaseview.action?pageId=452719525)**
