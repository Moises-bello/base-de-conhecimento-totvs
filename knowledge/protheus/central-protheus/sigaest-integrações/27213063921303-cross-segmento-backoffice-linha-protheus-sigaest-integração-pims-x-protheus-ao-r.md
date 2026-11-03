---
article_id: 27213063921303
category: SIGAEST - INTEGRAÇÕES
content_hash: 05d658a455316293e26e3787009c181ae41bc1b479255f7a02de2cb7a0772ddc
fetched_at: '2026-06-28T22:38:46.199586+00:00'
product: protheus
section_id: 21226442947351
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Integração PIMS x
  Protheus ao realizar a liberação de boletim não estorna todos os itens.
type: support-article
updated_at: '2025-03-12T12:27:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27213063921303-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Integra%C3%A7%C3%A3o-PIMS-x-Protheus-ao-realizar-a-libera%C3%A7%C3%A3o-de-boletim-n%C3%A3o-estorna-todos-os-itens
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27213063910679) Tempo aproximado para leitura: **00:01:25min** **Dúvida**No PIMS, ao realizar uma liberação de boletim, é gerado um estorno da movimentação no **ERP Protheus**, porém em cenários que **tem mais de um insumo (item), não está sendo estornado todos os insumos.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**A movimentação de liberação de boletim, gera uma movimentação de estorno via **MATA241** **(movimentação Multipla)** adapter [StockTurnover](https://tdn.totvs.com/x/c5maFQ) no Protheus.

Porém o **Protheus** dispõe de uma funcionalidade por meio da tecla **F12** que define se os estornos serão realizados por **Item ou Documento**. Nesse cenário para que o estorno ocorra para todos os insumos a pergunta deve estar **"Quanto ao Estorno = Por Documento"**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27213063912087)

**Observação:**  O parâmetro de configuração **F12** se trata de uma funcionalidade do **Protheus**, que serve para obter comportamento diferente dependendo de cada estorno que irá realizar, dessa maneira, deve definir qual forma vai utilizar, porém esse parâmetro não pode der "chumbado" para que não seja alterado via rotina (**MATA241**).

**No caso de estorno do movimento via PIMS**, sempre será feito por **documento(Boletim)**, então deve atentar-se se a configuração de estorno no Protheus, mediante a rotina informada, o pergunte **F12** se esta também configurado por "**Documento**", ao invés de "**Item**".

Por ser uma tratativa no **ERP PROTHEUS**, caso desejar podera solicitar uma melhoria no **PIMS(TOTVS Agro)** para que também exista a possibilidade de estorno por item.

[Central Colaborativa](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Integrações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/21226442947351-SIGAEST-INTEGRA%C3%87%C3%95ES)*
