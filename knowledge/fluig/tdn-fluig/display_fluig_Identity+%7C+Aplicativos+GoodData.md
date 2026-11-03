---
content_hash: 4216dd70372da56366697780259d520f628cdd359983857f5090197b555f456c
fetched_at: '2026-06-28T21:35:25.610525+00:00'
page_id: '286207374'
product: fluig
source: tdn-fluig
title: Identity | Aplicativos GoodData
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Aplicativos+GoodData
version: 56
---

# Falando de aplicativos GoodData...

---

Aplicativos GoodData são uma categoria específica de aplicativo disponibilizada pelo Identity. Diferente dos aplicativos do tipo Padrão, que são genéricos e podem ser configurados com virtualmente qualquer serviço, os aplicativos GoodData são pré-configurados para esta aplicação. Para isso, foram definidos dois tipos de aplicativos GoodData: (1) Fluig Analytics e (2) TOTVS Analytics.

# Pré-requisitos requisitos

Para configurar um aplicativo GoodData no Identity, é necessário atentar-se aos seguintes requisitos:

* Obter o código de um projeto existente no [Fluig Analytics](http://analytics.fluig.com) ou [TOTVS Analytics](http://analytics.totvs.com.br).

Este código é fornecido no [*ticket* de criação do projeto](http://tdn.totvs.com/pages/viewpage.action?pageId=107381593) Analytics. Ele também pode ser obtido através da URL de acesso ao projeto no Fluig Analytics, conforme demonstrado [nesta FAQ](http://tdn.totvs.com/pages/viewpage.action?pageId=286211256).

* Para aplicativos do tipo Fluig Analytics, o usuário [analytics@fluig.com](mailto:analytics@fluig.com.) deve constar no painel de usuários do projeto com permissão Admin.

* Para aplicativos do tipo TOTVS Analytics, o usuário [gooddata@totvs.com.br](mailto:gooddata@totvs.com.br) deve constar no painel de usuários do projeto com permissão Admin.

# Novo aplicativo Fluig Analytics

O procedimento abaixo demonstra a criação de um novo aplicativo do tipo Fluig Analytics.

falsefluigtruePasso 1

* Acesse a empresa no Identity com um usuário administrador. Acione o menu **Aplicativos**.

Passo 2

* Acionar **Novo aplicativo** e selecionar o tipo **GoodData**.

Passo 3

* Na aba Configurações, selecionar o tipo de aplicativo **Fluig Analytics**.

Passo 4

* Informar o código do projeto do Fluig Analytics.

* Acionar **Validar informações**. O Identity dará início à verificação do código informado junto à GoodData.

A utilização do código de um projeto em mais de um aplicativo na mesma empresa do Identity não é suportada.

Passo 5

* Caso o código seja válido, será apresentada a mensagem "Projeto validado com sucesso" e o Identity irá preencher automaticamente os campos **Nome do aplicativo** e **Descrição** com as informações do projeto.

* O administrador pode alterar o nome e descrição do aplicativo, caso deseje.

* Acionar **Salvar**.

Importante

Após a criação do aplicativo, o administrador deve abrir um ticket para o [Suporte Identity](https://suporte.totvs.com/portal/p/10098/suporte-fluig-home) para que seja habilitada a integração SSO (Single Sign On) entre o projeto Fluig Analytics e o contexto da empresa no Identity. Apenas após este procedimento será possível vincular usuários, grupos e acessar o projeto através do Identity. Saiba mais em .

 O Código do projeto informado é inválido

Caso o código do projeto não seja válido, o administrador deve verificar se o código foi preenchido corretamente, se o projeto não foi excluído do Analytics e se todos os  de configuração foram atendidos.

# Novo aplicativo TOTVS Analytics

O procedimento abaixo demonstra a criação de um novo aplicativo do tipo TOTVS Analytics.

falsetotvsPasso 1

* Acesse a empresa no Identity com um usuário administrador. Acione o menu **Aplicativos**.

Passo 2

* Acionar **Novo aplicativo** e selecionar o tipo **GoodData**.

Passo 3

* Na aba Configurações, selecionar o tipo de aplicativo **TOTVS Analytics**.

Passo 4

* Informar o código do projeto do TOTVS Analytics.

* Acionar **Validar informações**. O Identity dará início à verificação do código informado junto à GoodData.

A utilização do código de um projeto em mais de um aplicativo na mesma empresa do Identity não é suportada.

Passo 5

* Caso o código seja válido, será apresentada a mensagem "Projeto validado com sucesso" e o Identity irá preencher automaticamente os campos **Nome do aplicativo** e **Descrição** com as informações do projeto.

* O administrador pode alterar o nome e descrição do aplicativo, caso deseje.

* Acionar **Salvar**.

Importante

Após a criação do aplicativo, o administrador deve abrir um ticket para o [Suporte Identity](https://suporte.totvs.com/portal/p/10098/suporte-fluig-home) para que seja habilitada a integração SSO (Single Sign On) entre o projeto TOTVS Analytics e o contexto da empresa no Identity. Apenas após este procedimento será possível vincular usuários, grupos e acessar o projeto através do Identity. Saiba mais em .

 O Código do projeto informado é inválido

Caso o código do projeto não seja válido, o administrador deve verificar se o código foi preenchido corretamente, se o projeto não foi excluído do Analytics e se todos os  de configuração foram atendidos.

# Configurações config

Uma vez criado o aplicativo do tipo GoodData, a primeira aba exibida ao administrador é a de configurações, onde são listadas as informações do projeto e opções adicionais de utilização do aplicativo.

**Baixar metadados IDP**

Os metadados do aplicativo são utilizados para realizar a autenticação SSO (*Single Sign On*) entre o Identity e a GoodData. Após criar o novo aplicativo, o administrador deve baixar os metadados do IDP e enviá-los via *ticket* para o [Suporte Identity](https://suporte.totvs.com/portal/p/10098/suporte-fluig-home) para que seja configurado o SSO.

**Mais informações**

Ao acionar esta opção são apresentadas informações adicionais sobre o aplicativo, como o código do aplicativo, URL de acesso direto e URL de *logout* direto.

**Permitir que usuários se associem ao aplicativo**

Ao acionar esta opção o aplicativo torna-se navegável, ou seja, pode ser adicionado diretamente pelos usuários aos seus respectivos Launchpads sem depender do administrador do contexto

# Usuários

Após a configuração do aplicativo com o projeto do Fluig Analytics ou TOTVS Analytics é possível atrelar usuários do Identity neste aplicativo para que uma conta correspondente seja criada automaticamente na GoodData.

falseusuariosPasso 1

* Acesse a empresa no Identity com um usuário administrador. Acione o menu **Aplicativos**.

É possível pesquisar pelo aplicativo ou selecionar a opção **Aplicativo GoodData** no filtro para visualizar apenas os aplicativos do tipo GoodData.

Passo 2

* Acessar a aba **Usuários**.

Passo 3

* Acionar **Adicionar usuários**.

* Será carregada a lista com os nomes dos usuários cadastrados neste contexto do Identity junto ao e-mail e status.

Passo 4

* Acionar o botão **Adicionar** localizado ao lado dos usuários que devem ser atrelados ao aplicativo.

* O Identity irá solicitar ao Fluig/TOTVS Analytics a criação da conta deste usuário na GoodData e a associação dele ao projeto configurado no aplicativo. Usuários pré-existentes no projeto não são sincronizados com o Identity; todas as contas criadas a partir de aplicativos GoodData serão novas.

Usuários criados no Fluig/TOTVS Analytics através do Identity **só poderão acessar estes sistemas pelo aplicativo**.

Status de Sincronização

* Na aba Usuários dos aplicativos do tipo GoodData são apresentados ao lado dos nomes, os status dos usuários em relação ao projeto na GoodData.status

| Status | Descrição |
| --- | --- |
| Sincronizado | O usuário foi criado na GoodData e associado ao projeto. |
| Processando | O usuário foi adicionado ao aplicativo e uma solicitação para a criação do usuário e associação ao projeto foi enviada à GoodData. |
| Removido | O usuário foi removido do aplicativo e uma solicitação para desassociá-lo do projeto foi enviada à GoodData. A conta do usuário não é excluída do Fluig/TOTVS Analytics. |
| Erro | Não foi possível criar o usuário na GoodData. |

Usuário desativado ou excluído da empresa?

Ao desativar um usuário da empresa no Identity, a conta deste usuário no Fluig/TOTVS Analytics não é excluída, apenas desassociada do(s) projeto(s).

Ao excluir um usuário da empresa no Identity, a conta deste usuário no Fluig/TOTVS Analytics também será excluída.

# Grupos

As propriedades de um aplicativo do tipo GoodData também contam com uma aba específica para o gerenciamento dos grupos atribuídos ao aplicativo. O comportamento é similar ao da página de Usuários, demonstrada acima.

falsegruposPasso 1

* Acesse a empresa no Identity com um usuário administrador. Acione o menu **Aplicativos**.

É possível pesquisar pelo aplicativo ou selecionar a opção **Aplicativo GoodData** no filtro para visualizar apenas os aplicativos do tipo GoodData.

Passo 2

* Acessar a aba **Grupos**.

Passo 3

* Acionar **Adicionar grupos**.

* Será carregada a lista com os nomes dos grupos cadastrados neste contexto do Identity.

Passo 4

* Acionar o botão **Adicionar** localizado ao lado dos grupos que devem ser atrelados ao aplicativo.

* O Identity irá solicitar ao Fluig/TOTVS Analytics que seja realizada a criação da conta dos integrantes deste(s) grupo(s) na GoodData e a associação ao projeto configurado no aplicativo.

Usuários criados no Fluig/TOTVS Analytics através do Identity **só poderão acessar estes sistemas pelo aplicativo**.

Passo 5

* Para visualizar os integrantes de um grupo associado ao aplicativo, acionar **Ver usuários**.

* O administrador será redirecionado para a aba Usuários do aplicativo, onde o filtro será automaticamente preenchido com o nome do grupo selecionado.

Fique atento!

Os integrantes de um grupo associado a um aplicativo do tipo GoodData não podem ser removidos individualmente do aplicativo. É necessário desassociar o usuário em questão do grupo para que o vínculo com o aplicativo seja removido.

# Operações

É possível acompanhar o *status* das operações de sincronização dos usuários em relação ao projeto na GoodData, bem como visualizar as inconsistências que podem ter ocorrido e reprocessar a sincronização em caso de erro.

falseoperaçõesPasso 1

* Acesse a empresa no Identity com um usuário administrador. Acione o menu **Aplicativos**.

É possível pesquisar pelo aplicativo ou selecionar a opção **Aplicativo GoodData** no filtro para visualizar apenas os aplicativos do tipo GoodData.

Passo 2

* Acessar a aba **Operações**.

Passo 3

* Visualizar as operações realizadas.

É possível filtrar as operações por usuários ou por e-mail.

Além disso, também é possível filtrá-las pelo *status* – Processando, Erro, Pendente ou Sincronizado – e por operação realizada – Adição ou Remoção do usuário no aplicativo ou, ainda, Remoção do usuário da empresa.

Os possíveis *status* que as operações realizadas podem ter são detalhados .

Passo 4

* Para visualizar a inconsistência ocorrida na sincronização de um determinado usuário, acionar **Erro**, localizado na linha do usuário em questão.

* Na janela exibida, acionar **Mostrar detalhes**.

  
Passo 5

* Para reprocessar a operação para um determinado usuário, acionar **Reprocessar**, localizado na linha do usuário em questão.

Somente é possível reprocessar uma operação se ela estiver com o status **Processando** ou **Erro**.

Ao reprocessar uma operação, uma nova solicitação de criação e associação do usuário ao projeto é enviada à GoodData.

# Remover aplicativo do tipo GoodData

Ao remover um aplicativo do tipo GoodData, os usuários vinculados ao aplicativo diretamente ou através de grupos são desassociados do projeto Fluig/TOTVS Analytics configurado.

# Múltiplos projetos

Usuários que estiverem vinculados a mais de um projeto Fluig/TOTVS Analytics, ao acessarem o aplicativo pelo Launchpad, não são direcionados necessariamente ao projeto configurado no aplicativo. Isso ocorre porque o comportamento definido pela GoodData é direcionar o usuário para o último projeto acessado e esta regra não pode ser alterada pelo Identity.

No primeiro acesso pelo aplicativo é apresentada uma lista com todos os projetos aos quais o usuário está vinculado para que ele possa selecionar qual deseja acessar.

 ]]>
