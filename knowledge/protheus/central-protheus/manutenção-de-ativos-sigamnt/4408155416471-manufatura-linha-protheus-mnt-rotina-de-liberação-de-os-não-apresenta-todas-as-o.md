---
article_id: 4408155416471
category: Manutenção de Ativos (SIGAMNT)
content_hash: 1d7b25f31d13dbc95025ab667e53a69f5b40d5215328d94f01807bb63012b260
fetched_at: '2026-06-28T22:42:34.420760+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Rotina de Liberação de OS não apresenta
  todas as Ordens de Serviço
type: support-article
updated_at: '2021-09-09T19:13:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408155416471-Manufatura-Linha-Protheus-MNT-Rotina-de-Libera%C3%A7%C3%A3o-de-OS-n%C3%A3o-apresenta-todas-as-Ordens-de-Servi%C3%A7o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:00:50 min****Ocorrência**No módulo **Manutenção de Ativos - SIGAMNT**, ao tentar realizar a visualização das **Ordens de Serviço - O.S's** pendentes na rotina **Liberação de O.S - MNTA490** não são apresentadas **O.S's** com *status* de término igual a **N - Não** e **Situação** igual a **P - Pendente**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Causa**As **Ordens de Serviços Preventivas** com plano diferente **000001** não são apresentadas na rotina **MNTA490**  
  
**Solução**Na rotina **Liberação de O.S - MNTA490** são apresentadas as seguintes ordens de serviço:

* **Corretivas**
* **Preventivas** com plano  **000001**, ou seja, apenas as ordens geradas de forma manual.

**Importante**As ordens de serviço pendentes geradas pelo plano de manutenção devem ser liberadas pela rotina **Confirmação de Plano - MNTA340**.
