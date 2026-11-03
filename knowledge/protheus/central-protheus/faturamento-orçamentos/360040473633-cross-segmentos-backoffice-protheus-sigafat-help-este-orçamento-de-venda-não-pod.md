---
article_id: 360040473633
category: Faturamento - Orçamentos
content_hash: 518f0158d0972a522aa80c817a396f99e7b9eea69673403c4e35b3cd0b73bfb4
fetched_at: '2026-06-28T22:38:24.963713+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Help "Este Orçamento de Venda
  não poderá ser alterado!"
type: support-article
updated_at: '2024-11-28T20:06:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040473633-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-Este-Or%C3%A7amento-de-Venda-n%C3%A3o-poder%C3%A1-ser-alterado
---

**Dúvida**

Ao alterar um Orçamento de Vendas, o sistema exibe a mensagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053010534)

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões.

**Solução**

A mensagem somente ocorre quando o campo CJ\_PROPOST está preenchido.  
  
O campo CJ\_PROPOST tem por finalidade de uso a validação de orçamento que nasce de uma Oportunidade de Venda com Proposta Comercial, neste caso, se o sistema encontra o campo preenchido, ele entende que existe esta integração e não permite a alteração do orçamento.  
  
A validação !FwIsInCallStack("AT600ORC") passou a ser efetuada no MATA415 de 06/08/2019 a partir da release 12.1.17 em diante, o tratamento foi adicionado para não permitir alteração de orçamento/proposta comercial onde foi adicionado exceções para as rotinas FATA300 e FATA600.  
  
O orçamento de venda não poderá ser alterado quando:

* 1 Se o campo "Status (CJ\_STATUS)" for A, D, E ou F
* 2 Se o campo "Num. Proposta (CJ\_PROPOST)" preenchido
* 3 Se a função "AT60ORC" não estiver na pilha de chamada
* 4 Se a API de tributos não for chamada corretamente quando usado API de tributos
