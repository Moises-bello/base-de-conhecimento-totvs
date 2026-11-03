---
article_id: 11723154476695
category: Faturamento - Integrações
content_hash: 1e6d95ce81924f7d76850dd4e20e826295ee6a288678ff708cff77641c6a38dd
fetched_at: '2026-06-28T22:38:26.651143+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Integração
  Neogrid: Falha na gravação! Cliente não encontrado'
type: support-article
updated_at: '2023-01-17T12:27:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11723154476695-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Integra%C3%A7%C3%A3o-Neogrid-Falha-na-grava%C3%A7%C3%A3o-Cliente-n%C3%A3o-encontrado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**

Ao tentar realizar a integração do Pedido de Vendas com TOTVS Colaboração (Neogrid EDI) o sistema apresenta a mensagem "Falha na gravação! Cliente não encontrado."

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Causa**

A mensagem ocorre caso o XML possua a TAG: **\_DELIVERYCUSTOMERGOVERNMENTALINFORMATION** preenchida e o cliente não exista na base (a chave é o CNPJ)

**Solução**Para solucionar essa ocorrência, verifique se a chave **\_DELIVERYCUSTOMERGOVERNMENTALINFORMATION** está preenchida, no XML do pedido, e avalie se o cliente (CNPJ), descrito na chave, existe em seu cadastro. Caso não exista, basta cadastrar o cliente para que a mensagem deixe de ser apresentada.

**Saiba mais**: [DI\_Integração\_TOTVS\_Colaboração\_2\_0\_EDI\_de\_Vendas](https://tdn.totvs.com/x/vwJdDg)
