---
content_hash: 90ca750c15fa5fe93e5639b6eb83425111df0c4e71823554ad9202f8544fa700
fetched_at: '2026-06-29T00:08:07.267613+00:00'
page_id: '237376456'
product: rm
source: tdn-rm
title: TUTTX0_DT_Campo_Salario_Relatorio_Gerador_Delphi
type: documentation
url: https://tdn.totvs.com/display/LRM/TUTTX0_DT_Campo_Salario_Relatorio_Gerador_Delphi
version: 116
---

# CAMPO SALARIO NO RELATÓRIO "2.004.001-Envelope de pagamento - Labo 04.RRM" ESTÁ SENDO PREENCHIDO COM O SALARIO ATUAL.

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Gerar o campo Salario do relatório "2.004.001-Envelope de pagamento - Labo 04.RRM" de acordo com o salario utilizado no calculo do período.* |
| **Situação/Requisito:** | Ao gerar o relatório padrão 2.004.001-Envelope de pagamento - Labo 04.RRM para um mês anterior ao atual, no campo Salário sempre retornará o Salário atual do funcionário, mesmo que na época fosse outro. |
| **Solução/Implementação:** | *Realizado ajuste na estrutura do arquivo para que busque o campo "SALARIODECALCULO" da tabela PFPERFF para preenchimento do campo Salario no relatório.* |
| **Chamados relacionados:** | TUTTX0 |

divs
