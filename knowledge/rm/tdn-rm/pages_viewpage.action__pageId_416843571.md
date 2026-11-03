---
content_hash: 3a3219e35f4a340c3c1fbae0f0b319afc1b9140cf8d8aa245d2caf6f020d637a
fetched_at: '2026-06-29T00:09:12.260150+00:00'
page_id: '416843571'
product: rm
source: tdn-rm
title: Utilizando a atividade "Atualizar Registros Localizando na Tabela"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=416843571
version: 59
---

# Objetivo:

---

     Este documento tem como finalidade, demonstrar o uso da atividade **"Atualizar Registros Localizando na Tabela"**.

# Configuração:

---

## Informações Gerais:

### Objetivo:

A finalidade da atividade "Atualizar Registros Localizando na Tabela" é permitir que o usuário recupere dados de uma coluna da tabela resultante de uma consulta SQL.

### Passo a Passo:

Primeiramente é necessário arrastar a atividade "Atualizar Registros Localizando na Tabela" para o "Fluxo de Trabalho Sequencial"em sua fórmula visual.

OBS: Devemos lembrar que a atividade "Atualizar Registros Localizando na Tabela" deverá vir sempre acompanhada da atividade "Executar Consulta SQL".

Após atividade ter sido adicionada ao fluxo de trabalho, é necessário configurar as propriedades da atividade.

No exemplo acima, as propriedades foram preenchidas da seguinte maneira:

OBS

Não se esqueça de preencher as propriedades da atividade "Executar Consulta SQL"

[Mais de "Atividade Executar Consulta SQL"](http://tdn.totvs.com/pages/releaseview.action?pageId=146184324)

Após preencher as propriedades, salve e execute a Fórmula Visual. Verifique o resultado do processo. A Fórmula Visual deverá executar com sucesso. Com isso poderemos seguir para o exemplo de utilização real da atividade.

### EXEMPLO PRÁTICO

Vamos agora ver um exemplo prático do uso da atividade "Atualizar Registros Localizando na Tabela".

Após preenchermos as suas atividades iniciais, iremos adicionar agora, três outras atividades, são elas:

- Executar Código

c#1Executar CódigotrueOBS

[Mais de "Atividade Executar Código"](http://www.tdn.totvs.com/pages/viewpage.action?pageId=286522533)

- Expressão

OBS

A **Atividade de Expressão** deverá ser adicionada com a propriedade **Expressões** com qualquer valor, foi usado **1**, como exemplo.

OBS

[Mais de "Atividade Expressão"](http://www.tdn.totvs.com/pages/releaseview.action?pageId=149881523)

- Enviar e-mail

OBS

Lembre-se de preencher corretamente o assunto do e-mail,os destinatários, remetente e texto do e-mail. Como exemplo colocamos a informação obtida pela atividade "Atualizar Registros Localizando na Tabela" como texto do e-mail.

OBS

[Mais de "Atividade Enviar E-mail"](http://www.tdn.totvs.com/pages/releaseview.action?pageId=146184224)

Salve e execute e veja o resultado.

### RESULTADO

## Parâmetros da Atividade:

### Chave da Fonte de Dados (Obrigatório):

*Descrição*: Campos da fonte de dados que serão utilizados como chave para pesquisa.  
*Tipo*: String (Cadeia de caracteres)  
*Como usar*: Esse parâmetro é do tipo Cadeia de Caracteres, ou seja, deve-se utilizar um valor alfanumérico que represente a os campos da fonte de dados que serão utilizados como chave para pesquisa.  
*Valor utilizado na requisição*: CODCOLIGADA;CODFILIAL

### Chave de Pesquisa da Linha (Obrigatório):

*Descrição*: Campos da linha que serão utilizados como chave para pesquisa.  
*Tipo*: String (Cadeia de caracteres)  
*Como usar*: Esse parâmetro é do tipo Cadeia de Caracteres, ou seja, deve-se utilizar um valor alfanumérico que represente a os campos da linha que serão utilizados como chave para pesquisa.  
*Valor utilizado na requisição*: CODCOLIGADA;CODFILIAL

### Coluna que será Retornada pela Pesquisa (Obrigatório)

*Descrição*: Coluna que terá o seu valor retornado pela pesquisa.  
*Tipo*: String (Cadeia de caracteres)  
*Como usar*: Esse parâmetro é do tipo Cadeia de Caracteres, ou seja, deve-se utilizar um valor alfanumérico que represente a a coluna que terá o seu valor retornado pela pesquisa.  
*Valor utilizado na requisição*: NOME

### Fonte de Dados da Pesquisa (Obrigatório)

*Descrição*: É o resultado da consulta SQL em um conjunto de tabelas em Memória.  
*Tipo*: DataSet (Conjunto de Tabelas em Memória)  
*Como usar*: Esse parâmetro é do tipo Conjunto de Tabelas em Memória, ou seja, deve-se utilizar um conjunto de tabelas em memória contendo o resultado da consulta SQL proveniente da Atividade "Executar Consulta SQL" vinculada.  
*Valor utilizado na requisição*: Activity=rmsConsSQLActivity1, Path=DataSet

### Linha Para Atualização (Obrigatório)

*Descrição*: Linha da tabela que será chave da pesquisa.  
*Tipo*: DataRow (Linha de uma Tabela em Memória)  
*Como usar*: Esse parâmetro é do tipo Linha de uma Tabela em Memória, ou seja, deve-se utilizar uma linha de uma tabela em memória que represente a linha da tabela que será chave da pesquisa.  
*Valor utilizado na requisição*: Activity=rmsConsSQLActivity1, Path=Tables[0].Row

## Retorno da Atividade

### Valor Retornado (Opcional)

*Descrição*: Valor retornado pela pesquisa dos registros.  
*Tipo*: Objeto (Object)
