---
content_hash: f6a4e709eebb91d93f76c2eda5397509c3aec47e1644b2d4aa670466c483488a
fetched_at: '2026-06-28T21:35:26.345974+00:00'
page_id: '356813473'
product: fluig
source: tdn-fluig
title: Identity | Integração com o Zendesk
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=356813473
version: 23
---

# Falando de integração com o Zendesk...

---

Para utilizar o Zendesk integrado ao Identity, é preciso clonar o aplicativo Zendesk que vem por padrão, e realizar a configuração de segurança, conforme detalhado nessa documentação.

## Pré-requisitos

---

Para realizar a integração do Identity com o Zendesk, são necessários os seguintes itens:

* Ambiente próprio do cliente cadastrado no Zendesk com permissões de administração.

#f2f2f2#f2f2f2

Nesta documentação usaremos como exemplo um ambiente Zendesk chamado <https://qaidentity.zendesk.com>.

* Usuários cadastrados no Zendesk e no Identity com o mesmo e-mail.

Aviso

A integração entre o Zendesk e o Identity suporta apenas o acesso *Single Sign-on* (SSO) e não o provisionamento automático de usuários. O administrador deve cadastrar os usuários no Zendesk antes de  a eles no Identity.

## Clonar o aplicativo Zendesk

---

O primeiro passo para a integração é clonar o aplicativo padrão Zendesk disponibilizado pelo Identity:

**01.** Acessar o contexto da empresa no Identity como administrador.

**02.** Acionar o menu **Aplicativos**.

**03.** Em **Pesquisar**, buscar por "Zendesk".

**04.** Clicar sobre o aplicativo **Zendesk** para abrir a página de configurações.

**05.** Acionar a opção **Clonar** no canto direito da página.

**06.** Confirmar a operação acionando **Clonar**.

#f2f2f2#f2f2f2

Será gerado um novo aplicativo com base no Zendesk. O administrador pode alterar o nome do app clonado e atribuí-lo aos usuários que possuem cadastro no Zendesk para acesso SSO.

## Configurar o aplicativo Zendesk clonado clone

---

**01.** No novo aplicativo clonado do Zendesk, acessar a aba **Entrar**.

**02.** Acionar **Editar** no canto superior direito da página.

**03.** Marcar o **Tipo Init SSO** como "IDP\_INITIATED".

**04.** Em **URL do Consumidor de Asserções**, substituir {domain} pelo domínio da empresa no Zendesk.

#f2f2f2#f2f2f2

Por exemplo: <https://qaidentity.zendesk.com/access/saml>.

**05.** Em **Destinatário**, substituir {domain} pelo domínio no Zendesk.

#f2f2f2#f2f2f2

Por exemplo: <https://qaidentity.zendesk.com/access/saml>.

**06.** Em **Público**, informar a mesma URL definida nos campos Destinatário e URL do Consumidor de Asserções.

**07.** Em **Nome do Emissor SP**, informar a mesma URL definida nos campos Destinatário e URL do Consumidor de Asserções.

**08.** Acionar **Salvar**.

## Configurar segurança no Zendesk

---

A integração com o Zendesk exige o preenchimento de três informações nas configurações de segurança do ambiente: URL SAML SSO, Impressão digital do certificado e URL de saída remota.

falsesegurança\_zendeskPasso 1

* Acessar o contexto da empresa no Identity e fazer *download* do certificado SAML ().

* Abrir o certificado SAML baixado.

* Acessar a aba **Detalhes**.

* Localizar **Impressão Digital** na lista de campos apresentada.

* Copiar o valor exibido nesse campo ().

Passo 2

* Acessar o Zendesk da empresa com o administrador.

* Selecionar **Admin** (ícone de engrenagem) na barra lateral esquerda.

* Acessar **Segurança**, sob a seção **Configurações**.

* Na aba Administradores e agentes, habilitar o modo de autenticação ***Single Sign-on* (SSO)**.

* Habilitar a opção **SAML** para exibir o formulário de configuração.

* .

Passo 3

* Preencher o campo **URL SAML SSO** com o valor do parâmetro **URL da página de login** do  do Zendesk no Identity ().

* Preencher o campo **Impressão digital do certificado** com o valor obtido no Passo 1.

* Preencher o campo URL de saída remota com a URL do contexto da empresa no Identity, por exemplo, [https://suaempresa.fluigidentity.com/cloudpass/](https://joitrei04.customerfi.com/cloudpass/).

* Acionar **Salvar** no final da página.

 ]]>
