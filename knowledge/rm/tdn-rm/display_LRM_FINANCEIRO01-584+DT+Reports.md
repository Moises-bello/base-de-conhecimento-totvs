---
content_hash: e0bd49cb83a90bf9c18cfabe13773092b29861d9149c9ce9f8050c25dc8dd819
fetched_at: '2026-06-29T00:08:33.078437+00:00'
page_id: '274301881'
product: rm
source: tdn-rm
title: FINANCEIRO01-584 DT Reports
type: documentation
url: https://tdn.totvs.com/display/LRM/FINANCEIRO01-584+DT+Reports
version: 110
---

# FINREL0016 - RELATÓRIO DE LANÇAMENTOS A RECEBER EM ATRASO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Totvs Gestão Financeira |
| **Função:** | Reports |
| **Situação/Requisito:** | O relatório "FINRE-0016 - Lançamentos à Receber em atraso" do book do Reports do financeiro não apresenta os valores corretamente na coluna "Vr. Receber". Se um lançamento do TIN por exemplo  tivesse os valores de integração preenchidos, este valor não era considerado no valor líquido do lançamento. |
| **Solução/Implementação:** | Foi feito o ajuste no relatório "FINREL0016" para considerar também os valores de integração na coluna "Vr. Receber". Além do ajuste nesta coluna do relatório foi feito também o ajuste na coluna "Acumulado", esta coluna é a soma do valor líquido na data do vencimento mais os juros do lançamento.  Não houve alteração no código fonte do sistema, apenas ajuste no relatório do Reports. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |

divs
