---
content_hash: 72f1c8e225e5ae3d4865e10709b6323d1c0f933cded497d18893388ede5b67fb
fetched_at: '2026-06-29T00:06:25.742573+00:00'
page_id: '224444652'
product: rm
source: tdn-rm
title: TUDNO0_DT_Campo_Salario_Relatorio_Gerador_Delphi
type: documentation
url: https://tdn.totvs.com/display/LRM/TUDNO0_DT_Campo_Salario_Relatorio_Gerador_Delphi
version: 117
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
| **Chamados relacionados:** | TUDNO0 |

divs
