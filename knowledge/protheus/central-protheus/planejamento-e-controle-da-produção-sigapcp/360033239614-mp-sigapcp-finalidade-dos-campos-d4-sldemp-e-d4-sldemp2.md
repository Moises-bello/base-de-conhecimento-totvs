---
article_id: 360033239614
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 4fc003d38dcc62c04ea58b7c4eb592abd637f896f5e80e00a080ce44d0bd7fa0
fetched_at: '2026-06-28T22:42:47.210126+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'MP - SIGAPCP - Finalidade dos campos D4_SLDEMP  e D4_SLDEMP2 '
type: support-article
updated_at: '2024-06-28T18:13:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033239614-MP-SIGAPCP-Finalidade-dos-campos-D4-SLDEMP-e-D4-SLDEMP2
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:10 min**  
 **Dúvida**Qual o objetivo dos campos **D4\_SLDEMP - Saldo Qtde. Empenhada** e **D4\_SLDEMP2 - Saldo Qtde. Emp. 2a UM** na tabela **SD4 - Requisições Empenhadas?**  
   
 **Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
  
**Solução**Estes campos registram a quantidade empenhada e que não chegou a ser requisitada quando o usuário finalizou a **OP - Ordem de Produção.**   
A cada requisição de material realizada o campo **D4\_QUANT** **- Saldo da Qtd,. Empenhada**é atualizado com o saldo ainda a requisitar, quando a **OP**é encerrada esse valor é zerado e a quantidade remanescente, se existir, é transferida para o campo **D4\_SLDEMP,** já o campo **D4\_SLDEMP2** registra a quantidade na segunda unidade de medida do produto.  
O objetivo dessa movimentação é garantir que num eventual estorno do apontamento que encerrou a **OP** o campo **D4\_QUANT** volte a ter o valor correto, para isso será preenchido com o conteúdo do campo **D4\_SLDEMP** somado com a quantidade requisitada do material no apontamento estornado.
