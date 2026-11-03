---
article_id: 4413305496343
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 93885635fed43afe8abd1188e17b352cc3ecad4524f12baf2a0cf07389e1449d
fetched_at: '2026-06-28T22:38:57.284424+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Posso utilizar caracteres
  especiais em saldos por lote e endereço?
type: support-article
updated_at: '2021-11-19T11:30:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413305496343-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Posso-utilizar-caracteres-especiais-em-saldos-por-lote-e-endere%C3%A7o
---

**Dúvida**Quais os impactos de se utilizar caracteres especiais em saldos por lote na identificação do Lote do produto?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque Custos - Todas as versões  
  
**Solução**Ao incluir um saldo inicial ou movimentação o Protheus permite inclusão de caracteres especiais. Os campos **do tipo caractere** do Protheus aceitam qualquer conteúdo, inclusive caracteres especiais como ***aspas simples ( ' ), aspas duplas ( " ) , Pipe ( | ) e outros***, porém usar estes caracteres especiais pode resultar em erro de sintaxe em componentes de banco de dados do tipo query.  
  
Portanto, é recomendado evitar o uso destes caracteres que podem ser aceitos no Protheus, porém podem causar um erro de sintaxe em querys de banco de dados que irão considerar estes caracteres como delimitadores de conteúdo de campos.

***Exemplo de erro:***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413298569879/mceclip0.png)

**Saiba Mais:**  
*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
