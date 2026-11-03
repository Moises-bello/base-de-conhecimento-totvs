---
article_id: 4410791461271
category: SIGAEST - MOVIMENTAÇÕES
content_hash: cac53bbd5c94b8ae63036cb69aab6bca87b201964aba48aadad6c9e4de0aab32
fetched_at: '2026-06-28T22:38:55.484777+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Em quais cenários
  o Protheus obriga a inserção do Lote em Movimentos Internos?
type: support-article
updated_at: '2024-09-05T13:16:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410791461271-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Em-quais-cen%C3%A1rios-o-Protheus-obriga-a-inser%C3%A7%C3%A3o-do-Lote-em-Movimentos-Internos
---

**Dúvida**Em alguns casos, ao inserir Movimentação Interna o Sistema obriga a inserção do Lote. Em quais casos é obrigatório inserir o Lote/Sublote?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Ao efetuar Movimentos Internos e de Produção no Protheus, um detalhe muito importante a ser avaliado é o Tipo do Movimento (T.M), pois, dependendo de qual seja o tipo selecionado, o comportamento para obrigar ou não a inserção do lote mudará.

**Tipos de Movimentos que não permitem serem salvos sem a inserção do Lote:**

- Requisição.

**Tipos de Movimentos que permitem serem salvos sem a inserção do Lote:**

- Produção;

- Devolução.

**Por que ocorre este comportamento?**

Basicamente, um Tipo de Movimento de Requisição gerará uma saída de Estoque. Por este motivo, uma premissa é que já exista um saldo em lotes no Sistema e o mesmo irá solicitar para gerar a saída do Lote escolhido pelo usuário. Por este motivo não é possível salvar o movimento de requisição sem informar o Lote quando o produto tem este controle (B1\_RASTRO = L ou S).

Já em movimentos de Produção e Devolução, geram saldo em Lote. Se o usuário porventura esquecer de selecionar um lote existente, o Sistema cria um lote automático (preenchendo conforme o parâmetro MV\_PRXLOTE). Portanto, é um comportamento padrão que dá dinamismo na interação do usuário com o Protheus. Este mesmo comportamento ocorre no Documento de Entrada (MATA103), onde, se o usuário não preencher Lote, o Protheus irá criar um lote novo automaticamente.

**Saiba mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como informar o lote ao realizar o Apontamento de Produção?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010091382-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-informar-o-lote-ao-realizar-o-Apontamento-de-Produ%C3%A7%C3%A3o-)*

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
