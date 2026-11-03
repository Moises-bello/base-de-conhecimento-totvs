---
content_hash: 0d86193358e1c9c5da43505a836651a48f9bc468e7f33be8c4750682831b4011
fetched_at: '2026-06-29T00:10:42.802992+00:00'
page_id: '547851509'
product: rm
source: tdn-rm
title: Fórmula Visual em API
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547851509
version: 33
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Como cadastrar uma fórmula visual para executar em uma API**
3. **Gatilhos disponibilizados para APIs**
4. **Seleção e uso do contexto na Fórmula Visual**
5. **Exemplos de Utilização**

**01. VISÃO GERAL**

A partir da versão 12.1.29 é possível customizar APIs através de Formulas Visuais. Foram criados gatilhos específicos para esse tipo de FV, que mostraremos a seguir.

Leia mais sobre as disponibilizadas pelo host.

Leia mais sobre .

falseImportante:

Marcando a opção "Executa em API(Poco)", somente será permitido executar Fórmulas Visuais em API's construídas no padrão "POCO".  
API's construídas no padrão "**Data Server**" não aparecerão para serem usadas nesse modelo.  
Portanto, Api's no padrão "**Data Server**" continuam podendo ser usadas no modelo antigo (DataSet).

**02. COMO CADASTRAR UMA FÓRMULA VISUAL PARA EXECUTAR EM UMA API**

A Fórmula Visual deve estar cadastrada com a opção "**Executa em API (POCO)"** habilitada, conforme exibido na imagem abaixo.

Ao marcar a opção "**Executa em API (POCO)"**, automaticamente o campo "**Visível para todas as coligadas"** será habilitado e não é possível desmarcá-lo.

Lembre-se: Após salvar uma Fórmula Visual como executável em API não é possível desmarcar e vice-versa.

Após salvar, será disponibilizada uma aba para configurar os Gatilhos da Fórmula Visual. Ao configurar um gatilho o sistema passa a executar a Fórmula Visual quando a API configurada é executada.

**03. GATILHOS DISPONIBILIZADOS PARA APIS**

Com os gatilhos disponibilizados, a Fórmula Visual pode ser executada antes ou depois dos dos métodos da API, como Get, Post, Put, Patch ou Delete.

Abaixo estão todos os gatilhos para API:

Os gatilhos Antes/Depois de recuperar todos (get) correspondem ao GetAll e os gatilhos Antes/Depois de recuperar (Get), correspondem ao GetOne.

Utilizando os gatilhos **Antes** de algum dos métodos, a Fórmula Visual será executada antes de chamar a execução do endpoint.

Utilizando os gatilhos **Depois**de algum dos métodos, a Fórmula Visual será executada depois de chamar a execução do endpoint.

**04. SELEÇÃO E USO DO CONTEXTO NA FÓRMULA VISUAL**

É possível selecionar como contexto em uma Fórmula Visual de API, um controller de API (POCO).

Utilizando esse contexto, pode-se, por exemplo, selecionar campos da API retornada para capturar ou manipular os valores das propriedades.

Veja no exemplo abaixo, uma Fórmula Visual onde foi selecionado o contexto da API de usuários (Controller de usuários)  para que seja gerada uma exceção com o valor do campo userName.

* **Primeiro:** Selecionar o contexto para a Fórmula Visual:

* **Segundo:** Adicionar a atividade de Gerar exceção, clicar em Ligações, na propriedade "**Mensagem de Erro**", clicar em reticências.

Será exibido o Editor de Ligações, ao expandir a propriedade "**Fields"**, serão listados todos os campos da API que podem ser usados no contexto. Basta selecionar um campo/valor desejado. No exemplo abaixo será a propriedade userName.

Obs.: As propriedades das APIs serão sempre listadas abaixo da hierarquia de \_Items.

* **Terceiro:** Adicionar um gatilho para essa Fórmula Visual.

Importante: Os valores de contexto estarão disponíveis no sistema depois que a requisição da API for feita. Então, para usar o contexto com valores, é necessário utilizar gatilhos de Depois dos métodos.

Isso porque se forem usados gatilhos de antes, o sistema ainda não terá executado o endpoint e não terá os valores das propriedades.

* **Quarto:** Adicionar um gatilho para a Fórmula Visual. Neste exemplo, adicionamos o gatilho "**Depois de recuperar (Get)**".

No Postman, aplicativo que usamos para realizar testes de APIs, chamamos o endpoint de usuários, buscando o usuário mestre.

Veja que o retorno foi uma exceção, contendo na mensagem o valor do campo userName (do contexto) e o nome da Fórmula Visual.

Com a Fórmula Visual é possível fazer inúmeras implementações, como disparar um e-mail sempre que algum usuário for deletado, alterado ou criado, por exemplo. Alterar o valor de uma propriedade específica da API antes de incluir o registro no banco, criar condições e comportamentos diferentes para determinados registros, entre outros.

**05. EXEMPLOS DE UTILIZAÇÃO**

        No primeiro exemplo, vamos utilizar as atividade de "**Foreach**" e "**Expression**" para percorrer os resultados da API (Controller de Usuários), e concatenar uma string qualquer a propriedade "**familyName**". A string será adicionada pela atividade de expressão antes do valor do campo.

falseExemplo de Utilização1º Passo:

Ao cadastrar uma Fórmula Visual com a opção **Executa em API (POCO)** habilitada (como mostrado anteriormente) é necessário adicionar os objetos que serão utilizados ao gatilho.

