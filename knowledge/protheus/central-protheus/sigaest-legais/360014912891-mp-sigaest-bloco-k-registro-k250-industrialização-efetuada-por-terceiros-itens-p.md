---
article_id: 360014912891
category: SIGAEST - LEGAIS
content_hash: a21da6f1c822654c32d69c462e5bc8fe369e37c583fdf8539fd97eeb9e5304f0
fetched_at: '2026-06-28T22:38:51.556357+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: 'MP - SIGAEST - Bloco K - Registro K250: Industrialização Efetuada por Terceiros
  - Itens Produzidos'
type: support-article
updated_at: '2021-06-21T14:48:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014912891-MP-SIGAEST-Bloco-K-Registro-K250-Industrializa%C3%A7%C3%A3o-Efetuada-por-Terceiros-Itens-Produzidos
---

Apresenta os produtos que foram industrializados por terceiros.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Tipo** | **Tam** | **Dec** | **Obrig** |
| 01 | REG | Texto fixo contendo "K250" | C | 4 | - | O |
| 02 | DT\_PROD | Data do reconhecimento da produção ocorrida no terceiro | N | 8 | - | O |
| 03 | COD\_ITEM | Código do item produzido (campo 02 do Registro 0200) | N | 60 | - | O |
| 04 | QTD | Quantidade produzida | N | - | 3 | O |

Para a montagem deste registro, serão consideradas as Ordens de produção da tabela SC2 com **Tipo de Produção Externa (C2\_TPPR = E),** que possuam Movimentos de produção (**D3\_CF** com "**PR0**" ou "**PR1**") dentro do período de processamento.

Quando ocorre uma OP com o campo **C2\_TPPR = E,** o produto acabado gerará no Bloco K em seu registro K250 enquanto o(s) produto(s) consumido(s), no registro K255.

**Tipos de Produtos considerados**

03 (Produto em Processo) e 04 (Produto Acabado).

**Rotinas envolvidas**

MATA650 – Ordem de Produção  
MATA250 – Apontamento de Produção

**Tabelas envolvidas**

SC2 – Ordens de Produção  
SD3 – Movimentações Internas
