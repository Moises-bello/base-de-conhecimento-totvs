---
content_hash: 5e401d03523422eb0bf3f69ec42d45816a28e90a699f8cb51f179d5639da5b0a
fetched_at: '2026-06-29T00:08:03.876059+00:00'
page_id: '235327705'
product: rm
source: tdn-rm
title: Recurso RSS
type: documentation
url: https://tdn.totvs.com/display/LRM/Recurso+RSS
version: 48
---

# Índice:

---

.\*ndice:

# Objetivo:

---

        O objetivo deste guia é apresentar as configurações e demonstrar a criação de um canal RSS.

# Como Configurar:

---

        Para que o recurso de RSS possa ser utilizado com canais pertencentes ao RM, deve-se possuir um portal Corpore RM corretamente configurado, sendo necessário possuir a Tag "ServiceAlias" no arquivo "Web.config", configurada com o mesmo alias de banco de dados utilizado para login no RM.

Em ambientes que possuem vários alias cadastrados em um mesmo portal, deve-se separar um portal para cada alias que utilize o recurso de canais RSS do RM, configurando a Tag "ServiceAlias" corretamente.

Exemplo: <add key="ServiceAlias" value="CorporeRM" /> para um alias CorporeRM.

        O campo "URL de acesso ao Portal RM", localizado nos parâmetros globais do RM, aba "Gerais". Deve ser preenchidos com a URL do portal configurado.

         Necessário realizar a correta configuração do proxy do RSS, para isso clique em "Configurações" e as defina.

Observação: Para realizar a configuração do proxy é necessário que o serviço esteja em execução. false

# Passo a Passo Canais RSS Externos:

Passo a Passo Canais RSS Externos:1º Passo:

**1º Passo:** Acessar a visão "Leitor RSS".

2º Passo:

**2º Passo:** Após carregada a visão, acesse "Canais | Adicionar Canal".

3º Passo:

**3º Passo:** Após ser aberta a janela do canal, preencha as seguintes informações:

* URL do RSS do canal desejado
* Título do canal
* A opção Requer Senha deve ser marcada caso a URL do canal exija autenticação, neste caso, o usuário e senha para autenticação devem ser preenchidos
* A opção Enviar Email deve ser marcada caso o usuário queira receber notificações via Email.
* A opção Sincronizar canal automaticamente deve ser marcado caso seja necessário a atualização das informações do canal sem execução manual.

Observação: Caso a opção Adicionar aos favoritos seja marcada, o canal será exibido no botão Meus Canais.4º Passo:

**4º passo:**Após salvar o canal, o mesmo poderá ser selecionado e as informações visualizadas.

false

# Passo a Passo Canais RSS Nativos do RM:

Passo a Passo Canais RSS Nativos do RM:1º Passo:

**1º Passo:** Acessar a visão "Canais RSS".

2º Passo:

**2º Passo:** Após ser aberta a visão, inclua um novo registro. Na aba "Identificação" deve ser preenchido o "Título" do canal.

3º Passo:

**3º Passo:** Na aba "Permissões", use o botão incluir para definir os perfis que terão acesso ao canal RSS.

4º Passo:

**4º Passo:** Na aba "Fontes", use o botão de incluir para adicionar a fonte do canal.

          Na inclusão da Fonte RSS, é necessário a criação de uma consulta SQL que contenha o resultado que será analisado pelo RSS. Uma vez que essa consulta SQL sofrer alteração, o alerta será disparado.

          Clique no lookup do campo "Cons. SQL do Alerta", e selecione ou crie a consulta SQL do alerta.

          Nesse exemplo, iremos utilizar uma consulta SQL que retorna as coligadas cadastradas na base, exceto a coligada global. Após a seleção ou criação da consulta, clique OK.

5º Passo:

**5º Passo:** Após a inclusão da consulta, clique no botão "Selecionar" do campo "Identificador único" e marque os campos da fonte, em seguida clique em "OK".

          Pode-se utilizar os campos (CODCOLIGADA e NOME) retornados pela consulta SQL para exibição das informações no RSS utilizando chaves e o índice do campo na consulta SQL, iniciando por 0.

          Neste exemplo utilizaremos o nome da coligada no "Título" da fonte.

          Em seguida Clique no botão "Parâmetros", e associe o campo da consulta com o identificador utilizado no texto.

          Neste caso, o identificador {0} será substituído pelo campo "NOME" presente na consulta SQL.

6º Passo:

**6º Passo:** Adicione identificadores na "Descrição".

          Neste caso, foram utilizados dois identificadores, {0} e {1}.

          Em seguida Clique no botão "Parâmetros"  e associe os campos aos identificadores utilizados na descrição, neste caso o campo "NOME" é o identificador {0} e o campo "CODCOLIGADA" é o identificador {1}.

7º Passo:

**7º Passo:** Selecione a Fonte  de Leitura desejada.

         Neste caso foi utilizado a mesma consulta SQL, pois a mesma retorna as informações de coligadas.

        Em seguida, salve o cadastro da fonte e feche a mesma.

8º Passo:

**8º Passo:** Volte ao formulário de cadastro do canal na aba "Identificação" e clique em salvar. Observe que o campo com a URL do canal será preenchido.

          Após os procedimentos realizados, o canal já estará cadastrado no sistema.

9º Passo:

**9º Passo**: Para assinar o canal criado, acesse o visão "Meus Canais".

         Após ser aberta a visão, selecione o canal recém criado, e clique em "Processos | Assinar Canal RSS".

         Ao ser aberta a tela de assinatura do canal, preencha as informações:

* A opção Requer Senha deve ser marcada e preenchida com o usuário e senha do sistema
* A opção Enviar Email deve ser marcada caso o usuário queira receber notificações via Email.
* A opção Sincronizar canal automaticamente deve ser marcado caso seja necessário a atualização das informações do canal sem execução manual.

.        

Observação: Caso a opção Adicionar aos favoritos seja marcada, o canal será exibido no botão Meus Canais.

         Em seguida, clique em executar para assinar o canal.

10º Passo:

**10º Passo:** Acessando o leitor RSS as informações de coligadas são visualizadas.

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX e 12.01.XX

false

**Processo:** RSS

false

**SubProcesso:** Configurando RSS

falsefalse

**Status:** Finalizado

false

**Data:** 11/04/2016

false

**Autores:**
