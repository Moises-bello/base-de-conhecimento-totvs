---
content_hash: 249a4b26955c1891a879f374360f28a89b458ea957698bce1e5f942a685aa670
fetched_at: '2026-06-28T21:35:27.344368+00:00'
page_id: '544183258'
product: fluig
source: tdn-fluig
title: Identity | Filtrar acesso por IPs externos
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Filtrar+acesso+por+IPs+externos
version: 12
---

# Falando de filtrar acesso por IPs externos...

---

O filtro de acesso por IPs externos permite bloquear o acesso ao domínio da empresa no Identity a todos os endereços IP externos, exceto aqueles explicitamente liberados pelo administrador.

Caso o usuário já esteja conectado a um aplicativo, a sessão continuará ativa mesmo que o filtro de acesso do Identity tenha sido habilitado e o IP externo utilizado pelo usuário não tenha sido cadastrado pelo administrador.

Importante

Este recurso é voltado apenas à restrição de acessos realizados via IP externo. Endereços IP internos não serão bloqueados por essa configuração.

## Habilitar filtro de acesso por IPs externos

---

**01.**Acione o ícone **Configurações**no canto superior direito e selecione a opção **Segurança**. 

**02**. Acesse o recurso **Filtrar Acesso por IPs externos.**

#f2f2f2#f2f2f2

Por padrão, o recurso de Filtro de Acesso por IPs Externos estará **desabilitado** no contexto. Antes de habilitar o recurso, é necessário cadastrar, no mínimo, um IP externo.

**03.** No campo de texto, informe o endereço ou faixa de IPs permitidos e acione o botão **Adicionar**.

#f2f2f2#f2f2f2

Para adicionar um intervalo de endereços IP, utilize o seguinte padrão: 192.168.4.[0-10]. O formato "192.168.4.[0-10]" indica que todos os endereços IP entre 192.168.4**.0** e 192.168.4**.10** terão acesso liberado à empresa no Identity.

Para adicionar o IP que está sendo utilizado pelo usuário logado, acione o botão **Adicionar atual**.

**04.** Marque a opção **Habilitar Filtro de Acesso por IPs Externos**.

#f2f2f2#f2f2f2

Ao habilitar o filtro, apenas acessos oriundos dos endereços IP cadastrados terão o login permitido. Os demais endereços serão rejeitados e não poderão acessar o contexto.

Atenção

Caso o usuário já esteja conectado a um aplicativo, esta sessão continuará ativa mesmo que o filtro de acesso do Identity tenha sido habilitado e o IP externo utilizado pelo usuário não tenha sido cadastrado.

### Remover IP

---

**01.** Localize o endereço ou faixa de IPs a ser removido.

**02**. Ao lado do campo de texto, acione o botão **Excluir** .

# Perguntas frequentes

---

[Mensagem "Acesso restrito" ao tentar acessar o Identity](https://tdn.totvs.com/pages/viewpage.action?pageId=546690348)

]]>
