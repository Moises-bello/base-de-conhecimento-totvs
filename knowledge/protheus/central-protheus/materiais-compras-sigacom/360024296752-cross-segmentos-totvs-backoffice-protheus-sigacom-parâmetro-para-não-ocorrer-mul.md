---
article_id: 360024296752
category: Materiais - Compras (SIGACOM)
content_hash: 4bd79dacb43f87f05c3ab0d142482a6a9031804b9db05182bb932707b98be949
fetched_at: '2026-06-28T22:41:10.147513+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Parâmetro para não
  ocorrer “MultLock” no cadastro de fornecedores nas transações financeiras
type: support-article
updated_at: '2022-05-13T11:44:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024296752-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Par%C3%A2metro-para-n%C3%A3o-ocorrer-MultLock-no-cadastro-de-fornecedores-nas-transa%C3%A7%C3%B5es-financeiras
---

**Dúvida**Parâmetro para não ocorrer “MultLock” no cadastro de fornecedores nas transações financeiras

**Ambiente**Protheus – Compras – A partir da versão  P11.80  
  
  
**Solução**

Qual parâmetro para habilitar/desabilitar a atualização do cadastro do fornecedor nas transações financeiras?

Em ambientes com alto volume de movimentações para uma gama pequena de fornecedores, poderá ocorrer situações em que uma rotina reserva o registro do fornecedor na tabela SA2 para realizar a atualização, e quando uma segunda rotina tenta reservar o mesmo registro dispara o alerta de “MultLock”.

Este tipo de situação pode ocorrer no sistema e se trata de uma característica, levando em consideração que a atualização dos dados na tabela SA2 ocorre de maneira on-line.

Esta alteração visa atenuar as situações de concorrência entre processos que atualizam a tabela SA2.

Segue as opções de configuração para o parâmetro **MV\_ATUFORN:**

**Conteúdo .T.**  
O cadastro do fornecedor será atualizado ao realizar movimentações financeiras (default)

**Conteúdo .F.**  
O cadastro do fornecedor deixará de ser atualizado ao realizar uma movimentação financeira

**Observação:**Caso o parâmetro não existir, será realizada a atualização do cadastro do fornecedor normalmente.

A chamada do ponto de entrada MT103TRV foi descontinuado na função A050DupPag (FINXFIN.PRX) e substituído pelo tratamento através desse parâmetro, já que teriam o mesmo propósito.

**Saiba mais:   
<http://tdn.totvs.com/display/PROT/MV_ATUFORN>**
