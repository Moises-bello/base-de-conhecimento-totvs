---
content_hash: 97516bf00150d3ffbe8f2f7175e0bb7d44092928485f0ddff276dfc69148083d
fetched_at: '2026-06-29T00:08:47.332209+00:00'
page_id: '319787306'
product: rm
source: tdn-rm
title: Manual - Expressões
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=319787306
version: 3
---

As expressões do gerador permitem que sejam executadas funções, operações de texto, matemáticas, entre outras. Elas são utilizadas em vários componentes do gerador e podem utilizar dados das ligações, do contexto e dos registros dependendo de que ponto elas são executadas.

![](/download/attachments/319787306/expressoes.png?version=1&modificationDate=1512921929000&api=v2)

1Expressão

Informe nesta caixa o texto da expressão. Se for uma expressão de campo, o valor retornado de ser do mesmo tipo de dado do campo. Caso seja uma expressão de filtro, o valor retornado deve ser do tipo lógico (true ou false) e no caso da expressão do nome do arquivo, o retorno deve ser do tipo texto.

Esta expressão deve ser escrita em linguagem C# e as principais funções são listadas no botão de funções a esquerda do texto da expressão. Além das funções, poderão ser utilizados os dados disponíveis no botão de dados. Os dados disponíveis variam de acordo com o tipo de expressão.

O gerador de saídas irá compilar esta expressão no Layout, e caso ela não seja válida um erro será exibido ao salvar ou ao gerar o código do Layout não permitindo que o Layout seja gerado até que o erro seja corrigido.

Sempre utilize as funções "Convert" para converter os valores dos dados para o tipo que deseja ser trabalhado na expressão. No exemplo da imagem, a função "Convert.ToString()" converte o valor do dado NOME para o tipo texto (string) e permite que sejam executadas funções de texto em cima do valor do dado, como por exemplo a função StartsWith() que no caso da expressão da imagem, verifica se o campo NOME começa com a letra "A".

##### Exemplo:

Convert.ToString(CLIENTE.NOME).StartsWith("A")

Converte o valor da coluna NOME da ligação CLIENTE para texto e verifica se o valor começa com a letra A.

2Funções

Clique para visualizar as funções disponíveis para utilização na expressão.

As principais funções também estão disponíveis na documentação oficial a seguir:

* Convert: <https://msdn.microsoft.com/en-us/library/system.convert_methods(v=vs.110).aspx>
* Math: <https://msdn.microsoft.com/en-us/library/system.math(v=vs.110).aspx>
* String: <https://msdn.microsoft.com/en-us/library/system.string_methods(v=vs.110).aspx>

As seguintes funções utilitárias são específicas do gerador de saídas:

* Util.Round - Função utilizada para fazer o arredondamento de um valor numérico de acordo com o número de casas decimais desejadas.
* Util.Truncate - Função utilizada para truncar um valor numérico de acordo com o número de casas decimais desejadas.
* Util.ValueIn - Função utilizada para verificar se o valor passado como parâmetro está na lista de valores passadas.
* Util.AreEqual - Função utilizada para verificar se os dois valores passados são iguais.
* Util.IsEmpty - Função utilizada para verificar se o valor passado é vazio ou nulo.
* Util.If - Função utilizada para retornar um valor de acordo com a condição especificada.
* Util.Normalizar - Função utilizada para fazer a normalização de um texto passado como parâmetro. Ela irá retirar toda a acentuação, caracteres especiais, enter e tab do texto.
* Util.RetirarTabEnter - Função utilizada para retirar os caracteres de enter e tab de um texto.
* Util.RetirarAcentos - Função utilizada para retirar os caracteres acentuados de um texto.
* Util.RetirarCaracteresEspeciais - Função utilizada para retirar os caracteres especiais de um texto.
* Util.Left - Função utilizada para retornar uma quantidade determinada de caracteres a esquerda de um texto.
* Util.Right - Função utilizada para retornar uma quantidade determinada de caracteres a direita de um texto.

As seguintes funções estão disponíveis somente para o gerador de saídas RM:

* this.ExecuteFormula - Função utilizada para executar uma fórmula RM na expressão.

3Dados

Clique para visualizar os dados disponíveis para utilização na expressão.

Os principais tipos de dados utilizados pelo gerador e suas funções disponíveis estão na documentação oficial da linguagem, consulte cada um dos tipos para maiores informações. Verifique as funções disponíveis para manipulação de cada tipo nos seguintes links:

* String (Texto): <https://msdn.microsoft.com/en-us/library/system.string(v=vs.110).aspx>
* Integer (Número Inteiro): <https://msdn.microsoft.com/en-us/library/system.int32(v=vs.110).aspx>
* Decimal (Número Decimal): <https://msdn.microsoft.com/en-us/library/system.decimal(v=vs.110).aspx>
* DateTime (Data/Hora): <https://msdn.microsoft.com/en-us/library/system.datetime(v=vs.110).aspx>
* Boolean (Lógico): <https://msdn.microsoft.com/en-us/library/system.boolean(v=vs.100).aspx>

Dica

Por se tratar de um código C# que é compilado, todas as funções fazem a diferenciação de caracteres maiúsculos e minúsculos. Se o caso dos caracteres for diferente, um erro de compilação será exibido na hora de salvar ou gerar a classe do Layout. Neste sentido é interessante sempre utilizar os botões de funções e dados para adicionar o texto correto na expressão. Utilize também a funcionalidade que auxilia a completar a expressão, pressionando "CTRL+ESPAÇO" ou "CTRL+SHIFT+ESPAÇO" no editor de expressões.
