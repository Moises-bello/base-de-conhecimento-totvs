---
content_hash: a302529e5eed6a5dfaad469bc826835331aff707a99eaf2ceffae3606fbaee64
fetched_at: '2026-06-29T00:08:25.897950+00:00'
page_id: '271163602'
product: rm
source: tdn-rm
title: 213239 MEDU-1252 DT Copia turmas entre período letivo exige matriz no período
  letivo destino
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271163602
version: 114
---

# Processo de Cópia de Turmas entre Período Letivo

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Processo de Cópia de Turmas entre Período Letivo |
| **Situação/Requisito:** | No processo de cópia de turmas entre período letivo está sendo exigido que seja cadastrada na parametrização de curso a mesma matriz curricular do período letivo de origem no período letivo de destino. |
| **Solução/Implementação:** | Realizamos uma evolução no processo de cópia de turmas entre período letivo para que seja possível executar a cópia da turma mesmo que a matriz aplicada do período letivo de origem não esteja sendo ofertada no período letivo de destino, neste caso será necessário o usuário informar uma nova matriz aplicada correspondente ao período letivo de destino.  Comportamento:  Quando o sistema identificar que a matriz aplicada não está parametrizada no período letivo de destino será apresentado uma mensagem alertando ao usuário e questionando se deseja continuar.  Se o usuário continuar o sistema seguira a seguinte regra:   * Para o Ensino Básico;   Ao selecionar a nova matriz aplicada, o sistema apresentara para cópia as disciplinas conforme o período da grade da matriz aplicada selecionada.  Se nesta grade existir mais de um período, o usuário deverá selecionar o período desejado e o sistema apresentará as disciplinas conforme o mesmo.   * Para o Ensino Superior;   Ao selecionar a nova matriz aplicada, o sistema apresentara para cópia somente as disciplinas da matriz aplicada selecionada que existe na matriz aplicada da turma selecionada, ou seja, as disciplinas têm que existir nas duas grades.  Por exemplo:  Tenho “Matemática” em 2016, só vou listar “Matemática” para cópia se esta disciplina existir na matriz aplicada da grade de 2017.  Esta mesma regra se aplica se a matriz aplicada de 2016 estiver parametrizada em 2017.   Para demais ajustes o usuário deverá adicionar ou remover a disciplina manualmente na própria tela do processo de cópia. |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | 213239 |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
