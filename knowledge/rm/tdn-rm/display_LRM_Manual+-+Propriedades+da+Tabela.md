---
content_hash: 5b906b7b903315f625e762174be2fd38d1784c38dd396d137f0455664672a48c
fetched_at: '2026-06-29T00:08:47.292515+00:00'
page_id: '319787291'
product: rm
source: tdn-rm
title: Manual - Propriedades da Tabela
type: documentation
url: https://tdn.totvs.com/display/LRM/Manual+-+Propriedades+da+Tabela
version: 3
---

Na janela de propriedades da tabela é possível definir quais campos e tabelas do banco de dados serão utilizados para compor a tabela do contexto. Estas configurações serão utilizadas para gerar dinâmicamente a sentença SQL de SELECT para leitura do banco. Cada tabela do contexto pode conter campos de mais de uma tabela do banco, feito através de um relacionamento entre elas (LEFT JOIN).

Ao criar uma tabela é necessário selecionar uma tabela base e pelo menos um campo da tabela. Para adicionar um relacionamento entre elas, clique no botão Adicionar Relacionamento e informe as colunas do Join. O gerador RM verifica o cadastro da GLINKSREL para sugerir automáticamente os relacionamento.

Também é possível fazer operações de agrupamento (GROUP BY), ordenação (ORDER BY) e filtro (WHERE).

![](/download/attachments/319787291/propriedades_da_tabela.png?version=1&modificationDate=1512921892000&api=v2)

1Tabela Base

Selecione a tabela do banco de dados que será a base da sentença SQL que será gerada para fazer a leitura dos dados.

2Nome

Informe o nome da tabela no conjunto de dados, este nome pode ser o mesmo da tabela base porém não pode ser repetido para mais de uma tabela/consulta do conjunto de dados.

3Tempo Limite

Informe um tempo máximo para leitura dos dados da tabela no banco de dados (em segundos). Caso o tempo de leitura seja ultrapassado, ocorrerá um erro de timeout no momento da geração.

4Transformar colunas em registro

Selecione esta opção para transformar as colunas da tabela em registro, quando esta opção é selecionada, o gerador irá criar uma coluna chamada NOME e outra chamada VALOR contendo o nome do campo e o seu valor correspondente agrupado pela chave primária do tabela.

5Pesquisar Campo

Utilize a caixa de pesquisar campo para localizar um campo na lista de tabelas e campos utilizados para geração da senteça.

6Campos

Selecione todos os campos que serão retornados para a tabela do conjundo de dados.

7Alias

Informe um nome para identificar o campo na tabela do conjunto de dados, este nome pode ser o mesmo nome do campo, porem não podem ter dois campos com o mesmo Alias na tabela, caso seja selecionado dois campos com o mesmo nome, o gerador irá sugerir o nome do alias concatenando um número para cada campo repetido. Esta informação é utilizada para definir a clausula AS na senteça SQL para as tabelas e/ou campos do SQL.

8Agrupamento

Selecione a forma de agrupamento do campo. Quando um agrupamento diferente de Default é utilizado, o gerador irá adicionar uma clausula GROUP BY na instrução SQL gerada, contendo todos os campos que a opção de agrupamento seja Default e fazendo as operações de agrupamento nos outros campos.

9Adicionar Relacionamento

Clique para adicionar um relacionamento entre mais de uma tabela do banco de dados na sentença SQL (LEFT JOIN). Para mais informações consulte [Relacionamento da Tabela](/display/LRM/Manual+-+Relacionamento+da+Tabela).

10Filtro

Exibe a expressão do filtro de leitura da tabela, o filtro será utilizado para montagem da cláusula WHERE da sentença SQL gerada. Para mais informações consulte [Filtro da Tabela](/display/LRM/Manual+-+Filtro+da+Tabela+do+Conjunto+de+Dados).

11Alterar Filtro

Clique para alterar o filtro de leitura da tabela.

12Limpar Filtro

Clique para limpar o filtro de leitura da tabela.

13Filtro do Usuário

Exibe as configurações do filtro do usuário para a tabela. Para mais informações consulte [Filtro do Usuário](/pages/viewpage.action?pageId=319787294).

14Ordenação

Exibe as colunas de ordenação da tabela, essas colunas serão utilizadas para geração da cláusula ORDER BY da sentença SQL gerada. Para mais informações consulte [Ordenação da Tabela](/pages/viewpage.action?pageId=319787295).

15OK

Clique para salvar as propriedades da tabela.

16Cancelar

Clique para cancelar as alterações na tabela.
