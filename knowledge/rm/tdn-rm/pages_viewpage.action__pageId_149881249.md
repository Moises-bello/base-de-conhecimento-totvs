---
content_hash: dcec5ae0196076a9f16c6e459daa9b2f4d3504b05ea592c16f08a83cef40fde6
fetched_at: '2026-06-29T00:05:56.016423+00:00'
page_id: '149881249'
product: rm
source: tdn-rm
title: Utilizando a atividade "Aplicar Alterações na Tabela"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=149881249
version: 21
---

# Objetivo:

---

     Este documento tem como finalidade, demonstrar o uso da atividade **"Aplicar Alterações na Tabela"**.

# Configuração:

---

## Informações Gerais

### Objetivo:

A finalidade da atividade "Aplicar Alterações na Tabela" é permitir que o usuário sinalize que uma fonte de dados (sendo ela, conjunto de tabelas, uma única tabela ou uma linha) está com dados prontos à serem persistidos no banco de dados.

OBS: Essa sinalização é feita através do comando AcceptChanges. (O comando AcceptChanges sinaliza que os dados desse conjunto de tabelas estão prontos para serem persistidos no banco de dados, lembrando que o comando não grava diretamente os dados no banco de dados).  
OBS 2: Pode ser utilizado em conjunto com qualquer atividade que realize modificações em memória das tabelas, conjunto de tabelas e linhas das tabelas, como criação de colunas e/ou criação de registros.

### Passo a Passo:

Primeiramente é necessário arrastar a atividade "Aplicar Alterações na Tabela" para o "Fluxo de Trabalho Sequencial" em sua fórmula visual.

Após atividade ter sido adicionada ao fluxo de trabalho, é necessário configurar as propriedades da atividade.

No exemplo acima, as propriedades foram preenchidas da seguinte maneira:

- Conjunto de Tabelas:

- Linha da Tabela:

- Tabela:

Após preencher as propriedades, salve e execute a Fórmula Visual. Verifique o resultado do processo. A Fórmula Visual deverá executar com sucesso.

## Parâmetros da Atividade

### Conjunto da Dados (Opcional)

*Descrição*: Conjunto de tabelas onde o comando AcceptChanges será executado. (O comando AcceptChanges sinaliza que os dados desse conjunto de tabelas estão prontos para serem persistidos no banco de dados, lembrando que o comando não grava diretamente os dados no banco de dados).  
*Tipo*: DataSet (Conjunto de Tabelas em Memória)  
*Como usar*: Esse parâmetro é do tipo Conjunto de Tabelas em Memória, ou seja, deve-se utilizar um conjunto de tabelas em memória onde o comando AcceptChanges irá sinalizar que seus dados estão prontos para persistidos no banco.  
Valor utilizado na requisição: Activity=RMSWorkflow, Path=DataSet

### Linha da Tabela (Opcional)

*Descrição*: Linha da tabela onde o comando AcceptChanges será executado. (O comando AcceptChanges sinaliza que os dados dessa linha estão prontos para serem persistidos no banco de dados, lembrando que o comando não grava diretamente os dados no banco de dados)  
*Tipo*: DataRow (Linha de uma Tabela em Memória)  
*Como usar*: Esse parâmetro é do tipo Linha de uma Tabela em Memória, ou seja, deve-se utilizar uma linha de uma tabela em memória que represente a linha da tabela física no banco de dados onde o comando AcceptChanges irá sinalizar que seus dados estão prontos para serem persistidos no banco.  
*Valor utilizado na requisição*: Activity=RMSWorkflow, Path=Tables[0].Row

### Tabela (Opcional)

*Descrição*: Tabela onde o comando AcceptChanges será executado. (O comando AcceptChanges sinaliza que os dados dessa tabela estão prontos para serem persistidos no banco de dados, lembrando que o comando não grava diretamente os dados no banco de dados)}  
*Tipo*: DataTable (Tabela em Memória)  
*Como usar*: Esse parâmetro é do tipo Tabela em Memória, ou seja, deve-se utilizar uma tabela em memória que represente a tabela física no banco de dados onde o comando AcceptChanges irá sinalizar que seus dados estão prontos para serem persistidos no banco  
*Valor utilizado na requisição*: Activity=RMSWorkflow, Path=Tables[0].DataTable
