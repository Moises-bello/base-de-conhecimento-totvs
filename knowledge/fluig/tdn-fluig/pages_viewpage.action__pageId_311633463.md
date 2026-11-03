---
content_hash: e7ca510760699cd71908c78ba8d150aa7ff180cbda7793a0824c2f4e9e113ab3
fetched_at: '2026-06-28T21:35:25.821660+00:00'
page_id: '311633463'
product: fluig
source: tdn-fluig
title: Identity | Usuários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=311633463
version: 69
---

50%

5.\*ndice

50%

trueIdioma

# Falando de usuários...

---

A página de gerenciamento de usuários permite ao administrador da empresa consultar os nomes, e-mails, situação, quantidade e a página de cadastro de cada usuário, além de atribuir aplicativos e associar os usuários a grupos. Todas as alterações nos usuários são registradas no .

Também é a partir da página Gerenciar Usuários que é iniciado o procedimento de incluir novos usuários manualmente no contexto.

As situações possíveis para as contas no TOTVS Identity são:

* **Ativado:** o usuário criado/importado está ativo e pode acessar o contexto.
* **Convidado:** o usuário criado ainda não acessou o contexto pela primeira vez e por isso a conta ainda não foi ativada.
* **Desativado:** o usuário criado/importado foi desativado do contexto pelo administrador corporativo e por isso não pode mais acessá-lo.
* **Bloqueado**: o usuário criado/importado está impedido de acessar a empresa pois excedeu o limite de tentativas sem sucesso estabelecidas na política da empresa.

As funções disponíveis para as contas no TOTVS Identity são:

* **Administrador:** este tipo de conta garante o acesso ao gerenciamento de usuários, grupos, aplicativos e demais configurações do contexto da empresa no Identity.
* **Usuário comum:** este tipo de conta permite o acesso aos aplicativos navegáveis ou atribuídos ao usuário pelo administrador e ao perfil pessoal do usuário.

## Consultar usuários

---

**01.** Acione o menu **Usuários**.

#f2f2f2#f2f2f2

Será apresentada uma lista com todos os usuários cadastrados no contexto da empresa no TOTVS Identity, tanto os importados de um Active Directory quanto criados manualmente. Ao lado do nome de cada usuário é possível verificar o tipo da conta (Usuário comum ou Administrador) e a situação na empresa (**Ativado**, **Convidado**, **Desativado** ou **Bloqueado**).

### Buscar usuários

---

**01.** Acione o menu **Usuários.**

**02.** No campo **Buscar usuário**, escolha se a busca será pelo e-mail, por nome ou sobrenome ou pelo nome de usuário.

**03**. Informe o texto a ser buscado.

### Filtrar usuários

---

**01.** Acione o menu **Usuários.**

**02.** Acione o botão **Filtrar .**

**03**. Na área **Filtrar usuários**, modifique os filtros conforme a necessidade e acione o botão **Aplicar filtro**.

#f2f2f2#f2f2f2

As opções disponíveis são:

* **Filtrar por tipo:** permite o filtro por usuários comuns ou administradores.
* **Filtrar por situação:** permite o filtro por situação na empresa (**Ativado**, **Convidado**, **Desativado** ou **Bloqueado**).

**04.** Para remover os filtros utilizados e visualizar novamente a lista completa, acione **Limpar filtros**.

### Exportar usuários

---

**01.** Acione o menu **Usuários.**

**02.** Modifique os filtros conforme a necessidade.

**03**. Acione o botão **Exportar** .

**04**. Na mensagem de confirmação, acione a opção **Exportar**.

#f2f2f2#f2f2f2

Os registros exibidos na página no momento em que o botão Exportar foi acionado serão exportados em um arquivo CSV. Um link com validade de 48 horas é enviado ao endereço de e-mail do administrador que solicitou o relatório para que seja feito o download do arquivo exportado.

**05**. Acesse o e-mail e clique no link para fazer o download do relatório.

#f2f2f2#f2f2f2

O navegador deve apresentar automaticamente a opção para salvar um arquivo em formato CSV. Caso não ocorra, na guia aberta, acione a opção **Baixar**.

O arquivo CSV contém o e-mail, o identificador, nome completo, função (usuário comum ou administrador) e a situação no momento atual de geração do relatório.

## Adicionar usuário

---

