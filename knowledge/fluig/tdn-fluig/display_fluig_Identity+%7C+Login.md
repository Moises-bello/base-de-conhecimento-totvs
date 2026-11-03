---
content_hash: aef047175ed3282c3cbaa7890c9c7916ece72468fe17a9103543ee80f5bddb1a
fetched_at: '2026-06-28T21:35:25.005009+00:00'
page_id: '273980013'
product: fluig
source: tdn-fluig
title: Identity | Login
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Login
version: 141
---

50%

5.\*ndice

50%

trueIdioma

Dica!

Para tornar o sistema mais acessível, o recurso de Login é adaptado para aplicações leitoras.

# Falando de login...

---

A página de login é o portal por onde as pessoas acessam a empresa no TOTVS Identity. Para acessar a página de login, informa-se o domínio da empresa na barra de endereços do navegador, por exemplo: https://suaempresa.fluigidentity.com.

A pessoa só poderá autenticar-se através da página de login de uma empresa à qual pertence, caso contrário terá o acesso negado. Caso deixe de interagir com o Identity por mais de 2 horas, terá que informar novamente as credenciais de acesso.

O Identity permite a utilização de dois tipos de senhas no login: a [Senha pessoal](https://tdn.totvs.com/pages/viewpage.action?pageId=274828593) ou a senha de rede, sendo que esta última exige integração com o [Active Directory](https://tdn.totvs.com/x/ZWWPKQ).

A cada tentativa de autenticação, o Identity irá verificar se a senha informada pelo usuário está de acordo com a  da empresa, no que se refere à quantidade de caracteres, tempo de expiração, entre outras configurações. Caso a senha não esteja atendendo a algum dos requisitos, será necessário realizar a troca de senha, para que o login seja realizado com sucesso.

Na  também pode ser habilitada a configuração de tentativas máximas de acesso, e caso o usuário exceda a quantidade de tentativas sem sucesso, seu acesso é bloqueado e ele recebe por e-mail um aviso sobre o impedimento.

Caso o usuário esteja vinculado em várias empresas e esteja acessando pelo endereço genérico ([app.fluigidentity.com](https://app.fluigidentity.com)), a cada login é necessário escolher em qual empresa deseja entrar, ou então pode definir uma empresa como principal.

## Fazer login

---

**100%true5%**

**01.** Na página de login da empresa no Identity, informe o e-mail ou usuário da conta.

**02.** Informe a senha de acesso.

#f2f2f2#f2f2f2

Pode ser utilizada a senha pessoal ou a senha de rede, caso a integração com o Active Directory esteja habilitada para a empresa.

**03.** Acione **Entrar**.

#f2f2f2#f2f2f2

Após acionar Entrar, se as informações estiverem corretas, o Identity irá efetuar a autenticação no sistema. Com isso, caso exista um [termo de consentimento](https://tdn.totvs.com/x/MQxpHw) configurado, será necessário aceitá-lo para que a pessoa seja direcionada ao .

## Fazer login com CAPTCHA

---

Essa opção só é permitida se o recurso de [Segurança por CAPTCHA](https://tdn.totvs.com/x/WZNvI) tiver sido habilitado por quem administra a empresa no Identity.

**100%true5%**

**01.** Na página de login da empresa no Identity, informe o e-mail ou usuário da conta.

**02.** Informe a senha de acesso.

#f2f2f2#f2f2f2

Pode ser utilizada a senha pessoal ou a senha de rede, caso a integração com o Active Directory esteja habilitada para a empresa.

**03.** Acione **Entrar**.

#f2f2f2#f2f2f2

Será apresentada uma janela com um desafio, onde devem ser selecionados os blocos que contenham o objeto descrito no texto.

Caso não consiga compreender a imagem, é possível utilizar uma nova imagem acionando o botão  **Receber outro desafio**.

**04.** Clique em **Verificar**.

#f2f2f2#f2f2f2

Se as informações estiverem corretas, o Identity irá efetuar a autenticação no sistema.

Com isso, caso exista um [termo de consentimento](https://tdn.totvs.com/x/MQxpHw) configurado, será necessário aceitá-lo para que a pessoa seja direcionada ao .

## Fazer login com autenticação multifator (MFA)

---

Essa opção será apresentada somente se , ou se o recurso for **obrigatório** para um grupo ao qual ela faça parte.

**100%true5%**

**01.** Na página de login da empresa no Identity, informe o e-mail ou usuário da conta.

**02.** Informe a senha de acesso.

#f2f2f2#f2f2f2

Pode ser utilizada a senha pessoal ou a senha de rede, caso a integração com o Active Directory esteja habilitada para a empresa.

**03.** Acione **Entrar**.

#f2f2f2#f2f2f2

Caso o MFA tenha sido configurado como obrigatório para o grupo e ainda não tenha sido configurado pelo usuário informado, será necessário seguir as instruções indicadas na tela até concluir a configuração.

**04.** Acesse o aplicativo **My Safe id**em seu aparelho e visualize o código obtido.

#f2f2f2#f2f2f2

Recomendamos o uso do aplicativo My Safe id, mas existem outros aplicativos autenticadores no mercado e eles são compatíveis, pode-se optar pelo autenticador de sua preferência.

**05.** Na página de autenticação multifator no Identity, informe o código e acione **Entrar**.

#f2f2f2#f2f2f2

Após isso, se as informações estiverem corretas, o Identity irá efetuar a autenticação no sistema. Com isso, caso exista um [termo de consentimento](https://tdn.totvs.com/x/MQxpHw) configurado, será necessário aceitá-lo para que a pessoa seja direcionada ao .

Importante!

Para que o MFA funcione corretamente, é necessário que o dispositivo a partir do qual está sendo realizado o login e o dispositivo gerador do token estejam exatamente no mesmo horário. A variação de horário, mesmo que seja pouco tempo (1 minuto) já dá erro de token.

## Fazer login com a senha temporária

---

Apenas quem administra a empresa no Identity pode gerar senha temporária para os demais usuários, no momento do cadastro ou no gerenciamento. Quando é gerada uma senha temporária para o usuário, ele automaticamente não conseguirá mais acessar com a senha anterior.

**01.** Na página de login da empresa no Identity, informar o e-mail ou usuário da conta.

**02.** Informar a senha temporária repassada pela administração da empresa.

#f2f2f2#f2f2f2

Após isso, se as informações estiverem corretas, o Identity irá solicitar que seja feita a alteração de senha, antes de prosseguir com a autenticação no sistema.

## Fazer login com rede social

---

Essa opção será apresentada somente se um provedor tiver sido configurado. Para mais detalhes, consulte a documentação de .

**01.** Na página de login da empresa no Identity, clicar sobre a rede social que deseja utilizar para autenticação.

**02.** Informar a conta e a senha cadastrada na rede social.

#f2f2f2#f2f2f2

Após isso, se as informações estiverem corretas, o Identity irá efetuar a autenticação no sistema. Com isso, caso exista um [termo de consentimento](https://tdn.totvs.com/x/MQxpHw) configurado, será necessário aceitá-lo para que a pessoa seja direcionada ao .

## Definir empresa principal no login

---

Essa opção está disponível somente para usuários que estejam vinculados em várias empresas e estejam acessando pelo endereço genérico ([app.fluigidentity.com](https://app.fluigidentity.com)). A cada login é necessário escolher em qual empresa deseja entrar, ou então cada usuário pode definir uma empresa como principal.

**01.** Acesse o endereço <https://app.fluigidentity.com/> e informe o e-mail ou usuário da conta.

**02.** Informe a senha de acesso e acione **Entrar**.

#f2f2f2#f2f2f2

Após isso, se as informações estiverem corretas, o Identity apresenta a lista com todas as empresas as quais o usuário está vinculado.

**03**. Selecione a empresa que deseja acessar.

**04**. Marque a opção **Salve a escolha e acesse sempre a mesma empresa** para definir que sempre será a empresa acessada.

**05**. Acione **Entrar** para acessar o Identity.

#f2f2f2#f2f2f2

Para alterar a empresa definida como principal, é necessário acessar as .

## Recuperação de senha

---

Caso o usuário esteja com a situação **Convidado**, esse recurso realiza o reenvio do e-mail de convite. Usuários que estejam com a situação **Desativado** não podem fazer reset de senha. Caso o usuário não tenha e-mail cadastrado, o reset de senha deve ser solicitado ao usuário administrador.

**100%true5%**

**01.** Na página de login da empresa no Identity, acione a opção **Esqueceu sua senha?**.

**02.** No campo **E-mail**, informe o endereço de e-mail associado à conta da qual deseja recuperar a senha.

#f2f2f2#f2f2f2

Um e-mail contendo um código numérico para a redefinição da senha pessoal é enviado para a caixa de e-mail informada. A expiração desse código ocorre em 10 minutos.

**03**. Informe o código numérico recebido por e-mail no campo **Código de autenticação** e acione **Confirmar código**.

#f2f2f2#f2f2f2

Se o código informado estiver correto e dentro desse período válido, você pode definir uma nova senha de acesso.

**04**. Na tela de reset de senha, informe a nova senha.

#f2f2f2#f2f2f2

A nova senha deve seguir os requisitos que foram configurados na  da empresa.

A opção de seleção entre **Senha Pessoal** e **Active Directory** é apresentada apenas quando a empresa tem  e  habilitados em sua configuração.

Caso não exista AD configurado na empresa, ocorre somente a troca da senha pessoal. E caso não esteja habilitada a senha pessoal na empresa, ocorre somente a troca da senha do AD. Nestes dois casos, não é apresentada nenhuma opção de seleção em tela, com exceção caso você seja administrador da empresa.

**05**. Acione **Alterar senha** para concluir a recuperação de senha.

#f2f2f2#f2f2f2

Após isso, o Identity efetua a troca de senha e você é direcionado para o Launchpad.

Caso o usuário esteja vinculado a mais de uma empresa, é importante frisar que a senha pessoal, quando alterada, muda para todas as empresas. Já a senha do Active Directory é alterada somente para a empresa que foi selecionada no momento da troca.

## Criar conta via Auto-inscrição

---

Essa opção só é permitida quando o recurso de  tiver sido habilitado pelo administrador da empresa no Identity.

**01.** Na página de login da empresa no Identity, acionar **Crie sua conta**.

**02.** Informar o nome do usuário.

**03.** Informar o sobrenome do usuário.

**04.** Informar o e-mail corporativo.

#f2f2f2#f2f2f2

O e-mail corporativo deve pertencer a um dos domínios cadastrados pelo administrador da empresa no Identity.

**05.** Acionar **Criar conta**.

#f2f2f2#f2f2f2

Após o preenchimento do cadastro, a ativação da conta deverá ser feita através do convite enviado para o e-mail informado.

## Restaurar configuração de autenticação multifator (MFA)

---

Essa opção deve ser utilizada caso tenha ocorrido troca de aparelho ou exclusão da conta no aplicativo autenticador. Para utilizá-la, é necessário resgatar os códigos de recuperação armazenados no momento da configuração do MFA ou pela tela de . Caso tenha perdido o aparelho e não tenha os códigos de recuperação, a alternativa é entrar em contato com a administração da empresa e solicitar a restauração.

**01.** Na página de login da empresa no Identity, informar o e-mail ou usuário da conta.

**02.** Informar a senha de acesso.

**03.** Acionar **Entrar**.

**04.** Na página de autenticação multifator no Identity, acionar a opção **Perdeu o dispositivo?**.

**05**. Nos campos indicados, preencher os três códigos de restauração de acordo com a ordem solicitada. 

**06**. Acionar **Restaurar**.

#f2f2f2#f2f2f2

Se os códigos informados estiverem corretos, a configuração de MFA do usuário será restaurada. Para configurar novamente, basta acessar a tela de login.

## Recuperação de acesso após bloqueio por excesso de tentativas

---

O bloqueio por excesso de tentativas ocorre somente se a empresa estiver com essa configuração habilitada. Para mais detalhes sobre a configuração, consulte a documentação de .

IMPORTANTE!

Após o bloqueio por excesso de tentativas, o usuário não irá conseguir autenticar-se no Identity, mesmo informando a senha corretamente.

Lembrando que a configuração da política de senha é por empresa, então caso o usuário esteja vinculado a outra empresa sem limite de tentativas ou na qual a quantidade de tentativas seja superior, o acesso não é automaticamente bloqueado na outra empresa.

O usuário que estiver bloqueado por excesso de tentativas pode realizar a recuperação de senha pessoal na tela de login. Quando o reset de senha é concluído, o usuário é automaticamente desbloqueado. Caso não exista e-mail cadastrado para o reset de senha, a solicitação de recuperação de acesso deve ser feita ao administrador corporativo. A alteração da situação é realizada na tela de .

**100%true5%**

]]>
