---
content_hash: 1c76062641d3071a7c16a0e6ae81be59827960f2c674801b3f3aebd262dc3119
fetched_at: '2026-06-29T00:08:07.663201+00:00'
page_id: '237383336'
product: rm
source: tdn-rm
title: Visões de Dados (Consultas SQL)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=237383336
version: 68
---

# Índice

---

.\*ndice

# Objetivo

---

O objetivo deste documento é apresentar a ferramenta Visões de Dados e suas funcionalidades.

# Introdução

---

Utilizando a Visões de Dados é possível criar uma variedade de consultas *SQL*, partindo da simples a mais complexas. Não importando se o apresentado será uma simples lista de registros ou um resumo agrupado de funcionários por seção.

As consultas SQL podem ficar disponíveis para Objetos Gerenciais, então, crie Relatórios, Cubos, Planilhas entre outros. Agende o envio de dados gerados em tempo real.

# Funcionalidades

---

false15%

***Parâmetros***

8%

***Padrão***

25%

***Descrição***

true15%

*1 - Nova Consulta*

8%

-

25%

Permite ao usuário criar novas consultas SQL. O aceso ao ícone é concedido no(s) perfil(s) associado(s) ao usuário.

true15%

*2 - Exclusão*

8%

-

25%

Permite ao usuário excluir consultas SQL. O aceso ao ícone é concedido no(s) perfil(s) associado(s) ao usuário.

**Nota:** Consultas SQL associadas a outros processos como objetos gerência e anexos da visão ***não poderão*** ser excluídas.

true15%

*4 - Código*

8%

Em branco

25%

Código da consulta SQL.

**Nota:** Não é permitido caracteres especiais como ?>- etc.

true15%

*5 - Título*

8%

Em branco

25%

Campo destinado para informar o título da consulta SQL.

true15%

*6 - Visível a todas Coligadas*

8%

False

25%

Opção que habilita e desabilita a consulta SQL como Consulta SQL Global.

**Nota:** A opção "Visível a todas Coligadas" marcada habilita a visualização da consulta SQL em todas as demais coligadas que seu usuário possui acesso. Caso seja mantido a opção default do parâmetro a consulta estará dispensável somente para coligada corrente da sua criação.

true15%

