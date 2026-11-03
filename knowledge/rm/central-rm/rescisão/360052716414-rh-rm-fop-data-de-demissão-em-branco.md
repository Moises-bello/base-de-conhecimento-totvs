---
article_id: 360052716414
category: Rescisão
content_hash: fb728e31c64155b6ed5b4b5cf14d14edaab7e4e89f4c7d7118b25ee4a606cb01
fetched_at: '2026-06-28T22:46:55.292595+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - Data de Demissão em branco
type: support-article
updated_at: '2025-01-21T17:58:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052716414-RH-RM-FOP-Data-de-Demiss%C3%A3o-em-branco
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao acessar a visão do funcionário, não está sendo apresentada a data de demissão dos funcionários demitidos na base.   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esse incidente ocorre pois foi alterada somente a situação do Funcionário para **D - Demitido** sem que fosse feita a rotina de Rescisão dentro do sistema.  
  
**Solução**A maneira correta para se fazer essa alteração é processando-a pelo caminho: **Administração de Pessoal | Funcionários | ícone de Rescisão.** Ao executar a mesma e salvar o cadastro, é registrada a Data de Demissão do Funcionário e alterada automaticamente sua situação para D.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087332593/mceclip2.png)  
  
A conferência pode ser realizada ao acessar a rotina, onde quem possui a demissão feita corretamente, terá os dados referentes à demissão preenchidos e quem possuir a demissão feita de maneira incorreta e manual, não terá nenhuma informação preenchida.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086144094/mceclip1.png)  
  
Há a possibilidade de fazer o registro dos dados da rescisão na rotina de Rescisão normalmente caso o colaborador tenha sido demitido de maneira incorreta, apenas situação alterada. No entanto, se for de interesse realizar os devidos cálculos, estes não poderão ser feitos pelo sistema. Sendo assim, não será possível pedir o cálculo da rescisão destes funcionários por se tratar geralmente de competência retroativa.
