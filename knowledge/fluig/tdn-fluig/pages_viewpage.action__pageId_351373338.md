---
content_hash: 7c869b4722cca88c904921f8e88453a602f1b4bcbc06ed6d8702f8ca9dd55abf
fetched_at: '2026-06-28T21:35:26.233140+00:00'
page_id: '351373338'
product: fluig
source: tdn-fluig
title: Identity | Atualização do certificado SAML nas aplicações SSO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=351373338
version: 97
---

# Falando de atualização do certificado SAML nas aplicações SSO...

---

O certificado no padrão X.509 é usado para configurar o *Single Sign On* (SSO) em aplicações que suportam o padrão [SAML](http://tdn.totvs.com/display/fluig/Como+criar+um+novo+aplicativo+do+tipo+SAML). Por exemplo: ao , o certificado SAML é enviado para a plataforma, o que visa garantir a confiabilidade das operações. Por motivos de segurança, uma data de expiração é atribuída ao certificado.

A duração atual do certificado é de 5 anos a partir da data de criação do contexto. Ao final desse período, é necessário renová-lo e atualizá-lo nas aplicações SSO.

Não é necessário renovar o certificado SAML imediatamente após o aparecimento da mensagem de aviso de expiração, mas é fundamental que ele seja renovado antes da data de expiração.

oculto

**Observação interna:**

O conteúdo dessa página foi replicado ao artigo [https://centraldeatendimento.fluig.com/hc/pt-br/articles/360033487714](https://centraldeatendimento.fluig.com/hc/pt-br/articles/360033487714/)

Se for realizado algum ajuste, lembrar de repassar a esse artigo!

atualizar

## Como fazer a renovação

A renovação do certificado SAML ocorre em duas etapas:

* A primeira etapa é renovar o certificado por um novo período no próprio contexto do Identity. Acesse nossa documentação e observe o passo a passo da renovação do e do [Certificado SAML RSA 2048](https://tdn.totvs.com/x/BwefKQ).
* Após renovar o certificado SAML do contexto, deve-se dar início à segunda etapa: a atualização do certificado nas aplicações SSO integradas ao Identity, como o ,  e os .

### Atualizar o certificado no TOTVS Fluig Plataforma fluig

---

Para atualizar o certificado SAML na plataforma, basta editar a empresa que está , testar a conexão e salvar sem alterar nada. O certificado atualizado será baixado automaticamente.

**01.** [Acessar sua plataforma com o usuário **wcmadmin**](http://tdn.totvs.com/pages/viewpage.action?pageId=203767554).

**02.** Acionar **Painel de Controle** → aba **WCM → Empresas**.

**03.** Selecionar a empresa integrada ao Identity e acionar **Editar**.

**04.** Acessar a aba **Autenticação**.

**05.** Abrir o combo **Ações** e acionar **Testar conexão**.

#f2f2f2#f2f2f2

Deve ser apresentada a mensagem "Conexão com o servidor do Identity realizada com sucesso", o que indica que a integração entre a plataforma e o Identity está funcionando corretamente.

**06.** Acionar **Salvar**.

Para confirmar a atualização do certificado, acesse o [Volume](http://tdn.totvs.com/pages/viewpage.action?pageId=233766796) da instalação da plataforma. Dentro desse diretório, na pasta *certs*, é armazenado o certificado SAML. Abra-o para verificar a nova data de validade. 

### Atualizar o certificado na GoodData gooddata

---

A renovação do certificado na  deve ser solicitada através de um *ticket* para a Equipe de Suporte do Identity.

**01.** Acessar o [**Portal do cliente**](https://suporte.totvs.com/).

**02.** Acionar **Central de chamados**.

**03.** Abrir um novo *ticket* solicitando a atualização do certificado na GoodData e informando a URL do contexto da empresa no Identity (Ex.: <http://minhaempresa.fluigidentity.com>).

#f2f2f2#f2f2f2

O analista responsável pelo *ticket* entrará em contato com o suporte da GoodData requisitando a atualização do certificado no projeto GoodData.

### Atualizar o certificado nos ERPs TOTVS totvs

---

Para aplicar o novo certificado SAML nos ERPs Protheus, Logix, Datasul ou RM, basta refazer a integração *One Click* nas configurações da aplicação. Cada ERP possui uma documentação específica detalhando o procedimento de integração:

* [Linha Protheus](http://tdn.totvs.com/pages/viewpage.action?pageId=73892524)



* [Linha Datasul](http://tdn.totvs.com/display/public/FRAMJOI/Identity+-+Linha+Datasul)

* [Linha Logix](http://tdn.totvs.com/display/public/FRAMJOI/Identity+-+Linha+Logix)

### Atualizar o certificado no Zendesk zendesk

---

Para atualizar a , basta informar a Impressão Digital do novo certificado SAML nas configurações de segurança da aplicação.

falsezendesk\_tutorialPasso 1

* Fazer o [*download* do certificado](http://tdn.totvs.com/pages/viewpage.action?pageId=273980166#Seguran%C3%A7a-ObterocertificadoSAML) SAML renovado.
* Abrir o certificado SAML baixado ().

* Acessar a aba **Detalhes**.

* Localizar **Impressão Digital** na lista de campos apresentada.

* Copiar o valor da impressão digital do certificado.

Passo 2

* Acessar o Zendesk da empresa com o administrador.

#f2f2f2#f2f2f2

A página de login do Zendesk pode ser acessada diretamente através da URL https://{domain}.zendesk.com/access/normal.

* Selecionar **Admin** (ícone de engrenagem) na barra lateral esquerda.

* Acessar **Segurança**, sob a seção **Configurações**.

* Localizar as configurações de **SAML** na seção ***Single Sign-on* (SSO)**.

* Colar o valor da Impressão Digital copiado do certificado SAML no campo **Impressão digital do certificado\*** ().

* Acionar **Salvar**.

### Atualizar o certificado em outros apps

---

Para substituir o certificado SAML em outros aplicativos de terceiros configurados pela empresa no Identity, deve-se entrar em contato com o fornecedor da aplicação e solicitar a atualização do certificado.

]]>
