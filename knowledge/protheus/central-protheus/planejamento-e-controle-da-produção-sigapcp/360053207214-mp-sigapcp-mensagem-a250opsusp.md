---
article_id: 360053207214
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 8c1936de8af8f58bad03cc685a09387df9eb4060b712f304a030f8db63cb59c1
fetched_at: '2026-06-28T22:42:47.242864+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: MP - SIGAPCP - Mensagem A250OPSUSP
type: support-article
updated_at: '2023-10-30T20:11:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053207214-MP-SIGAPCP-Mensagem-A250OPSUSP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:46 min**  
**Ocorrência**Ao tentar realizar o apontamento de produção no módulo do **PCP - Planejamento e Controle da Produção** é apresentada a mensagem **A250OPSUSP**.  
  
**Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
  
**Causa**O campo **C2\_STATUS - Situação** da **OP - Ordem de Produção** está igual a **U - Suspensa** e o parâmetro **MV\_OPSUSP - Valida OP Suspensa no apontamento da Producao?** está igual a **.T.**.  
  
 **Solução**Para conseguir realizar o apontamento é necessário:

* Alterar o campo **C2\_STATUS** da **OP** através do **MATA650 - Ordens de Produção** para **N - Normal**;
* Ou alterar o parâmetro **MV\_OPSUSP** para **.F.**.
