---
content_hash: 33543b0345bf03d3068a2fa885fba66e28b52164a235cb42ef0d8fbcb2d0bc7e
fetched_at: '2026-06-29T00:05:56.352565+00:00'
page_id: '149881513'
product: rm
source: tdn-rm
title: Utilizando a atividade "Para cada Iteração" e "Para cada Iteração API"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=149881513
version: 11
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Como utilizar a atividade "Para cada iteração" para executar em uma API**

**01. VISÃO GERAL**

O objetivo deste documento é mostrar como deve ser utilizada a atividade "Para cada Iteração" de uma Fórmula Visual.  Essa atividade cria um foreach na Fórmula Visual, percorrendo todos os registros. 

**02. EXEMPLO DE UTILIZAÇÃO**

      Para nosso exemplo, vamos utilizar as seguintes atividades: 

* Criar Coluna na Tabela
* Consulta SQL
* Para cada Iteração
* Sequência
* Localizar Registro na Tabela
* Expressão

      Essa Fórmula Visual adicionará uma coluna no grid da tela de Coligadas, chamada de 'Coluna\_Teste' e em cada linha terá a palavra 'Teste' antes do Nome da Coligada. 

Importante

Existe uma limitação ao usar atividade do tipo ' **ForEachActivity**' ou '**ForEachApiActivity**' junto a atividade de '**CodeActivity**'.

Ao utilizar essas atividades em conjunto, poderá acarretar na seguinte ocorrência:

Importante

Ao usar mais de uma atividade pai e filha do mesmo tipo ' ForEachActivity' ou 'ForEachApiActivity', a Fórmula Visual pode não executar como esperado. Não prestamos suporte a esse tipo de fluxo da Fórmula Visual, pois não é possível garantir o fluxo dos dados nos componentes.

Observamos que existe um fluxo conhecido desse cenário e existe uma solução de contorno que em alguns casos soluciona o problema. 

Na maioria dos casos que existe esse fluxo de atividades:  Foreach > Foreach > Consulta SQL > Se/Senão,  a atividade de Se/Senão, não consegue referenciar corretamente ao retorno da Consulta SQL. Na maioria dos casos, adicionar uma atividade de Expressão para receber a coluna da Consulta SQL e utilizar a expressão como fonte de dados para o Se/Senão, faz com que a Fórmula Visual funcione como esperado.

Exemplo do fluxo sem a atividade de expressãoExemplo do fluxo com a atividade de expressão

Adicionando a atividade de expressão como possível solução de contorno:

falseQuadro de passos1º Passo:

Primeiramente, é necessário arrastar a atividade "Criar Coluna na Tabela" para o "fluxo de trabalho" sequencial em sua fórmula visual.

Em seguida, preencha as propriedades como Nome da Coluna, que será o nome exibido no grid e a Tabela, que nesse exemplo será um DataTable.

2º Passo:

Depois, adicione uma atividade "Consulta SQL".

Clique com o Botão direito do mouse na atividade e selecione uma consulta SQL e localize a Consulta criada. 

Neste exemplo foi criada a consulta 'TesteColunaFV', com a seguinte query: "select codcoligada, nome from gcoligada (NOLOCK)".

Atividade de Consulta SQL na FV:

3º Passo:

Adicione a atividade 'Para cada Iteração'. Essa atividade permite fazer um fluxo de tarefas para cada item da coleção informada.

Neste exemplo, vamos usar a coluna criada na primeira atividade e percorrer suas linhas. 

| **Propriedades**   * **Nome:** Nome da Atividade * **Descrição:** Descrição da Atividade * **Habilitado:** Opção de habilitar ou desabilitar a atividade * Lista de Itens: Deve ser informado onde está a listagem que será percorrida no Foreach. |
| --- |

Atenção

As **iterações** da atividade **Foreach** são realizadas na propriedade **Lista de Items**, que tem como tipo da propriedade objetos **Ienumerable.**

4º Passo:

Adicione a atividade de sequência, para informar as atividades que serão feitas para cada item do foreach.

5º Passo:

A seguir, basta adicionar as atividades que serão executadas para cada linha.

Neste exemplo, com a atividade 'Localizar Registro na Tabela', vamos associar o registro da nova coluna com os resultados retornados na consulta SQL, por meio da PK, que é a CODCOLIGADA. 

6º Passo:

E por fim, com a atividade de 'Expressão', vamos alterar o texto que será inserido em cada linha da nova coluna.

Neste exemplo usaremos a string 'Teste' + nome da Coligada:

11º Passo:

salve a Fórmula Visual. Neste exemplo utilizamos o gatilho 'Após a Leitura da Visão' para o DataServer de Coligada.

Após abrir a tela de Coligada, foi exibida a coluna criada, como esperado.

      

**03. **COMO UTILIZAR A ATIVIDADE DE "PARA CADA ITERAÇÃO" PARA EXECUTAR EM UMA API****

      Em execuções em API, a atividade de foreach tem o mesmo comportamento do descrito acima. Mas é necessário utilizar a atividade 'Para Cada Iteração (API)'.

      No exemplo abaixo vamos mostrar como referenciar um campo da API como Lista de Itens do Foreach. Vamos considerar que o contexto de Coligada (CompanyCrudserver) já esteja selecionado.  Leia mais sobre [Fórmula Visual em API](https://tdn.totvs.com/x/9YynI). 

      Assim como as outras atividades em uma FV para API, após selecionar o Contexto e clicar em 'Ligações', serão listadas as propriedades da API do contexto para facilitar o uso da atividade. 

Importante!

* Lembre-se de que deve ser selecionado o objeto a ser percorrido. Nesse caso, nunca selecione o tipo, pois a tipagem não deve ser parte da estrutura de repetição.
* As **iterações** da atividade **ForeachAPI**são realizadas na propriedade **Lista de Items**, que tem como tipo da propriedade qualquer tipo de objeto presentes na estrutura Fields[] de um contexto de API
