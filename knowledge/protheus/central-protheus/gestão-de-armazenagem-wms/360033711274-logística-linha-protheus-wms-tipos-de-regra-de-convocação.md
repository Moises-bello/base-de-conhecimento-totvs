---
article_id: 360033711274
category: Gestão de Armazenagem (WMS)
content_hash: 126ab89bdd6da8b07e6a8bf84714efe7734c103f582a3faf785db217c3a492c8
fetched_at: '2026-06-28T22:45:48.178543+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Tipos de regra de convocação
type: support-article
updated_at: '2025-10-31T19:53:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033711274-Log%C3%ADstica-Linha-Protheus-WMS-Tipos-de-regra-de-convoca%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36023798903703)***Tempo aproximado para leitura:**00:01:18 min**  
**Dúvida**Quais são os tipos de regra de convocação?  
  
**Ambiente**TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (SIGAWMS) - A partir da versão 11.80.  
  
**Solução**No cadastro **Regra de Convocação - WMSA350** é possível optar pelos tipo regra: 1 - Limite e 2 - Sequencia. No entanto, cada qual tem sua particularidade:  
  
Limite: será aplicada somente na efetivação do serviço de **WMS - *Warehouse Management System***, ou seja, exclusivamente na convocação. Já passou pela execução do serviço e tem o objetivo de limitar a área de atuação dos operadores.  
  
Sequência: será usada exclusivamente na execução do serviço para direcionar o fluxo da operação por ordem crescente ou decrescente de endereços.  
  
**Importante**  
A regra de convocação complementa o parâmetro **MV\_WMSPRIO - Regra de prioridade de convocação.**Na tabela **D12 - Movimentos Serviços WMS** temos os campos **D12\_SEQPRI - Seq. Exec** e **D12\_PRIORI - Prioridade**, onde para este último:   
ZZ é a ordenação ou prioridade do documento no **Monitor de Serviço - WMSA332**, as próximas posições são preenchidas com as informações do parâmetro **MV\_WMSPRIO** e as duas últimas posições serão o tipo regra limite ou sequência.   
  
**Saiba mais**  
Assista ao *Webinar* sobre o cadastro **Regras de Convocação**: [Webinar TOTVS | Regras para a Convocação WMS](https://www.youtube.com/watch?v=TgvM8CA5LpA)
