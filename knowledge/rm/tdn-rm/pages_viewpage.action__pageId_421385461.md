---
content_hash: 331a4021d68f5d303944556ac2d9badaa36c265767ff86a766e7d2a63dd74bb0
fetched_at: '2026-06-29T00:09:16.128871+00:00'
page_id: '421385461'
product: rm
source: tdn-rm
title: Importar Insumos via Excel 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385461
version: 4
---

---

A importação de arquivos via Excel consiste em incluir insumos em um novo projeto ou em um projeto já existente. Com o intuito de remover a obrigatoriedade da utilização de licenças do Microsoft Office no ambiente, foram modificadas as formas de importação e exportação de informações de planilhas Excel, para permitir que o TOP trabalhe os dados de forma autônoma e independente da solução da Microsoft. Foi modificado o processo de importação mas o produto final não será modificado, serão realizadas as mesmas etapas de processo originais e as mesmas inclusões/alterações de registros de insumos no TOP. Esta opção somente ficará habilitada caso algum projeto esteja aberto e o usuário tenha permissão. A funcionalidade consiste em gerar uma planilha ou cenário espelho do arquivo Excel que se escolheu importar.

Passo a passo:

Arquivo (Localização + Nome): Informe a localização e o nome do arquivo a ser importado.

Colunas do Excel: Informe a posição das colunas na planilha Excel correspondentes aos campos Código, Descrição, Descrição Completa, Unidade, Grupo de Custo e Fracionamento para o Insumo e os campos Descrição do Preço, Valor e Valor Improdutivo para o preço do Insumo.

O campo Linha Inicial é utilizado devido a necessidade do arquivo Excel ter um cabeçalho ou identificação dos dados da importação, portanto deve ser indicado pelo usuário onde será o início da importação. Este campo é obrigatório seu preenchimento e somente poderá ser inserido números maiores que zero e terá o valor inicial igual a 1.

**Atenção:**

Para informar o número da coluna, tenha como referência a coluna A que é considerada como a coluna de número 1. Dessa forma, a coluna B será a de número 2 e assim, sucessivamente.

Aconselha-se que os arquivos de importação excel possuam informações preenchidas a partir da coluna A. Quando a coluna não estiver sido preenchida, a contagem de colunas será definida a partir da primeira coluna preenchida pois a importação excel utiliza o intervalo de colunas com dados, importando a partir da primeira coluna preenchida com valor. Exemplo:

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | B | C | D | E | F | G | H | I | J |
|  |  | **Código** | **Descrição** | **Unidade** | **Grupo de Custo** | **Fracionamento** | **Desc. do Preço** | **Valor** | **Valor Imp** |
|  |  | E00001 | Compactador | H | Equipamentos | S | Preço1 | 10,00 | 20,00 |
|  |  | E00002 | Betoneira | H | Equipamentos | S | Preço1 | 50,00 | 60,00 |

Caso o excel estiver preenchido de acordo com o exemplo acima, os índices a serem utilizados na parametrização da importação excel serão definidos a partir da primeira coluna preenchida, ou seja, o índice de número 1 estará relacionado a coluna C.

O código do insumo obedece à máscara do insumo definida nos , caso contrário, será exibida uma tela para que a máscara seja ajustada.

Caso a unidade do insumo que está sendo importado não esteja previamente cadastrada no sistema, será exibida uma tela para que uma nova unidade seja cadastrada ou associada ao insumo uma unidade equivalente.

Ao importar a planilha, caso a mesma esteja "aberta", é necessário que após alguma alteração, a planilha seja salva, pois caso contrário os dados modificados não serão importados.

Associação de Grupos de Custo: Associe os Grupos de Custos já cadastrados nos sistema aos Grupos de Custo a serem importados na planilha. Defina um Grupo de Custo default, que será aplicado quando o grupo de custo não for localizado.

Definir parâmetros: Informe se a planilha Excel possui linha de cabeçalho, se os preços importados serão ativados e se os códigos serão preenchidos com zero.

**Atenção:**

Caso seja importado mais de um preço para um mesmo insumo, somente o último preço importado será ativo.

**Observações:**

Se a célula que retorna o campo Código não for informada ou estiver em branco, o mesmo receberá o número do identificador (IDISM). Se a célula que retorna o campo Descrição não for informada ou estiver em branco, será atribuída a descrição do próximo registro que contenha o mesmo código, caso contrário o insumo não será importado.

