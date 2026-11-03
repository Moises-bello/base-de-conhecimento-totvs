---
content_hash: 2983435fe1fd387212b8588e843eaf1bf4a9e0723dea57978c17751687c498c2
fetched_at: '2026-06-29T00:06:16.993278+00:00'
page_id: '212903387'
product: rm
source: tdn-rm
title: TTPAMY_DT_Campo_Grau_Instrucao_Cadastro_Funcionarios
type: documentation
url: https://tdn.totvs.com/display/LRM/TTPAMY_DT_Campo_Grau_Instrucao_Cadastro_Funcionarios
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
| **Chamados relacionados:** | *TTPAMY* |
| **Versões/Release:** | *11.82.42* |

divs
