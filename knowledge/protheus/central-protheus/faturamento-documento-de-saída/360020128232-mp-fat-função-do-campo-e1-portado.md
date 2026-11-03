---
article_id: 360020128232
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 8e310d72e60c36cea5427f9aade9f23ccf600f2b66fa98679c1bd337d2ac2f57
fetched_at: '2026-06-28T22:38:45.172744+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: 'MP - FAT - Função do Campo E1_PORTADO '
type: support-article
updated_at: '2021-04-28T15:13:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020128232-MP-FAT-Fun%C3%A7%C3%A3o-do-Campo-E1-PORTADO
---

**Dúvida**

Função do Campo E1\_PORTADO .  
  
**Ambiente**

Microsiga Protheus –  A partir da versão 11.80.  
  
**Solução**

Ao incluir no cadastro de cliente o campo **A1\_BCO1** ele preenche no pedido de venda o campo **C5\_BANCO**porem, ao faturar esse pedido a informação não esta sendo levada para a tabela SE1 em nenhum campo. Ele deveria levar para o campo **E1\_PORTADO**?

Este campo **E1\_PORTADO**é preenchido com o código que o título foi enviado via borderô ou transferência de carteira, então ele é preenchido quando o título tiver em borderô lançado, ou for transferido para outra carteira.

Rotina **FINA060**Rotina de transferência onde consegue colocar o título em borderô e ou transferir pra outra carteira.
