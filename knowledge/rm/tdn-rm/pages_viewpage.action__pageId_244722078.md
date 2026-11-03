---
content_hash: 9689c1a100fea07a202b9720584183bae8bafb198991066f41fec87497d1405d
fetched_at: '2026-06-29T00:08:14.949819+00:00'
page_id: '244722078'
product: rm
source: tdn-rm
title: Criação de Cubo .Net
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244722078
version: 14
---

# Índice:

---

.\*ndice:

# Objetivo:

---

      O objetivo deste documento é a auxiliar usuários na criação de um Cubo.Net utilizando como fonte de dados uma consulta SQL.

# Introdução:

---

      O Cubo .Net é uma estrutura de dados manipuláveis que possibilita um melhor gerenciamento de seus dados.

# Como Criar:

---

      Para criação de um Cubo é necessário realizar os seguintes passos.

falseComo CriarAcesso ao módulo

 Acesse o módulo Inteligência de Negócios:

A partir da versão 12.1.29.215 e 12.1.31.120 é possível acessar o cadastro de Cubo direto da Aba **Gestão** dos módulos de produtos. Quando acessada pelos módulos de Produtos será consumida a licença do contexto e não a TOTVS I.

Nos módulos de Globais, como Serviços Globais, Inteligência de Negócios ou Integração a tela de Cadastro de Cubos não estará visível no menu Gestão, apenas a tela de Visão de Cubos. Nesses módulos é necessário seguir conforme os passos deste tópico.

Acesso aos Cubos

Na aba Gestão Estratégica, acesse o menu Cubo:

Criação do Cubo

Clique no botão Incluir e preencha os campos obrigatórios Titulo, Categoria e Fonte de Dados. Neste exemplo, utilizaremos uma Consulta SQL como Fonte de Dados. Com isso, é necessário preencher também o campo Consulta SQL conforme a imagem abaixo:

O Título informado vai definir o nome usado para a exportação do cubo no Portal, portanto é recomendável evitar caracteres inválidos para um nome de arquivo e link(Url), Como exe:  , \ / & ' " : \* ? = |

Criação da Cons. SQL

Para este exemplo, utilizaremos a Consulta SQL abaixo:

Passagem de Parâmetro

Como observado, a consulta necessita de parâmetro(s). Para fixar este(s) valor(es) é necessário estar na tela de edição do Cubo e clicar no botão "Parâmetros" (localizado em frente o Lookup de Fonte de Dados). Em seguida informar o valor para o(s) parâmetro(s) (Os parâmetros serão solicitados também na atualização do Cubo).

Depois de selecionado o botão "Parâmetros" a tela abaixo será exibida para edição dos parâmetros:

Importante

Caso a consulta SQL contenha uma Fórmula ela não será executada, pois fórmulas necessitam de um contexto para serem executadas. Os parâmetros do tipo :FRM\_ serão tratados como parâmetros de Valor Fixo.

# Execução do Cubo:

---

      Com o processo de criação concluído o cubo já pode ser manipulado conforme exemplo a seguir:

falseExecução do CuboAtualização

Selecione o Cubo e dê um duplo clique. Será apresentada uma caixa de diálogo perguntando se deseja realizar a atualização. Clique em "Sim" para conclusão da atualização.

Lista de Campos

Após atualização, o cubo será carregado com a janela "Lista de Campos do Cubo" aberta. Está janela é utilizada para incluir os campos retornados pela Fonte de Dados. Esta opção pode ser acessada também ao clicar no botão "Campos disponíveis":

Execução

Após arrastar os campos da janela de "Lista de Campos do Cubo", os dados estão preparados para serem manipulados.

Importante

Em um cenário, onde o cliente possua campos sensíveis em um cubo já gerado, é necessário que o cubo seja regerado, com o usuário com menos permissão para que seja refletido o comportamento de não mostrar tais campos.

Existe também uma flag de regeração automática com uma opção.

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.44 ou Superiores

false

**Processo:** Criação de Cubo .Net utilizando como fonte de dados uma consulta SQL

falsefalse

**Status:** Finalizado

false

**Data:** 10/08/2016

false

**Autores:**
