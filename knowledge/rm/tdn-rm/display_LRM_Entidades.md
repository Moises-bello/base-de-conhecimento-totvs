---
content_hash: f05e41e076d41e4a33201b845a0c6cc4251718d03b66072230f5fc4faeb7ea0b
fetched_at: '2026-06-29T00:08:45.592907+00:00'
page_id: '311632318'
product: rm
source: tdn-rm
title: Entidades
type: documentation
url: https://tdn.totvs.com/display/LRM/Entidades
version: 63
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é trazer uma visão de como funciona a tela de Entidades.

# Introdução:

---

       Para determinar quais campos serão utilizados pelo relatório é necessário criar uma entidade de sua [Fonte de Dados](http://tdn.totvs.com/x/uCGTEg).

# Como criar:

---

       Para criar uma nova Entidade, basta clicar em "+ Novo" e informar os campos abaixo:

***Fonte de dados:***Informe de qual [Fonte de Dados](http://tdn.totvs.com/x/uCGTEg), cadastrada anteriormente, as informações serão buscadas.

***Nome da Entidade:***Este campo é automaticamente preenchido com o nome da sua Fonte de Dados, mas pode ser alterado.

O nome da entidade não deve começar com números, ou conter apenas números.

***Descrição:*** Informe uma descrição.

Entidade1Campos da entidade

Selecione os campos que serão utilizados no relatório.

Utilize "Pesquisar coluna" para facilitar a busca, caso a entidade tenha muitas colunas.

Utilize os filtros para buscar pelos campos já selecionados ou sem seleção.

***Exemplo prático abaixo:***

2Campos relacionais

500350

    Assista ao vídeo com áudio para compreender a funcionalidade de Campos Relacionais.

false

       Só será possível cadastrar um campo relacional, quando a Fonte de Dados utilizar conexão com um Provedor Integrado e for do tipo Tabela.

       Na estrutura do relatório é necessário informar qual será o Membro de Dados (Entidade) de cada detalhe. Quando necessário utilizar um campo na mesma banda do relatório, que não pertence a Fonte de Dados cadastrada, é possível criar um campo relacional.

Ex: No detalhe do relatório será mostrado os dados de um funcionário e de sua seção. Como a tabela de Funcionários não possui os dados completos de sua seção, será necessário criar um campo relacional.

Para cadastrar um ou mais campos relacionais, basta selecionar a guia "Campos Relacionais" e clicar em "+ Adicionar" seguindo os passos abaixo:

Campos1Inicio

       Primeiramente, utilize o lookup para pesquisar a tabela que servirá como fonte de dados para as colunas virtuais.

       Prosseguindo com o exemplo citado acima, vamos selecionar a tabela "PSECAO".

       Em seguida, selecione os campos que serão utilizados no relatório e clique em "*Próximo*".

Utilize "Pesquisar coluna" para facilitar a busca, caso a entidade tenha muitas colunas.

Utilize os filtros para buscar pelos campos já selecionados ou sem seleção.

2Passo 2

       Na fase dois (“*Relação*”) há dois caminhos a se seguirem.

       O primeiro trata do relacionamento direto: Quando encontrado relacionamento direto, o wizard avançará para a fase 3 (“*Resumo*”) e apresentará a ligação definida.

3Passo 3

       O segundo trata do relacionamento intermediário: Quando não há um relacionamento direto entre duas tabelas, é possível utilizar uma tabela intermediária.

       Utilizamos como exemplo a tabela PFUNC, PPESSOA e GIMAGEM para retornar a imagem do colaborador. As tabelas PFUNC e GIMAGEM não fazem relacionamento direto, então a PPESSOA será intermediária nessa ligação.

       Para isso, na fase 1 ("Inicio") pesquise pela tabela onde a informação desejada se encontra. Selecionamos o campo IMAGEM, na tabela GIMAGEM. Clique em próximo.

       Na fase 2 (“Relação”) selecione no combo a tabela que fará a ligação intermediaria. Feita a seleção, clique em adicionar.

false

Quando o relacionamento apresentar mais de uma opção entre a tabela intermediária e final, o sistema criará outro combo. Nesta fase, denominado “Relacionamentos Disponíveis”. Neste momento, escolha o relacionamento entre a tabela intermediária e final do campo relacional.

       Finalizada a seleção do caminho, clique em adicionar novamente para que o caminho seja montado e visualizado na parte superior da fase. Clique em próximo para avançar para fase 3. Na fase 3, clique em “Finalizar”.

false

A opção “Buscar Relacionamentos Diretos” estará sempre disponível na fase 2 (“Relação”). Ela lista todas as tabelas que se relacionam diretamente com a tabela corrente.

Não necessariamente as tabelas listadas vão chegar ao destino final desejado.

Essa opção deve ser utilizada quando o usuário conhecer as tabelas do banco e já souber o caminho desejado para chegar em sua tabela destino.

3Campos SQL

       Campos SQL têm a finalidade de permitir a interação entre os dados de Entidades distintas.

Ex: Uma consulta SQL que retorna determinadas informações de um funcionário, porém precisa de um parâmetro que é o identificador do Funcionário. Sabe-se que existe uma Entidade cadastrada que retorna o campo Identificador do Funcionário.

Dessa forma, através dos Campos SQL é possível ligar os parâmetros da Consulta SQL aos campos de uma ou mais Entidades.

É importante que na estrutura do Relatório, as Entidades ligadas aos parâmetros estejam na mesma banda ou em bandas superiores a Consulta SQL.

Para cadastrar um ou mais campos SQL, basta selecionar a guia "Campos SQL" e clicar em "+ Adicionar" seguindo os passos abaixo:

Campos SQL

***Alias:*** Informe o alias de sua Consulta SQL

***Sentença SQL:*** Digite a sentença SQL

Seguindo o exemplo citado acima, vamos cadastrar uma Consulta SQL que precisará de dois parâmetros que são retornados pela Entidade "Funcionário" e um parâmetro geral.

Nesta consulta, a tabela PFHSTSAL tem as informações de histórico salarial de um Funcionário e retornará o ultimo salário recebido, antes do salário atual.

sql

Recomendamos que a consulta retorne resultados 1x1.

Caso a consulta retorne 1xN, somente a primeira linha retornada será exibida no relatório.

Note que a opção "Ligar parâmetros" aparece na tela. Clique nela para vincular os parâmetros da sentença aos parâmetros cadastrados ou aos parâmetros de Entidade.

Ligação de Parâmetros1Parâmetro Gerais

Continuando com o exemplo citado acima, 1 dos 3 parâmetros da Consulta será buscado dos parâmetros gerais (que são parâmetros cadastrados previamente e podem ter seu valor alterado na hora de geração do relatório).

Nesse caso, o parâmetro "CODIGO" foi ligado à um Parâmetro Geral.

Caso o parâmetro ainda não tenha sido cadastrado, clique na opção "Adicionar parâmetros" para adicionar um novo parâmetro e vincular o mesmo a sua consulta SQL.

2Parâmetros de Entidades

Continuando com o exemplo citado acima, 2 dos 3 parâmetros da Consulta serão buscados dos parâmetros de entidades.

Neste caso, deve-se escolher a Entidade e a coluna correspondente em que o valor será buscado.

É recomendado salvar o cadastro da Entidade antes de prosseguir para a etapa de Parâmetros da Entidade, para que assim os dados da Entidade atual sejam exibidos corretamente na listagem.

Um mesmo parâmetro só pode ser ligado em uma das abas, ou seja, ele não pode ser ligado à um parâmetro geral e à um parâmetro de entidade ao mesmo tempo.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.22 ou Superiores

false

**Processo:** Entidades

falsefalse

**Status:** Em elaboração

false

**Data:** 08/12/2017

false

**Autores:**
