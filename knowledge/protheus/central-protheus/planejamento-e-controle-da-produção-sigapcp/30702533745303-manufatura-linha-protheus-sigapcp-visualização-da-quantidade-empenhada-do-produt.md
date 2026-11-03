---
article_id: 30702533745303
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: bf58243c94e512bf9895a8de03b21392ac50ceb6ef033966574b45c2e5eb6572
fetched_at: '2026-06-28T22:42:47.144190+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Visualização da quantidade empenhada
  do produto
type: support-article
updated_at: '2025-03-18T11:23:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30702533745303-Manufatura-Linha-Protheus-SIGAPCP-Visualiza%C3%A7%C3%A3o-da-quantidade-empenhada-do-produto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30702533728279) Tempo aproximado para leitura: **00:00:52 min** **Dúvida**Como rastrear a quantidade empenhada do produto nas **OPs - Ordens de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para rastrear a quantidade empenhada do produto é necessário acessar a rotina de**Empenhos múltiplos - MATA381** filtrando pelo produto e  definindo a quantidade como maior que zero, **D4\_QUANT  > 0** . Assim é possível identificar quais as ordens de produção estão empenhadas para o produto.  
  
O campo **D4\_QUANT - Saldo da Quantidade Empenhada** indica o saldo empenhado no momento. Esse valor, é um dos que compõem a quantidade empenhada que é apresentada ao acessar o **Cadastro do produto - MATA010**  ao pressionar a tecla **F4**.
