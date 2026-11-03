---
content_hash: 933101f01ac75b6bc865aea29558449e3fb766f36c8b273009389612be9b9357
fetched_at: '2026-06-29T00:08:17.658139+00:00'
page_id: '257130744'
product: rm
source: tdn-rm
title: TVU197_DT_Erro_Recalculo_Envelope_CALCMED
type: documentation
url: https://tdn.totvs.com/display/LRM/TVU197_DT_Erro_Recalculo_Envelope_CALCMED
version: 116
---

# ERRO NO RECÁLCULO DE ENVELOPE UTILIZANDO FÓRMULA COM A FUNÇÃO CALCMED

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Recálculo Envelope* |
| **Situação/Requisito:** | Erro no recálculo do envelope apresentando a mensagem: Coleção foi modificada; talvez a operação de enumeração não seja executada.  A situação ocorria no recálculo de evento com fórmula utilizando a função CALCMED. |
| **Solução/Implementação:** | Foi ajustado no processo de cálculo de média, para não efetuar lançamentos quando chamado pela CALCMED. |
| **Chamados relacionados:** | *TVU197* |

divs
