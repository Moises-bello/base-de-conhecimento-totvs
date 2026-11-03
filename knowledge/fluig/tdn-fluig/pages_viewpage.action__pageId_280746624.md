---
content_hash: accd5faa4d7c79af73a7a56078009314545b09f16935b727425c56611419bddf
fetched_at: '2026-06-28T21:35:25.324239+00:00'
page_id: '280746624'
product: fluig
source: tdn-fluig
title: Identity | Configurações do usuário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=280746624
version: 64
---

# Falando de configurações do usuário...

---

Essa página oferece aos usuários os campos para cadastrar e alterar informações pessoais, mudar a senha pessoal, mudar o e-mail corporativo, obter os plugins dos navegadores e o Desktop Launcher, além da configuração de autenticação multifator.

## Acessar as configurações do usuário

---

**01.** No canto superior direito da tela, acione o ícone  que representa o perfil do usuário.

**02.** Acione **Meu perfil** ou **Gerenciar conta**.

#f2f2f2#f2f2f2

Na parte esquerda da tela, serão apresentadas as seguintes opções de configuração: Informações pessoais, Autenticação multifator e Plugins.

## Informações pessoais

---

### Alterar nome de usuário

---

**01.** No menu de configurações do usuário, acesse a opção **Informações pessoais**.

**02.** Localize o campo **Nome do usuário** e acione **Editar** .

**03**. Na janela aberta, informe o novo nome e acione **Alterar nome**.

### Alterar senha pessoal

---

