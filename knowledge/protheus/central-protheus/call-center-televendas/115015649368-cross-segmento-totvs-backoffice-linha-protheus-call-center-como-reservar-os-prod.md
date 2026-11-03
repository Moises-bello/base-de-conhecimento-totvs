---
article_id: 115015649368
category: Call Center - Televendas
content_hash: b07c7757f204d36eb2157dbebd09f7a2084fd289660c3b0ac80ad9813e8fed51
fetched_at: '2026-06-28T22:41:30.176967+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Call Center -  Como reservar
  os produtos no atendimento Televendas
type: support-article
updated_at: '2021-09-22T14:59:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015649368-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Call-Center-Como-reservar-os-produtos-no-atendimento-Televendas
---

**Dúvida**  
Como reservar estoque no atendimento Televendas.  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Call Center - a partir da versões.  
  
**Solução**  
No atendimento Televendas do Call Center (TMKA273), não efetua-se reserva de produto.  
  
A reserva no estoque(B2\_RESERVA) é efetuada após o atendimento ter gerado o pedido de venda e a partir da liberação do pedido.  
  
Se deseja garantir o produto para a venda, deverá utilizar o cadastro de reservas do módulo faturamento (Mata430) e efetuar uma reserva manual do produto, para depois, através do campo C6\_RESERVA , vincular a reserva ao pedido, e posteriormente,  a mesma possa ser baixada no sistema.  
  
Caso o campo C6\_RESERVA não esteja disponível no browser, abra o dicionário de dados no módulo Configurador, edite a tabela SC6, deixando o campo C6\_RESERVA como usado e no browser.  
Salve a tabela, atualize o dicionário de dados e reinicie o Smartclient para que o sistema assuma as novas configurações.
