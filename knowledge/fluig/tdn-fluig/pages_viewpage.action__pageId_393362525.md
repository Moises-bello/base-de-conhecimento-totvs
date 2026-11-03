---
content_hash: 49ac2978bf2a81b7ff1d298884320d618867ae76c1101921eb5555d2ca676953
fetched_at: '2026-06-28T21:35:26.685276+00:00'
page_id: '393362525'
product: fluig
source: tdn-fluig
title: IDE - Por que as imagens do Kit Intranet não são exibidas quando ativo a integração
  com o Identity?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=393362525
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma integrado ao TOTVS Identity

# Ocorrência

Tenho o Kit Intranet publicado em minhas páginas e quando ativo a integração com o Identity as imagens do widget Slideshow e artigos não são exibidas. Porém, se desabilito a integração com o Identity, funciona perfeitamente. Por que isso ocorre?

# Causa

Isso ocorre porque nas configurações da plataforma (wcmadmin), a URL do Portal foi preenchida com o endereço IP do servidor de instalação (por exemplo: http://192.168.15.54:8080), porém nas configurações do aplicativo Fluig no Identity foi informado o endereço de domínio do servidor (http://fluig.suaempresa.com.br).

# Solução

A URL do Portal preenchida no wcmadmin e o Domínio preenchido no aplicativo Fluig do Identity devem apontar para o mesmo endereço.

**Para verificar a URL do Portal no wcmadmin**

**01.** Acessar a plataforma com o usuário wcmadmin.

**02.** Acessar o **Painel de Controle** → **WCM** → **Configuração do sistema**.

**03.** Na aba Portal, verifique o endereço informado no campo **URL do Portal**.

**Para verificar o Domínio no aplicativo Fluig**

**01.** Acesse o Identity com um usuário administrador.

**02.** Clique sobre o Menu **Aplicativos**.

**03.** Busque pelo aplicativo Fluig que foi configurado.

**04.** Clique sobre o nome do app para abrir as configurações.

**05.** Acesse a aba **Editar** e verifique o endereço informado no campo **Domínio**.

Lembrando que é necessário informar /portal/idp ao final dessa URL, por exemplo, "<http://192.168.15.54:8080/portal/idp>" para que o acesso seja realizado corretamente.
