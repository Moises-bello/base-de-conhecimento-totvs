---
content_hash: 77b2c0400e0f89d5f4ccd8324aed307d28004f86a428ce2e3ccf33282797d35c
fetched_at: '2026-06-28T21:35:26.144138+00:00'
page_id: '344467549'
product: fluig
source: tdn-fluig
title: Identity | Modos de provisionamento
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Modos+de+provisionamento
version: 37
---

# Falando de modos de provisionamento...

---

Os aplicativos do tipo Padrão oferecem diferentes modos de provisionamento que permitem automatizar a criação e desativação de contas nos serviços integrados ao TOTVS Identity.

[**Fluig**](https://tdn.totvs.com/x/nocKDg): Este modo de provisionamento foi criado especificamente para a integração do TOTVS Identity com a plataforma Fluig. Quando configurado, ao invés da criação do usuário no Fluig ser realizada no primeiro acesso, ela é feita no momento em que o [aplicativo é atribuído à conta do usuário](http://tdn.totvs.com/pages/viewpage.action?pageId=331856582#Configura%C3%A7%C3%B5esdeAplicativosPadr%C3%A3o-Atribuiroaplicativoaosusu%C3%A1rios) no Identity. Isso garante maior autonomia ao administrador, que não precisa aguardar o usuário realizar o acesso para que o cadastro no Fluig seja realizado.

Outra vantagem é que o modo provisionamento Fluig garante que ao remover o usuário do aplicativo no Identity, a conta deste usuário também será desativada no Fluig.

**[SCIM](http://www.simplecloud.info/)**: O *System for Cross-domain Identity Management* (Sistema de Gerenciamento de Identidade de Domínio Cruzado) é um padrão aberto para automatizar a troca de informações de identidade do usuário entre domínios de identidade e aplicações.

Para que o provisionamento SCIM configurado em um aplicativo do Identity funcione corretamente, é necessário que a aplicação a qual ele está direcionando também suporte esse padrão. Os ERPs Logix e [Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=185736879) são exemplos de aplicações que suportam o modo de provisionamento SCIM.

Importante

Usuários com status **Convidado** ou **Desativado** não serão provisionados, apenas usuários com status Ativo. Para usuários convidados, o provisionamento ocorrerá no momento em que a conta for ativada.

oculto

**OBS**: Liberar essa informação quando o projeto SMARTLINK for concluído.

**[SMARTLINK:](https://tdn.totvs.com/x/eFvUK)** Já neste modo de provisionamento, a integração permite o recebimento e envio de mensagens de criação, bloqueio ou até mesmo a edição de usuários para os ERPs TOTVS, incluindo um novo tipo de aplicativo ou um novo modo de integração nos aplicativos existentes para integração. Os ERPs  [Datasul](https://tdn.totvs.com/display/framework/Configurando+o+Datasul) ou [Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=185736879) são exemplos de aplicações que suportam o modo de provisionamento do SMARTLINK.

## Habilitar provisionamento Fluig

---

Não existe a possibilidade de acessar a opção "Habilitar Provisionamento" no aplicativo padrão do Fluig, portanto, é necessário realizar um clone do aplicativo padrão. 

**01.** Acionar o menu [Aplicativos](https://tdn.totvs.com/x/2RK4Ew).

**02**. Acionar o nome do aplicativo para visualizar as configurações.

**03.** Acessar a aba **Provisionar** nas configurações do aplicativo.

**04.** Acionar **Editar**.

**05.** Assinalar a opção **Habilitar Provisionamento**.

**06.** Em **Modo de Provisionamento**, marcar a opção **Fluig**.

**07.** Em **Tipo de Autenticação**, marcar a opção **OAuth 1.0a**.

**08.** No campo **URL REST**, informar a URL da API de criação de usuários do Fluig, substituindo {dominio} pelo endereço de acesso ao Fluig:

**09.** Em **Nome do usuário do Administrador do Domínio**, informar o e-mail de um usuário que seja administrador tanto do Fluig quanto do Identity. Este usuário deve existir em ambas as ferramentas.

**10.** Informar a senha desse mesmo administrador no campo **Senha do Administrador do Domínio**.

**11.** Definir uma senha padrão temporária para os usuários que serão criados através do provisionamento em **Senha Temporária do Usuário**.

**12.** Acionar **Salvar**.

## Habilitar provisionamento SCIM

---

**Veja a imagem**

**01.** Acionar o menu [Aplicativos](https://tdn.totvs.com/x/2RK4Ew).

**02**. Acionar o nome do aplicativo para visualizar as configurações.

**03.**Acessar a aba **Provisionar** nas configurações do aplicativo.

**04.** Acionar **Editar**.

**05.** Assinalar a opção **Habilitar Provisionamento**.

**06.** Em **Modo de Provisionamento**, marcar a opção **SCIM**.

**07.** Definir se o **Modo Pull** deve ser ativado.

**08.** Definir o **Tipo de Autenticação**.

**09.** Informar a **URL REST**.

**10.** Informar o **Nome do usuário Administrador do Domínio**.

**11.** Informar a **Senha do Administrador do Domínio**.

**12.** Definir uma senha padrão temporária para os usuários que serão criados através do provisionamento em **Senha Temporária do Usuário.**

#f2f2f2#f2f2f2

Essa senha será atribuída aos novos usuários da aplicação provisionados via modo SCIM.

**13.** Acionar **Salvar**.

oculto

**OBS**: Liberar essa informação quando o projeto SMARTLINK for concluído.

Habilitar provisionamento SMARTLINK

---

**[Veja a imagem](https://tdn.totvs.com/download/attachments/344467549/image-2022-04-07-17-20-37-007.png?version=1&modificationDate=1652293038410&api=v2)**

**01.** Acionar o menu [Aplicativos](https://tdn.totvs.com/x/2RK4Ew).

**02**. Acionar o nome do aplicativo para visualizar as configurações.

**03.** Acessar a aba **Provisionar** nas configurações do aplicativo.

**04.** Clonar o aplicativo.

**05.** Acionar **Editar**.

**06.** Assinalar a opção **Habilitar Provisionamento**.

**07.** Em **Modo de Provisionamento**, marcar a opção **SMARTLINK.**

**08.** Definir uma senha padrão temporária para os usuários que serão criados através do provisionamento em **Senha Temporária do Usuário**.

**09.** Acionar **Salvar**.

**10.** Abrir a edição da empresa pelo SysAdmin.

**11.** Verificar que a integração com o SMARTLINK está ativa.

]]>
$("b:contains('oculto')").parent().parent().hide();
]]>
