---
article_id: 360000607668
category: Contabilidade Gerencial - Reprocessamento
content_hash: 97d0d8f3b82daffd55b34178d3e0b6a614a07786e3434488c356e46fbbf02e36
fetched_at: '2026-06-28T22:40:41.965119+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Configuração do parâmetro
  MV_TPVALOR
type: support-article
updated_at: '2022-05-23T16:55:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000607668-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Configura%C3%A7%C3%A3o-do-par%C3%A2metro-MV-TPVALOR
---

**Dúvida**No módulo **de contábil gerencial** como controlar a forma de **identificação** dos saldos a débito e a crédito nos relatórios?   
  
**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
**Solução**

O parâmetro [MV\_TPVALOR](https://tdn.totvs.com/pages/viewpage.action?pageId=146966519) controla a forma de identificar os saldos a serem impressos nos relatórios. Informe:

* D = Procedimentos Para imprimir os caracteres D (quando saldo Devedor) ou C (quando saldo Credor). Este tipo de identificação ignora a condição normal da conta.

* S = Procedimentos Para imprimir sinal negativo antes do valor quando o saldo da conta estiver contrário à condição normal da conta.

* P = Procedimentos Para imprimir parênteses quando o saldo da conta estiver contrário à condição normal da conta.

* C = Procedimentos Para imprimir somente C quando o saldo da conta for Credor, independente da condição normal da conta. Os valores devedores não terão nenhum identificador impresso.

* N = Procedimentos Para imprimir saldo com sinal(-) se o saldo for credor. Não considera a condição normal da conta.
