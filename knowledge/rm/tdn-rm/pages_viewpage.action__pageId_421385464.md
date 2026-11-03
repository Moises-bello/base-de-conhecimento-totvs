---
content_hash: 6f23ded150ccdd13d81e1acd9e79e2e3945c35173daf577ae7e35b6880684d11
fetched_at: '2026-06-29T00:09:16.147804+00:00'
page_id: '421385464'
product: rm
source: tdn-rm
title: Importação de Composição via Excel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385464
version: 3
---

**Importação de Composição via Excel**

---

A importação de arquivos via Excel consiste em incluir composições em um novo projeto ou em um projeto já existente. Com o intuito de remover a obrigatoriedade da utilização de licenças do Microsoft Office no ambiente, foram modificadas as formas de importação e exportação de informações de planilhas Excel, para permitir que o TOP trabalhe os dados de forma autônoma e independente da solução da Microsoft. Foi modificado o processo de importação mas o produto final não será modificado, serão realizadas as mesmas etapas de processo originais e as mesmas inclusões/alterações de registros de composições no TOP. Esta opção somente ficará habilitada caso algum projeto esteja aberto e o usuário tenha permissão. A funcionalidade consiste em gerar uma planilha igual ao arquivo Excel que se escolheu importar.   
   
O campo Linha Inicial é utilizado devido a necessidade do arquivo Excel ter um cabeçalho ou identificação dos dados da importação, portanto deve ser indicado pelo usuário onde será o início da importação. Este campo é obrigatório seu preenchimento e somente poderá ser inserido números maiores que zero e terá o valor inicial igual a 1.  
Passo a passo:  
Acesse (local Utilitários | Conversões | Importar Arquivos Excel | Importar Composições Via Excel)  
Arquivo (Localização + Nome): Informe a localização e o nome do arquivo a ser importado.  
Colunas do Excel: Informe a posição das colunas na planilha Excel corresponde aos campos Código, Descrição, Descrição Completa, Unidade, Tipo da Composição e Produção por Hora para a Composição e os campos Código, Quantidade, Coeficiente Produtivo, DMT para os recursos da Composição.

**Atenção:**

Para informar o número da coluna, tenha como referência a coluna A que é considerada como a coluna de número 1. Dessa forma, a coluna B será a de número 2 e assim, sucessivamente.  
Aconselha-se que os arquivos de importação excel possuam informações preenchidas a partir da coluna A. Quando a coluna não estiver sido preenchida, a contagem de colunas será definida a partir da primeira coluna preenchida pois a importação excel utiliza o intervalo de colunas com dados, importando a partir da primeira coluna preenchida com valor. Exemplo:

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | B | C | D | E | F | G | H | I | J | K |
|  |  | **Código** | **Descrição** | **Unidade** | **Tipo da Composição** | **Produção por Hora** | **Código** | **Quantidade** | **Coef. Produtivo** | **DMT** |
|  |  | 000005 | Escavação de tubulões | M3 | 1 | 10 | E00001 | 2 | 7 | 5 |
|  |  | 000006 | Escavação de Terreno | M3 | 1 | 20 | E00002 | 5 | 7 | 5 |

Caso o excel estiver preenchido de acordo com o exemplo acima, os índices a serem utilizados na parametrização da importação excel serão definidos a partir da primeira coluna preenchida, ou seja, o índice de número 1 estará relacionado a coluna C.  
O código do insumo obedece a máscara do insumo definida nos Parâmetros do Projeto, caso contrário será exibida uma tela para que a máscara seja ajustada. Caso a unidade do insumo que está sendo importado não esteja previamente cadastrada no sistema, será exibida uma tela para que seja cadastrada uma nova unidade ou associado ao insumo uma unidade equivalente.  
Ao importar a planilha, caso a mesma esteja "aberta", é necessário que após alguma alteração, a planilha seja salva, pois caso contrário os dados modificados não serão importados.  
Definir parâmetros: Informe se a planilha Excel possui linha de cabeçalho e se os dados a serem importados devem sobrescrever os dados já existentes no projeto.

