---
article_id: 360061867134
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 20feb1db0558945c30e5d4570f2aaedbaea4b2152a77cc52131720bf39057081
fetched_at: '2026-06-28T22:38:43.991049+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - "Seleciona tudo" com filtro
  na rotina Documento de saída
type: support-article
updated_at: '2026-03-12T18:23:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061867134-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Seleciona-tudo-com-filtro-na-rotina-Documento-de-sa%C3%ADda
---

**Ocorrência**

Na rotina "Documentos de Saída (MATA460A)", ao efetuarmos o filtro na caixa de pesquisa por número do pedido e utilizarmos o facilitador de "Marcar todos", a rotina "flega" todos os pedidos que estejam com o status de Pedido de Venda Liberado independente dos que estão ocultos no browser, gerando o documento de saída para todos os pedidos que estão liberados.

![20210304_150522.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003504521)

**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12

**Causa**  
Ao aplicar o filtro pela caixa de pesquisa da rotina "Documento de Saída (MATA460A)" informando um pedido, ao selecionar o botão "marcar/desmarcar todas - Selecionar todos", o sistema marcará todos os itens que estejam com o status de pedido de venda liberado independente de estarem ocultos ou não, conforme a função MarkBrow:

[**Função MarkBrow**](https://tdn.totvs.com/x/16YXDg)

**Solução**  
Para solucionar essa ocorrência, temos duas opções:

**1 -** Para que seja marcado apenas o pedido da caixa de pesquisa é necessário selecionar manualmente.

![20210304_151930.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360104505273)

**2 -** Outra opção, é utilizar em conjunto os pontos de entrada **M460QRY** e **M460FIL**:

* [**M460QRY - Adição de elementos**](https://tdn.totvs.com/x/xYRn)
* [**M460FIL - Seleção de Markbrowse**](https://tdn.totvs.com/x/s4Rn)
