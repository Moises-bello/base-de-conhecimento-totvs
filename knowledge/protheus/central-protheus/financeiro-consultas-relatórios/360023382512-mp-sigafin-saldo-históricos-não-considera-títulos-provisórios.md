---
article_id: 360023382512
category: Financeiro - Consultas / Relatórios
content_hash: be0f840e5f94b9d8a587168ccdb5d1a6d627ebda5798c6db780cef5131c4e4a0
fetched_at: '2026-06-28T22:37:58.393488+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: MP - SIGAFIN - Saldo históricos não considera títulos provisórios
type: support-article
updated_at: '2021-04-28T15:19:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023382512-MP-SIGAFIN-Saldo-hist%C3%B3ricos-n%C3%A3o-considera-t%C3%ADtulos-provis%C3%B3rios
---

**Ocorrência**  
 No módulo Financeiro, ao emitir a Consulta Posição de Clientes (FINC010), em Saldos históricos, os títulos provisórios não são considerados mesmo que na pergunta "Considera provisórios" esteja sim.  
   
 **Ambiente**Microsiga Protheus – Financeiro – A partir da versão 11.80  
   
 **Causa**   
O Saldo Histórico exibido em tela considera o valor definido no campo A1\_SALDUP e este campo absorve somente valores de títulos efetivos. Tanto é que, ao executar a rotina Refaz Dados Clientes e Fornecedores, os títulos provisórios não são considerados para refazer o cálculo. A opção Considera provisórios definido nos parâmetros da rotina terá efeito somente ao selecionar a opção "Tit. Aberto".
