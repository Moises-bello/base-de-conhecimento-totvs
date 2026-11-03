---
article_id: 4412981721495
category: SIGAEST - CUSTOS
content_hash: 3b90c79bfc009dbaa0f8a70488d5f345e5e28c74a959158b1bda2afe34280865
fetched_at: '2026-06-28T22:39:02.179147+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Jobs M330JPRCCONNECT
  e M330JOBSTART não estão sendo encerrados. Como corrigir?
type: support-article
updated_at: '2023-11-16T19:16:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412981721495-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Jobs-M330JPRCCONNECT-e-M330JOBSTART-n%C3%A3o-est%C3%A3o-sendo-encerrados-Como-corrigir
---

**Dúvida**Após a rotina de recalculo de custo, a rotina não encerra os JOBS, os mantendo presos na execução da instância em aberto do sistema Protheus. Como resolver este problema?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**O processo M330JOBSTART e M330JPRCCONNECT se tratam funções internas, normalmente são encerradas após execução da rotina MATA330 via Schedule ou de forma manual, utilizamos a função ManualJOB para simular WorkinThreads. Caso não seja finalizado, é necessário derrubar a sessão do usuário em questão, via Dbaccess.

É importante validar, que sua rotina MATA330 esteja atualizada com as últimas liberações, disponíveis no portal do cliente: **[Clique aqui para baixá-las](https://suporte.totvs.com/portal/p/10098/download)**

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*

[*Clique aqui e saiba mais sobre a função ManualJOB para simular WorkinThreads*](https://tdn.totvs.com/display/tec/ManualJob)