**Exemplo:**  
No exemplo abaixo, o Insumo E00001 não possui descrição na primeira linha, portanto, no momento da importação o insumo assumirá a descrição da linha seguinte que possui o mesmo código. Caso o insumo da próxima linha possua código diferente, a descrição não poderá ser copiada e o mesmo não será importado.

| Código | Descrição | Unidade | Grupo de Custo | Fracionamento | Desc. do Preço | Valor | Valor Imp. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E00001 |  | H | Equipamentos | S | Preço 1 | 40,00 | 16,00 |
| E00001 | Compactador | H | Equipamentos | S | Preço 2 | 57,30 | 12,00 |

A célula que retorna o campo Descrição Completa poderá receber o valor do campo Descrição, porém não há obrigatoriedade em informar a coluna Descrição Completa.

Se a célula que retorna o campo Unidade estiver vazia, será atribuída ao insumo a unidade do próximo registro de mesmo código. Depois das validações anteriores, caso a unidade não tenha sido informada ou estiver vazia, será atribuída ao Insumo a unidade "UN".

**Exemplo:**  
No exemplo abaixo, o insumo E00001 não possui Unidade na primeira linha, portanto, no momento da importação o insumo assumirá a unidade da linha seguinte, desde que possua o mesmo código, caso contrário, o insumo assume a unidade 'UN'.

| Código | Descrição | Unidade | Grupo de Custo | Fracionamento | Desc. do Preço | Valor | Valor Imp. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E00001 | Compactador |  | Equipamentos | S | Preço 1 | 40,00 | 16,00 |
| E00001 | Compactador | H | Equipamentos | S | Preço 2 | 57,30 | 12,00 |

A busca pelo Grupo de Custo será efetuada utilizando o código ou a descrição.

Se a célula que retorna o campo Grupo de Custo não for informada ou estiver vazia, será atribuído o Grupo de Custo do registro seguinte de mesmo código do insumo, caso não tenha outro registro com o mesmo código será atribuído o Grupo de Custo definido como default.

Se a célula que retorna o campo Fracionamento não for informada ou estiver vazia, será atribuído o fracionamento do registro seguinte de mesmo código, caso contrário o registro será definido como fracionável.

Para que o insumo seja considerado como especializado, o campo 'Especializado' deve ser definido como 'SIM'. Caso esteja preenchido como 'NÃO' ou esteja sem preenchimento, o insumo será importado como um insumo comum.

**Produtos Vinculados:**

Na importação de insumos via Excel, é possível trazer os produtos vinculados, mesmo que os insumos já possuam códigos no sistema. Para isso, basta incluir na planilha de Excel as colunas "Produtos Vinculados" e "Produto Principal". Na coluna "Produtos Vinculados", insira os códigos dos produtos separados por ponto e vírgula (;). Na coluna "Produto Principal", marque com '1' o produto principal e com '0' para os demais.

**Atenção:** No momento da importação, informe no campo correspondente a qual coluna do Excel pertencem os dados de "Produtos Vinculados" e "Produto Principal".

Exemplo:

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Código** | **Descrição** | **Unidade** | **Grupo de Custo** | **Fracionamento** | **Desc. do Preço** | **Valor** | **Valor Imp.** | **Produtos Vinculados** | **Produto Principal** |
| E00001 | Compactador | H | Equipamentos | S | Preço 2 | 57,3 | 12 |  |  |
| E00001 | Compactador | H | Equipamentos | S | Preço 1 | 40 | 16 | 06.01;06.02 | 1;0 |

A planilha de exemplo acima ficaráconforme mostrado na imagem abaixo:

**Atenção:**

O insumo especializado somente será importado caso o insumo pai já exista na base ou na planilha a ser importada.

Caso a célula que retorna a Descrição do preço não for informada ou estiver vazia, será atribuída a descrição "Preço em  DD/MM/AAAA, onde DD/MM/AAAA refere-se a data".

Caso a célula que retorna o Preço não for informada ou estiver vazia, o preço não será importado.

Caso a célula que retorna o Valor Improdutivo não for informada ou estiver vazia, será importado valor 0 (zero).

Os demais campos Valor, Valor sem Lei e Valor Improdutivo serão importados com valor 0 (zero).

Caso o arquivo Excel possua mais de uma planilha, será importado apenas a primeira planilha do arquivo.

 Veja Também

---
