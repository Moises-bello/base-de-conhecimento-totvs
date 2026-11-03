---
content_hash: c130cb7086c5ad28877148ad4128f21dc1fe265c02882beb8d569f5adac14ba5
fetched_at: '2026-06-29T00:08:47.300639+00:00'
page_id: '319787293'
product: rm
source: tdn-rm
title: Manual - Filtro da Tabela do Conjunto de Dados
type: documentation
url: https://tdn.totvs.com/display/LRM/Manual+-+Filtro+da+Tabela+do+Conjunto+de+Dados
version: 3
---

O filtro da tabela permite que sejam adicionadas clausulas de filtro na leitura dos dados do banco. Será gerada uma cláusula WHERE na sentença como todos os filtros adicionados. Selecione o campo, operador, seus valores e clique em adicionar ou modificar para alterar o filtro. Qualquer campo das tabelas poderá ser utilizado para montagem do filtro.

![](/download/attachments/319787293/filtro_da_tabela_do_conjunto_de_dados.png?version=1&modificationDate=1512921897000&api=v2)

1Pesquisar

Digite parte do nome do campo para fazer a pesquisa na lista de campos.

2Campos

Selecione o campo que deseja adicionar a condição de filtro.

3Operador

Selecione o operador do filtro, que pode ser:

|  |  |
| --- | --- |
| = | Define que o valor do campo deverá ser igual ao valor informado. |
| <> | Define que o valor do campo deverá ser diferente do valor informado. |
| > | Define que o valor do campo deverá ser maior do que o valor informado. |
| >= | Define que o valor do campo deverá ser maior ou igual ao valor informado. |
| < | Define que o valor do campo deverá ser menor do que o valor informado. |
| <= | Define que o valor do campo deverá ser menor ou igual ao valor informado. |
| IS NULL | Define que o valor do campo deverá ser nulo. |
| IS NOT NULL | Define que o valor do campo não poderá ser nulo. |
| LIKE | Define que o valor do campo deverá conter o valor informado. O caractere % pode ser utilizado para criar máscaras de valores, por exemplo "%MARIA%", onde o valor do campo deverá conter a palavra MARIA em qualquer posição do texto. |
| NOT LIKE | Define que o valor do campo não poderá conter o valor informado. Da mesma forma que a operação LIKE, a NOT LIKE pode conter o caractere % para máscara de valores. |
| BETWEEN | Define que o valor do campo deverá estar numa faixa de valores entre o Valor e o Valor Final. |

4Valor

Informe o valor para aplicação do filtro do campo.

5Valor Final

Informe o valor final para aplicação do filtro do campo. Este valor deverá ser informado quando for utilizado o operador BETWEEN.

6E/OU

Selecione a condição de filtro deverá fazer uma operação AND ou OR quando houver mais de uma condição. E define se todas as condições do grupo devem ser respeitadas ou se uma OU outra deve ser respeitada.

7Adicionar

Clique para adicionar uma nova condição na expressão de filtro de acordo com as opções definidas.

8Modificar

Clique para alterar a condição selecionada na expressão de acordo com as opções definidas.

9Adicionar Grupo

Clique para criar um grupo de condições. Isto irá criar na cláusula FROM um grupo de expressões entre parêntesis permitindo que sejam adicionadas expressões de filtro tipo: NOME = 'X' AND (STATUS = 1 OR STATUS = 2).

10Excluir

Clique para excluir a condicão selecionada na expressão do filtro.

11Limpar

Clique para limpar todas as condições do filtro.

12Mover para Cima

Clique para mover a condição selecionada na expressão para cima no grupo.

13Mover para Baixo

Clique para mover a condição selecionada na expressão para baixo no grupo.

14Expressão

Exibe a lista de condições da expressão de filtro que será criada. Clique em uma condição para carregar o campo, operador e valores associados a esta condição.

15OK

Clique para salvar as condições do filtro e fechar a tela.

16Cancelar

Clique para cancelar a alteração do filtro.

Dica

É possível criar parâmetros do filtro para que eles possam ser informados no momento da execução do Layout. Para isso, basta colocar nos valores da condição o nome do parâmetro entre colchetes. Por exemplo ao colocar o valor [DATA], o parâmetro DATA será criado no Contexto, permitindo que ele seja informado no momento da leitura. Para mais informações consulte [Parâmetros do Contexto](/pages/viewpage.action?pageId=319787287).
