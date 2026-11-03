---
content_hash: 9b83264be23f8aca5dfa21d7a8e9d9ade03e03857218cd3951f36df3db5cf64e
fetched_at: '2026-06-29T00:09:11.379719+00:00'
page_id: '403746935'
product: rm
source: tdn-rm
title: Utilização de Filtros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403746935
version: 10
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

   Os filtros são utilizados para melhorar a visualização dos registros em uma visão ou mesmo trazer aqueles que lhe fazem necessidade.

## **02. EXEMPLO DE UTILIZAÇÃO**

Para criar um filtro na visão dos sistemas clique no botão Filtros | Novo Filtro.

        Acessando Filtros | Novo Filtro você verá todos os filtros disponíveis para uso, bem como sua expressão de filtragem. Esta janela lhe oferece os recursos de Inclusão, Exclusão, Alteração, Renomear filtros e cópia de Filtros. Aqui determinado também qual filtro será usando todas as vezes que você abrir a visão do filtro.

Vejas os operadores disponíveis:

* **IGUAL A (=)** Retornar registros igual a um determinado valor passado pelo usuário
* **DIFERENTE DE (<>):**Retornar Registros diferentes de um determinado valor passado pelo usuário
* **MAIOR QUE(>):**Retornar Registros maiores que um determinado valor passado pelo usuário
* **MAIOR OU IGUAL A (>=):**Retornar maiores ou igual a de um determinado valor passado pelo usuário
* **MENOS QUE (<):**Retornar Registros menor que um determinado valor passado pelo usuário
* **MENOR OU IGUAL QUE (<=):**Retornar Registros menores ou iguais a um determinado valor passado pelo usuário
* **IS NULL:**Retornar registros com conteúdos nulos
* **IS NOT NULL:** Retornar registros com conteúdos não nulos
* **LIKE:** Determina se uma cadeia de caracteres (string) corresponde a um padrão especificado. Um padrão pode incluir caracteres normais e curingas.
* **NOT LIKE:** inverte a comparação, verificando se a cadeia de caracteres NÃO corresponde ao padrão especificado. Para utilizar intervalos de valores. Ao utilizar esse operador, tanto o campo Valor quanto o Valor Final ficam habilitados para que sejam informados os valores de início e fim.
* **IN (SQL):**Para utilizar uma sentença SQL como filtro. No campo Valor selecione a sentença SQL (que está cadastrada no menu Utilitários | Consultas SQL).
* **NOT IN (SQL):** Para utilizar uma sentença SQL como filtro. No campo Valor selecione a sentença SQL (que está cadastrada no menu Utilitários | Consultas SQL). Nesse caso, o resultado será contrário ao IN.
* **IN (VALORES):**Para utilizar mais de um valor no operador IN no campo selecionado.
* **NOT IN (VALORES):** Para utilizar mais de um valor no operador NOT IN no campo selecionado.

        Para os filtros de data existem datas dinâmicas: Ontem, Hoje, Amanhã, Nesta Semana, Neste Mês e Neste Ano. Essas datas dinâmicas e o calendário podem ser exibidos se o campo for do tipo data e clicando no ícone ...(reticências) do campo Valor. Ainda podem ser feitas manipulações nas datas dinâmicas.

 **EXEMPLO:**

* Para retornar lançamentos que vencem na próxima semana deve ser utilizado o campo "Vencimento", o operador deve ser "=" e o valor "Nesta Semana+1"
* Para utilizar um filtro que chama um segundo filtro utilize o botão "Novo grupo".
* Para utilizar uma sentença SQL como filtro utilize o operador IN e no campo Valor selecione a sentença SQL (que está cadastrada no menu Utilitários | Consultas SQL).
* Podem ser utilizados os conectivos "e" e "ou".

Importante

Ao utilizar o conectivo "**OU**" é necessário que a condição esteja entre parênteses "()".   
Para utilizar os parênteses basta clicarem em "**Novo Grupo**" e arrastar adicionar condições dentro.

# **Parâmetro Para o Filtro**

---

        Para utilizar um parâmetro no filtro selecione um campo da base de dados, o **Operador** ("=", "LIKE" ou outro) e no campo **Valor** informe:[Texto a ser exibido na execução do filtro], que funciona como um parâmetro.

Exemplo;   
  Operador: LIKE  
  Valor: [Nome do usuario]

Ao executar o filtro, na tela vai aparecer um local para informar o valor do parâmetro.

**OUTROS EXEMPLOS:** Visão de Clientes/Fornecedores:

