---
article_id: 360027510912
category: Financeiro - Contas a Pagar
content_hash: 9904abaa05df69ca939ef87fad5f0c1236532336f9186cb89eb5b9ec08d24519
fetched_at: '2026-06-28T22:38:08.510270+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Error.log no parâmetroaFields:
  Field E2_FILIAL is not exist on FWTABLESTRUCT:ADDINDEX(FWTABLESTRUCT.PRX)'
type: support-article
updated_at: '2022-08-17T23:04:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027510912-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Error-log-no-par%C3%A2metroaFields-Field-E2-FILIAL-is-not-exist-on-FWTABLESTRUCT-ADDINDEX-FWTABLESTRUCT-PRX
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Error.log no parâmetroaFields: Field E2\_FILIAL is not exist on FWTABLESTRUCT:ADDINDEX(FWTABLESTRUCT.PRX)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**  
Este erro é apresentado devido a ordem do campo **E2\_FILIAL** não estar de acordo com o padrão.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse **Configurador** > **Base de Dados** > **Dicionário** > **Base de Dados** e valide se o campo não está com a ordem 01.  
2. Realizar alteração no **Configurador**, levando o campo para a ordem correta, que no padrão é a ordem 01.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027608971/mceclip0.png)

**Importante:**  
Este campo é reservado do sistema e não deve ter sua ordem alterada. O mesmo incidente pode ser apresentado no campo **E1\_FILIAL**, para movimentos a receber.
