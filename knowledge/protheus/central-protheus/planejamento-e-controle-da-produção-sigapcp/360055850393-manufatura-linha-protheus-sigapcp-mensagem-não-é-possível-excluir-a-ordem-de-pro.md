---
article_id: 360055850393
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 5582326c434be060cb3d73d5dac55d65eb734dfe9fae6bd9fc85d5365ffb1527
fetched_at: '2026-06-28T22:42:44.557486+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Mensagem: Não é possível excluir a
  Ordem de Produção. Existem Pedidos de Compras vinculados a Ordem de Produção: XXXXXXXXXX'
type: support-article
updated_at: '2024-06-19T18:13:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055850393-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-N%C3%A3o-%C3%A9-poss%C3%ADvel-excluir-a-Ordem-de-Produ%C3%A7%C3%A3o-Existem-Pedidos-de-Compras-vinculados-a-Ordem-de-Produ%C3%A7%C3%A3o-XXXXXXXXXX
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:40 min**  
**Ocorrência**No módulo **SIGAPCP - Planejamento e Controle da Produção**, ao tentar excluir uma **OP - Ordem de Produção** através do **MATA650 - Ordens de Produção** é apresentada a mensagem **Não é possível excluir a Ordem de Produção. Existem Pedidos de Compras vinculados a Ordem de Produção: XXXXXXXXXX**

![msg.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093058013/msg.png)

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Essa mensagem é apresentada quando tem um **Pedido de Compra** relacionado a **Ordem de Produção** ou uma **OP** relacionada a uma **SC - Solicitação de Compra** e esta está relacionada ao **Pedido de Compra**.  
  
**Solução**Para solucionar a situação é necessário excluir o **Pedido de Compra** que está impedindo a exclusão da **OP**.  
Para isso realize primeiro a verificação:

* Abra a tabela **SC7 - Pedido de Compra** via **APSDU** e verifique no campo **C7\_OP - Ordem de Produção** se existe a **OP** relacionada a algum pedido. Se tiver realize a exclusão do pedido.

Caso não seja encontrado nenhum **Pedido de Compra** relacionada a **OP** em questão realize a seguinte verificação

* Abra a tabela **SC1 - Solicitação de Compra**via **APSDU** e verifique se há algum **SC** relacionada a **OP**. Se tiver, pegue o número da **Solicitação de Compra** no campo **C1\_NUM - Numero da SC** e verifique se existe esse código no campo **C7\_NUMSC - Numero da SC** da tabela **SC7**. Se existir é necessário excluir esse **Pedido de Compra**.

**Importante**  
A exclusão do **Pedido de Compra** deve ser realizado através do Sistema padrão. O registro **não** deve ser excluído via **APSDU**.  
Caso tenha dúvidas de qual programa utilizar a para a exclusão do **Pedido** é necessário verificar junto com a equipe de **Compras**.
