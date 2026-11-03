---
article_id: 360015913171
category: Financeiro - Contas a Receber
content_hash: 24f1b5bf9aefb7ccf3d038efdc5e6e7df5e2850694a9507b484dd01a7b2ab0bf
fetched_at: '2026-06-28T22:38:15.079935+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN - FINA460 - Liquidação não traz títulos que contenham impostos
type: support-article
updated_at: '2021-04-28T15:17:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015913171-MP-SIGAFIN-FINA460-Liquida%C3%A7%C3%A3o-n%C3%A3o-traz-t%C3%ADtulos-que-contenham-impostos
---

**Dúvida**A rotina de liquidação a receber não traz títulos que contenham impostos em sua composição?   
   
 **Ambiente**Microsiga Protheus – Financeiro – A partir da versão 11.80  
  
  
**Solução**Os impostos da natureza do título origem devem estar contidos na natureza da liquidação para serem elegíveis à seleção de uma liquidação.  
A natureza escolhida no pergunta garante que não teremos títulos disponíveis para seleção que tenham mais impostos retidos na natureza anterior, gerando inconsistência na base de dados, **excluindo**as retenções antigas, com a nova natureza.  
Concluindo a natureza utilizada na liquidação, deve possuir os mesmos impostos do título a ser liquidado.
