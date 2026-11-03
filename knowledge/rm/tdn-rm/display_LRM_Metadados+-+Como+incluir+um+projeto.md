---
content_hash: 24de84502f9eb8c0ff1058184724bb3c148370550ce4c6c21da60d24767ea185
fetched_at: '2026-06-29T00:11:02.796701+00:00'
page_id: '61934702'
product: rm
source: tdn-rm
title: Metadados - Como incluir um projeto
type: documentation
url: https://tdn.totvs.com/display/LRM/Metadados+-+Como+incluir+um+projeto
version: 28
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**

**01. VISÃO GERAL**

      O Metadados permite ao usuário a criação e desenvolvimento visual de lógicas de negócio com o objetivo de estender a solução TOTVS RM.

      A ideia é criar um mecanismo de geração automática de formulários através da utilização de um dicionário de dados fornecendo um modelo de persistência, negócio e apresentação, facilitando a transformação de dados em informações que ajudem no processo de tomada de decisão das organizações que utilizam o ERP Linha RM.

**Conceito:** O Metadados consiste em uma interface para usuários para criação, consulta, atualização e destruição de dados. Esse é o propósito final de um projeto de Metadados.

Atenção

A Partir das versões abaixo todos os projetos de metadados serão incluídos no arquivo \_BrokerCustom.dat ao invés do \_Broker.dat

|  |
| --- |
| 12.1.2209 |
| 12.1.2205.142 |
| 12.1.34.206 |

**02. EXEMPLO DE UTILIZAÇÃO**

Como exemplo vamos criar um Projeto de CADASTRO DE FUNCIONÁRIOS RELACIONANDO COM DEPENDENTES.

falseExemplo de Utilização1º Passo:

**Incluindo Tipo de dados:**

      Para iniciarmos o projeto será necessário cadastrar os tipos de dados, para isto siga os passos abaixo seguindo a planilha disponibilizada com os tipos de dados.

* C*adastrar* *os* *tipos de dados abaixo:*

|  |  |  |  |
| --- | --- | --- | --- |
| **Nome** | **Tipo SQL** | **Tipo Oracle** | **Tipo Linguagem** |
| **Inteiro** | **int** | **number(10,0)** | **System.Int32** |
| **Varchar** | **varchar** | **varchar2** | **System.String** |
| **Data** | **datetime** | **date** | **System.DateTime** |
| **Inteiro Curto** | **smallint** | **number(5,0)** | **System.Int16** |
| **String** | **varchar** | **varchar2** | **System.String** |
| **Moeda** | **money** | **NUMBER(10,2)** | **System.Decimal** |
| **Char** | **char(1)** | **char(1)** | **System.Char** |
| **Memo** | **TEXT** | **clob** | **System.String** |
| **Imagem** | **IMAGE** | **blob** | **System.Byte[]** |

2º Passo:

**Incluindo Tabela:**

      A segunda etapa é a criação das tabelas que serão utilizadas no projeto. Execute o processo de acordo com a figura.

Ao acessar a tela inclua os dados respectivos a esta tabela seguindo os exemplos abaixo:

3º Passo:

**Tabela de Funcionário:**

4º Passo:

**Tabela de Dependente:**

Quando utilizado o preenchimento automático em um campo novo,na alteração de uma tabela, é necessário o preenchimento do campo "Valor Padrão"

5º Passo:

**Incluindo Relacionamento:**

      Esta funcionalidade possibilitará relacionar as tabelas criadas no metadados.

Ao selecionarmos a tabela filha campo IDFUNC (Tabela ZMDDependente) e a tabela pai (ZMDFUNCIONARIO) campo IDFUNC, estabelecemos um relacionamento entre as tabelas através desses campos.

Todas as definições como configurações de campo e relacionamentos já pré-estabelecidos no modelo de persistência servirão como base para a criação do modelo de negócio, seguindo o conceito de herança. Neste ponto será possível escolher quais os campos de um objeto de persistência serão utilizados no DataServer além de permitir criar novos campos que serão considerados como campos calculados.  
  
Para mais informações, acesse:

 É importante frisar que a FK só é criada na criação da tabela após a primeira geração do projeto. Desse modo, não é possível fazer a alteração de um FK em uma tabela já existente.6º Passo:

**Incluindo modelo de Negócio:**

A tela será apresentada com as tabelas relacionadas na seguinte estrutura:

7º Passo:

**Incluindo Formulários:**

Através da GUIA Apresentação é possível definir funções que serão apresentadas na TELA que será criada como Exemplos: caixa de pesquisa, caixa de Seleção, caixa de opção etc.

No exemplo iremos trabalhar com o campo CODCOLIGADA e iremos utilizar caixa de seleção onde estaremos utilizando os itens do cadastro de coligadas.

Este recurso proporcionará realizar pesquisas no cadastro de coligadas quando selecionado (Após a inclusão do metadado)

8º Passo:

**Incluindo Projeto Metadados:**

      Esta opção possibilitará inclusão do projetos para criação do metadado no sistema pre definido. Para realizar o processo siga as orientações disponibilizadas no exemplo abaixo.

Atenção

**Na criação do projeto de metadados, é necessário incluir um ID de Segurança único para o projeto.**

9º Passo:

**Acessando o Metadado Criado:**

**1º Passo:**

Será necessário a Liberação de acesso para o usuário: Após a inclusão do Metadado deverá ser disponibilizado a permissão para o usuário acessar o mesmo no sistema.

Esta parametrização é necessária pelo fato do recurso (Metadados) criar outros menus no sistema o que ficará até o momento bloqueado para o usuário.

Neste caso realize o processo:

Acesse o perfil ao qual este usuário possui as permissões selecionando o contexto ao qual refere-se o processo:

      Em seguida será possível acessar o seu projeto.