**Atenção:**

Caso seja importado mais de um preço para um mesmo insumo, somente o último preço importado será ativado.

**Observações:**

**Referente à Composição:**

Se a célula que retorna o campo Código não for informada ou estiver em branco, o mesmo receberá o número do identificador (IDCMP).  
Se a célula que retorna o campo Descrição não for informada ou estiver em branco, será atribuída a descrição do próximo registro que contenha o mesmo código, caso contrário a composição não será importada e um log será gerado.

**Exemplo:**

No exemplo abaixo a descrição da composição 000005 não foi informada na primeira linha da planilha. No momento da importação, será adicionada a mesma a descrição da proxima linha de mesmo código. Caso contrário a composição não será importada.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Código** | **Descrição** | **Unidade** | **Tipo da** **Composição** | **Produção por Hora** | **Código** | **Quantidade** | **Coef. Produtivo** | **DMT** |
| 000005 | Escavação de Tubulões | M3 | 1 | 10 | E00001 | 2 | 7 | 5 |
| 000005 |  | M3 | 1 | 10 | F00004 | 3 | 4 | 2 |

A célula que retorna o campo Descrição Completa poderá receber o valor do campo Descrição, porém não há obrigatoriedade em informar a coluna Descrição Completa. Se a célula que retorna o campo Unidade estiver vazia, será atribuída ao insumo a unidade do próximo registro de mesmo código. Depois das validações anteriores, caso a unidade não tenha sido informada ou estiver vazia, será atribuída à Composição a unidade "UN". Caso a Unidade informada não esteja previamente cadastrada no projeto, o será exibida uma tela para que uma nova unidade seja cadastrada ou associada a uma unidade equivalente.

**Exemplo:**

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Código** | **Descrição** | **Unidade** | **Tipo da** **Composição** | **Produção por Hora** | **Código** | **Quantidade** | **Coef. Produtivo** | **DMT** |
| 000005 | Escavação de Tubulões | M3 | 1 | 10 | E00001 | 2 | 7 | 5 |
| 000005 | Escavação de Tubulões | M3 | 1 | 10 | F00004 | 3 | 4 | 2 |

Sugere-se a utilização de colunas diferentes para descrição da composição e descrição do recurso, para evitar falhas de preenchimento pelo usuário, pois caso seja a mesma coluna será criada uma composição com a descrição do insumo.

**Exemplo:**

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Código** | **Descrição** | **Descrição Recurso** | **Unidade** | **Tipo daComposição** | **Produção por Hora** | **Código** | **Quantidade** | **Coef. Produtivo** | **DMT** |
| 000005 | Escavação de Tubulões | Escavadeira | H | 1 | 10 | E00001 | 2 | 7 | 5 |
| 000005 | Escavação de Tubulões | Areia | M3 | 1 | 10 | F00004 | 3 | 4 | 2 |

Pode ser criado um registro para composição ou suas informações podem ser preenchidas no primeiro recurso.

**Exemplo:**

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Código** | **Descrição** | **Descrição Recurso** | **Unidade** | **Tipo daComposição** | **Produção por Hora** | **Código** | **Quantidade** | **Coef. Produtivo** | **DMT** |
| 000005 | Escavação de Tubulões |  | H | 1 |  |  |  |  |  |
| 000005 |  | Areia | M3 | 1 | 10 | F00004 | 3 | 4 | 2 |

