---
article_id: 360018760611
category: Call Center - Televendas
content_hash: 7c6ba50baad5fd515a9a43f47cd99e759479e6f9f8c1b0c6b115f1fc5d6b5275
fetched_at: '2026-06-28T22:41:30.335943+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK-Ocorrência do Help
  OUTROVEND na Exclusão de Pedidos SIGATMK
type: support-article
updated_at: '2022-06-22T19:13:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018760611-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Ocorr%C3%AAncia-do-Help-OUTROVEND-na-Exclus%C3%A3o-de-Pedidos-SIGATMK
---

**Dúvida**

Ao tentar excluir um pedido/orçamento na rotina TMKA150 aparece o Help OUTROVEND.  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK- a partir da versão 11.  
  
**Solução**Ocorrência do **Help OUTROVEND** ao tentar excluir um Pedido pela rotina **TMKA150** do módulo Call Center (SIGATMK):

![outrovend.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014224591/outrovend.png)

A rotina TMKA150 - Exclusão de Pedidos deve ser utilizada quando for cadastrada uma venda indevida ou quando for necessário eliminar um orçamento não concretizado.

A condição para execução da exclusão, é que o Operador seja igual ao Vendedor que incluiu a venda e agora está excluindo a mesma ou Operadores com configuração de Supervisor (**U7\_TIPO** - no Cadastro de Operador igual a Supervisor).

Caso contrário, o sistema não permitirá a exclusão e apresentará este Help.
