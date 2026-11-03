---
article_id: 7071214718615
category: Financeiro - Contas a Receber
content_hash: c82d685353bcf544b0b48af4882c1eee582b8700b9c5977d1f1a215910a4b390
fetched_at: '2026-06-28T22:38:14.114554+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - HELP EXCHEQUE
type: support-article
updated_at: '2023-01-25T22:06:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7071214718615-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-HELP-EXCHEQUE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:02 min**  
  
**Ocorrência**  
No módulo Financeiro, ao tentar realizar o cancelamento da baixa do cheque pela rotina cheques recebidos (FINA191) é apresentada o HELP: EXCHEQUE

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7070891451543/mceclip0.png)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**  
É apresentado este Help, pois deve realizar o cancelamento da baixa do cheque primeiramente pela rotina **FINA740** ou **FINA040** para depois realizar o cancelamento na rotina **FINA191**.  
  
Solução  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o módulo **Financeiro**, **Atualizações**, **Funções Contas a Receber**:  
2. Selecionar o título que teve baixa total ou parcial com cheque  
3. Clica em outras **ações**, selecionar **baixas**, **Canc Baixa**, como o exemplo abaixo:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7071170562071/mceclip3.png)

       Caso tenha ocorrido várias baixas será exibido a tela abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7071017155607/mceclip2.png)

Observação: Quando houver mais de uma baixa o cancelamento dos títulos deve ser do último baixado ao primeiro   
4. Depois cancelar o cheque na rotina de **cheque recebidos FINA191**.
