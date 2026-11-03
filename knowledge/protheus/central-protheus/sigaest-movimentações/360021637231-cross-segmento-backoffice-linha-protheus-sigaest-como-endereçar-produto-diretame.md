---
article_id: 360021637231
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 1370652279f3b7c7685211484bd11f7a68833601dbc24b7e670974f77b4c8e31
fetched_at: '2026-06-28T22:38:53.930548+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como endereçar Produto
  diretamente da rotina de Documento de Entrada "automaticamente"?
type: support-article
updated_at: '2023-09-13T19:18:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021637231-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-endere%C3%A7ar-Produto-diretamente-da-rotina-de-Documento-de-Entrada-automaticamente
---

**Dúvida**Como posso endereçar um produto logo após o movimento de Entrada sem precisar acessar à rotina de Endereçamento - MATA265 ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Para um produto ser endereçado "automaticamente" com entrada de uma nova nota (MATA103) ou em apontamento da produção (MATA250) deve-se habilitar o parâmetro MV\_DISTMOV. Ele serve para indicar se permite o endereçamento logo após a inclusão do movimento de entrada (Nota/Produção)

Quando habilitado e após movimento de Nota/Produção, será aberta uma tela para a distribuição ao(s) endereço(s) desejado(s) do armazém do produto conforme as imagens abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003054121)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003054201)

Com este parâmetro, ganha-se muito em performance no dia a dia, deixando de ter a necessidade de endereçar manualmente pela rotina MATA265.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
