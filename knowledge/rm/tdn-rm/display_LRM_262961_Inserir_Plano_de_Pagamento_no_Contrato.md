---
content_hash: 7eb9164d1de61fa30d33e6d76385304a0519dc6a41a30f15344e2aeb6228ffd8
fetched_at: '2026-06-29T00:08:23.816776+00:00'
page_id: '270092443'
product: rm
source: tdn-rm
title: 262961_Inserir_Plano_de_Pagamento_no_Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/262961_Inserir_Plano_de_Pagamento_no_Contrato
version: 112
---

# Inserir Plano de Pagamento no Contrato

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Lookup de plano de pagamento |
| **Situação/Requisito:** | Os planos de pagamento cadastrados, não são mostrados, para serem inseridos no contrato do aluno.  As datas de início e fim estão válidas e as matrizes aplicadas estão cadastradas. |
| **Solução/Implementação:** | Ajuste na consulta SQL de seleção de planos de pagamento a qual estava considerando as datas no formato 'MMDDYYYY' ('MESDIAANO')  O formato foi alterado para 'YYYY-MM-DD' a fim de se fazer uma comparação correta entre datas priozando ano, mes e dia nessa ordem. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | MEDU-1648 |
| **Requisito (ISSUE):** | *N/A* |

divs
