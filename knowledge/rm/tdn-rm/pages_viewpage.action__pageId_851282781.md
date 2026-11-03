---
content_hash: b66851f0b5d78f765a8ce54dbec57e114490c115345e8edaea0a5f7a7ac9dec0
fetched_at: '2026-06-29T00:11:53.726555+00:00'
page_id: '851282781'
product: rm
source: tdn-rm
title: Tenantização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=851282781
version: 19
---

# Índice

---

Índice

# Introdução

---

**Tenantização** refere-se ao processo de adaptação ou desenvolvimento de uma aplicação para suportar múltiplos tenants.

Um "tenant" neste contexto é uma entidade (como uma empresa, organização ou cliente) que utiliza a aplicação como se fosse dedicada a ela, embora compartilhe recursos de computação com outros tenants na mesma instância da aplicação.

Um dos aspectos críticos da tenantização é garantir que os dados de cada tenant sejam segregados e seguros, impedindo o acesso não autorizado entre tenants.

# Tenantização no RM

---

A tenantização do RM é realizada através do **Alias de banco de dados** cadastrado no ambiente.

No Contexto client do RM.Exe (**Aplicativo Desktop**) podemos considerar que cada alias é um Tenant. tendo em vista que os alias que estão aparecendo são carregados automaticamente por uma tela nativa do sistema que foi construída para aquele propósito.

Porém quando falamos em **API**´s (Application Programming Interface) a maneira mais comum do RM Tenantizar as requisições é no domínio da URL da Rota dos serviços.

**Exemplos:**

**Rota Tenantizada**

A Api de Usuários é exposta na rota: [http://meudominio:8051/api/framework/v1/users](http://meudominio:8051/api/framework/v1/users/mestre) onde o domínio "meudominio" seria o tenant na requisição.

**Rota Não Tenantizada**

Diferente da rota [http://minhamaquina:8051/api/framework/v1/users](http://minhamaquina:8051/api/framework/v1/users/mestre) onde o domínio "minhamaquina" não representa um tenant e sim o nome da máquina que está provendo o serviço.

Atenção

Quando a rota do serviço não estiver tenantizada, o sistema assumirá que o tenant do serviço chamado é o tenant(connectionId) presente no Token.

# Como Tenantizar os serviços do RM

---

Para que as API´s do sistema sejam **tenantizadas**, é necessário utilizar a tag  **[SubDomainMask](https://tdn.totvs.com/pages/viewpage.action?pageId=126192093#Par%C3%A2metrosdosArquivosdeConfigura%C3%A7%C3%A3o(*.config)-SubdomainMask)** no arquivo de configuração do **Server**(**Host**).

Exemplo:

xml]]>Atenção

É **imprescindível** que a variável **[ALIAS]** esteja presente no valor da tag, pois é este valor que será sobrescrito pelo nome do Alias de banco de dados.

Ao iniciar o **Server(Host)** a tag **[SubDomainMask](https://tdn.totvs.com/pages/viewpage.action?pageId=126192093#Par%C3%A2metrosdosArquivosdeConfigura%C3%A7%C3%A3o(*.config)-SubdomainMask)**será verificada e caso esteja preenchida de forma correta os serviços do sistema serão expostos para cada alias configurado.

**Exemplo:**

Rota da Api de Usuários: ...[/api/framework/v1/users/mestre](http://meudominio:8051/api/framework/v1/users/mestre)

Existem 2 Alias cadastrados no sistema TOTVS e TOTVS\_HOMOLOG

Ao subir o **Host**um serviço para cada alias será exposto respeitando o valor da tag **[SubDomainMask](https://tdn.totvs.com/pages/viewpage.action?pageId=126192093#Par%C3%A2metrosdosArquivosdeConfigura%C3%A7%C3%A3o(*.config)-SubdomainMask).**

[/api/framework/v1/users](http://meudominio:8051/api/framework/v1/users/mestre)

[http://TOTVS\_HOMOLOG.totvscloud.com.br](http://TOTVS.totvscloud.com.br)[/api/framework/v1/users](http://meudominio:8051/api/framework/v1/users/mestre)

ConfiguraçõesMulti Tenant

### Várias Empresas/ Ambientes (Produção/Homologação)

No Caso de ambiente **Multi Tenant** é necessário 1 DNS para cada Alias.

Atenção

Os DNS´s **obrigatoriamente** precisam ter no **domínio** da URL o nome do **Alias do Banco de Dados,** pois é através do domínio que conseguimos identificar o Alias.

**Exemplo:**

Alias : **TOTVS**

DNS : http://**TOTVS**.[totvscloud.com.br](http://totvscloud.com.br)

Single Tenant

### Empresa única / Ambiente (Apenas 1 Alias)

Como é um ambiente **Single Tenant**  é necessário **apenas** 1 DNS.

Atenção

O DNS **não necessariamente** precisa ter no domínio da URL o nome do Alias configurado, porém será necessário que a tag  **[DefaultDB](https://tdn.totvs.com/pages/viewpage.action?pageId=126192093#Par%C3%A2metrosdosArquivosdeConfigura%C3%A7%C3%A3o(*.config)-DefaultDB)** esteja configurada no arquivo de configuração do **Server**(**Host**).

Caso o DNS possua o Alias no Domínio da URL, é necessário realizar a configuração da tag **[SubDomainMask](https://tdn.totvs.com/pages/viewpage.action?pageId=126192093#Par%C3%A2metrosdosArquivosdeConfigura%C3%A7%C3%A3o(*.config)-SubdomainMask)** conforme passos anteriores.

Atenção

Ao utilizar o **Smart Client** em um **ambiente externo** é necessário que exista um **DNS Exposto** na internet **para cada Tenant** , para que a aplicação consiga se comunicar.

"
