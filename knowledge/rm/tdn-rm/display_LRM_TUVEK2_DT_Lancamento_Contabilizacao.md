---
content_hash: 9abea3267ce11969d43722c0fdac28ebf445404d629bd049e11d748e3e45a263
fetched_at: '2026-06-29T00:08:07.310469+00:00'
page_id: '237380430'
product: rm
source: tdn-rm
title: TUVEK2_DT_Lancamento_Contabilizacao
type: documentation
url: https://tdn.totvs.com/display/LRM/TUVEK2_DT_Lancamento_Contabilizacao
version: 116
---

# CONTABILIZAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Contabilização |
| **Situação/Requisito:** | O processo de contabilização está integrado com outros backoffices e ao gerar o lote o sistema está validando o código do lote na CLOTE quando o parâmetro “ Gera contabilização no Labore antes de enviar para o Saldus” está desmarcado. |
| **Solução/Implementação:** | Criado validação onde é verificado se o parâmetro referente à utilização de sistemas de backoffice de terceiros estiver marcado, o sistema deverá verificar o número do lote na tabela PCONTABILIZACAO e não na tabela CLOTE. |
| **Chamados relacionados:** | TUVEK2 |

divs
