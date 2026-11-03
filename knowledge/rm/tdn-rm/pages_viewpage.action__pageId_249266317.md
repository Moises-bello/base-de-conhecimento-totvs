---
content_hash: 21ac96864d5ff36c5d539c81785bfc05cac3f4d5e6d729c563cae1a6d05634bb
fetched_at: '2026-06-29T00:08:16.943561+00:00'
page_id: '249266317'
product: rm
source: tdn-rm
title: TVPQPW_DT_Geração_Encargos_Provisão_Acumulada_Adiantamento_13o
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=249266317
version: 117
---

# GERAÇÃO DE ENCARGOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração de Encargos* |
| **Situação/Requisito:** | *Quando o funcionário recebe adiantamento da 1 parcela de 13º salário o sistema está levando em consideração para o cálculo do valor do encargo 41 provisão FGTS.s/13 salário*  *Mas não está ocorrendo da mesma forma para o encargo 40 provisão de 13 salário.* *Gerando desta forma divergências contábeis.* |
| **Solução/Implementação:** | * *Criação do campo " ABATEADIANT13O" na tabela de encargo.* * *Inclusão da flag "Abate Adiantamento de 13º" no cadastro de encargos.*   *Através da criação do parâmetro o usuário poderá optar pelo abatimento ou não do adiantamento de 13º no cálculo da provisão de 13º salário (encargo tipo 7).*  *Com a flag desmarcada, a provisão desconsidera o adiantamento de 13º para realização do cálculo do encargo 40 e com a mesma marcada realiza o cálculo abatendo o valor adiantado.* |
| **Chamados relacionados:** | *TVPQPW* |

divs
