---
content_hash: 0e9bde35235c063f2ea3cca4e93bb4f48d6d90864bc23345a8f442621a52e387
fetched_at: '2026-06-29T00:12:03.605650+00:00'
page_id: '911866835'
product: rm
source: tdn-rm
title: RPT00033.1 Ordem de Execução
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=911866835
version: 5
---

# Índice:

---

2.\*ndice:

# Objetivo:

---

Neste documento será explicado e exemplificado o mecanismo de execução de Stored Procedures no RM Reports, tal qual informações de prioridade, execução e afins.

# StoredProcedures repetidas

---

No caso de **controles de StoredProcedure** apontados para a mesma **StoredProcedure**, esta será executada apenas uma vez.

### Exemplificando

Para exemplificar, abaixo está demonstrado um relatório contendo 5 controles de **StoredProcedure,**todos apontados para a mesma StoredProcedure, de nome **ATUALIZAR\_CONTADOR**. Esta Procedure tem como função inserir em uma tabela criada apenas para este exemplo, a contagem de registros que possuem na tabela naquele momento:

sql

Ao executar o relatório, podemos notar que, apenas de todas as bandas serem carregadas corretamente, apenas um registro foi realizado na tabela **EXEMPLO**, justamente pelo fato da StoredProcedure ter sido executada apenas uma vez:

# Antes ou depois de carregados os dados?

---

Para responder se uma StoredProcedure é executada ou não antes do carregamento dos dados do relatório é necessário compreender que existem dois tipos principais de StoredProcedure para a arquitetura do RM Reports: **Com parâmetros contextuais** e **sem parâmetros contextuais.**

## Stored Procedures com Parâmetros Contextuais

Essas são aquelas StoredProcedures que possuem parâmetros que dependem de um campo do relatório para serem resolvidos.

A procedure abaixo possui o parâmetro **CHAPA1:**

E para exemplificar, a procedure será utilizada em um relatório que percorre algumas linhas da tabela de Funcionários (**PFUNC**). Note que o campo destacado tem o mesmo nome do parâmetro (**CHAPA1**):

Este relatório será executado filtrando o Funcionário de chapa 00010:

Note que, ao realizar um **SELECT** na tabela **CHAPAS\_PFUNC** que antes estava vazia, agora está preenchida com a chapa 00010, proveniente do campo **CHAPA1:**

Dessa forma, podemos compreender que, caso a StoredProcedure possua parâmetros que dependam da execução do relatório (Como nesse caso, onde a StoredProcedure dependia do valor do campo **CHAPA1**), estas serão executadas na ordem em que estão posicionadas na banda. Mas e no caso de StoredProcedures que possuem parâmetros fixos (Parâmetros que não dependem da execução do relatório) ou mesmo nenhum parâmetro?

## Stored Procedures com Parâmetros Contextuais

No caso de StoredProcedures que possuem parâmetros fixos ou nenhum parâmetro, a **StoredProcedure** será sempre executada **ANTES** dos dados  serem buscados na base de dados ou resolvidos e carregados no relatório, independentemente de onde forem posicionados ou sequer de qual banda ela está posicionada.

Isso quer dizer que posicionar um controle de **StoredProcedure** no Cabeçalho, Rodapé ou no próprio Detalhe não o fará ser executado naquela ordem especificamente.

Isso ocorre porque o mecanismo de execução do RM Reports é arquiteturado para considerar que **StoredProcedures** sempre deverão ser executadas antes de qualquer busca de dados atrelados à banda ao qual pertence àquele controle de **StoredProcedure**

### Exemplificando

Para exemplificar, o código SQL mais acima será editado, mudando o nome do parâmetro para **CHAPA**. Este será o nome do parâmetro do novo relatório que será utilizado.

O relatório utilizado agora não percorrerá mais a tabela de Funcionários (PFUNC) e sim a tabela personalizada CHAPAS\_PFUNC, através da seguinte Consulta SQL:

Note que, para exemplificar, a procedure foi adicionada em um Subdetalhe relacionado ao Detalhe da tabela **CHAPAS\_PFUNC**. Pelo fato de essa tabela ser preenchida justamente pela procedure, se o fluxo normal fosse adotado e a banda de Detalhe fosse resolvida para então o Subdetalhe ser resolvido, nenhum dado seria retornado e o relatório ficaria vazio. Note também que o parâmetro CHAPA foi adicionado ao relatório como parâmetro fixo, de mesmo nome do existente na procedure.

Antes da execução, todas linhas da tabela **CHAPAS\_PFUNC** foram excluídas e durante a execução, a chapa passada é a chapa **00015**, para diferenciar do exemplo anterior:

E como resultado temos:

Esse resultado só é possível pelo fato de StoredProcedures que não dependem de campos do relatório serem executadas antes mesmo da primeira banda de Detalhe ser resolvida.

## Condensando tudo

Como exemplo final, vamos condensar tanto StoredProcedures contextuais quanto não contextuais em um só relatório. Este relatório possui duas procedures:

* **REGISTRA\_COLIGADA:** responsável por salvar o **CODCOLIGADA** da tabela **GCOLIGADA** dentro de uma tabela personalizada criada apenas para esse exemplo, através de um parâmetro fixo que representará o código da Coligada a ser buscado.
* **ATUALIZA\_COLIGADA**: responsável por salvar o **NOME** da tabela **GCOLIGADA** dentro da mesma tabela personalizada, de acordo com um parâmetro contextual que representará o código da Coligada a ser utilizado como base.

Desta forma, o código SQL será o seguinte:

Já o relatório será montado utilizando duas Consultas SQL trabalhando como Detalhe e SubDetalhe:

DetalheDetalhe

Dessa forma, espera-se que no Detalhe seja impresso o Código da Coligada e no subdetalhe, o Nome:

Note também que a StoredProcedure **REGISTRA\_COLIGADA**, que possui parâmetro fixo, foi adicionada ao Subdetalhe. Como explicado e exemplificado anteriormente, por se tratar de uma StoredProcedure não contextual, esta será executada antes de qualquer resolução de dados, então não importa onde ela é adicionada.

E ao executar:

# Concluindo

---

Sempre que houver inconsistências na execução de StoredProcedures em um relatório, se atente principalmente à se se trata de múltiplos controles de StoredProcedure atrelados à mesma procedure ou então se se trata da execução de StoredProcedures não contextuais em meio à contextuais, considerando que a primeira sempre executará anteriormente à segunda.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.20 ou Superiores

false

**Processo:** Uso de StoredProcedures

falsefalse

**Status:** Finalizado

false

**Data:** 07/02/2024

false

**Autores:**
