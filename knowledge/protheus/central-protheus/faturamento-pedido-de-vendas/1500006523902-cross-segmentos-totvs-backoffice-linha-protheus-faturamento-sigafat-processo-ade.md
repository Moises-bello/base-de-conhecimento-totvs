---
article_id: 1500006523902
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 7670de6442fddf3e10c04c705b145a000d273fc87665e0bfd100061e76d7af1c
fetched_at: '2026-06-28T22:38:41.050697+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Processo adequado para ajustes de código do cliente utilizado indevidamente
type: support-article
updated_at: '2021-06-10T12:51:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006523902-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Processo-adequado-para-ajustes-de-c%C3%B3digo-do-cliente-utilizado-indevidamente
---

**Dúvida**

Foi efetuado um cadastro indevido de cliente , onde já foi efetuado até a geração da nota fiscal para este cliente, porém, é necessário trocar o código do cliente. Quais tabelas devem ser verificadas para ajustar o código do cliente? Qual o processo correto?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - todas as versões  
  
**Solução**

Uma vez que é gerado uma nota fiscal (**mata461**), existe vários módulos que podem ter sido integrados no processo como fiscal, financeiro, contabilidade, estoque, comissões , etc..

O processo o correto para esta situação é excluir a nota gerada e deixar o pedido de venda (**MATA410**) em aberto.

Através da alteração do pedido de venda , trocar o cliente utilizado e posteriormente, ou inibir o cadastro do cliente (**MATA030**) através do campo **a1\_msblql** para que não seja utilizado ou mesmo excluir o cadastro caso não haja nenhuma movimentação , para que assim não haja vínculo com outras tabelas.

É ideal tratar o processo conforme acima para manter a integridade dos processo do ERP e do Banco de Dados.

**Obs. O suporte não orienta manipulação de tabelas via banco de dados, qualquer alteração deve ser avaliada pelo DBA da empresa.**