*7 - [Segurança por linha e por coluna na Consulta SQL](http://tdn.totvs.com/x/NViZDg)*

8%

False

25%

Esta opção permite determinar, para cada consulta, se ela deve considerar ou não a [segurança](http://tdn.totvs.com/x/NIivCw) por [perfil/usuário](http://tdn.totvs.com/x/HJO2C) ou segurança de campos.

true15%

*8 - Aplicação*

8%

Módulo Corrente

25%

Demostra qual o aplicativo a consulta SQL está associada.

**Nota:** Uma vez salvo os dados não é possível trocar o sistema.

true15%

*9 - Editor de Query*

8%

Em branco

25%

Editor de Query é o principal campo do cadastro de consultas SQL onde é possível criar e/ou dar manutenção nas consultas SQL.

**Nota:**  O "SET LANGUAGE" não deve ser utilizado em consultas SQL pois o mesmo influencia no contexto da aplicação que está compartilhando daquela conexão.

true15%

*10 - [Conexões Externas](http://tdn.totvs.com/x/KgGSAw)*

8%

Em branco

25%

Permite configurar uma conexão externa para que a consulta SQL busque informações em outras bases de dados.

true15%

*11 - [Disponibilidade](http://tdn.totvs.com/x/7G0MEQ)*

8%

True

25%

Permite que a consulta SQL criada esteja disponível/visível em visões, filtros, relatórios, menus e portal.

# Schema da consulta

---

Para o correto funcionamento da funcionalidade de Visão de Dados é necessário que o sistema consiga recuperar o schema da consulta SQL ao salvá-la. Caso seja retornado um erro na recuperação do schema, entre em contato com o seu DBA para análise e reescrita da consulta.

É importante lembrar que para outros executores de consultas SQL conseguir recuperar o schema de uma consulta não é requisito. No RM é necessário, pois existem validações de segurança (de campos, por perfil, por usuário...) entre outras funcionalidades que necessitam dele para funcionar como esperado.

Ao editar uma consulta SQL, é necessário validar todas as referências através do botão "Procurar Referências".

Caso tenha adicionado ou removido campos da consulta, será necessário editar a consulta em todos os objetos referenciados para que os campos sejam atualizados.

Caso a Consulta SQL esteja associada à um Objeto de Negócio e tenha sido editada de forma a modificar seu esquema ou parâmetros, o Objeto de Negócio será desativado e será necessário validar novamente essas informações. Nesse caso, ao clicar em "Salvar" será exibida a mensagem de alerta abaixo. que possibilita o acesso à interface de edição do Objeto de Negócio conforme detalhado em :

# Limitações

---

As visões de dados têm como objetivo apenas retornar dados.   
Por isso, existem as seguintes limitações:

* Obrigatoriedade de uma cláusula **SELECT**.
* Não são permitidas as cláusulas **ALTER**, **DELETE**, **DROP**,**INSERT**, e **UPDATE**.
* Não é permitida a utilização dos métodos **EXEC** e **EXECUTE***[ver nota abaixo]*
* Termo **DECLARE**, não é recomendado o uso.

Bloqueio dos comandos de execução

Com a intenção de bloquear a execução de comandos de alteração de dados, a partir da versão **12.1.2302** bloquearemos os métodos *EXEC* e *EXECUTE*.  
A virada ocorrerá da seguinte forma:

* visões de dados criadas antes da versão citada, que utilizem estes métodos, continuarão funcionando normalmente;
* no entanto, não será possível alterar estas visões de forma a preservar o *exec* ou *execute* (não será possível salvar a visão com estes comandos);
* não será possível criar novas visões, ou importar visões de dados criadas em outras versões, que possuam estes métodos.

Podem existir também outras limitações específicas de cada SGBD.

# Parâmetros e Variáveis

---

A utilização de parâmetros deve seguir o modelo de COLUNA = :NOME\_DO\_PARAMETRO, onde o valor a ser atribuído pelo filtro na clausula WHERE deve ser substituído pelo parâmetro, precedido de :(Dois pontos). A consulta SQL pode não suportar declarações de constantes e variáveis conforme o padrão PL/SQL, modelo usado diretamente no SGDB.

Para obter uma lista de variáveis aceitas na Consulta SQL, veja aqui:

É possível também, adicionar um sufixo para informar o tipo de um parâmetro, nos quais temos definido os seguintes sufixos:

**\_D**: Campos do tipo Data/Hora  
**\_V**: Campos do tipo numérico (fracionado)  
**\_N**: Campos do tipo numérico (inteiro 4 bytes)  
**\_S**: Campos do tipo alfanumérico.  
**\_H**: Campos do tipo numérico (inteiro 2 bytes)

Exemplo de uma consulta SQL utilizando dois parâmetros, :CIDADE e :PAIS

Na execução da consulta os parâmetros são apresentados para informar o valor.

Em alguns casos pode ocorrer que alguma diretiva ou palavra reservada do SGDB não seja aceita pela Consulta SQL.

Exemplo não suportado, onde o termo "define" não é reconhecido.  
O código abaixo pode ser executado diretamente pelo SGDB, mas não pela Consulta SQL.

c#RDarkExemplo

# Fórmula como parâmetro

---

Em uma consulta SQL é possível utilizar uma Fórmula RM, como parâmetro em um filtro na clausula Where, isso possibilita somar à consulta todos os recursos da Fórmula e enriquecer a funcionalidade.

Exemplo de duas Fórmulas simples, uma retorna um valor do tipo String e outra um número.

Na consulta SQL o nome do parâmetro é informado com o prefixo FRM\_ acrescido do Nome da Fórmula, definido pelo campo código no cadastro da Fórmula.

Na execução da consulta o parâmetro da Fórmula foi adicionado diretamente no filtro, e não precisa ser apresentado ao usuário.

# Banco de dados externo

---

Em casos de erro ao salvar uma consulta em uma base de dados externa que utilize parâmetros (ex: COLUNA = :NOME\_DO\_PARAMETRO), recomenda-se adicionar o sufixo de tipo ao nome do parâmetro. Exemplo: COLUNA = :NOME\_DO\_PARAMETRO\_D

# Comentários

---

São suportados comentários na sentença SQL, entretanto deve ser utilizado com cuidado para não interferir e gerar erros de interpretação da consulta.  
Em SQL Server e Oracle são aceitos dois tipos básicos de comentários, por bloco e por linha:

Comentário por Bloco deve começar com **/\*** e finalizar com **\*/**, pode conter quebra de linha.

Comentário por Linha deve iniciar com **--** , tudo a direita na linha poderá ser comentado. Não suporta quebra de linha.

c#RDarkExemploIMPORTANTE

**Algumas regras devem ser seguidas para evitar erros de interpretação de código.**

**IMPORTANTE destacar que a ferramenta de consulta SQL do RM interpreta os comentários e sintaxe SQL de forma diferente e mais restrita que um ferramenta de banco de dados comum, existem restrições e limitações que deve ser respeitadas.**

* Deve-se evitar utilizar comentários dentro de cláusulas SQL
* Não usar Parênteses no comentário ")"
* Evitar comentários dentro de expressões lógicas
* Preferir usar comentários antes ou após a sentença SQL
* Preferir usar comentários em bloco
* Seguir as boas práticas de mercado, <https://www.w3schools.com/sql/sql_comments.asp>

Devem ser evitadas algumas formas de comentários, como:

c#RDarkUSO NÃO RECOMENDADO

Deve-se evitar usar comentários dentro de uma cláusula ou uma expressão com parênteses.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Visões de Dados

falsefalse

**Status:** Em Construção

false

**Data:**

false

**Autores:**
