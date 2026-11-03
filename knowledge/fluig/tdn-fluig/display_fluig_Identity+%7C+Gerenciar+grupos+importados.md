---
content_hash: 2d68e041f4fbb07f02a6352761e6442792bde97a0871da1f77d8f08633a2aed7
fetched_at: '2026-06-28T21:35:25.465999+00:00'
page_id: '285663545'
product: fluig
source: tdn-fluig
title: Identity | Gerenciar grupos importados
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Gerenciar+grupos+importados
version: 26
---

# Falando de gerenciar grupos importados...

---

Essa página permite ao administrador aceitar ou rejeitar a criação dos grupos importados do Active Directory para a empresa no TOTVS Identity.

A importação de grupos permite replicar no Identity a estrutura de grupos existente no Active Directory. Usuários adicionados e removidos dos grupos são sincronizados, através do SmartSync, entre o Identity e o Active Directory.

Usuários atrelados a um grupo no Active Directory e aceitos pelo administrador são automaticamente atrelados ao mesmo grupo no Identity, caso este tenha sido importado.

listagrupospendentes

## Acessar lista de grupos pendentes

---

**01.**Acessar as configurações  e selecionar a opção [Active Directory](https://tdn.totvs.com/x/AptUE).

**02.** Na seção [Gerenciar Active Directories](https://tdn.totvs.com/display/TIdentity/Gerenciar+Active+Directories), acionar o link **Gerenciar Active Directories**.

**03**. Acionar a opção **Visualizar**, localizada na coluna **Grupos pendentes** do Active Directory desejado.

oculto

Acessar lista de grupos importados

---

**01.** Acionar o ícone **Configurações**no canto superior direito e selecionar a opção **Active Directory**.

**02.** Acionar **Visualizar** localizado ao lado direito do nome do Active Directory cadastrado.

#f2f2f2#f2f2f2

Na parte de baixo da tela são apresentadas as abas **Usuários** e **Grupos**, que possibilitam uma visualização da quantidade de usuários e grupos importados por meio da sincronização com o AD em questão. Para mais detalhes sobre os usuários, consulte a documentação .

**03**. Acionar a aba **Grupos** e visualizar os grupos importados.

#f2f2f2#f2f2f2

Na tela é apresentada a quantidade total de grupos de permissão importados no período, e também as quantidades de grupos em cada status: pendentes, processando, aceitos e rejeitados.

#e8f6f0#e8f6f0

![](http://tdn.totvs.com/download/thumbnails/286221066/dica.png)

**DICA!**  
Utilize os recursos da tela para trazer uma visualização mais precisa:

* **Filtrar por um período**: Utilize as opções disponíveis para visualizar os grupos importados em todos os dias, hoje, nos últimos 7 dias, nos últimos 30 dias ou por um período personalizado.  
  No período personalizado, é possível selecionar uma data inicial e final no calendário, ou selecionar a opção **Somente data inicial**, para trazer os dados até a data atual.
* **Filtrar por situação**: As situações apresentadas em destaque na tela são filtros, por meio deles é possível selecionar a situação desejada (grupos pendentes, processando, aceitos e rejeitados)
* **Buscar por grupo**: Utilize a busca para pesquisar pelo nome do grupo.  
  É importante notar que a busca remove a seleção dos filtros acima, trazendo todos os resultados.
