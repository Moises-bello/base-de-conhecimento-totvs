---
content_hash: ab2b55489716f1e65e4d06912257302d0304177a79edf130082c120ba3e0849e
fetched_at: '2026-06-29T00:08:47.216152+00:00'
page_id: '319787267'
product: rm
source: tdn-rm
title: Manual - Formatação Padrão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=319787267
version: 3
---

A formatação padrão define como cada tipo de dado dos campos dos registros do gerador deverão ser formatados no arquivo final. Esta formatação poderá ser alterada posteriormente campo a campo. Cada tipo de dado possui propriedades específicas que serão detalhadas a seguir.

![](/download/attachments/319787267/formatacao_padrao.png?version=1&modificationDate=1512921824000&api=v2)

1Tipo de Dado

Selecione o tipo de dado para alterar as propriedades.

2Propriedades

Informe arqui as propriedades específicas para cada tipo de dado.

#### Texto

|  |  |
| --- | --- |
| Caractere de preenchimento | Informe qual caractere deverá ser utilizado para preenchimento do campo até o tamanho do campo. Por padrão o gerador irá preencher com espaços em branco. |
| Caso dos caracteres | Selecione aqui as opções para converter os caracteres para maiúsculo, minúsculo ou não fazer nenhuma conversão (Normal). |
| Expressão regular dos caracteres não permitidos | Informe uma expressão regular que será utilizada para remover caracteres do texto, utilize esta opção para remover qualquer caractere do valor de origem como por exemplo aspas, espaços, quebras de linha ou outros. |
| Expressão regular para pesquisa no texto | Informe uma expressão regular que será utilizada para selecionar um pedaço do texto dentro do texto de origem, utilize um grupo para definir o texto que será extraído. Por exemplo, se você quiser extrair somente o primeiro nome de um texto, utilize a expressão: "([A-Za-z]+) " |
| Máscara de entrada | Informe uma máscara de entrada que deverá ser aplicada ao texto de origem. Por exemplo você poderá adicionar o caractere separador "-" a um CEP que não contenha este caractere utilizando a máscara: "00000-000".  Para mais informações consulte: <https://msdn.microsoft.com/en-us/library/system.windows.forms.maskedtextbox.mask(v=vs.110).aspx> |
| Modo de preenchimento | Selecione a forma como o texto deverá ser preenchido com o caractere de preenchimento. Por padrão o gerador não faz o preenchimento. Você pode preencher com os caracteres a direita ou a esquerda. |
| Substituir caracteres especiais | Utilize esta opção para remover qualquer caractere especial do texto de origem, caracteres especiais são caracteres que não contém letras, números ou espaços. |
| Tipo de dado do sistema | Esta propriedade indica qual é o tipo mapeado do sistema para o tipo de dado selecionado e é somente informativa. |
| Valor nulo | Informe o valor que deverá ser utilizado quando o valor de origem for vazio ou nulo. |

#### Número Inteiro

|  |  |
| --- | --- |
| Caractere de preenchimento | Informe qual caractere deverá ser utilizado para preenchimento do campo até o tamanho do campo. Por padrão o gerador irá preencher com zeros quando o tipo de dado é inteiro. |
| Modo de preenchimento | Selecione a forma como o texto deverá ser preenchido com o caractere de preenchimento. Por padrão o gerador irá preencher a esquerda para o tipo de dado inteiro. |
| Separador de milhares | Informe qual caractere deverá ser utilizado como separador de milhares, por padrão o gerador não utiliza um separador de milhar. |
| Tipo de dado do sistema | Esta propriedade indica qual é o tipo mapeado do sistema para o tipo de dado selecionado e é somente informativa. |
| Valor nulo | Informe o valor que deverá ser utilizado quando o valor de origem for vazio ou nulo. |

#### Número Decimal

|  |  |
| --- | --- |
| Caractere de preenchimento | Informe qual caractere deverá ser utilizado para preenchimento do campo até o tamanho do campo. Por padrão o gerador irá preencher espaços em branco quando o tipo de dado é decimal. |
| Casas decimais | Informe o número de casas decimais que será utilizado para formatação do valor. |
| Modo de arredondamento | Selecione a forma como o gerador deverá fazer o arredondamento do número de acordo com o número de casas decimais. Você poderá fazer o arredondamento ou truncar o valor. |
| Modo de preenchimento | Selecione a forma como o texto deverá ser preenchido com o caractere de preenchimento. Por padrão o gerador não faz o preenchimento para o tipo de dado decimal. |
| Separador de milhares | Informe qual caractere deverá ser utilizado como separador de milhares, por padrão o gerador não utiliza um separador de milhar. |
| Separador decimal | Informe qual caractere deverá ser utilizado como separador decimal, por padrão o gerador irá utilizar o separador decimal padrão do sistema no momento da criação do Layout. |
| Tipo de dado do sistema | Esta propriedade indica qual é o tipo mapeado do sistema para o tipo de dado selecionado e é somente informativa. |
| Valor nulo | Informe o valor que deverá ser utilizado quando o valor de origem for vazio ou nulo. |

#### Data

|  |  |
| --- | --- |
| Caractere de preenchimento | Informe qual caractere deverá ser utilizado para preenchimento do campo até o tamanho do campo. Por padrão o gerador irá preencher espaços em branco quando o tipo de dado é data. |
| Máscara de formatação | Informe um máscara que será utilizada para formatação do valor. Por padrão o gerador irá utilizar a máscara "dd/MM/yyyy", exibindo dia, mês e ano.  Para mais informações consulte: <https://msdn.microsoft.com/en-us/library/8kb3ddd4(v=vs.71).aspx> |
| Modo de preenchimento | Selecione a forma como o texto deverá ser preenchido com o caractere de preenchimento. Por padrão o gerador não faz o preenchimento para o tipo de dado data. |
| Tipo de dado do sistema | Esta propriedade indica qual é o tipo mapeado do sistema para o tipo de dado selecionado e é somente informativa. |
| Valor nulo | Informe o valor que deverá ser utilizado quando o valor de origem for vazio ou nulo. |

#### Lógico

|  |  |
| --- | --- |
| Caractere de preenchimento | Informe qual caractere deverá ser utilizado para preenchimento do campo até o tamanho do campo. Por padrão o gerador irá preencher espaços em branco quando o tipo de dado é lógico. |
| Modo de preenchimento | Selecione a forma como o texto deverá ser preenchido com o caractere de preenchimento. Por padrão o gerador não faz o preenchimento para o tipo de dado lógico. |
| Texto falso | Informe o texto utilizado quando o valor de origem for falso. Por padrão o gerador utiliza o texto "False". |
| Texto verdadeiro | Informe o texto utilizado quando o valor de origem for verdadeiro. Por padrão o gerador utiliza o texto "True". |
| Tipo de dado do sistema | Esta propriedade indica qual é o tipo mapeado do sistema para o tipo de dado selecionado e é somente informativa. |
| Valor nulo | Informe o valor que deverá ser utilizado quando o valor de origem for vazio ou nulo. |
