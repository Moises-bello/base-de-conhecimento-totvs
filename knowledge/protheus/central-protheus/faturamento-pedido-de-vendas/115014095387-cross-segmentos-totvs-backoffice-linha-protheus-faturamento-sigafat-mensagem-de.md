---
article_id: 115014095387
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: d766741a0b6b64727b16994fe14298ca5d4a6ae3d992256de53aa2e5d0114fce
fetched_at: '2026-06-28T22:38:38.328524+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: ' Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)  -
  Mensagem de lote vencido "LOTEVENC" no faturamento'
type: support-article
updated_at: '2023-03-16T11:04:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115014095387--Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Mensagem-de-lote-vencido-LOTEVENC-no-faturamento
---

**Ocorrência**  
Ao preencher lote (C6\_LOTECTL) manualmente no pedido de vendas aparece o Help: LOTEVENC

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9014948763799/mceclip0.png)

**Causa**

Inserir no pedido de venda um produto com lote vencido

**Ambiente**  
Cross Segmentos TOTVS Backoffice (Linha Protheus) - SIGAFAT - a partir da versão 11.  
  
**Solução**

Para solucionar esta situação, há 4 maneiras:

* 1 - Ir na rotina Manutenção de lotes (MATA390)

Caminho: Módulo de Estoque/Custos > Atualização, > Movimentações > Internas > Rastreabilidade > Manutenção e clique em "**Validade e fabricação"**, desta forma, altere a data de validade do lote de forma que este não esteja mais vencido e salve.

* 2 - Outra opção é habilitar o parâmetro **MV\_LOTVENC** igual a Sim, desta forma, se o lote estiver vencido poderá ser liberado para a venda.

* 3 - Verifique a data de criação do lote no campo **B8\_DATA** se a data estiver a frente da emissão do pedido ele ira apresentar o HELP. Será necessário ajustar a data.

**Exemplo:**

Data Criação Lote **[B8\_DATA]:** 31/12/2019

Data Criação Pedido de Venda **[C5\_EMISSAO]**: 10/09/2019 (irá bloquear e mostrar a mensagem pois lote não foi gerado para liberar nessa data, o pedido de venda deve ser mais velho que a criação do lote).

* 4 - Liberar o lote bloqueado/vencido na rotina MATA275 - Bloqueio de lotes e preencher o campo Lote "C6\_LOTECTL" manualmente com o código do Lote (B8\_LOTECTL).

**OBS 1:** Pode ocorrer de ao salvar o lote informado, ser apresentado o Help informativo "A240DTVALI", porém o processo continua normalmente (é possível salvar).

**OBS 2:** Dúvidas de como liberar o lote pela rotina MATA275, dúvidas sobre o Help "A240DTVALI", contate a Equipe Protheus Estoque.