Esses passos se referem à inclusão manual de usuários em uma empresa do TOTVS Identity. Para conhecer a importação de usuários do Active Directory, consulte a documentação de [Active Directory.](https://tdn.totvs.com/x/AptUE)

**01.** Acione o menu **Usuários**.

**02.** Acione o botão **Adicionar usuário**.

**03.** Insira as informações solicitadas na aba **Dados da conta**.

#f2f2f2#f2f2f2

As informações solicitadas são:

Novo usuário

**Nome**  
Nome do usuário

**Sobrenome**  
Sobrenome do usuário

**Deseja habilitar o acesso com um nome de usuário?**Esse campo é apresentado somente se o acesso com nome de usuário for habilitado para a empresa.  
Ao habilitar essa opção, o usuário acessará o sistema através de um nome de usuário, sem usar um e-mail. Essa forma de acesso só está disponível para usuários comuns.

**Usuário**Esse campo é apresentado somente se o acesso com nome de usuário estiver habilitado.  
Login utilizado para autenticação no Identity e nos aplicativos TOTVS. Esse login deve respeitar os seguintes requisitos: ter até 150 caracteres, não começar nem terminar com caracteres especiais e ser único na empresa.

**E-mail**Esse campo é apresentado somente se o acesso com nome de usuário estiver desabilitado.Endereço de e-mail que será utilizado para autenticação no Identity e nos aplicativos TOTVS. O endereço de e-mail deve ser válido e é único para cada conta do contexto.

**Deseja tornar este usuário administrador?**  
Ao habilitar essa opção, define que este usuário terá papel de administrador, gerenciando usuários, grupos, aplicativos e demais configurações do contexto do Identity.

Opções de ativação

Na seção **Opções de ativação** é realizada aseleção da forma de ativação da conta. As opções disponíveis são:

* **E-mail de Convite**: Quando assinalada, a ativação da conta é realizada através de um *link* contido no convite enviado para o e-mail do usuário.
* **Senha Temporária**: Quando assinalada, a ativação da conta é realizada assim que o cadastro é concluído pelo administrador. Para visualizar a senha temporária gerada, o administrador deve acessar a página de visualização do usuário. Nenhum convite é enviado por e-mail nesta modalidade de ativação.

Ambas as formas de ativação exigem que o usuário crie uma senha pessoal para ter acesso ao contexto.

É possível configurar qual das formas de autenticação virá pré-selecionada no cadastro de novo usuário pela página [Novas contas](https://tdn.totvs.com/x/UJlUE).

Campos customizados

A seção **Campos customizados** só é apresentadase houver campos criados no recurso de [Customização](https://tdn.totvs.com/x/CptUE) do Identity.

**04.** Acione a aba **Grupos** e marque os grupos que devem ser associados ao usuário**.**

#f2f2f2#f2f2f2

Por padrão, o usuário é automaticamente associado no grupo Everyone, que concentra todos os usuários da empresa. É possível utilizar a busca para filtrar, caso existam muitos grupos cadastrados.

Associando o usuário aos grupos, todos os aplicativos vinculados serão associados automaticamente ao usuário.

**05**. Acione a aba **Aplicativos** e marque os aplicativos que devem ser associados ao usuário**.**

#f2f2f2#f2f2f2

O usuário é automaticamente associado aos aplicativos vinculados ao grupo Everyone e aos demais grupos em que ele for adicionado. É possível utilizar a busca para filtrar os aplicativos desejados.

**06**. Acione **Adicionar usuário** para concluir a inclusão do usuário.

## Visualizar usuário

---

A página de dados de usuário reúne informações de cadastro e permite ao administrador tomar uma série de ações relativas à conta do usuário como, por exemplo, reenviar o convite por e-mail, redefinir a configuração MFA, alterar o tipo do usuário, associar grupos, atribuir aplicativos, provisionar no Active Directory, desativar a conta, entre outros.

**01.** Acione o menu **Usuários**.

**02.** Localize o usuário desejado na lista.

**03.** Clique sobre o nome do usuário ou sobre o ícone **Visualizar**  para abrir a respectiva página com os dados.

#f2f2f2#f2f2f2

DADOS DO USUÁRIO

**Nome**Campo único para o nome e sobrenome do usuário.

Para usuários sincronizados com o Active Directory, o Primeiro Nome (First Name) será considerado até o primeiro espaço. Os termos a seguir serão considerados Sobrenome (Last Name). Por exemplo: Se o nome informado neste campo for **Luis Fernando da Silva**, o primeiro nome será **Luis** e **Fernando da Silva** será considerado o sobrenome.

**E-mail** ou **nome de usuário**E-mail ou nome utilizado para acesso do usuário ao contexto da empresa no Identity.

**Tipo de usuário**Os tipos existentes são: administrador ou usuário comum.

* **Administrador:** este tipo de conta garante o acesso ao gerenciamento de usuários, grupos, aplicativos e demais configurações do contexto no Identity.
* **Usuário comum:** este tipo de conta permite o acesso aos aplicativos navegáveis ou atribuídos ao usuário pelo administrador e ao perfil pessoal do usuário.

**Situação**O usuário pode estar **Ativado**, **Convidado**, **Desativado** ou **Bloqueado**. Abaixo da situação é apresentada a data em que ocorreu a última alteração na situação do usuário.

**Departamento**Departamento vinculado ao usuário.

**Senha temporária**A senha temporária é exibida apenas se o usuário ainda não tiver alterado a senha temporária gerada pelo administrador.

**Campos customizados**

A seção **Campos customizados** só é apresentadase houver campos criados no recurso de [Customização](https://tdn.totvs.com/x/CptUE) do Identity.Caso tenham campos customizados, esses campos aparecem para consulta abaixo das informações cadastrais do usuário.

ASSOCIADOS AO USUÁRIO

**Grupos**Quantidade de grupos aos quais o usuário foi associado.

**Aplicativos**Quantidade de aplicativos atribuídos ao usuário.

**Provisionamento Active Directory**Situação dos usuários importados no Active Directory. Permite realizar o provisionamento da conta no Active Directory, caso exista uma diretório vinculado ao contexto.

**Autenticação MFA**Indica como está o acesso com autenticação multifator desse usuário: Desabilitado, Configurado e Não configurado.

## Editar usuário

---

**01.**Acione o menu **Usuários**.

**02.** Localize o usuário desejado na lista.

**03**. Acione o ícone **Editar**  e altere as informações desejadas.

#f2f2f2#f2f2f2

As informações que podem ser alteradas são: Nome do usuário, Tipo de usuário, Departamento e campos customizados (caso tenham). O e-mail ou nome de usuário não pode ser alterado pelo usuário administrador.

**04.** Acione **Salvar** para confirmar as alterações.

## Exportar dados pessoais

---

**01.** Acione o menu **Usuários**.

**02.** Localize o usuário desejado na lista.

**03**. Acione o ícone **Exportar** .

**04.** Informe o e-mail do usuário como confirmação.

**05.** Acione **Exportar**para confirmar.

#f2f2f2#f2f2f2Será feito o *download* dos dados do respectivo usuário relacionados à empresa atual em um arquivo JSON. Neste arquivo é possível consultar todo o histórico de visualizações e alterações que houve nos dados pessoais relacionados a esse usuário.

## Grupos do usuário

---

### Associar usuário a grupos

---

**01.**Acione o menu **Usuários.**

**02**. Localize o usuário desejado na lista apresentada.

**03.** Acione **Mais opções** localizado na linha do usuário e clique na opção **Associar grupos**.

#f2f2f2#f2f2f2

É apresentada uma lista com todos os grupos cadastrados no contexto da empresa no TOTVS Identity, tanto os importados do Active Directory quanto criados manualmente.

**04.** Marque na área correspondente ao grupo que deve ser incluído e acione **Associar** **grupos** para confirmar.

### Gerenciar grupos

---

**01.**Acione o menu **Usuários.**

**02**. Localize o usuário desejado na lista apresentada.

**03.** Acione **Mais opções** localizado na linha do usuário e clique na opção **Gerenciar grupos**.

#f2f2f2#f2f2f2

É apresentada uma lista com todos os grupos aos quais o usuário foi associado.

**04.** Localize os grupos dos quais deseja remover o usuário e acione **Remover grupo** .

## Aplicativos do usuário

---

### Adicionar aplicativos

---

**01.**Acione o menu **Usuários.**

**02.** Localize o usuário desejado na lista apresentada.

**03.** Acione **Mais opções**  localizado na linha do usuário e clique na opção **Associar aplicativos**.

#f2f2f2#f2f2f2

É apresentada uma lista com todos os aplicativos cadastrados no contexto da empresa no TOTVS Identity.

**04.** Localize na lista os aplicativos desejados ou utilize o campo **Buscar aplicativos** para encontrá-los.

**05.** Marque na área correspondente ao aplicativo que deseja atribuir e então acione **Associar aplicativos**.

### Gerenciar aplicativos

---

**01.**Acione o menu **Usuários.**

**02.** Localize o usuário desejado na lista apresentada.

**03.** Acione **Mais opções**  localizado na linha do usuário e clique na opção **Gerenciar aplicativos**.

#f2f2f2#f2f2f2

Serão listados os aplicativos atribuídos diretamente à conta do usuário ou associados aos grupos do usuário. Somente os aplicativos associados ao usuário podem ser removidos por meio dessa tela.

**04.** Localize os aplicativos que deseja remover, acione **Mais opções** e então **Remover aplicativo**.

## Provisionamento do Active Directory

---

**01.**Acione o menu **Usuários**.

**02.** Localize o usuário desejado na lista.

**03.** Clique sobre o nome do usuário ou sobre o ícone **Visualizar**  para abrir a respectiva página com os dados do usuário.

#f2f2f2#f2f2f2

O quadro **Provisionamento Active Directory** apresenta a situação de provisionamento do usuário no Active Directory.

* **Provisionamento habilitado** : Apresenta o AD no qual o usuário está provisionado e a opção **Mais detalhes** para consulta aos dados do Active Directory (Domínio da conta, DN Raíz, ObjectGUID e ImmutableID).
* **Provisionamento não configurado** : A opção **Provisionar** é apresentada para que o usuário seja criado em um dos diretórios AD vinculados ao contexto do TOTVS Identity.
* **Provisionamento disponível para configuração** : Caso não exista nenhum [AD vinculado](https://tdn.totvs.com/x/W55UE) ao contexto da empresa no Identity, nenhuma informação será exibida no quadro e a cor de fundo apresentada será cinza.

### Consultar detalhes

---

**01.**Acione o menu **Usuários**.

**02.** Localize o usuário desejado na lista.

**03.** Clique sobre o nome do usuário ou sobre o ícone **Visualizar**  para abrir a respectiva página com os dados do usuário.

**04**. No quadro **Provisionamento Active Directory**, acione o botãoe então**Mais detalhes**.

#f2f2f2#f2f2f2

Serão listados para consulta o Domínio da conta, DN Raíz, ObjectGUID e ImmutableID do usuário sincronizado com o Active Directory.

### Provisionar usuário

---

**01.**Acione o menu **Usuários**.

**02.** Localize o usuário desejado na lista.

**03.** Clique sobre o nome do usuário ou sobre o ícone **Visualizar**  para abrir a respectiva página com os dados do usuário.

**04**. No quadro **Provisionamento Active Directory**, acione o botãoe então**Provisionar Active Directory**.

**05**. Preencha os campos de dados da conta para provisionar o usuário para o Active Directory.

#f2f2f2#f2f2f2

Os dados necessários para o provisionamento são:

**Active Directory**  
Selecione o diretório desejado dentre aqueles que foram .

**DN Raiz** e **Domínio da Conta**Os campos DN Raiz e Domínio da Conta são preenchidos automaticamente com base no Active Directory selecionado, mas podem ser editados caso desejado.

**Senha provisória** e **Redigite a senha**  
Informe a senha temporária e repita a senha para confirmação. Esta senha será atribuída apenas à conta do usuário criada no Active Directory.

**06.** Acione **Salvar**.

#f2f2f2#f2f2f2

Será enviada uma requisição para o Active Directory através do SmartSync, para que o usuário seja criado no domínio escolhido. Após o provisionamento, o usuário poderá autenticar-se com a senha do Active Directory neste contexto do Identity, caso a administração da empresa tenha habilitado este recurso.

## Autenticação MFA

---

**01.**Acione o menu **Usuários**.

**02.** Localize o usuário desejado na lista.

**03.** Clique sobre o nome do usuário ou sobre o ícone **Visualizar**  para abrir a respectiva página com os dados do usuário.

#f2f2f2#f2f2f2

O quadro **Autenticação MFA** apresenta a situação desse recurso de segurança para o usuário em questão.

* **Autenticação com MFA habilitada** : A configuração foi realizada pelo usuário e a opção **Desabilitar** pode ser utilizada pelo administrador em caso de perda ou roubo do aparelho do usuário.
* **Autenticação com MFA desabilitada** : O usuário ainda não configurou a autenticação multifator em sua conta.

### Desativar acesso com MFA do usuário

---

Esta opção permite que a configuração da autenticação multifator seja feita novamente em caso de troca de aparelho ou remoção da conta previamente cadastrada no aplicativo , por exemplo.

**01.**Acione o menu **Usuários**.

**02.** Localize o usuário desejado na lista.

**03.** Clique sobre o nome do usuário ou sobre o ícone **Visualizar**  para abrir a respectiva página com os dados do usuário.

**04**. No quadro **Autenticação MFA**, acione o botãoe então**Desabilitar**.

**05**. Insira uma justificativa e a senha para confirmar a ação.

#f2f2f2#f2f2f2

A justificativa é obrigatória e fica registrada em histórico, posteriormente pode ser consultada no relatório de auditoria.

**05**. Acione o botão **Desabilitar**.

#f2f2f2#f2f2f2

Caso o usuário faça parte de um grupo com MFA obrigatório, é necessário configurar novamente a autenticação multifator para que o acesso ao Identity seja liberado.

## Reenviar convite

---

Essa opção só é apresentada caso o usuário esteja com a situação **Convidado**.**01.**Acione o menu **Usuários**.

**02.** Localize o usuário desejado na lista.

**03.** Clique sobre o nome do usuário ou sobre o ícone **Visualizar**  para abrir a respectiva página com os dados do usuário.

**04**. Em Ações, acione **Mais opções** e então**Reenviar convite**.

#f2f2f2#f2f2f2

Uma nova mensagem de convite é enviada ao e-mail do usuário com um *link* para ativação da conta nesse contexto do TOTVS Identity.

## Senha temporária

---

Essa senha é gerada para usuários criados a partir da opção de ativação por senha temporária, ou para reset de senha nos casos em que o usuário não tem e-mail cadastrado e, consequentemente, não consegue efetuar o reset de senha pela tela de login.

### Copiar senha temporária

---

**01.**Acione o menu **Usuários**.

**02.** Localize o usuário desejado na lista.

**03.** Clique sobre o nome do usuário ou sobre o ícone **Visualizar**  para abrir a respectiva página com os dados do usuário.

**04**. Localize o campo **Senha temporária** e acione **Copiar senha temporária** .

#f2f2f2#f2f2f2

Após acionar essa opção, a senha temporária é copiada para a área de transferência do usuário autenticado, e deve ser repassada ao usuário que necessita do acesso ao Identity. No primeiro login, o usuário é obrigado a alterar essa senha.

### Resetar senha

---

Essa função só é permitida para usuário sem e-mail. Quando é gerada uma senha temporária para o usuário, ele automaticamente não consegue mais acessar com a senha anterior.

**01.**Acione o menu **Usuários**.

**02.** Localize o usuário desejado na lista.

**03.** Clique sobre o nome do usuário ou sobre o ícone **Visualizar**  para abrir a respectiva página com os dados do usuário.

**04**. Em Ações, acione **Mais opções** e então **Resetar senha**.

#f2f2f2#f2f2f2

Após acionar essa opção, será apresentada ao administrador uma senha temporária. Essa senha deve ser informada ao usuário, para que ele possa efetuar o login normalmente. No primeiro login, o usuário é obrigado a alterar essa senha.

## Desativação temporária

---

Esse recurso possibilita que o usuário seja desativado por um período predefinido e após esse período, seja automaticamente reativado no TOTVS Identity.

### Planejar desativação temporária

---

**01.**Acione o menu **Usuários**.

**02.** Localize o usuário desejado na lista.

**03.** Clique sobre o nome do usuário ou sobre o ícone **Visualizar**  para abrir a respectiva página com os dados do usuário.

**04**. Em Ações, acione **Mais opções** e então **Desativação temporária**.

**05.** Preencha as informações necessárias.

#f2f2f2#f2f2f2

**Data Inicial**Data em que o usuário deve ser desativado. Caso a data inicial configurada seja a atual, a desativação pode levar algumas horas para ser executada.

**Data Final**  
Data em que o usuário deve ser reativado.

**Descrição**  
Campo opcional, para que sejam incluídas mais informações sobre a desativação.

**06.** Acione **Desativar**.

#f2f2f2#f2f2f2

Após salvar, o período de desativação temporária será apresentado na tela de dados do usuário.

A desativação temporária não sincroniza a situação do usuário desativado no TOTVS Identity com o Active Directory.

### Alterar período de desativação temporária

---

**01.**Acione o menu **Usuários**.

**02.** Localize o usuário desejado na lista.

**03.** Clique sobre o nome do usuário ou sobre o ícone **Visualizar**  para abrir a respectiva página com os dados do usuário.

**04**. Localize o campo Desativação temporária e acione **Editar desativação**.

**05.** Ajuste as informações necessárias.

**06.** Acione **Desativar**.

#f2f2f2#f2f2f2

O período de desativação temporária será apresentado na tela de dados do usuário.

### Remover período de desativação temporária

---

**01.**Acione o menu **Usuários**.

**02.** Localize o usuário desejado na lista.

**03.** Clique sobre o nome do usuário ou sobre o ícone **Visualizar**  para abrir a respectiva página com os dados do usuário.

**04**. Localize o campo Desativação temporária e acione **Remover desativação .**

#f2f2f2#f2f2f2

O usuário não será desativado no período definido previamente.

## Desativar usuário

---

**01.**Acione o menu **Usuários**.

**02.** Localize o usuário desejado na lista.

**03.** Clique sobre o nome do usuário ou sobre o ícone **Visualizar**  para abrir a respectiva página com os dados do usuário.

**04**. Em Ações, acione **Mais opções** e então **Desativar usuário**.

**05.** Confirme a desativação acionando **Desativar**.

#f2f2f2#f2f2f2

Após confirmar, o usuário não terá mais acesso ao contexto em que foi desativado, a menos que seja reativado por um administrador.

Nos contextos em que a opção  esteja ativada, o usuário também será desativado no Active Directory.

## Reativar usuário

---

Essa opção só é apresentada caso o usuário esteja com a situação **Desativado**.

**01.**Acione o menu **Usuários**.

**02.** Localize o usuário desejado na lista.

**03.** Clique sobre o nome do usuário ou sobre o ícone **Visualizar**  para abrir a respectiva página com os dados do usuário.

**04**. Em Ações, acione **Mais opções** e então **Ativar usuário**.

**05.** Confirme a ativação acionando **Ativar**.

#f2f2f2#f2f2f2

O usuário volta a ter acesso completo à conta no contexto.

## Excluir usuário

---

**01.**Acione o menu **Usuários**.

**02.** Localize o usuário desejado na lista.

**03.** Clique sobre o nome do usuário ou sobre o ícone **Visualizar**  para abrir a respectiva página com os dados do usuário.

**04**. Em Ações, acione **Excluir usuário** .

**05.** Para confirmar a exclusão, acione **Excluir**.

#f2f2f2#f2f2f2

Após confirmar, a conta do usuário será totalmente removida da empresa e não poderá ser restaurada. O usuário não terá mais acesso ao contexto do TOTVS Identity do qual foi removido.

Caso o usuário excluído tenha sido importado a partir do Active Directory, sua conta será automaticamente incluída na lista de [Rejeitados](http://tdn.totvs.com/pages/viewpage.action?pageId=273989076).

Atenção

No processo para excluir um usuário existem etapas que são assíncronas e também destacamos que remover registros pode ser oneroso em relação ao tempo do processamento do banco de dados. Com isso, pode haver variação de tempo na exclusão para cada usuário do TOTVS Identity, por este motivo, recomendamos que após a confirmação da exclusão, o usuário atualize a página para validar de fato que o usuário em questão foi removido.

## Desbloquear usuário

---

Essa opção só é apresentada caso o usuário esteja com a situação **Bloqueado**, ou seja, tenha sido bloqueado por excesso de tentativas de login.

**01.**Acione o menu **Usuários**.

**02.** Localize o usuário desejado na lista.

**03.** Clique sobre o nome do usuário ou sobre o ícone **Visualizar**  para abrir a respectiva página com os dados do usuário.

**04**. Em Ações, acione **Mais opções** e então **Desbloquear**.

**05.** Na janela de confirmação, acione **Desbloquear**.

#f2f2f2#f2f2f2

Com isso, o usuário estará poderá voltar a tela de login para autenticar-se ou acionar a opção **Esqueceu sua senha?**.

Dica!

Caso o usuário tenha um e-mail de reset de senha configurado, ele próprio consegue realizar o desbloqueio pela opção de .

]]>
