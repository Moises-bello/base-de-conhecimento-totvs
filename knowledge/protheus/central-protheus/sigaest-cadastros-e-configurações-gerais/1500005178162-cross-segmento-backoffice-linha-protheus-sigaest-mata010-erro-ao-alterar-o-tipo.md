---
article_id: 1500005178162
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: b054172f88433e1c9119490c700e5ba67c0412cc1cf04884ce4fe8ab69ec7025
fetched_at: '2026-06-28T22:39:09.481197+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - Erro ao
  alterar o tipo de controle de Rastreabilidade de Lote para Sub-lote
type: support-article
updated_at: '2025-03-12T12:27:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005178162-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Erro-ao-alterar-o-tipo-de-controle-de-Rastreabilidade-de-Lote-para-Sub-lote
---

**Dúvida**Ao alterar, via MATA010 - Cadastro de Produtos, o tipo de controle de Rastro (B1\_RASTRO) de Lote para Sublote ocorre o erro "Tipo de Rastreabilidade - Não pode ser alterado. Ja ocorreram movimentos deste produto após o ultimo fechamento". Como corrigir para conseguir alterar?  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006904922)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos- Todas as versões  
  
**Solução**

Para alterar o controle de Lote para Sublote, é importante entender que primeiramente o saldo do produto nos lotes devem ser previamente zerados (SB2 e SB8).

Para que consiga alterar, o Protheus solicita que não haja nenhum movimento (mesmo que seja Inventário) para o produto após o último fechamento.

Se houve qualquer que seja o movimento, deve-se fazer um novo Fechamento de Estoque, para em seguida, conseguir alterar o controle de Lote para Sub-lote.Desta forma não ocorre a mensagem de erro.

**Saiba mais:**

*[MP - SIGAEST - Como alterar o tipo de controle de rastreabilidade de Lote para Sub-lote?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005086241)*

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033382-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
