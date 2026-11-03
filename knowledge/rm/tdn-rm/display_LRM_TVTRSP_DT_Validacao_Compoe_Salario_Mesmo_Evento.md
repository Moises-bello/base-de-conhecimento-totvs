---
content_hash: 841269c3f8d62c821a11bf85bb8ef35b6cc044f52d3b96499eeec13908241e8b
fetched_at: '2026-06-29T00:08:18.169561+00:00'
page_id: '263193624'
product: rm
source: tdn-rm
title: TVTRSP_DT_Validacao_Compoe_Salario_Mesmo_Evento
type: documentation
url: https://tdn.totvs.com/display/LRM/TVTRSP_DT_Validacao_Compoe_Salario_Mesmo_Evento
version: 111
---

# REPROGRAMAÇÃO SALARIAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Reprogramação Salarial* |
| **Situação/Requisito:** | Ao utilizar uma Reprogramação Salarial para funcionário que possui uma Atividade que compõe Salário e outra que não compõe associadas ao mesmo evento, o sistema acusa erro:  Não é permitido associar o mesmo evento em atividades que compõe e outra que não compõe salário.  Atividades Encontradas:  - Atividade Aula associada ao evento [0253] |
| **Solução/Implementação:** | Alterado a validação que impede de ter atividades que compõe ou não compõe com o mesmo evento.  A validação passa a ser um aviso, sendo que antes era um erro e impedia a execução da reprogramação salarial. |
| **Chamados relacionados:** | *TVTRSP* |

divs
