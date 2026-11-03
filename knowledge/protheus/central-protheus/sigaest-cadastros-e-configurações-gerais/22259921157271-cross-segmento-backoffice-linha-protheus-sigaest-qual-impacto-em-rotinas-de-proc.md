---
article_id: 22259921157271
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: dda13fafe73c4e00f6bbb91bed9879d60ef653234724dcdd96fec9bbacbb081b
fetched_at: '2026-06-28T22:39:09.733298+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Qual impacto em rotinas
  de processamento para produtos bloqueados MSBLQL?
type: support-article
updated_at: '2025-03-12T12:24:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22259921157271-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Qual-impacto-em-rotinas-de-processamento-para-produtos-bloqueados-MSBLQL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22259857980567) Tempo aproximado para leitura: **00:03:20 min** **Dúvida**Qual impacto em rotinas de processamento para produtos bloqueados MSBLQL?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Os campos MSBLQL não são campos exclusivos dos modulos e são campos reservados que podem ser inseridos em qualquer tabela, é um tratamento criado pelo framework que permite incluir no dicionario, em qualquer tabela, e tem o nome padronizado por exemplo D3\_MSBLQL. Ao incluir o nome do campo automaticamente as caracteristicas são preenchidas por terem tamanho, tipo e etc pre-determinados.(<https://tdn.totvs.com/display/public/framework/Campo+Reservado+_MSBLQD+e+_MSBLQL>)

No cadastro de produtos este campo é ativado por padrão e como descrito no link:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como bloquear um produto no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003255781-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-bloquear-um-produto-no-Protheus)

aparece na tela de cadastro do produto com o titulo "Blq. de tela" ou seja, se será bloqueado em telas.

Sua função como descrito nos links é bloquear, neste caso, o produto, em telas.

Portanto um produto bloqueado não poderá usado em qualquer tela, movimentação interna, transferencia, OP, pedido de venda, nota de entrada e etc, todas as telas em que pode ser informado o produto, pois automaticamente as telas fazem o bloqueio do framework com o assistente REGBLOQ.

Em Rotinas de processamento, onde não tem uma tela para informar o produto, este bloqueio não acontecerá por não existir uma tela.

***Saiba mais:***

[MP - SIGAEST - MATA010 - Erro ao excluir produto no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003255781-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-bloquear-um-produto-no-Protheus#:~:text=Saiba%20mais%3A,Gerais%20no%20Estoque)

[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003255781)
