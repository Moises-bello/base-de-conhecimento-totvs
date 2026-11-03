---
article_id: 360029068852
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 9cfc4da0405cd596a24d2b140fd22badad9ecac53413711f53a7bb62a16c2c42
fetched_at: '2026-06-28T22:42:45.847781+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Relacionamento do apontamento de horas
  improdutivas com a tabela SD3
type: support-article
updated_at: '2022-06-15T16:25:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029068852-Manufatura-Linha-Protheus-SIGAPCP-Relacionamento-do-apontamento-de-horas-improdutivas-com-a-tabela-SD3
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:56 min****Dúvida**Como a rotina **MATA682 - Apontamento de horas improdutivas** se relaciona com a tabela **SD3 - Movimentos Internos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**O apontamento registrado no **MATA682** pode resultar num registro de requisição na tabela **SD3** referente ao centro de custo vinculado ao recurso apontado. Para isso, o Sistema valida o conteúdo do parâmetro **MV\_MOTNMOD - Identifica quais motivos de parada não devem gerar requisição de MOD**, no qual devem ser cadastrados os motivos de parada que não devem gerar registro na tabela **SD3**.   
Sendo assim, somente os apontamentos de parada registrados com tipos não relacionados neste parâmetro resultam em registros na tabela **SD3**.
