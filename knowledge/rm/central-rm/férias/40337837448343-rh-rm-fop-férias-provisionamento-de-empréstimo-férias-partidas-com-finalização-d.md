---
article_id: 40337837448343
category: Férias
content_hash: d23b31ecbcf7adf02b8cef773692de228bce5434f91e6938a2d3ee6303cc05ca
fetched_at: '2026-06-28T22:46:56.105169+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias - Provisionamento de Empréstimo: Férias Partidas com
  Finalização da Parcela na Competência Atual'
type: support-article
updated_at: '2026-05-08T19:46:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40337837448343-RH-RM-FOP-F%C3%A9rias-Provisionamento-de-Empr%C3%A9stimo-F%C3%A9rias-Partidas-com-Finaliza%C3%A7%C3%A3o-da-Parcela-na-Compet%C3%AAncia-Atual
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40337837437079) Tempo aproximado para leitura: 00:02:45 min

**Dúvida**  
No módulo de Folha de Pagamento, ao calcular o recibo de férias de um colaborador com provisionamento Crédito do Trabalhador, o sistema não lança a provisão do segundo mês quando o empréstimo é finalizado na competência atual.

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

12.1.2406.277  
12.1.2410.229  
12.1.2502.145  
12.1.2506 e superiores

**Causa**  
Esse incidente ocorre, pois o sistema considera que, como o empréstimo é finalizado dentro da competência atual, não é necessário lançar o evento de provisão para o segundo mês. Os dias restantes do empréstimo são contabilizados no mês atual ao processar a folha.

**Solução**  
Para entender o correto funcionamento do sistema e a lógica por trás do lançamento, considere os seguintes pontos:  
  
Para melhor entendimento segue exemplo abaixo:

1. Veja que o empréstimo do colaborador está considerado como encerrado em 03/2026, e a competência atual do sistema também é 03/2026.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40337802670103)
2. Dessa forma, apenas o evento de provisão referente ao primeiro mês (12 dias) é lançado o evento de Código de Cálculo 485.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40337802670743)
3. Os 8 dias das férias restante da competência são compensados no mesmo mês por meio do evento de Código de Cálculo 480.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40337837438743)
4. Por fim, o evento de Código de Cálculo 480 é lançado, registrando o valor integral do desconto da parcela do Crédito do Trabalhador. Assim, o desconto total é realizado no mês atual, sem a necessidade do evento de provisão para o segundo mês, uma vez que o empréstimo não está mais ativo para próxima competência.