A célula que retorna o campo Tipo da Composição pode assumir os valores 0, 1, 2 ou 3 que corresponde à CPU, Por produção, Turma Típica e Por Unidade de Serviço, respectivamente. Caso sejam informados valores diferentes dos citados ou a coluna referente à planilha Excel não for informada, o Tipo da Composição será definido como CPU. Caso a coluna referente ao tipo da Composição na planilha Excel estiver vazia será lançado o tipo da Composição da primeira linha preenchida, caso contrário será atribuído 0 - CPU ao tipo da Composição.  
O campo Produção por Hora será importado somente se o Tipo da Composição estiver definido como 1 – Por Produção. Caso a linha referente à coluna da planilha Excel não for informada, o campo Produção por Hora receberá valor 1. Caso a célula informada estiver vazia, o sistema percorrerá todas as linhas e atribuirá o valor da Produção por Horas da primeira preenchida, caso contrário será atribuído valor 1.

**Processo**

Ao importar a composição via Excel mesmo sem a opção sobrescrever, o sistema listar as composições que já existem e mudam os preços com a nova inserção de insumos.

* Quantidade de Composições Criadas
* Quantidade de Composições Alteradas
* Quantidade de composições que não formam alteradas, pois não estava marcado para atualizar
* Informar uma um log separado quais as composições estão em cada um dos cenários.

**Referente ao recurso da composição:**

O campo Código receberá o valor correspondente ao código do recurso da composição. Caso o valor referente à coluna Excel não for informada ou o valor do campo estiver vazio, o recurso não será importado e um log será gerado.

O campo Quantidade receberá o valor referente à quantidade do recurso. Caso o recurso seja um insumo não fracionável, sua quantidade será arredondada e a informação será adicionada ao log. Caso o recurso for uma composição por Turma Típica, os valores de suas quantidades somadas devem totalizar 1, caso contrário o recurso não será importado e a informação será adicionada ao log. O campo Coeficiente Produtivo receberá o valor do coeficiente produtivo da composição, sendo que essa informação será importada somente se todas as condições seguintes forem atendidas:   
O recurso deve ser um insumo; O insumo deve ser do tipo Equipamento (A); A composição que está sendo importada deve ser do tipo Produção por Hora ; A célula deve estar preenchida; O número da coluna Excel referente ao Coeficiente Produtivo deve ser informado. Caso alguma das condições acima não for atendida, o Coeficiente Produtivo será definido como 1.

**Atenção:**

Quando o parâmetro "Aceita Coeficiente Improdutivo Igual a Zero" estiver marcado e o coeficiente produtivo for definido como 1, o processo de importação será realizado. Quando o parâmetro estiver desmarcado e o coeficiente produtivo estiver definido como 1 ou não for informado, que nesse caso por definição é igual a 1, o recurso não será importado e a informação será adicionada ao log.  
O campo DMT (Distância Média de Transporte) receberá o valor referente ao campo DMT do recurso, sendo que a informação será importada apenas se as condições seguintes forem atendidas:  
O recurso deve ser um insumo ou composição; O insumo ou composição deve ser do tipo Transporte (F); A composição que está sendo importada deve ser do tipo Produção por Hora; A célula deve estar preenchida; O numero referente a coluna Excel referente ao DMT deve ser informado. Caso alguma das condições acima não for atendida, o DMT será definido como 1.  
Caso algum Insumo ou Composição que estiver sendo importada tenha o mesmo código de um Insumo ou Composição cadastrado no projeto, será exibida uma tela para que seja escolhido como o recurso será importado, Insumo ou Composição. Caso a opção Ignorar seja escolhida, o recurso não será importado.

**Definição de Parâmetros:**

**Sobrescrever**:

Marque essa opção se desejar sobrescrever os dados das composições e recursos cadastrados no projeto, com os dados importados da planilha do Excel. Caso o parâmetro sobrescrever for selecionado os dados das composições e seus respectivos recursos que estiverem no projeto serão substituídos pelos dados das composições e recursos de mesmo código que estiverem no Excel. Caso o parâmetro sobrescrever não for selecionado os dados das composições e seus respectivos recursos que estiverem no projeto não serão substituídos pelos dados das composições e recursos de mesmo código que estiverem no Excel. Mas ainda será importado caso existam novos recursos.
