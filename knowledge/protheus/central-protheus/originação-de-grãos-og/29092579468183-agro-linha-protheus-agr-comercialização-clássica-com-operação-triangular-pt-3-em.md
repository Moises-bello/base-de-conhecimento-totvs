---
article_id: 29092579468183
category: Originação de Grãos (OG)
content_hash: 2358a662aa6dd0761b30d23ce543a4638dbb66690e92ae04ad14aa8ddadb21d3
fetched_at: '2026-06-28T22:45:37.549019+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Comercialização Clássica com Operação Triangular
  PT 3 em Gestão Agroindústria - Manutenção
type: support-article
updated_at: '2025-01-09T14:31:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29092579468183-Agro-Linha-Protheus-AGR-Comercializa%C3%A7%C3%A3o-Cl%C3%A1ssica-com-Opera%C3%A7%C3%A3o-Triangular-PT-3-em-Gest%C3%A3o-Agroind%C3%BAstria-Manuten%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29092587638551) Tempo aproximado para leitura: **00:00:30 min** **Dúvida**Como é realizado um processo de **Comercialização Clássica com Operação Triangular PT 4 em Gestão Agroindústria - Manutenção**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução  
Dados Gerais:**

| Produto: | TOTVS Agro Beneficiamento |
| --- | --- |

| Linha de Produto: | Linha Protheus |
| Segmento: | Agroindústria |
| Módulo: | Gestão de Agronegócio |
| Função: | OGA250 - Romaneio com pesagem |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | DAGROCCO-3918 |

**Requisito/Requisito:**Ao reabrir o romaneio, necessário ajustar os itens da aba comercialização, excluir o item de subtipo **46 -  (S) Remessa por** **Venda a Ordem**. e limpar os campos de **ID.Mov e Subtipo**.  
Na confirmação do romaneio deve ser gerado as duas **NF**.  
  
**Solução:**Realizado ajuste na atualização do romaneio para excluir o item da aba comercialização com subtipo **46 -  (S) Remessa por Venda a Ordem** e limpar os campos de **ID.Mov e Subtipo**.

Realizado ajuste na confirmação do romaneio, para gerar as duas notas fiscais, primeiro será gerado a **NF** da remessa da operação triangular e em seguida a **NF** da venda da operação triangular. Esta sequencia é para poder referenciar a **NF** de remessa no pedido da **NF** de venda, sendo informado os campos **C6\_NFORI, C6\_SERIORI, C6\_ITEMORI**.
