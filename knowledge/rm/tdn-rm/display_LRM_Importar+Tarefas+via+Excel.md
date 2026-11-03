---
content_hash: f2eeecedb5e2283624eba8cc80cbe80bb0dffadd186f0d48bb07c3f68c34cd16
fetched_at: '2026-06-29T00:09:16.012736+00:00'
page_id: '421385440'
product: rm
source: tdn-rm
title: Importar Tarefas via Excel
type: documentation
url: https://tdn.totvs.com/display/LRM/Importar+Tarefas+via+Excel
version: 13
---

**Importar Tarefas via Excel**

---

A importação de arquivos via Excel consiste em incluir ou alterar tarefas em um projeto. Com o intuito de remover a obrigatoriedade da utilização de licenças do Microsoft Office no ambiente, foram modificadas as formas de importação e exportação de informações de planilhas Excel, para permitir que o TOP trabalhe os dados de forma autônoma e independente da solução da Microsoft. Permite realizar as mesmas etapas de processo originais e as mesmas inclusões/alterações de registros de tarefas no TOP, podendo ou não modificar o produto final.

Está opção somente ficará habilitada caso algum projeto esteja aberto e o usuário tenha permissão.

A funcionalidade consiste em gerar uma planilha ou cenário espelho do arquivo Excel que se escolheu importar.

**Campos disponíveis na importação**:

**Cenário:** Informar para qual cenário ou planilha será realizada a importação das tarefas

**Linha Inicial:** O campo Linha Inicial é utilizado devido a necessidade do arquivo Excel ter um cabeçalho ou identificação dos dados da importação, portanto deve ser indicado pelo usuário onde será o início da importação. Este campo é obrigatório seu preenchimento e somente poderá ser inserido números maiores que zero e terá o valor inicial igual a 1.

**Arquivo (Localização + Nome):** Informe a localização e o nome do arquivo a ser importado.

**Colunas do Excel:** São as colunas do Excel relativas aos campos da tarefa para a importação. Salientando que os Campos Livres parametrizados para o projeto também serão passíveis de importação.

**Codificar automaticamente:** Se necessário gerar a codificação automática das tarefas, marque a opção codificar automaticamente. Neste caso, Identificador de Obras deverá ser informado, com o número da coluna na planilha que contém os asteriscos, que indicam quais tarefas devem ser consideradas como obra.

Para usar esta opção, obrigatoriamente o primeiro item a ser importado precisa ser uma obra. Informe o número da coluna (no arquivo Excel) que corresponde aos campos Código, Nome, Descrição, Código Auxiliar da Tarefa, Quantidade, Unidade, Valor Cotado, Descrição Completa, Cód.. Recurso, Tipo Rec (G/L) e BDI Dif.. Caso não exista algum desses campos na planilha, preencha a coluna do Excel correspondente, com valor zero. Se a opção de codificar automaticamente esteja habilitada o campo Código ficará inativo.

**Unidade de Serviço:**Para que a associação da Unidade de Serviço na tarefa possa ser importada, é necessário que a mesma esteja cadastrada no projeto.

**Local de Serviço:**Para que a associação do Local de Serviço na tarefa possa ser importada, é necessário que a mesma esteja cadastrada no projeto.

**Disciplina:** Para que a associação da Disciplina na tarefa possa ser importada, é necessário que a mesma esteja cadastrada no projeto.

**Natureza Orçamentária:** Para que a associação da Natureza Orçamentária na tarefa possa ser importada, é necessário que a mesma esteja cadastrada na coligada ou existir a utilização de Natureza Orçamentária Global. A Natureza Orçamentária será associada se as seguintes regras forem atendidas: Se estiver parametrizado para Utilizar Controle Orçamentário a utilização deve ser na Tarefa, e se não utiliza o Controle Orçamentário a Tarefa deve ser de Valor Cotado.

**Grupo Orçamentário:** Para que a associação do Grupo Orçamentário na tarefa possa ser importado, é necessário que o mesma esteja cadastrado na coligada. O Grupo Orçamentário será associado se as seguintes regras forem atendidas: Se estiver parametrizado para Utilizar Controle Orçamentário a utilização deve ser na Tarefa, e se não utiliza o Controle Orçamentário a Tarefa deve ser de Valor Cotado.

**Atualizar tarefas existentes:** Caso não esteja marcado e a tarefa já existir, a mesma não será atualizada.

