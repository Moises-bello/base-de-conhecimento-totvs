---
article_id: 29090758176791
category: SIGAACD - Automação e Coleta de Dados
content_hash: fccf0f4e1ce00335c0a92d3cac8f707d23fa5a2b29ebab231324cb4094ed6819
fetched_at: '2026-06-28T22:39:11.234926+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDV035 - Lote Inválido
  ao inventariar pelo Coletor
type: support-article
updated_at: '2025-03-12T12:45:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29090758176791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDV035-Lote-Inv%C3%A1lido-ao-inventariar-pelo-Coletor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29090766834967) Tempo aproximado para leitura: **00:01:27 min** **Dúvida**Ao tentar inventariar um lote novo ou produto novo que não tem saldo no arquivo SB2, ocorre mensagem de Lote Inválido/Produto Inválido. O que fazer para resolver?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29090934148631)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões  
  
**Solução**A rotina de Inventário no Coletor (ACDV035) utiliza o mesmo F12 da rotina MATA270. E nela, há um pergunte crucial para isso. Se trata da pergunta "**Valida a Existência do Produto?**"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29090758165655)

Quando ela está = Não, o Sistema não valida se existe ou não SB2/SB8 do produto na base, e então ele permite lotes novos ou produtos que não tem SB2.

Porém, quando a pergunta está = Sim, ele passa a validar, e se for inserido um lote ou produto novo, ocorrerá a mensagem na tela do Coletor: **Lote Inválido** ou **Produto Inválido**

Mantendo a pergunta Valida Existência do Produto = Não, a mensagem não ocorrerá no coletor.

Saiba mais:

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
