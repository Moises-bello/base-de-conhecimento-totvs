---
content_hash: 8ad0c2a5b3fc9d4f2900b570686636a43ff2cc88b48bdaeb14e56d659f13b9bc
fetched_at: '2026-06-29T00:08:09.756973+00:00'
page_id: '239041260'
product: rm
source: tdn-rm
title: TUSREI_Validador_eSocial_duplicidade_dependente
type: documentation
url: https://tdn.totvs.com/display/LRM/TUSREI_Validador_eSocial_duplicidade_dependente
version: 113
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *eSocial* |
| **Situação/Requisito:** | Ao validar a base de dados para o eSocial, o sistema apresenta erro de forma individual, o certo seria demonstrar a quantidade de erros de forma geral. Desta forma fica inviável determinar qual o tamanho do trabalho que deverá ser realizado, uma vez que não é possível saber o tamanho dos ajustes a serem realizados. |
| **Solução/Implementação:** | Ajuste no validador do eSocial para não abortar o processo quando o funcionário tem dois dependentes com mesmo grau de parentesco (Pai ou Mãe). |
| **Chamados relacionados:** | *-* |
| **Versões/Release:** | 11.82.44 |

divs
