---
content_hash: c17a85a167a9cec9d5121932708551760e81f0816e25e26c29ba71bb6d4e9504
fetched_at: '2026-06-29T00:11:53.814389+00:00'
page_id: '85164224'
product: rm
source: tdn-rm
title: Criação de Layout no Gerador de Saídas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=85164224
version: 21
---

# Introdução:

---

Este documento tem por objetivo auxiliar na criação de um layout simples no Gerador de Saídas, para exemplificação de uso da ferramenta.

Neste exemplo será criado um relatório de **Funcionários e seus dependentes**, que pode ser seguido e depois adaptado para as necessidades do usuário.

Manual

Esta documentação tem como objetivo resumir o uso do Gerador de Saídas em um exemplo simples e prático. Aqui não serão explicados termos e componentes da ferramenta. Para acesso à estas e mais informações, acesse: 

# Incluindo um novo Layout

---

* Primeiramente, iremos acessar a visão do Gerador de Saídas (Contida em **Gestão → Ferramentas de Análise → Gerador de Saída**) e então, cadastrar um novo Layout do Gerador de Saídas. Determinaremos o Nome como **"Funcionários e seus Dependentes"** e então, selecionaremos uma categoria em que o usuário utilizado possui permissões:

* Agora, vamos abrir o Layout recém criado para podermos editá-lo. Isso pode ser feito clicando duas vezes sobre o Layout cadastrado. Logo após, é apresentada a tela de parametrização do gerador de Saídas:

# Editando e Parametrizando o Layout

---

* Com a tela de parametrização aberta, iremos adicionar primeiramente um novo Contexto. Para este exemplo utilizaremos uma  simples, mas você pode utilizar toda a gama de Contextos diferentes suportados pelo Gerador de Saídas

## Adicionando um Contexto

---

Contexto

Para aprender mais sobre o que é um contexto e a importância dele para o Gerador de Saídas, acesse: 

* Para adicionar o Contexto, iremos clicar em **Contextos** no canto inferior esquerdo da tela (Ou apertar **F5** no teclado), acessar a aba recém habilitada **Adicionar Contexto** e então, selecionar **Consulta SQL**:

* Agora basta selecionar a Consulta SQL cadastrada no sistema:

Consulta SQL

Abaixo a Consulta SQL que está sendo utilizada:

sqlParâmetros na Consulta SQL

É possível também utilizar parâmetros na consulta SQL conforme exemplo abaixo:

sqlAtenção

Ao utilizar filtros de visão que fazem o uso da condição (**In SQL**) onde a consulta SQL possua parâmetros, os parâmetros precisam começar com a Letra **F** e logo após um *número* identificando o parâmetro. 

Exemplo:

sqlfalse

Variáveis de contexto não precisam seguir este padrão:

sql

* Após a seleção da *Consulta SQL*, podemos notar que no **Contexto** recém adicionado já constam os campos da sentença SQL

Agora finalizamos a etapa de seleção de Contexto e iremos adicionar um **Layout.**

## Adicionando um Arquivo

---

Contexto

Para aprender mais sobre o que é um arquivo e a importância dele para o Gerador de Saídas, acesse:

* Para adicionar um Arquivo, primeiramente iremos acessar novamente a aba **Layout**, presente no canto inferior esquerdo da tela (Ou apertando **F4**):

* Logo então selecionaremos na árvore chamada **Layout** o item **Arquivos**. Assim, os botões **Adicionar Arquivo**e **Adicionar Registro**serão liberados. Selecionamos **Adicionar Arquivo** para adicionar um novo arquivo ao *Layout* do Gerador de Saídas:

* No campo **Nome**, definimos o Nome deste arquivo que será gerado.
* Nas ***Propriedades*** iremos determinar o caractere "**|**" como separador de campos e linhas:

* E após a criação do **Arquivo**, é necessário determinar os **Registros** que serão impressos.

## Adicionando um Registro

---

Contexto

Para aprender mais sobre o que é um registro e a importância dele para o Gerador de Saídas, acesse:

* Assim como com os **Arquivos**, selecionaremos na árvore chamada **Layout** o item **Registros** e então,  **Adicionar Registro** para adicionar um novo registro ao *Layout* do Gerador de Saídas.

### **Criação dos Campos** **do Registrocampos**

Um registro pode conter vários campos. Para criar os campos, selecione o registro com duplo-clique.

false

No painel demonstrado abaixo são apresentadas as informações sobre o registro selecionado:

Nos **Campos** (na parte inferior da tela) poderão ser criados os campos do layout.

O botão  criará campos visíveis que serão gravados no arquivo texto.

O botão  criará campos invisíveis.

Estes servem somente para executar cálculos e utilizarem expressões e não são gravados no arquivo texto.

Utilize o botão  para excluir campos.

Os botões  e  auxiliam na movimentação de campos criados na ordem incorreta.