Essa opção só é permitida caso o uso de senha pessoal esteja habilitado nas [configurações de segurança](https://tdn.totvs.com/x/sZJvI) da empresa.

**01.** Nas configurações do usuário, acesse a opção **Informações pessoais**.

**02.** Localize o campo **Senha Pessoal** e acione **Editar senha** .

**03.** Informe a senha atual e a nova senha, de acordo com os requisitos apresentados à direita.

#f2f2f2#f2f2f2

Para mais detalhes sobre os requisitos, consulte a documentação de .

Importante!

A complexidade de senha é definida por empresa, mas a senha pessoal é única para cada usuário. Quando o usuário for resetar sua senha, precisa definir uma senha que atenda aos critérios de todas as empresas onde está cadastrado.

**04.** Acione **Editar senha** para confirmar a alteração.

### Alterar e-mail corporativo

---

Essa opção é disponibilizada apenas quando a troca de e-mail for habilitada pelo administrador nas [configurações de segurança](https://tdn.totvs.com/x/sZJvI).**01.**Nas configurações do usuário, acesse a opção **Informações pessoais**.

**02**. Localize o campo **E-mail corporativo** e acione **Editar** .

**03.** Informe o novo e-mail corretamente nos dois campos.

**04**. Acione **Alterar e-mail** para salvar a informação.

#f2f2f2#f2f2f2

Uma mensagem de confirmação é apresentada assim que o e-mail for alterado em tela. O link de confirmação será enviado para o novo endereço de e-mail cadastrado, e tem validade de 24 horas. Após a confirmação pelo usuário, a alteração do e-mail é concluída.

Enquanto a mudança não for confirmada, ao lado do novo e-mail aparece o ícone  (que indica a pendência de confirmação) e o ícone  que pode ser acionado para desfazer a alteração de e-mail.

Caso a mudança não seja confirmada no link em até 24 horas, a alteração do e-mail é cancelada.

### Alterar a senha do Active Directory

---

Essa opção só é permitida caso a troca de senha do Active Directory tenha sido habilitada na [Política de Senha](http://tdn.totvs.com/pages/viewpage.action?pageId=273992622) do contexto.

**01.** Nas configurações do usuário, acesse a opção **Informações pessoais**.

**02**. Na seção Minhas empresas, localize a empresa e acione a opção **Alterar senha do Active Directory**.

#f2f2f2#f2f2f2

Essa opção é apresentada ao lado do nome das empresas em que o recurso de alteração de senha do Active Directory esteja habilitado.

**03.** Informe a senha atual e a nova senha, de acordo com os requisitos apresentados à direita.

#f2f2f2#f2f2f2

Para mais detalhes sobre os requisitos, consulte a documentação de .

**04.** Acione **Editar senha** para confirmar a alteração.

### Consultar empresas

---

**01.** Nas configurações do usuário, acesse a opção **Informações pessoais**.

#f2f2f2#f2f2f2

Na seção Minhas empresas são listadas as empresas do Identity em que o usuário está cadastrado através do seu e-mail.

### Definir empresa principal

---

Essa opção está disponível somente para usuários que estejam vinculados em várias empresas.

**01.** Nas configurações do usuário, acesse a opção **Informações pessoais**.

#f2f2f2#f2f2f2

Na seção Minhas empresas são listadas as empresas do Identity em que o usuário está cadastrado através do seu e-mail.

**02.** Localize a empresa que deseja definir como principal para acesso.

**03.** Acione o ícone e então **Selecionar como empresa principal**.

#f2f2f2#f2f2f2

Para facilitar a identificação, a empresa definida como principal recebe o ícone .

Após definir a empresa principal, ao autenticar-se pelo endereço genérico ([app.fluigidentity.com](https://app.fluigidentity.com)) o acesso é direto para a empresa definida, eliminando a necessidade de escolher em qual empresa deseja entrar.

### Retirar seleção de empresa principal

---

Essa opção está disponível somente para usuários que estejam vinculados em várias empresas e que tenham uma empresa principal definida.

**01.** Nas configurações do usuário, acesse a opção **Informações pessoais**.

#f2f2f2#f2f2f2

Na seção Minhas empresas são listadas as empresas do Identity em que o usuário está cadastrado através do seu e-mail.

**02.** Localize a empresa principal (está identificada com o ícone ).

**03.** Acione o ícone e então **Retirar seleção de empresa principal**.

#f2f2f2#f2f2f2

Após remover a empresa principal, ao autenticar-se pelo endereço genérico ([app.fluigidentity.com](https://app.fluigidentity.com)), a cada login será necessário escolher em qual empresa deseja entrar.

## Autenticação multifator

---

A autenticação multifator (do inglês *Multi-factor authentication* ou MFA) oferece uma camada adicional de segurança no acesso ao Identity, através da exigência de um código gerado no seu celular pelo aplicativo . Ao habilitar o recurso de MFA em sua conta, também recomenda-se copiar e guardar os códigos de recuperação, que serão solicitados em caso de troca de aparelho.

Para mais informações sobre a configuração deste recurso na empresa, acesse .

### Configurar autenticação multifator

---

**01.** Nas configurações do usuário, acesse a opção **Autenticação multifator**.

**02.** Baixe o aplicativo My Safe id pela [App Store](https://itunes.apple.com/br/app/safe-id/id1304505629?mt=8) ou [Play Store](https://play.google.com/store/apps/details?id=com.fluig.mfa) no seu dispositivo móvel.

#f2f2f2#f2f2f2

Recomendamos o uso do aplicativo My Safe id, mas existem outros aplicativos autenticadores no mercado e eles são compatíveis, pode-se optar pelo autenticador de sua preferência.

**03.** Abra o aplicativo **My Safe id**.

**04.** Pressione  no aplicativo.

#f2f2f2#f2f2f2

Com isso, será aberta a câmera do dispositivo.

**05.** Aponte a câmera do aparelho para o código (QR CODE) exibido pelo Identity.

#f2f2f2#f2f2f2

Caso prefira, você pode configurar a autenticação multifator manualmente, acionando a opção **Adicionar manualmente** e informando os dados necessários:

* Título: Nome da empresa
* Conta: e-mail do usuário (o mesmo e-mail utilizado para autenticar-se no Identity).
* Chave: Chave exibida pelo Identity.

No entanto, recomendamos o uso do QR CODE, pois essas informações já são trazidas automaticamente.

No momento em que a câmera reconhecer o código, a conta será cadastrada no My Safe id e um código de 6 dígitos será gerado e exibido na tela do dispositivo. Este código é renovado automaticamente a cada 30 segundos.

**06.** Preencha o código gerado pelo My Safe id na página de configuração da autenticação multifator do Identity no campo indicado.

#f2f2f2#f2f2f2

O código informado será verificado e, caso esteja correto, uma mensagem de sucesso será apresentada pelo Identity. A partir de agora, sempre será solicitado o código gerado pelo My Safe id, após informar as credenciais de acesso, para autenticação na empresa no Identity.

É importante guardar os , para redefinir a configuração da autenticação multifator em caso de troca de aparelho ou exclusão dos dados no My Safe id.

Importante!

Para que o MFA funcione corretamente, é necessário que o dispositivo a partir do qual está sendo realizado o login e o dispositivo gerador do token estejam exatamente no mesmo horário. A variação de horário, mesmo que seja pouco tempo (1 minuto) já causa erro de token.

### Obter códigos de recuperação

---

Os códigos de recuperação serão solicitados na tela de login para redefinir a configuração de MFA, em caso de troca de aparelho ou exclusão dos dados no aplicativo autenticador.

**01.** Nas configurações do usuário, acesse a opção **Autenticação multifator**.

**02**. No item **Códigos de recuperação**, acione a opção de sua preferência.

#f2f2f2#f2f2f2

As opções disponíveis são:

 **Baixar códigos**: um arquivo .txt será baixado e deve ser armazenado em um lugar seguro.

 **Copiar códigos**: os códigos serão copiados para a área de transferência, e podem ser colados e enviados para seu e-mail, por exemplo.

Caso queira, também é possível acionar a opção **Visualizar**, para conferir os códigos e suas respectivas ordens em tela. 

As instruções para utilizar os códigos de recuperação para restaurar a configuração de MFA podem ser consultadas na documentação de .

### Desativar autenticação multifator

---

**01.** Nas configurações do usuário, acesse a opção **Autenticação multifator**.

**02**. No item **Autenticação multifator ativa**, acione o botão **Desativar**.

**03**. Preencha a senha para confirmar a ação.

**04**. Acione **Desativar**.

#f2f2f2#f2f2f2

Com essa opção desativada, não será mais exigido o código de autenticação multifator na tela de login do Identity.

Caso o usuário faça parte de um grupo com MFA obrigatório, será obrigatório configurar novamente o MFA para autenticar-se na empresa.

## Plugins

---

### 

### Obter o plugin do navegador

---

O plugin do Identity é necessário para que o serviço possa preencher automaticamente as credenciais em aplicativos do tipo Plugin. Para mais detalhes, consulte a documentação .

**01.**Nas configurações do usuário, acesse a opção **Plugins**.

**02.** Localize a opção **Plugin do Navegador.**

**03.** Passe o mouse pelo ícone do plugin e acione **Iniciar download**.

#f2f2f2#f2f2f2

Com isso, o usuário será direcionado para o repositório de *plugins* do navegador.

### Obter o Desktop Launcher

---

O Desktop Launcher é necessário para que o serviço possa preencher automaticamente as credenciais em aplicativos do tipo Thick. Para mais detalhes, consulte a documentação .

**01.**Nas configurações do usuário, acesse a opção **Plugins**.

**02**. Localize a opção **Desktop Launcher**.

**03.** Passe o mouse pelo ícone do plugin e acione **Iniciar download**.

#f2f2f2#f2f2f2

Com isso, será aberta uma nova guia para o download do arquivo .msi.

### Obter o aplicativo My Safe id

---

**01.**Nas configurações do usuário, acesse a opção **Plugins**.

**02.**Localize a opção desejada: My Safe ID para Android ou iOS.

#f2f2f2#f2f2f2

O usuário será direcionado para a página da loja correspondente ao sistema operacional selecionado. Para mais detalhes, consulte a  e também o item **Autenticação multifator**desta documentação.

]]>
