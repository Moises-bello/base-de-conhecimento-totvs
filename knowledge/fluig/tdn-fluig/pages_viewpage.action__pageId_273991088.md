---
content_hash: c183d9a69744b7933ba7a6724dae126c5ad79fe3144923a45784eca56e1caca0
fetched_at: '2026-06-28T21:35:25.076017+00:00'
page_id: '273991088'
product: fluig
source: tdn-fluig
title: Identity | Ativação de nova conta e entrar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273991088
version: 23
---

# Falando de ativação de nova conta e entrar...

---

As configurações desta página são específicas para os usuários criados no contexto do TOTVS Identity através da importação via Active Directory. É possível definir se as credenciais do AD podem ser utilizadas para acessar o domínio da empresa no Identity, se devem ser disponibilizadas para os aplicativos Plugin e se as mudanças de status da conta no Active Directory e na empresa dentro do Identity devem ser sincronizadas.

Usuários importados e aceitos pelo administrador são automaticamente ativados, dispensando a utilização de e-mails de convite ou senhas temporárias.

## Configurar ativação/autenticação de contas importadas do AD

---

**01.**Acionar o ícone **Configurações**no canto superior direito.

**02.** Selecionar a opção **[Active Directory](https://tdn.totvs.com/x/AptUE).**

**03**. Na seção **Ativação de nova conta e entrar**, efetuar as configurações necessárias.

#f2f2f2#f2f2f2

As configurações disponíveis são:

**Permitir credenciais do Active Directory**Definir se será permitido aos usuários acessar a empresa no TOTVS Identity utilizando as credenciais do Active Directory (e-mail e senha de rede).

**Salvar as credenciais do Active Directory no Identity**  
Ao assinalar esta opção, os aplicativos do tipo Plugin podem ser configurados para fazer o acesso utilizando a credenciais do Active Directory.

**Salvar o cache de senhas do Active Directory**  
Quando habilitado, será salvo um hash das senhas dos usuários no TOTVS Identity, não permitindo que sejam decifradas e proporcionando um login muito mais rápido.

**Permitir login somente com senha do Active Directory para usuários importados do AD**  
Possibilita escolher se deve ser bloqueada a autenticação com senha pessoal para usuários importados do Active Directory.

**Sincronizar mudanças no estado do usuário do Active Directory para o Identity**  
Ao assinalar esta opção, usuários desativados no Active Directory também serão desativados automaticamente da empresa no Identity. A sincronização do estado é realizada via SmartSync.

**Sincronizar mudanças no estado do usuário do Identity para o Active Directory**Ao assinalar essa opção, as mudanças no estado do usuário no Identity devem ser sincronizadas para o Active Directory, com isso, os usuários desativados no Identity também serão desativados automaticamente no Active Directory.

#fdf7e8#fdf7e8

![](http://tdn.totvs.com/download/thumbnails/286221066/importante.png)

**IMPORTANTE!**
  
Caso existam ADs sem configuração no contexto, as opções **Sincronizar mudanças no estado do usuário do Active Directory para o Identity** e **Sincronizar mudanças no estado do usuário do Identity para o Active Directory** ficam desabilitadas e não podem ser marcadas.
