---
article_id: 360057479693
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 6b4da56de37bedac643778499fc37c59060931943f7e92a0c3ae99b09cac541c
fetched_at: '2026-06-28T22:42:45.743899+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Procedimento alteração MV_PRECISA
type: support-article
updated_at: '2021-06-17T12:52:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057479693-Manufatura-Linha-Protheus-SIGAPCP-Procedimento-altera%C3%A7%C3%A3o-MV-PRECISA
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:58 min**  
**Dúvida**Qual o procedimento que deve ser realizado ao alterar o **MV\_PRECISA - Fator de divisão referente ao período mínimo dos Calendários (PCP)**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**  
Após a alteração do **MV\_PRECISA**, revise todos os calendários e exceções, as informações estarão distorcidas por conta da alteração do **MV\_PRECISA**, será necessário corrigi-las.  
  
Mas antes de recriar os calendários verifique se o **MV\_PRECISA** está com um valor válido:

|  |  |
| --- | --- |
| **Período Mínimo** | **MV\_PRECISA** |
| 1 minuto | 60 |
| 5 minutos | 12 |
| 10 minutos | 6 |
| 15 minutos - **padrão** | 4 |
| 30 minutos | 2 |
| 60 minutos | 1 |

**Importante**  
Recomendamos realizar os procedimentos primeiramente em ambiente de **teste**.
