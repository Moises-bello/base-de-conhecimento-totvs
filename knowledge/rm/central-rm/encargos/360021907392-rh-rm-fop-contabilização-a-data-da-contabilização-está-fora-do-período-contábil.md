---
article_id: 360021907392
category: Encargos
content_hash: efe4cdf82f4c856ac5f8cd92b9ee064cda45675b5736800851f1507f2c3a71d2
fetched_at: '2026-06-28T22:46:53.345590+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - Contabilização: A data da contabilização está fora do período
  contábil do Gestão Contábil'
type: support-article
updated_at: '2025-01-16T20:36:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021907392-RH-RM-FOP-Contabiliza%C3%A7%C3%A3o-A-data-da-contabiliza%C3%A7%C3%A3o-est%C3%A1-fora-do-per%C3%ADodo-cont%C3%A1bil-do-Gest%C3%A3o-Cont%C3%A1bil
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min  
  
Ocorrência**Em encargos, ao tentar realizar a geração dos lançamentos contábeis é apresentada a mensagem de erro: **A data da contabilização está fora do período contábil do Gestão Contábil**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esse incidente ocorre, pois a parametrização de data do **Período Contábil** está expirada, fazendo com que não tenha a data corrente para o lançamento contábil.  
 **Solução**Para solucionar essa ocorrência, realize os passos abaixo:  
  
1. Primeiro deverá alterar a **Data Final** do período contábil.  
  
2. Acesse **Backoffice | Gestão Contábil | Ambiente | Parâmetros | Lançamentos | Período Contábil**  
  
3. No campo **Data Final**, informe uma data válida posterior à da competência atual do sistema.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13585449376023)  
 **Importante**  
A data inicial do período não pode ser posterior ou igual a data de fechamento.
