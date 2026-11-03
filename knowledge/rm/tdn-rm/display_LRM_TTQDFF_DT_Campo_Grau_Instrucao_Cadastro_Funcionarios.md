---
content_hash: 4e34da87fd09d7081e503fc485c6dd258fc4618984d5065f89a3407aef35621b
fetched_at: '2026-06-29T00:06:17.079557+00:00'
page_id: '212904436'
product: rm
source: tdn-rm
title: TTQDFF_DT_Campo_Grau_Instrucao_Cadastro_Funcionarios
type: documentation
url: https://tdn.totvs.com/display/LRM/TTQDFF_DT_Campo_Grau_Instrucao_Cadastro_Funcionarios
version: 1
---

# CADASTRO DE FUNCIONÁRIOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de funcionários* |
| **Situação/Requisito:** | *Ao acessar o cadastro de funcionário que possua o valor Grau de Instrução "NULL", era exibida uma mensagem de erro e o cadastro do funcionário fechava.* |
| **Solução/Implementação:** | *Campo do cadastro de funcionário "Grau de Instrução" estava sendo tratado como Não Nulo no código, porém, a coluna na base de dados possibilita inserção de valores nulos. O campo continua com o comportamento de campo obrigatório, somente a propriedade que define se é nulo ou não que foi alterada.* |
| **Chamados relacionados:** | TTQDFF |
| **Versões/Release:** | *12.1.9* |

divs