**Atenção:**  
Para informar o número da coluna, tenha como referência a coluna A que é considerada como a coluna de número 1. Dessa forma, a coluna B será a de número 2 e assim, sucessivamente.  
   
Aconselha-se que os arquivos de importação Excel possuam informações preenchidas a partir da coluna A. Quando a coluna não estiver sido preenchida, a contagem de colunas será definida a partir da primeira coluna preenchida pois a importação Excel utiliza o intervalo de colunas com dados, importando a partir da primeira coluna preenchida com valor.

Esta importação será realizada tarefa por tarefa. Desta forma, caso alguma tarefa gere erro na inserção ou alteração, as outros serão importadas normalmente e o log irá apresentar os erros detectados.

**Exemplo:**

   
Caso o Excel estiver preenchido de acordo com o exemplo acima, os índices a serem utilizados na parametrização da importação Excel serão definidos a partir da primeira coluna preenchida, ou seja, o índice de número 1 estará relacionado a coluna C.

A coluna Vínculo Serviço será utilizada para fazer a associação entre a planilha de serviço e de atividade, neste campo deverá ser informado um código de tarefa da planilha de serviço.

A coluna Quantidade Vínculo irá informar a quantidade desejada no vínculo. Esta quantidade está limitada à quantidade do serviço e caso seja menor que o valor da importação, será exibido no log. Caso esta coluna não seja informada, a tarefa receberá o saldo disponível do serviço para vinculação.

**Observações:**

Se a célula que retorna o campo Nome estiver com o número zero, será preenchido no campo nome, após importação o texto 'Tarefa sem Nome'.

Se a célula que retorna o campo Descrição estiver com o número zero, será preenchido no campo descrição, após importação o texto 'Tarefa sem Descrição'.

Se a célula que retorna o campo Unidade estiver com o número zero, será exibida uma tela onde deverá se informada uma unidade default.

Se a célula que retorna o campo BDI Diferenciado estiver com o número zero, após importação o campo DBI da tarefa será preenchido com '1'.

Na importação da associação do recurso à tarefa, é verificado se existe algum insumo ou alguma composição com o código informado. Caso seja encontrado um insumo e uma composição com o mesmo código do recurso no arquivo, será exibido uma tela para o usuário informar qual dos recursos irá ser utilizado (insumo ou composição) para aquela tarefa.

Se a unidade da tarefa não existir no Cadastro de Unidades, será exibida a janela de Importação de Unidade para a tarefa. Através dessa janela a unidade pode ser convertida para uma que já exista ou inserida. Se o código da tarefa já existir, o mesmo será ignorado.

A máscara da tarefa que está sendo importada tem que estar igual ao parâmetro 'Máscara da Tarefa', definida nos parâmetros do projeto.

As Etapas não podem ter quantidade.

Todas as linhas em branco existentes na planilha serão desconsideradas pelo sistema.

O campo "Linha inicial", localizado na tela "Importar Tarefa via Excel", se refere às linhas com dados preenchidos. Ao preencher este campo, desconsidere eventuais linhas em branco no início do arquivo.

Em projetos cujo status é: paralisado ou concluído ou revisado ou cancelado não será permitida a importação de tarefas via Excel.

Se o campo 'Código da obra' estiver em branco a obra e suas 'filhas' não serão importadas.

Se o campo 'Código da Tarefa' estiver em branco a tarefa não será importada.

Se a célula que retorna o campo Tipo Recurso (Global ou Local) estiver em branco, o mesmo será preenchido como 'Local'.

**Atenção:**

Após importação deve-se realizar o cálculo do projeto, e atualizar a planilha ou o cenário para carregar os valores.  
Em um comportamento anterior, quando uma tarefa era importada sem valor ou recurso associado, somente quantidade, a mesma era importada como Etapa. Hoje o comportamento é outro, a tarefa, mesmo sem valor ou recursos, caso possua quantidade, será importada como serviço.

Durante a importação de tarefas via MS-Excel, o usuário pode importar para as duas planilhas (atividade e serviço) ou optar por uma das planilhas.

Nessa funcionalidade agora é possível alterar informações da tarefa pelo processo de importação:

Exemplo:

Alterando a quantidade na planilha o processo de importação atualiza no sistema.

- Planilha antes da importação:

- Utilizando o Excel baixo:

Planilha após a importação:
