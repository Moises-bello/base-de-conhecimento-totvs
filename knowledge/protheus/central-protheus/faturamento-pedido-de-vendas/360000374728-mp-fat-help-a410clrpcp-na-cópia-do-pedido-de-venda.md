---
article_id: 360000374728
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 2ffb19f6aab57355e9f7edc3cd6a80bb2edd3b552df4bea3c1169c865f3f935c
fetched_at: '2026-06-28T22:38:41.274480+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP-FAT- Help A410CLRPCP na cópia do Pedido de Venda
type: support-article
updated_at: '2021-04-28T15:51:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000374728-MP-FAT-Help-A410CLRPCP-na-c%C3%B3pia-do-Pedido-de-Venda
---

**Ocorrência**

Ao clicar para copiar um pedido de venda, obtemos a mensagem em anexo.

**Help:A410CLRPCP**

![](https://totvssuporte.zendesk.com/attachments/token/xOWkFIMfkJjWfiC4YeKcShtna/?name=inline755383414.png)

**Ambiente**Microsiga Protheus -  a partir da versão 12.1.17.  
   
 **Causa**

A falta de função (NOFUNCW), indica que o fonte onde a função foi criada deve estar desatualizado.  
   
 **Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
 1. Baixe o pacote mais atual da rotina **matv410a,  conforme ambiente:**

12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=813322> ; 12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=813321> ; 12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=813320> ;

2. Aplique o pacote, via TDS, em seu ambiente de testes para validação e posteriormente, no ambiente de prodição.

**Obs:  A aplicação do pacote deve ser efetuado por um analista que detenha o conhecimento técnico para o procedimento, caso tenha dúvidas de procedimento, entre em contato com a equipe de FrameWork para auxiliá-lo.**
