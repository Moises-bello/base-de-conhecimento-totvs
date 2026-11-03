---
article_id: 25856730801943
category: Meu RH - Pagamento
content_hash: 1a0bc617934b09eb5e1b0d70e7a75df9593c6b8691b3ce7f2decafca2184487e
fetched_at: '2026-06-28T22:47:33.861696+00:00'
product: rm
section_id: 1500000835221
source: central-rm
title: RH - RM - Meu RH - Valor líquido do envelope de pagamento divergente ou duplicado
type: support-article
updated_at: '2025-03-06T14:30:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25856730801943-RH-RM-Meu-RH-Valor-l%C3%ADquido-do-envelope-de-pagamento-divergente-ou-duplicado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25856745345559) Tempo aproximado para leitura: **00:02:10 min****Ocorrência**Ao acessar o Meu RH e selecionar o envelope de pagamento, o sistema apresenta o valor líquido incorreto, conforme exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25861716552343)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25861740753431)  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**Esse incidente ocorre, pois a parametrização da tabela dinâmica **PDESCPER** está incorreta com duplicidade nos períodos cadastrados.  
  
**Solução**

Acesse a tabela dinâmica em **Folha de Pagamento** |**Administração de pessoal** > **Cadastros Globais** > **Tabelas Dinâmicas** e procure pela tabela **PDESCPER**. Cadastre todos períodos utilizados no envelope de pagamento com uma descrição fixa (Exemplo: Pagamento Mensal, Rescisão, etc...) e certifique-se que exista apenas um código para cada período evitando repetições nos períodos como por exemplo: Código 1 e 01, Código 2 e 02.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25949378874647)

Esse tipo de registro na tabela PDESCPER irá duplicar o valor do líquido, devendo existir apenas um código para cada período. Segue exemplo de como parametrizar corretamente a tabela dinâmica.

Períodos envelope de pagamento:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25861535479063)

Tabela PDESCPER:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25858427167383)

**Observação**: O valor Código da tabela PDESCPER deve ser correspondente ao numero do período do envelope de pagamento.

Após ajustar os cadastros, o valor líquido e a descrição dos períodos ficará correta no aplicativo Meu RH.
