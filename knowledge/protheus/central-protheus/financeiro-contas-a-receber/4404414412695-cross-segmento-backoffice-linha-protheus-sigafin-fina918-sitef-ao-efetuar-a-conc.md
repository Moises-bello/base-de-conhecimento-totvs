---
article_id: 4404414412695
category: Financeiro - Contas a Receber
content_hash: 8eab7b3df841191d943377f3e01b662f8f7f5e775567976c87200001cfb21231
fetched_at: '2026-06-28T22:38:13.800486+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN -FINA918 (SITEF) - Ao
  efetuar a conciliação de pagamento  alguns titulos estão caindo na aba conciliado
  parcialmente
type: support-article
updated_at: '2021-07-19T13:03:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404414412695-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA918-SITEF-Ao-efetuar-a-concilia%C3%A7%C3%A3o-de-pagamento-alguns-titulos-est%C3%A3o-caindo-na-aba-conciliado-parcialmente
---

**Ocorrência**Ao efetuar a conciliação de pagamento alguns títulos estão caindo na aba conciliado parcialmente  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12  
  
**Causa**Diferença de valor   
  
**Solução**Os títulos caem na aba parcialmente conciliados, porque a chave de localização não foi encontrada. inteira.  
  
Por exemplo: a chave de localização é:  
**NSUTEF + VALOR +DTPAGAMENTO+ DEBITO/CREDITO**É necessário bater os campos da chaves das tabelas SE1 e FIF, geralmente o valor de centavos faz cair na aba parcialmente. Aumentando a margem nos parâmetros  da rotina, ao efetuar a conciliação novamente verá que caíra na aba conciliados.  
  
Segue a documentação dentro dela explica a chave de conciliação.  
[MP- SIGAFIN - FINA916 - Não faz a conciliação de vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058597953-MP-SIGAFIN-FINA916-N%C3%A3o-faz-a-concilia%C3%A7%C3%A3o-de-vendas?source=search)
