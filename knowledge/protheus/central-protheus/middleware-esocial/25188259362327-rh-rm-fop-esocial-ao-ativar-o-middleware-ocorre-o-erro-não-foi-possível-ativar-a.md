---
article_id: 25188259362327
category: MIDDLEWARE eSocial
content_hash: 6f0c00ae5484971784d54030ad002584e996880039d2ea62a0b420cb30734d79
fetched_at: '2026-06-28T22:43:05.096717+00:00'
product: protheus
section_id: 360005445753
source: central-protheus
title: 'RH - RM - FOP - eSocial - Ao ativar o Middleware ocorre o erro: Não foi possível
  ativar a integração com o Middleware pois existem eventos na fila pendentes de retorno
  do TAF (status 3 e 4)'
type: support-article
updated_at: '2024-07-26T13:47:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25188259362327-RH-RM-FOP-eSocial-Ao-ativar-o-Middleware-ocorre-o-erro-N%C3%A3o-foi-poss%C3%ADvel-ativar-a-integra%C3%A7%C3%A3o-com-o-Middleware-pois-existem-eventos-na-fila-pendentes-de-retorno-do-TAF-status-3-e-4
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25188243030423) Tempo aproximado para leitura: **00:02:30 min****Ocorrência**Ao ativar o Middleware ocorre o erro **Não foi possível ativar a integração com o Middleware pois existem eventos na fila pendentes de retorno do TAF (status 3 e 4). Antes da ativação do Middleware é necessário finalizar o envio dos mesmos através do TAF e atualizar o status na fila do RM.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25188259345687)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro ocorre pois uma das premissas para **[Ativação do Middleware](https://tdn.totvs.com/pages/releaseview.action?pageId=563428854#passos-914091633)** é não possuir eventos pendentes de atualizações, com status 3 e 4.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25188243034135)

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Identifique os eventos na fila de eventos, ou realize as consultas no banco de dados para identificar esses eventos:  
**Consulta 1 - FILA DE EVENTOS:** SELECT STATUS, \* FROM PESOCIALEVENTOS WHERE STATUS = 3 OR STATUS = 4  
**Consulta 2 - FILA DE EVENTOS COMPLEMENTAR:** SELECT STATUS, \* FROM PESOCIALEVENTOSCOMPL WHERE SATUS = 3 OR STATUS = 4  
2. Após identificar os eventos, será necessário realizar uma avaliação interna, **se os eventos devem ser transmitidos ou poderão ser** [**excluídos da fila**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017738251-RH-RM-FOP-eSocial-Exclus%C3%A3o-de-eventos-da-fila-independente-do-status);  
3. Após conferir todos os eventos, realize a ativação novamente.
