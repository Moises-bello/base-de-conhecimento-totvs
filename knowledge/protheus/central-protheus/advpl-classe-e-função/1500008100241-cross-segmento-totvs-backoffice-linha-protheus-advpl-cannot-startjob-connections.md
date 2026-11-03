---
article_id: 1500008100241
category: ADVPL - Classe e Função
content_hash: 19caa928f9ca2031278ffa1438a45d6c7a9261542f3af2efb1eed6413bc88b09
fetched_at: '2026-06-28T22:40:14.538084+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Cannot StartJob()
  - Connections Disabled
type: support-article
updated_at: '2022-11-17T17:57:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008100241-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Cannot-StartJob-Connections-Disabled
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Erro "***Cannot* StartJob() - *Connections Disabled***" apresentado ao executar a função **StartJob**() em uma rotina ou ponto de entrada.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL - Todas as versões  
  
**Causa**Este erro é gerado pois a capacidade de iniciar novas threads de seu **AppServer**em que o usuário chegou ao limite. Quando é iniciada um *Job* a partir de uma função em tempo de execução (**STARTJOB**) este *job*é iniciado no próprio **AppServer**/porta que a função chamadora esta alocada. Como o seu **AppServer**esta no limite de conexões/memoria é gerado o erro.

Todo *Job*executado a partir de uma função não entra nas regras do balance e são chamadas/executadas no mesmo serviço.  
  
**Solução**  
Para evitar este erro você precisará aumentar o número de **Slaves**do seu ambiente para evitar que com o acumulo de usuários os seus **Slaves**cheguem ao limite de conexões.

**Saiba mais**[Balanceamento de carga](https://tdn.totvs.com/display/tec/Balanceamento+de+carga)
