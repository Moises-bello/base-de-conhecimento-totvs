---
content_hash: 683d96ae9a65a45c4189692a677a557361133c261bb7964239babc8c0aa9a13a
fetched_at: '2026-06-29T00:08:45.556609+00:00'
page_id: '311632287'
product: rm
source: tdn-rm
title: Grupo de Relatório
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=311632287
version: 34
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é trazer uma visão de como funciona tela de Cadastro de Grupo de Relatório.

# Introdução:

---

       Os Grupos de Relatórios basicamente são agrupadores para organizar os relatórios.

       Por exemplo, uma empresa tem a intenção de criar relatórios que contenham informações sobre a Folha de Pagamento e sobre o Fluxo de Caixa. Neste caso, seriam criados dois grupos de relatórios, um para os relatórios da Folha de Pagamento e outro para o Fluxo de Caixa, e os relatório criados posteriormente serão agrupados em seu respectivo grupo.

       Caso a empresa não deseje ter essa distinção, bastar criar um grupo de relatório "Geral" e agrupar todos os relatórios dentro dele.

# Como criar:

---

       Para criar um novo Grupo de Relatório, basta clicar em "+ Novo" e informar os campos abaixo:

***Código:*** Informe o código do Grupo de Relatório, deve ser um código único e será por ele que o Grupo de Relatório será identificado.

***Descrição:*** Informe uma descrição.

***Linha de Produto:*** Informe a Linha de Produto a qual esse Grupo de Relatório pertence (por exemplo: RM)

***Aplicação:*** Informe a Aplicação a qual esse Grupo de Relatório pertence (por exemplo: RH)

***Módulo:***Informe o Módulo a qual esse Grupo de Relatório pertence (por exemplo: Folha de Pagamento)

***Exemplo prático abaixo:***

# Perfis:

---

A partir da versão 12.1.28, o TReports limita o acesso a relatórios de acordo com os perfis autorizados configurado no Grupo de relatórios.

Ao acessar o cadastro de um Grupo, será possível através do campo 'Perfis' fazer configuração de quais perfis [configurados no RAC](https://tdn.totvs.com/x/Tg18FQ) podem acessar os relatórios relacionados a este grupo. Desta forma é possível limitar o acesso de determinados relatórios somente a determinados usuários.

 Durante s a criação de um novo registro, o campo perfil listará os perfis que estão associados ao usuário logado. O campo poderá ser alterado para inclusão/remoção de outros perfis.

A associação de Perfis a um grupo influenciará nos relatórios em que um usuário terá acesso, ou seja, se os perfis de um novo usuário não estiverem inclusos no grupo criado acima, o usuário não verá nenhum dos relatórios daquele grupo.

Breaking Change

Para sistemas atualizados de versões anteriores a 12.1.28,  será necessário acessar os cadastros de grupos do sistema e adicionar os perfis desejados. Inicialmente após a migração, serão somente configurado o perfil 'Admin'.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Cadastro Grupo de Relatório

falsefalse

**Status:** Finalizado

false

**Data:** 08/12/2017

false

**Autores:**
