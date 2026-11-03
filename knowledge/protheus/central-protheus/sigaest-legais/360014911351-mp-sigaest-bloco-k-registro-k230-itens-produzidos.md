---
article_id: 360014911351
category: SIGAEST - LEGAIS
content_hash: c63a1ab1c22b4867467db7182b7c3de2538444984fc6f3b1251fc6f28bfd50e8
fetched_at: '2026-06-28T22:38:51.550037+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: 'MP - SIGAEST - Bloco K - Registro K230: Itens Produzidos'
type: support-article
updated_at: '2021-04-28T15:12:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014911351-MP-SIGAEST-Bloco-K-Registro-K230-Itens-Produzidos
---

**Dúvida**O que é o Registro K230: Itens Produzidos?  
  
**Ambiente**Protheus – Estoque/Custos – A partir da versão 11.80  
  
**Solução**

Neste registro é informada a produção acabada de produto em processo ou produto acabado, onde possua os tipos 03 (Produto em Processo) ou 04 (Produto Acabado).

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Tipo** | **Tam** | **Dec** | **Obrig** |
| 01 | REG | Texto fixo contendo "K230" | C | 4 | - | O |
| 02 | DT\_INI\_OP | Data de início da ordem de produção | N | 8 | - | OC |
| 03 | DT\_FIN\_OP | Data de conclusão da ordem de produção | N | 8 | - | OC |
| 04 | COD\_DOC\_OP | Código de identificação da ordem de produção | C | 30 | - | OC |
| 05 | COD\_ITEM | Código do item produzido (campo 02 do Registro 0200) | N | 60 | - | O |
| 06 | QTD\_ENC | Quantidade de produção acabada | N | - | 3 | O |

Para a montagem deste registro, serão consideradas as Ordens de produção da tabela SC2 com **Tipo de Produção Interna (C2\_TPPR = I ou vazio),** que possuam movimentos de produção (**D3\_CF** com "**PR0**" ou "**PR1**") e também as Ordens de Produção sem movimentos de produção, porém, com movimentos de Requisição/Devolução dentro do período de processamento do **Bloco K**. Mesmo que a quantidade de produções realizadas no período for ZERO, e exista algum movimento de requisição para a ordem de produção, será realizada a gravação do Registro K230 para o produto, pois indica que o processo produtivo foi iniciado e não finalizado dentro do período.

**Outras informações:**

- No campo DT\_INI\_OP é gravada a data em que o primeiro movimento para a OP foi gerado na tabela SD3;

- Caso a OP tenha sido finalizada em um período posterior ao do processamento, o campo DT\_FIN\_OP será gravado sem conteúdo;

- Ordens de Produção geradas pelo módulo de Manutenção de Ativos (SIGAMNT) não são consideradas neste registro.

**Tipos de Produtos considerados**

03 e 04.

**Rotinas envolvidas**

MATA650 – Ordem de Produção  
MATA250 – Apontamento de Produção

**Tabelas envolvidas**

SC2 – Ordens de Produção  
SD3 – Movimentações Internas

**Saiba mais:**

*[MP - SIGAEST - Bloco K - Registro K235: Insumos Consumidos (Produção)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014702652-MP-SIGAEST-Bloco-K-Registro-K235-Insumos-Consumidos-Produ%C3%A7%C3%A3o-)*

*[Clique aqui e veja mais artigos sobre Legais/Fiscais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)*