* **CAMPO:** Nome Fantasia  
  **OPERADOR:** =  
  **VALOR:** [Nome]%  
  **RESULTADO ESPERADO:** Na execução do filtro, será solicitado o nome. Suponha que seja digitada somente a letra "A", então o filtro será de todos os nomes fantasia que começam com a letra A.
* **CAMPO:** Código  
  **OPERADOR:** BETWEEN  
  **VALOR:** [Início]  
  **RESULTADO ESPERADO:** Na execução do filtro, será solicitado o início e o fim. Suponha que seja digitado para o Início C00000 e para o Fim C99999, então o filtro retorna todos os Clientes que possuem código dentro do intervalo de C00000 a C99999.  Quando o parâmetro for do tipo data, será exibida uma máscara de data no campo. Caso queira, também pode se escolher a data clicando no botão de reticências, será exibido um calendário para se escolher a data do parâmetro.o no botão de reticências, será exibido um calendário para se escolher a data do parâmetro.

# **Expressão**

---

        O Campo expressão exibe todos os critérios do filtro que está sendo editado ou inserido, bem como a sua montagem e seu agrupamento. Para excluir os critérios do filtro selecione o critério e clique no primeiro X. Para excluir todos de uma vez só, clique no segundo X. Alem disso é possível alternar a ordem dos critérios, clicando nos critérios e clicando nas setas na barra de tarefas da expressão.  No critério do Filtro, você pode definir propriedades para cada item:

* **PROIBIR ALTERAÇÃO DE CRITÉRIO;** Na primeira coluna representada pelo Cadeado, caso ela esteja marcado o check, indica que é um critério que não poderá ser alterado.
* **PROIBIR VISUALIZAÇÃO DO CRITÉRIO:** Na segunda coluna representada por Pontos Coloridos, caso esteja marcado o check, indica que o usuário não irá visualizar o critério quando editar o filtro.
* **ACTION DE PESQUISA:**Na coluna Action, caso se escolha uma Action para associá-la ao critério, indica que caso o critério possua parâmetro, este poderá ser associado á um campo de pesquisa e o resultado dessa pesquisa irá preencher o parâmetro. Essa pesquisa será com base em um campo disponível pela Action.  Para definir a Action deve-se acessar á coluna de Actions e clicar no botão reticências. Isso irá abrir a tela de Auto Procura. Nessa tela será necessário preencher os campos:

***ACTION:***Defina a Action que será usada para efetuar a busca do registro.

***CAMPO CHAVE:***Campo que será usado para preencher o parâmetro do critério.

***CAMPO DE PESQUISA*:** Campo que será exibido no momento da execução do Filtro, para fazer a pesquisa do registro na Action.

**OBSERVAÇÕES:**

Esses itens são permitidos somente aos usuários que sejam Supervisores ou á usuários que sejam autorizados á Inserir\Editar Filtros Globais no Perfil á que eles pertencem.

**EXEMPLO:** Acesse a tela de Tabelas Dinâmicas e acesse o Gerenciador de Filtro. Crie um novo Filtro com o seguinte critério: CODCOLIGADA=\[CODCOLIGADA\]. Na coluna Action da expressão clique no botão de reticências. Na tela de Auto Procura preencha os campos da seguinte forma: Action: FinCFOAction

* Campo Chave{\*}: CODCOLIGADA
* Campo de Pesquisa{\*}: NOME

        Após o preenchimento clique em OK na tela de Auto Procura. Clique em OK na tela de criação de filtro. Nomeie o Filtro como "Exemplo de Action". Execute o Filtro criado. Será exibido à tela de Parâmetro do Filtro com o Campo CODCOLIGADA como lookup. Clique nas reticências. Faça a busca por um registro que exista na tabela de Cliente\Fornecedor. Após encontrar o registro dê um duplo clique ou clique em OK. O valor do campo CODCOLIGADA que estiver no registro que foi encontrado da tabela de Cliente\Fornecedor será utilizado para preencher o parâmetro. Clique em OK. Os registros serão filtrados com base na coligada escolhida.

**DICA:**  
O uso do "NOLOCK" nas consultas SQL melhora o desempenho e seu uso é incentivado principalmente nas consultas de tabelas muito grandes. Este recurso é exclusivo para bases SQL Server.

Veja como usar o "NOLOCK" em uma consulta:

* SELECT\* \* \*FROM\* NOME\_TABELA \*(NOLOCK){\*};

false

**Versão:** 12.01.XX
