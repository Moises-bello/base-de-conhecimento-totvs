---
content_hash: 560ea7d823059fc3ca3b8d09c6fc9f671f30c1a1b1a389ca3b8235424f7d3852
fetched_at: '2026-06-29T00:11:32.948310+00:00'
page_id: '751511801'
product: rm
source: tdn-rm
title: Categorias de Recurso no RM
type: documentation
url: https://tdn.totvs.com/display/LRM/Categorias+de+Recurso+no+RM
version: 15
---

# Introdução

---

         ***Categorias** são agrupadores de Recursos Smart View no RM* e funcionam principalmente como controladores de permissão do recurso, e dessa forma, é possível determinar o nível de acesso de diferentes perfis para o recurso que estiver atrelado àquela categoria.

INLINEPermissionamento no Smart View

Não é recomendado fazer a distribuição de permissões de recursos diretamente no Smart View pois não há garantias que o RM respeitará as permissões que foram adicionadas externamente ao ERP

Provedor de Segurança com Descoberta Manual

Caso o Smart View esteja configurado para utilizar o Provedor de Segurança como **Descoberta Manual**, o compartilhamento de recursos pode falhar. Para correto uso do sistema de permissão do Smart View integrado ao RM, deve ser utilizada a **Descoberta Automática** conforme instruído na documentação: 

false

# Criando uma Categoria

---

1 - O acesso às Categorias é feito através da aba **Gestão → Ferramentas de Análise → Smart View**:

2 - Na visão, temos as categorias criadas:

3 - Para criar uma nova categoria, basta clicar no ícone de incluir a esquerda e adicionar o nome da categoria.

Não é obrigatório a inclusão de um perfil para criar uma nova categoria

4 - Na aba "*Perfis da Categoria do Recurso do Smart View*" é possível atrelar mais de um perfil à categoria.

Na inclusão do perfil é necessário adicionar o **Nível de Acesso do Perfil**:

* **Leitor:**O usuário terá permissões apenas de visualizar o recurso.
* **Editor:**O usuário poderá visualizar e editar o recurso.

false

# Adicionando Categoria ao Recurso

---

1 - Acessar o menu do **Smart View** em **Gestão → Ferramentas de Análise**:

2 - No recurso selecionado, será apresentado o seletor de categoria, assim basta selecionar a categoria criada.

3 - Após selecionar a categoria e clicar em salvar, será feita a atualização das permissões da categoria com o Smart View:

A partir da versão 12.1.2406

1 - Acessar o menu do **Smart View** em **Gestão → Ferramentas de Análise**:

2 - No recurso selecionado, clicar em Editar, Na tela de edição do recurso será apresentado o seletor de categoria, assim basta selecionar a categoria criada. 

3 - Após selecionar a categoria e clicar em **selecionar**, será feita a atualização das permissões da categoria com o Smart View:

false

# Visualização de compartilhamento no Smart View

---

* Acessando o TReports, entre no recurso onde foi inserido a categoria:

* Clicando no ícone de compartilhamento é possível visualizar a permissão ao perfil inserido anteriormente na categoria associada ao recurso:

Índicefalsefalse

**Produto:** Framework

false

**Versão:** 12.1.2306

false

**Processo:** Integração com o
