---
article_id: 10409483539223
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 1f9740d0b1d9ceaa90d6520b33afaaffb695880f1fa382eb2dd18f1cbdfb78ed
fetched_at: '2026-06-28T22:38:42.658391+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Comportamento
  do campo “Qtd. Liberada” (C6_QTDLIB)
type: support-article
updated_at: '2022-11-22T17:27:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10409483539223-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Comportamento-do-campo-Qtd-Liberada-C6-QTDLIB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como funciona o campo “Qtd. Liberada” (C6\_QTDLIB) ao preenche-lo no Pedido de Vendas (MATA410)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**O campo “Qtd. Liberada” (C6\_QTDLIB), disponível na linha dos itens do Pedido de Vendas (MATA410), indica a quantidade a ser submetida a análise de Crédito e Estoque, ou seja, a quantidade a ser liberada do produto no processo de venda. Este campo pode receber seu conteúdo de forma automática ou manual.

Ao preencher o campo “Qtd. Liberada” (C6\_QTDLIB), e salvar o Pedido de Vendas (MATA410), o sistema realiza a inclusão da Liberação dos Itens do Pedido de Vendas (Tabela SC9), porém não é realizada a gravação do conteúdo do campo na tabela de Itens do Pedido de Vendas (Tabela SC6).

Ou seja, o preenchimento do campo “Qtd. Liberada” (C6\_QTDLIB) tem como finalidade a criação do registro na tabela SC9, o conteúdo do campo não fica gravado na tabela SC6.

**Observação:** Não é possível auditar, via Audit Trail, a edição do campo “Qtd. Liberada” (C6\_QTDLIB), pois a ferramenta audita alterações em Banco de Dados, e, como especificado acima, este campo realiza a inclusão da tabela SC9, mas seu conteúdo não é gravado/alterado/excluído na tabela SC6.

**Saiba mais**:

[Liberação / Bloqueio do Pedido de Vendas](https://tdn.totvs.com/x/RjS4Ew)

[Embedded Audit Trail (SIGACFG)](https://tdn.totvs.com/x/AicrF)
