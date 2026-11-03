---
article_id: 39716693394967
category: Férias
content_hash: f705973a22252b4de7971b17ff22df4fc39fc2e174d1a810180ac737ea0435d5
fetched_at: '2026-06-28T22:46:56.127013+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias: Como realizar lançamento das férias em período diferente
  da folha?'
type: support-article
updated_at: '2026-04-13T20:29:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39716693394967-RH-RM-FOP-F%C3%A9rias-Como-realizar-lan%C3%A7amento-das-f%C3%A9rias-em-per%C3%ADodo-diferente-da-folha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39716717462935) Tempo aproximado para leitura: **00:02:08 min**  
  
**Dúvida**  
Como realizar o lançamento de envelope em períodos distintos no módulo de Folha de Pagamento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**  
Caso os lançamentos de férias e da folha mensal tenham sido realizados no mesmo período e seja necessário separá-los para que as férias fiquem em um período posterior, deve-se realizar o cancelamento do lançamento atual e reprocessar a rotina após a alteração do período de cálculo.

* Observa-se que no envelope de exemplo, foram realizados os lançamentos de férias e folha mensal no mesmo período, no período 1.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39716717463447)

Caso desejar que esses lançamentos sejam divididos em períodos diferentes, é necessário realizar o cancelamento das férias lançadas, para que posteriormente ela seja reprocessada em um período posterior. Segue passo a passo:

1. Cancelar as férias lançadas, conforme documentação:

   [RH - RM - FOP - Férias: cancelamento de férias lançadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003145371-RH-RM-FOP-F%C3%A9rias-cancelamento-de-f%C3%A9rias-lan%C3%A7adas)
2. Após isso, cancelar o movimento de férias no envelope, conforme documentação:

   [RH - RM - FOP - Cancelamento do Movimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057701274-RH-RM-FOP-Cancelamento-do-Movimento)

   ⚠️ Observação: Ao cancelar movimento, é necessário marcar a flag de cancelar movimento de férias:   
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39716693374487)

   ⚠️ Na próxima tela, é necessário selecionar todos os eventos de férias a serem cancelados do envelope:

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39716693376279)
3. Depois, é necessário realizar a alteração de período para um período posterior ao utilizado para o lançamento anterior, no exemplo será utilizado o período 3.

   Para isso, acesse **Configurações | Locais** conforme a imagem abaixo: 

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39716717468311)
4. Após a alteração do parâmetro, acesse a rotina padrão de férias e realize o novo lançamento.

   [RH - RM - FOP - Férias: Lançamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007913092-RH-RM-FOP-F%C3%A9rias-Lan%C3%A7amento)
