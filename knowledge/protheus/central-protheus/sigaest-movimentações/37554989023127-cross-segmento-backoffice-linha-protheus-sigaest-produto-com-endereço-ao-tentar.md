---
article_id: 37554989023127
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 2f40142b46cc47baf0d30f8bbffba941e75bd8c23bab16eaf1615d2cb34c36a0
fetched_at: '2026-06-28T22:38:54.124314+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Produto com endereço
  ao tentar excluir Nota de Entrada que não atualizou estoque obriga seleção de endereço
type: support-article
updated_at: '2026-01-09T13:29:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37554989023127-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Produto-com-endere%C3%A7o-ao-tentar-excluir-Nota-de-Entrada-que-n%C3%A3o-atualizou-estoque-obriga-sele%C3%A7%C3%A3o-de-endere%C3%A7o
---

Ao excluir Documento de Entrada com TES que não atualiza estoque para produto que controla localização, ocorre erro de obrigatoriedade da localização mesmo sem movimentação de estoque. A causa foi corrigida na ISSUE DMANMAT01-46987, que evita validar saldo por endereço quando não há movimentação física. A solução é aplicar os pacotes indicados para a versão do ambiente, testando antes em homologação.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37554972586135) Tempo aproximado para leitura: **00:02:30 min**  
  
**Ocorrência**

Ao excluir Documento de Entrada que utilizou uma **TES que Não Atualiza Estoque (F4\_ESTOQUE=N)** e para um produto que **controla Localização (B1\_LOCALIZ=S)**, apresenta o Help de obrigatoriedade de informação da Localização. Como realizar o estorno, sendo que o produto não movimentou Estoque?

|  |
| --- |
| **ATENÇÃO**  **Identificamos um ou mais itens que passaram a controlar localização após a entrada deste Documento de Entrada. Para prosseguir com o estorno/exclusão do documento, É OBRIGATÓRIO, selecionar endereços válidos e com saldos a serem estornados.** |

![LOCALIZ.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/37554972586263)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Causa**

Esse incidente foi gerado uma correção na ISSUE de [Manutenção DMANMAT01-46987](https://tdn.totvs.com/x/HTYOPQ), pois, no padrão para produtos que não movimentaram Saldos Físicos de Estoque, não deve validar Saldo por Endereço. Portanto o Help é apresentado indevidamente  
  
**Solução**

Aplicar os pacotes disponibilizados nos links abaixo para o respectivo release de seu ambiente. Sugerimos sempre aplicar em uma Base de homologação primieramente e testar antes de sua base de ptodução.

***12.1.2510:***[***https://r.totvs.io/p/1230166***](https://r.totvs.io/p/1230166)***;***

***12.1.2410:***[***https://r.totvs.io/p/1230169***](https://r.totvs.io/p/1230169)***;***

***12.1.2310:***[***https://r.totvs.io/p/1230168***](https://r.totvs.io/p/1230168)***;***

Saiba Mais:

[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