Crie campos com nomes que estejam relacionados ao seu conteúdo. Para informar mais a respeito dos campos utilize o campo **Descrição**.

* Iremos então adicionar um novo campo, utilizando o botão . Devemos informar o tamanho, se o campo é obrigatório e o tipo de dados que ele receberá:

A propriedade **Modo** pode assumir os seguintes valores:

**• Primeiro valor**  
**• Último valor**  
**• Chave Primária**  
**• Contar**  
**• Somar**  
**• Média**

* Agora é necessário realizar a atribuição do campo à sua propriedade no contexto, mas antes de realizar essa atribuição, devemos atrelar o contexto que será fornecedor dos campos ao registro. Para isso, iremos selecionar a aba **Contexto** no canto inferior esquerdo da tela, selecionar a tabela da consulta SQL e arrastá-la até a propriedade **Ligação** do **Registro**:

Se for necessário adicionar dois Contextos do tipo **Conjunto de Dados** ou **Consulta SQL** a um mesmo registro é aconselhável que estes contextos sejam revistos. Provavelmente eles possuem relação entre si e podem ser transformados em um contexto apenas.

* Por fim, vamos atrelar então as **colunas** da tabela proveniente da Consulta SQL aos **Campos** do **Registro** do Gerador de Saídas. Para fazer isso, iremos selecionar a coluna desejada na aba de **Contexto** e arrastá-la até a propriedade **Ligação** do campo do Registro:

false

Após a associação, não se esqueça de definir o **Tipo de Dados**, **Tamanho** e **Modo** do campo.

* Por fim adicionamos mais duas colunas aos seus respectivos campos e estamos prontos para realizar a geração:

* Agora toda a configuração do Layout do Gerador de Saídas está feita. Iremos então realizar a geração deste Layout.

# Gerando o Layout Configurado

---

* Para realizar a geração deste Layout iremos retornar a visão do Gerador de Saídas, selecionaremos o Layout e na aba **Processos**, iremos clicar em **Geração de Saídas**:

* Seremos então apresentados ao Assistente de Geração de Saídas. Aqui iremos determinar as informações de acordo com a necessidade de onde gerar o arquivo e afins:

Geração no Servidor

geracaoServidor

A partir da versão **12.1.2406.155,** caso o ambiente esteja com a tenantização ativa (A tag **TENANTPATHENABLED** esteja marcada como **true**), gerações do *Gerador de Saídas*que estiverem marcadas para **Gerar arquivos no servidor** permitirão apenas a determinação do caminho relativo em que o arquivo deverá ser salvo no servidor, por razões de segurança e privacidade de informações. Nestes casos o arquivo será gerado de acordo com o determinado na tag [**FileServerPath**](https://tdn.totvs.com/display/LRM/Configuracao+das+Tags+FileServerPath+e+LogPath)(ou na pasta compartilhada padrão do sistema caso a tag não tenha sido fornecida), dentro de uma pasta chamada **Saidas** e por fim, dentro do caminho relativo fornecido:

* Em um cenário hipotético que a pasta do servidor seja "**\\MinhaMaquinaDeArquivos\DiretorioCompartilhado**", e o caminho relativo fornecido seja **"Departamento\Equipe",**a saída será gerada no caminho:

false

**\\MinhaMaquinaDeArquivos\DiretorioCompartilhado\NomeDoTenant\Saidas\Departamento\Equipe**

Para gerações que deverão ser salvas no mesmo dispositivo-cliente (Sem a marcação **Gerar arquivos no servidor**), o usuário poderá escolher livremente onde na sua própria máquina, deseja salvar os arquivos provenientes da geração.

Layouts marcados com **Usa Diretório Padrão** também serão salvos de forma tenantizada, com a possibilidade de determinar o caminho relativo em que deverão ser salvos.

* E por fim, após a execução, podemos notar que o arquivo salvo no diretório determinado (Neste caso não marcamos para *Gerar arquivos no servidor*) possui os registros dais quais determinamos na configuração do Gerador de Saídas:

## Associando uma Fórmula aos campos do registro

---

* Ao adicionar um  ele pode ser vinculado a vários tipos de ligação.

* Ao selecionar o tipo Fórmula, será apresentada a visão com as Fórmulas do RM.

Proibido selecionar Fórmula na coligada Zero

Caso seja selecionada alguma Fórmula que esteja na coligada Zero, será apresentado um aviso informando que não é permitido, portanto deve ser selecionada outra Fórmula.  
Quando for possível identificar será apresentado qual o Registro e o Campo, que a Fórmula esta vinculada.

Ao editar o Layout e tentar salvar o aviso de erro será apresentado, sendo possível identificar qual o Registro, Campo e Fórmula a ser corrigida!

Para maiores informações:

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha);

Índicefalsefalse

**Produto:** Framework

false

**Processo:**Gerador de Saídas

falsefalseStatus

GreenCONCLUÍDO
