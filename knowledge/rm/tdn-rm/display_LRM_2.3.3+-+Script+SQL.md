---
content_hash: f3e47aaebc36d6879e989c5d28d675c6df59aea8cf4d59c48998ba098a7bcfc5
fetched_at: '2026-06-29T00:11:21.220481+00:00'
page_id: '689067192'
product: rm
source: tdn-rm
title: 2.3.3 - Script SQL
type: documentation
url: https://tdn.totvs.com/display/LRM/2.3.3+-+Script+SQL
version: 32
---

# O que é?

A Atividade de Script SQL permite executar sentenças SQL diretamente em uma base de dados durante a execução de um Projeto de Teste. É utilizada para realizar operações como inclusão, alteração, ou exclusão de dados, facilitando a construção e a preparação de cenários de teste.

# Para que serve?

Essa atividade serve para interagir com o banco de dados em um contexto de testes, possibilitando manipulação de dados de forma automatizada. Pode ser usada para:

* Alterar informações de uma base de dados em uma coligada específica.
* Ajustar parâmetros da base onde serão executados os scripts automatizados.
* Manipular registros para preparar ou validar cenários de teste.
* Obter dados da base como variável de ambiente para ser utilizado em outras Atividades do Projeto de Teste.

# Exemplo de Uso

Como cadastrarComo Cadastrar 1. Navegação para o cadastro

 1. Navegue no menu do TOTVS Automação de Testes e clique em: **Atividades** → **Banco de Dados**→ **Script SQL.**

 2. Na tabela que será mostrada, clique no botão verde em destaque para iniciar o cadastro.

2. Link para Definir cabeçalho (Nome e nível de acesso)