Para nosso exemplo, vamos utilizar a API de Usuários (Controller de Usuários) nos gatilhos "**Depois de recuperar todos (get)**" e "**Depois de recuperar (get)**".

2º Passo:

Em seguida na estrutura da fórmula, vamos adicionar as atividades "**Para Cada Iteração (API)**" e "**Expression**" no Fluxo de Trabalho Sequencial da fórmula, como mostra imagem abaixo:

É necessário que seja preenchido o contexto (Controller de Usuário) da fórmula para capturar ou manipular os valores das propriedades da API utilizada.

3º Passo:

* **Configurando a Atividade Para Cada Iteração (API)**

Nas propriedades da atividade, clique em Ligações () e selecione o lookup do campo "**Lista de Items**".

Na tela "**Editor de Ligações**", selecione a seguinte ligação: "**RMSWorkflow | [] Fields | \_Items**".

Essa configuração é necessária, por que temos que selecionar o objeto ao qual queremos percorrer. No nosso exemplo, selecionamos o "**\_items**", por que queremos percorrer todos os resultados da API.

Leia mais sobre [Atividade Para cada Iteração e Para cada Iteração API](https://tdn.totvs.com/x/qQLvC)

4º Passo:

* **Configurando a Atividade de Expression**

Nas propriedades da atividade, selecione o lookup do campo "Expressões" e adicione a seguinte expressão: "**'Teste FV: ' + rmsForEachApiActivity1.\_Items.Name.FamilyName**".

Essa expressão irá concatenar a string "**Teste FV:**" com o campo "**familyName**" depois de executar o método "**GetAll**" ou "**GetOne**" na API.

Em seguida, é necessário configurar o valor calculado, pois é ele quem vai receber a expressão criada acima.

Para realizar a configuração, clique em Ligações () e selecione o lookup do campo "**Valor Calculado**".

Na tela "**Editor de Ligações**", selecione a seguinte ligação: "**rmsForEachApiActivity1 | [] Fields | \_Items | Name | Formatted | AsString**".

5º Passo:

Após realizar todas as configurações necessárias na formula, acessamos o Postman (aplicativo que usamos para realizar testes de APIs), e chamamos o endpoint de usuários.

Verifique que ao executar o "**GetAll**", o campo "**familyName**" está sendo concatenado corretamente com a string "**Teste FV**" (condição criada na expressão da formula).

Na execução do "**GetOne**", foi passado como parâmetro o usuário "**mestre**", verifique que regra também é aplicada corretamente.

        No segundo exemplo, vamos utilizar as atividades de "**Se/Senão**" e "**Expression**" para criar uma condição, que será executada somente se o "**UserName**" de um usuário for "**Teste\_01**" Depois de executar o método "**POST**" ( no postman aplicativo que usamos para realizar testes de APIs) na API de Usuário.

falseExemplo de Utilização1º Passo:

Ao cadastrar uma Fórmula Visual com a opção **Executa em API (POCO)** habilitada (como mostrado anteriormente) é necessário adicionar os objetos que serão utilizados ao gatilho.

Para nosso exemplo, vamos utilizar a API de Usuários (Controller de Usuários) no gatilho "**Depois do método (post)**".

2º Passo:

Em seguida na estrutura da fórmula, vamos adicionar as atividades "**Se/Senão**" e "**Expression**" no Fluxo de Trabalho Sequencial da fórmula, como mostra imagem abaixo:

É necessário que seja preenchido o contexto (Controller de Usuário) da fórmula para capturar ou manipular os valores das propriedades da API utilizada.

3º Passo:

* **Configurando a Atividade Se/Senão**

Nas propriedades da atividade:

1. Selecione a Condition "**Condição de Regra Declarativa**";
2. Selecione o lookup do campo "**ConditionName**" e clique em "**Novo**" para criar uma nova condição;
3. Na tela "Editor de Condição de Regra" crie a seguinte condição: **this.ApiService.GetViewModelValue("\_Items.UserName").ToString() == "Teste\_01"**
4. Ao selecionar a condição criada o campo "Expression" será preenchido automaticamente pela condição criada.

Imagem explicativa abaixo:

* Leia mais sobre [Atividade Se/Senão](https://tdn.totvs.com/x/_YvCC)
4º Passo:

* **Configurando a Atividade de Expression**

Nas propriedades da atividade, selecione o lookup do campo "Expressões" e adicione a seguinte expressão: "**'Teste: ' + RMSWorkflow.\_Items.ExternalId**".

Essa expressão irá adicionar a string "**Teste:**" ao campo "**ExternalId**" depois de executar o método "**Post**" na API. (A expressão será aplicada somente se entrar na condição criada anteriormente).

Em seguida, é necessário configurar o valor calculado, pois é ele quem vai receber a expressão criada acima.

Para realizar a configuração, clique em Ligações () e selecione o lookup do campo "**Valor Calculado**".

Na tela "**Editor de Ligações**", selecione a seguinte ligação: "**RMSWorkflow| [] Fields | \_Items | ExternalId | AsString**".

5º Passo:

Após realizar todas as configurações necessárias na formula, acessamos o Postman (aplicativo que usamos para realizar testes de APIs), e chamamos o endpoint de usuários.

Verifique que ao executar o "**Post**", onde o usuário possui o "**UserName**" = "**Teste\_01**", o campo "**externalId**" está sendo atualizado corretamente com a string "**Teste:**" (condição criada na expressão da formula).

Quando utilizado o gatilho "**Antes do método post (post)**" a alteração é salva no banco, quando utilizado o gatilho "**Depois do método post (post)**" a atualização é feita somente no retorno da API.
