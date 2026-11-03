---
article_id: 360034301974
category: Financeiro - Contas a Receber
content_hash: cd4f26b31ee1c3e03bd7f74fdc131831073bd6d2b82e76f6e877ed855a9148d0
fetched_at: '2026-06-28T22:38:15.091720+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN - FINR190 - Como não demonstrar as baixas feitas por Liquidação
  a Receber e a Pagar
type: support-article
updated_at: '2021-04-28T15:17:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034301974-MP-SIGAFIN-FINR190-Como-n%C3%A3o-demonstrar-as-baixas-feitas-por-Liquida%C3%A7%C3%A3o-a-Receber-e-a-Pagar
---

**Dúvida**Como não imprimir as liquidações a receber e a pagar?  
  
 **Ambiente**Microsiga Protheus - Financeiro - FINR190 - A partir da versão 11.80  
  
**Causa**Esse incidente ocorre, pois a parametrização do motivo de baixa está permitindo movimentar a tabela **SE5**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1-Acesse a rotina **FINA490** encontre o motivo de baixa que está sendo utilizando para baixar o título.  
2-Clique no botão **Editar**, altere a coluna **Mov.Bancaria** para conter o conteúdo **N** no campo do motivo de baixa para não demostrar no relatório **FINR190**.