[Clique aqui para obter as informações do cabeçalho](https://tdn.totvs.com/pages/viewpage.action?pageId=859591806)

3. Preenchimento dos CamposVersão

Especifica a versão da atividade em questão. O objetivo de versionar uma atividade é para quando necessitamos ter mais de uma atividade em versões diferentes. Isso irá nos auxiliar a ter um histórico de atualizações e assegurar que as mudanças feitas sejam rastreáveis e reversíveis, se necessário.

Se for necessário utilizar mais de uma versão do RM no seu ambiente, é recomendado que a versão da atividade seja compatível com o sistema RM em uso. Caso contrário, pode-se optar por uma versão padrão de sua preferência.

*Exemplo utilizando a versão do RM*

*Exemplo utilizando a versão padrão*

Descrição

Fornece uma descrição detalhada da atividade, explicando seu propósito e operações, facilitando a compreensão e manutenção futura.

Cenário de Execução Contexto

Quando selecionado a opção **Contexto**, temos duas possibilidades em relação aonde o Script será executado, que vai depender de como seu projeto está configurado.

Cenários:

1. Seu Projeto de Teste possui uma **[Restauração de banco](https://tdn.totvs.com.br/pages/viewpage.action?pageId=689067189)**:
   1. Nesse caso o script será executado na base que foi restaurada.
2. Seu Projeto de Teste não possui [Restauração de banco](https://tdn.totvs.com.br/pages/viewpage.action?pageId=689067189) mas possui uma [**Credencial de banco de dados**](https://tdn.totvs.com.br/display/LRM/1+-+Banco+de+Dados) cadastrada no **[Ambiente](https://tdn.totvs.com/display/LRM/4+-+Ambientes)**.
   1. O Script será executado na base cadastrada no [Ambiente](https://tdn.totvs.com/display/LRM/4+-+Ambientes).

**OBS:**Caso seu projeto tenha uma [Restauração de banco](https://tdn.totvs.com.br/pages/viewpage.action?pageId=689067189) e uma [Credencial de banco de dados](https://tdn.totvs.com.br/display/LRM/1+-+Banco+de+Dados) cadastrada no [Ambiente](https://tdn.totvs.com/display/LRM/4+-+Ambientes) a base utilizada será da restauração.

Base Específica

Ao escolher o **Base específica**, a sentença SQL será executada em uma base de dados informada manualmente. Nesse caso, é necessário fornecer a [**Credencial de banco de dados**,](https://tdn.totvs.com.br/display/LRM/1+-+Banco+de+Dados) independentemente do banco restaurado pelo Projeto de Teste.

* **Uso**: Utilizado quando a execução precisa ocorrer em uma base de dados diferente da restaurada pelo projeto ou não existir um atividade de Restauração de Base no contexto do Projeto

Recomendado para cenários onde o script SQL deve ser executado em um banco externo ou dedicado.

É obrigatório que no cadastro da credencial informada seja preenchido o nome da base de dados (SQL) ou nome do pluggable (Oracle).

Script Sql

Utilize esse campo para escrever o Script Sql que deve ser executado na sua base.

Evite utilizar em suas sentenças a expressão SELECT \* FROM TABELA, uma vez que o uso de uma sentença tão genérica pode causar problemas, como por exemplo:

1. Campos novos forem criados e seu script não for atualizado.
2. Se sua tabela contiver campos que não são fixos, ou seja, que atualizam o seu valor no momento da criação ou edição. Campos como: **Data de criação, Data de Atualização, Data de Deleção.**
Variável de Ambiente

Este campo é habilitado ao ativar a opção "Armazenar resultado do Script em Variável de Ambiente". Ele permite definir o nome da variável que armazenará o resultado do Script SQL declarado anteriormente.

**1.** Lembre-se de que o resultado do Script SQL só poderá ser armazenado em uma variável de ambiente caso retorne apenas uma linha e uma coluna. Já que não é possível armazenar uma lista de valores dentro da variável.

**2.** Garanta que o nome da variável de ambiente não seja igual a nenhuma variável existente no menu **[Ambientes](https://tdn.totvs.com/display/LRM/4+-+Ambientes)**. Caso isso ocorra a substituição pelo valor obtido na consulta afetará a variável existente no Ambiente.

**3.** Use as variáveis de ambiente em todas as atividades que fizerem sentido para o seu propósito de teste.

O valor retornado pelo script SQL será salvo no contexto da execução e poderá ser reutilizado em outros pontos do projeto de teste por meio desta variável.

Utilizando Variáveis de Ambiente em Outro Cadastro

As variáveis de ambiente permitem armazenar valores que podem ser reutilizados em diferentes atividades dentro do Projeto de Teste. Isso permite automatizar processos dependentes de base ou que testam um jornada.

**Criar a Variável de Ambiente**

Para armazenar um resultado de Script SQL em uma variável de ambiente, ative a opção *"Armazenar resultado do Script em Variável de Ambiente"*.

Defina um nome claro e descritivo para a variável, alinhado ao seu propósito no teste, para facilitar a manutenção e o entendimento do projeto.

* Exemplo: Criamos a variável **CodCurso**, que armazena o código de um curso buscado no banco de dados.

Escreva o nome da variável de forma natural, sem nenhum tipo de caractere especial. **Ex:** **{** , **}**, **\***, **&**, etc... Variáveis de ambiente

As Variáveis de Ambiente são utilizadas para configurar e personalizar o comportamento da Atividade. Elas permitem definir valores específicos ou dinâmicos que podem ser usados durante a execução dos testes, assegurando que o teste execute conforme o ambiente em que o mesmo é executado. As Variáveis de Ambiente são cadastradas no cadastro de Ambiente onde informamos os valores fixos ou de forma dinãmica no cadastro de Script SQL.

Consulte quais campos permitem o uso das Variáveis de Ambiente nessa Atividade:

[Script SQl - Variáveis de Ambiente](https://tdn.totvs.com/pages/viewpage.action?pageId=842287134).

Saiba mais sobre [Ambientes](https://tdn.totvs.com/display/LRM/4+-+Ambientes).

Exemplo prático

Imagine que um analista precisa validar um processo em um ambiente de testes do RM. Antes de executar o teste, é necessário atualizar alguns parâmetros específicos na base de dados, como habilitar uma funcionalidade que está sendo testada ou limpar registros antigos que poderiam interferir nos resultados.

**Solução**: Usar a **Atividade de Script SQL** para inserir, atualizar ou excluir dados da base de testes, garantindo que a configuração necessária esteja pronta para o teste.

Exemplo de Utilização de Variáveis de Ambiente em Outro Cadastro

Imagine que estamos automatizando o teste de um sistema de gestão escolar, no qual precisamos cadastrar uma nova escola e garantir que seu código único seja armazenado e reutilizado em outras etapas do teste. Para isso, utilizamos uma variável de ambiente do Script SQL chamada **CodEscola**. Essa variável será utilizada para capturar o código da escola e poderemos utilizar este valor em outras atividades dentro do contexto do Projeto de Teste. Por exemplo: No cadastro de **requisição SOAP**.

Na atividade SOAP, a variável **CodEscola** é utilizada para associar um curso à escola cadastrada, garantindo que a requisição envie corretamente o código único da escola.

* Exemplo da variável sendo utilizada em uma atividade Soap:

Para uma variável ser utilizada corretamente ela deve está entre chaves simples.

**Exemplo: {CodEscola}**

---

# Saiba mais

A atividade suporta o uso de variáveis de ambiente para configurar e personalizar a execução de scripts SQL. Isso é útil para adaptar a execução a diferentes configurações e cenários, sem a necessidade de alterar o código do script.

# FAQ

**P: Como posso garantir que meu script SQL seja seguro e eficiente?**

R: Sempre teste suas sentenças SQL em um ambiente de desenvolvimento antes de executá-las em produção. Use cláusulas `WHERE` quando necessário e evite `SELECT *` em tabelas grandes. Garanta que suas consultas não afetem todos os registros da tabela por engano.

**P: Qual a melhor prática para usar o Script SQL em testes de parâmetros no RM?**

R: Ao utilizar o Script SQL para definir parâmetros no RM, é importante lembrar que muitos processos do RM trabalham com cache. Insira o Script SQL após a Atividade de Restauração de Base e antes da Atividade que irá subir o Host do RM, garantindo que os parâmetros sejam atualizados corretamente.

**P: Qual o impacto de rodar um Script SQL sem a Atividade de Restauração de Base no início do teste?**

R: Se o banco de dados não for restaurado antes da execução do script, os dados podem estar em um estado inconsistente, o que pode comprometer os resultados do teste. É sempre recomendado rodar a Atividade de Restauração de Base antes do Script SQL, especialmente em ambientes de teste que dependem de um estado inicial limpo.
