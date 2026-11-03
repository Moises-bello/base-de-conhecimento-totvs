---
content_hash: b48518857ac36ec497082f100757342bbd9241acca98dc4aaac1c787854b7096
fetched_at: '2026-06-29T00:08:14.290162+00:00'
page_id: '244447622'
product: rm
source: tdn-rm
title: TUVXXI_DT_Campo_Salario_Relatorio_Gerador_Delphi
type: documentation
url: https://tdn.totvs.com/display/LRM/TUVXXI_DT_Campo_Salario_Relatorio_Gerador_Delphi
version: 115
---

# CAMPO SALARIO NO RELATÓRIO "2.004.002-Envelope de pagamento - Labo 04 - Imp.Matricial - (Arquivo).RRM" ESTÁ SENDO PREENCHIDO COM O SALARIO ATUAL.

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Gerar o campo Salario do relatório "2.004.002-Envelope de pagamento - Labo 04 - Imp.Matricial - (Arquivo).RRM" de acordo com o salario utilizado no calculo do período.* |
| **Situação/Requisito:** | Ao gerar o relatório padrão 2.004.002-Envelope de pagamento - Labo 04 - Imp.Matricial - (Arquivo).RRM para um mês anterior ao atual, no campo Salário sempre retornará o Salário atual do funcionário, mesmo que na época fosse outro. |
| **Solução/Implementação:** | *Realizado ajuste na estrutura do arquivo para que busque o campo "SALARIODECALCULO" da tabela PFPERFF para preenchimento do campo Salario no relatório.* |
| **Chamados relacionados:** | TUVXXI |

divs
