---
article_id: 16147904278935
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: af9d2c3d7bee3b709cb4e2ed8c1609e3716d8b72de2bf86e16b88924a867b5fc
fetched_at: '2026-06-28T22:38:45.349282+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Parâmetros da rotina Exclusão
  de Documentos de Saída (MATA521)
type: support-article
updated_at: '2025-10-03T20:08:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16147904278935-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Par%C3%A2metros-da-rotina-Exclus%C3%A3o-de-Documentos-de-Sa%C3%ADda-MATA521
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16147897823511) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Quais os parâmetros disponíveis na rotina Exclusão de Documentos de Saída (MATA521)?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
**Solução**

Os parâmetros da Exclusão de Documentos de Saída podem ser configurados ao pressionar a tecla [F12] na rotina.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/16147190765719)**

|  |  |
| --- | --- |
| **PARÂMETRO** | **OPÇÕES** |
| **Mostra Lanç. Contab?**  Indica se exibe os lançamentos contábeis criados na modalidade on-line. | * Sim * Não |
| **Aglut. Lançamentos?**  Indica se aglutina os lançamentos que possuem a mesma definição contábil. | * Sim * Não |
| **Contabiliza?**  Indica se os lançamentos contábeis devem ser gerados durante a exclusão do documento de saída. Não será possível gerá-lo pela contabilização Off-Line. | * Sim * Não |
| **Retornar Ped. Venda?**  Informando em carteira o sistema retorna a situação dos pedido para não liberado, informando apto a faturar sujeita os pedidos a liberação novamente.   * Selecionando a opção **Carteira** os campos referentes ao *Lote* e *Endereçamento* no Pedido de Venda (SC6) serão mantidos conforme informados, pois o pedido será sujeito a liberação do usuário, o qual poderá definir os lotes e endereços que desejar.      * Selecionando a opção **Apto a Faturar**   + Os produtos ao serem sujeitos a liberação imediata pela própria rotina de exclusão terão suas reservas refeitas com as informações da liberação anterior na tabela SC9 para o novo faturamento, já que os saldos já estavam separados para esta movimentação.   + Caso o parâmetro **MV\_SELLOTE** esteja como '**1**' os campos referentes ao *Lote* e *Endereçamento* no Pedido de Venda (SC6) serão apagados.   + Caso o parâmetro **MV\_SELLOTE** esteja como '**2**' os campos referentes ao *Lote* e *Endereçamento* no Pedido de Venda (SC6) **não** serão apagados, mas ainda assim as liberações levarão em conta os dados da SC9 conforme mencionado. | * Carteira * Apto a Faturar |

**Saiba Mais**

**[Explicativo dos Parâmetros da Exclusão de Documentos de Saída](https://tdn.totvs.com/x/0e4IIg)**
