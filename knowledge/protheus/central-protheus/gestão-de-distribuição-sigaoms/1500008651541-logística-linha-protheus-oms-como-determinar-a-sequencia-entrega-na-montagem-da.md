---
article_id: 1500008651541
category: Gestão de Distribuição (SIGAOMS)
content_hash: 83cfaa9c2d7df81dde3396bb8232cc0434715b013eeebcd36d488dfa339c30c1
fetched_at: '2026-06-28T22:45:49.662325+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Como determinar a sequencia entrega na Montagem
  da Carga
type: support-article
updated_at: '2021-07-14T00:22:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008651541-Log%C3%ADstica-Linha-Protheus-OMS-Como-determinar-a-sequencia-entrega-na-Montagem-da-Carga
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:00:54 min**  
**Dúvida**Como determinar a **sequencia entrega** na **Montagem da Carga - OMSA200**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Na **criação da carga** ou na **manutenção da carga** é possível **alterar a sequencia de entrega dos pedidos**.  
  
Essa ação poderá ser acionada das seguintes formas:

* **Atualizações/Cargas/Montagem de Carga/Carregamento/Montagem de Carga**, após selecionar os pedidos da carga, acessar o **botão Outras Ações/Seq. Ent**
* **Atualizações/Cargas/Montagem de Carga/Carregamento/Manutenção/botão Outras Ações/Seq. Ent**

Para que o Sistema grave a ordem de sequencia de entrega alterada pelo usuário, será validado o preenchimento do parâmetro **MV\_SEQENT**, que **deverá estar igual a 1.**O parâmetro possui as configurações abaixo:  
  
**1=Sequencia.**  
Será ordenado pelos campos : **PED\_SEQROT, PED\_ROTA, PED\_FILORI, PED\_PEDIDO, SC9.C9\_ITEM**  
  
**2=Rota/Sequencia.**  
Será ordenado pelos campos : **PED\_ROTA, PED\_SEQROT, PED\_FILORI, PED\_PEDIDO, SC9.C9\_ITEM**
