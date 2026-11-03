---
article_id: 360021503832
category: Financeiro - Contas a Receber
content_hash: 5db898260537b24289f0ee03670149cc57011a24f8a2cf8dd785bc295e329b4b
fetched_at: '2026-06-28T22:38:15.112548+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'MP -SIGAFIN - Quando campo A1_RECIRRF em branco não gerar o  financeiro '
type: support-article
updated_at: '2023-11-08T17:28:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021503832-MP-SIGAFIN-Quando-campo-A1-RECIRRF-em-branco-n%C3%A3o-gerar-o-financeiro
---

**Dúvida**

Campo A1\_RECIRRF em branco não gerar financeiro ?

**Ambiente**Microsiga Protheus – Financeiro – A partir da versão 12.1

**Solução**Na versão 11 com o campo A1\_RECIRRF em Branco gera um abatimento no financeiro, ao preparar um documento de saída, ou lançamento no financeiro.  
Feito Correção para versão 12 para não gerar o titulo de abatimento quando o campo A1\_RECIRRF estiver em branco.

Foi feito um ajuste na versão 12, pela inovação do Financeiro onde foi identificado em casos de uso um erro no sistema.  
  
Para correção do erro foi criado uma variável que valida se o campo está como "0" pra reter.  Se estiver diferente, despreza. Como em branco estava alimentado um valor para o IRRF, corrigido o caso, após criar a variável lCalcIrf

A correção não afeta o sistema configurado da forma correta, seguindo a documentação

**CLIENTE**

Recolhe IRRF **(A1\_RECIRRF) = SIM**

Sendo assim, na versão 12 é necessário utilizar as configurações corretas conforme link

[Retenção IRRF](http://tdn.totvs.com/pages/viewpage.action?pageId=47908805)
