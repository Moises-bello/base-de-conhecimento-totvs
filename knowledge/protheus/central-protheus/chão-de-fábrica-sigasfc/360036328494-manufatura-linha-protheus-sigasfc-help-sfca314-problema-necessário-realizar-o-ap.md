---
article_id: 360036328494
category: Chão de Fábrica (SIGASFC)
content_hash: 2de8b7b684e74ea9ae1dcd030467cef0937725d061391baf7ebf3960c1eed82e
fetched_at: '2026-06-28T22:42:49.855225+00:00'
product: protheus
section_id: 360005696234
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGASFC - Help: SFCA314 Problema: Necessário
  realizar o apontamento da operação anterior'
type: support-article
updated_at: '2025-06-05T20:01:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036328494-Manufatura-Linha-Protheus-SIGASFC-Help-SFCA314-Problema-Necess%C3%A1rio-realizar-o-apontamento-da-opera%C3%A7%C3%A3o-anterior
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:00 min****Ocorrência**Ao tentar encerrar um apontamento de uma operação iniciado no **SFCA310 - Apontamento de Produção Modelo I** é apresentada a mensagem **Help: SFCA314 Problema: Necessário realizar o apontamento da operação anterior**, mesmo que a operação anterior já tenha sido encerrada.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048374153/mceclip0.png)

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Chão de Fábrica (SIGASFC) - Versão 12  
  
**Causa** Essa mensagem é apresentada quando a **Data de Início - CYV\_DTRPBG** do reporte das operações seguintes, ou seja, operação 02 não pode ser menor que o campo **Data Fim - CYV\_DTRPED** do reporte da operação anterior, ou seja, da operação 01.  
Se as datas forem iguais, o Sistema irá validar o campo de **tempo/hora,** ou seja, a **Hora Início - CYV\_HRRPBG** da operação que está tentando encerrar deve ser maior que a **Hora Fim - CYV\_HRRPED** da operação anterior.**Solução**Estornar o apontamento da operação anterior para ajustar a **data/hora**, para que seja possível realizar o apontamento da operação seguinte. Ou ajustar a **data/hora** da operação que está tentando encerrar.
