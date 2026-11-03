---
content_hash: 2750cede42bfcc46df3b2c565b5fd86ebf7acb2e48772a85260cb9418f02cb79
fetched_at: '2026-06-29T00:09:01.850543+00:00'
page_id: '378284660'
product: rm
source: tdn-rm
title: Utilizando Gatilhos de Cadastros
type: documentation
url: https://tdn.totvs.com/display/LRM/Utilizando+Gatilhos+de+Cadastros
version: 18
---

# Índice

---

.\*ndice:

# Objetivo

---

       Neste documento será explicado quando são executadas fórmulas visuais com gatilhos de Cadastros.

Para os exemplos citados abaixo, estamos considerando uma fórmula que tenha em sua estrutura uma atividade de "Transformar Registro em XML", para receber o DataSet da tabela da tela. E um atividade de "Exceção" para exibir os dados XML capturados na atividade anterior. Consulte o documento  para mais informações sobre outras atividades de Fórmula Visual.

# Gatilho Antes da Leitura da Visão e Após a Leitura da Visão

---

* **Gatilho Antes da Leitura da Visão:**Utilizando o gatilho "Antes da Leitura da Visão", a fórmula visual será executada no momento em que o usuário clicar na visão (Antes mesmo de carregar algum registro do banco de dados).

**Exemplo:**Na edição da fórmula criada, configure o gatilho "Cadastros | Antes da Leitura da Visão" com a action "GlbUsuario (por exemplo)". Feita a configuração, acesse o menu de usuários. A formula será executada nesse momento, **antes** de preencher o DataSet com a consulta padrão do RM, ou seja, nenhum dado de usuário será retornado na FV.

* **Gatilho Após a Leitura da Visão:** Utilizando o gatilho "Após a Leitura da Visão", a fórmula visual será executada no momento em que o usuário clicar na visão (Assim que os registros do banco de dados forem carregados, exibido nos detalhes da exceção).

**Exemplo:**Na edição da fórmula criada, configure o gatilho "Cadastros | Após da Leitura da Visão" com a action "GlbUsuario (por exemplo)". Feita a configuração, acesse o menu de usuários. A formula será executada nesse momento, **após** o preenchimento do DataSet com a consulta padrão RM, ou seja, os dados do menu de usuários será retornado na FV.

# Gatilho Antes da Leitura de Edição e Após a Leitura de Edição

---

* **Gatilho Antes da Leitura da Edição:** Utilizando o gatilho "Antes da Leitura de Edição" a formula visual será executada no momento em que a o usuário clicar na edição de um registro (Antes mesmo de carregar a tela e algum registro do banco de dados).

**Exemplo:** Na edição da fórmula criada, configure o gatilho "Cadastros | Antes da Leitura de Edição" com a action "GlbUsuario (por exemplo)". Feita a configuração, acesse o menu de usuários, selecione um registro qualquer e clique em "Editar". A formula será executada nesse momento, **antes**da abertura de tela e do preenchimento do DataSet com a consulta padrão do RM, ou seja, nenhum dado da tela de edição do usuário será retornado na FV.

* **Gatilho Após a Leitura de Edição:** Utilizando o gatilho "Após a Leitura de Edição", a fórmula visual será executada no momento em que a o usuário clicar na edição de um registro (Assim que os registros do banco de dados forem carregados, exibido nos detalhes da exceção).

**Exemplo:** Na edição da fórmula criada, configure o gatilho "Cadastros | Após a Leitura de Edição" com a action "GlbUsuario (por exemplo)". Feita a configuração, acesse o menu de usuários, selecione um registro qualquer e clique em "Editar". A fórmula deverá ser executada nesse momento, **após** o preenchimento do DataSet com a consulta padrão RM, ou seja, os dados da tela de edição será retornado na FV.

# Gatilho Antes da Atualização do Registro(Inicio) e Após a Atualização do Registro(Inicio)

---

* **Gatilhos Antes e Após da Atualização do Registro (Inicio):**São gatilhos manipulados através da necessidade do cliente onde o mesmo faz a requisição para um determinado produto onde o produto irá programar uma determinada rotina. Ou seja, **antes** da atualização do registro o desenvolvedor do produto irá desenvolver uma rotina para que seja executada nestes gatilhos. Lembrando que as implementações são feitas apenas pelos desenvolvedores mediante a necessidade do cliente.

# Gatilho Antes da Atualização do Registro(Fim) e Após a Atualização do Registro(Fim)

---

* **Gatilhos Antes e Após da Atualização do Registro (Fim):**São gatilhos também manipulados através da necessidade do cliente onde o mesmo faz a requisição para um determinado produto onde o produto irá programar uma determinada rotina. Ou seja, logo **após** a atualização do registro o desenvolvedor do produto irá desenvolver uma rotina para que seja executada nestes gatilhos. Lembrando que as implementações são feitas apenas pelos desenvolvedores mediante a necessidade do cliente.

# Gatilho Antes de Salvar um Registro e Após Salvar o Registro

---

* **Gatilho Antes da Atualização do Registro (Inicio):** Utilizando o gatilho "Antes de Salvar um Registro" a formula visual  será executada no momento em que o usuário salvar em um registro (Antes mesmo da alteração ser registrada do banco de dados).

**Exemplo:** Na edição da fórmula criada, configure o gatilho "Cadastros | Antes da Atualização do Registro (Inicio)" com a action "GlbUsuario (por exemplo)". Feita a configuração, acesse o menu de usuários, selecione um registro qualquer e clique em "Editar", em seguida faça a alteração de algum campo e clique em Salvar. A fórmula deverá ser executada nesse momento, **antes** de preencher o DataSet com atualização do registro. 

* **Gatilho Após a Atualização do Registro (Fim):** Utilizando o gatilho "Após Salvar o Registro", a fórmula visual será executada no momento em que o o usuário salvar em um registro (Assim que o registro for atualizado no banco de dados).

**Exemplo:** Na edição da fórmula criada, configure o gatilho "Cadastros | Após a Leitura de Edição" com a action "GlbUsuario (por exemplo)". Feita a configuração, acesse o menu de usuários, selecione um registro qualquer e clique em "Editar", em seguida faça a alteração de algum campo e clique em Salvar. A fórmula deverá ser executada nesse momento, **após** preencher o DataSet com atualização do registro, ou seja, a atualização do registro será retornado na FV.

# Gatilho Antes da Leitura da Visão de Lookup e Após a Leitura da Visão de Lookup

---

* **Gatilho Antes da Leitura da Visão de Lookup:** Utilizando o gatilho "Antes da Leitura da Visão de Lookup" a formula visual  será executada no momento em que o usuário clicar no Lookup (Antes mesmo do carregamento da tela e de algum registro do banco de dados).

**Exemplo:** Na edição da fórmula criada, configure o gatilho "Cadastros | Antes da Leitura da Visão de Lookup" com a action "GlbConsSQLData (por exemplo)". Feita a configuração, acesse um menu qualquer, e clique em "Anexos | Consulta SQL | Inserir Consulta SQL" em seguida na tela de "Inserir uma consulta SQL a uma Action", clique no lookup do campo "Consulta SQL". A fórmula deverá ser executada nesse momento, **antes** da abertura da tela e do preenchimento do DataSet com a consulta padrão do RM, ou seja, nenhum dado de será retornado na FV.

* **Gatilho Após a Leitura da Visão de Lookup:** Utilizando o gatilho "Após da Leitura da Visão de Lookup" a formula visual  será executada no momento em que o usuário clicar no Lookup (Assim que os registros do banco de dados forem carregados, exibido nos detalhes da exceção).

**Exemplo:** Na edição da fórmula criada, configure o gatilho "Cadastros | Após a Leitura da Visão de Lookup" com a action "GlbUsuario (por exemplo)". Feita a configuração, acesse um menu qualquer, e clique em "Anexos | Consulta SQL | Inserir Consulta SQL" em seguida na tela de "Inserir uma consulta SQL a uma Action", clique no lookup do campo "Consulta SQL". A fórmula deverá ser executada nesse momento, **após** o preenchimento do DataSet com a consulta padrão RM, ou seja, os dados da tela de lookup será retornado na FV.

# Gatilho Antes da Leitura dos Valores de Lookup e Após a Leitura dos Valores de Lookup

---

* **Gatilho Antes da Leitura dos Valores de Lookup:** Utilizando o gatilho "Antes da Leitura dos Valores de Lookup" a formula visual  será executada no momento em que o usuário selecionar um valor para o lookup (Antes mesmo do carregamento do registro selecionado no banco de dados).

**Exemplo:** Na edição da fórmula criada, configure o gatilho "Cadastros | Antes da Leitura dos Valores de Lookup" com a action "GlbConsSQLData (por exemplo)". Feita a configuração, acesse um menu qualquer, e clique em "Anexos | Consulta SQL | Inserir Consulta SQL" em seguida na tela de "Inserir uma consulta SQL a uma Action", clique no lookup do campo "Consulta SQL", selecione um registro e clique em OK. A fórmula deverá ser executada nesse momento, **antes** do preenchimento do DataSet com a consulta padrão do RM, ou seja, nenhum dado da consulta selecionada será retornado na FV.

* **Gatilho Após a Leitura dos Valores de Lookup:** Utilizando o gatilho "Após a Leitura dos Valores de Lookup" a formula visual  será executada no momento em que o usuário selecionar um valor para o lookup (Assim que as dados do registro selecionado forem carregados, exibido nos detalhes da exceção).

**Exemplo:** Na edição da fórmula criada, configure o gatilho "Cadastros | Após a Leitura dos Valores de Lookup" com a action "GlbConsSQLData (por exemplo)". Feita a configuração, acesse um menu qualquer, e clique em "Anexos | Consulta SQL | Inserir Consulta SQL" em seguida na tela de "Inserir uma consulta SQL a uma Action", clique no lookup do campo "Consulta SQL", selecione um registro e clique em OK. A fórmula deverá ser executada nesse momento, **após** o preenchimento do DataSet com a consulta padrão RM, ou seja, os dados da consulta selecionada pelo lookup será retornado na FV.

# Gatilho Antes da Leitura do DataSet Vazio e Após a Leitura do DataSet Vazio

---

* **Gatilho Antes da Leitura do DataSet:**Utilizando o gatilho "Antes da Leitura do DataSet", a fórmula visual será executada no momento em que o usuário clicar na visão (Antes mesmo de criar o DataSet).

**Exemplo:**Na edição da fórmula criada, configure o gatilho "Cadastros | Antes da Leitura da Visão" com a action "GlbUsuario (por exemplo)". Feita a configuração, acesse o menu de usuários. A formula será executada nesse momento, **antes**de criar o DataSet, ou seja, nenhuma estrutura será retornado na FV.

* **Gatilho Após a Leitura do DataSet:** Utilizando o gatilho "Após a Leitura do DataSet", a fórmula visual será executada no momento em que o usuário clicar na visão (Assim que o DataSet for criado).

**Exemplo:**Na edição da fórmula criada, configure o gatilho "Cadastros | Após da Leitura da Visão" com a action "GlbUsuario (por exemplo)". Feita a configuração, acesse o menu de usuários. A formula será executada nesse momento, **após** a criação do DataSet (sem exibir nenhum dado do menu), ou seja, somente o DataSet será retornado na FV.

# Gatilho Antes da Leitura das Propriedades e Após a Leitura das Propriedades

---

* **Gatilho Antes da Leitura das Propriedades:**Utilizando o gatilho "Antes da Leitura das Propriedades", a fórmula visual será executada no momento em que o usuário clicar na visão (Antes mesmo de carregar o menu e alguma propriedade do banco de Dados).

**Exemplo:**Na edição da fórmula criada, configure o gatilho "Cadastros | Antes da Leitura da Leitura das Propiedades" com a action "GlbUsuario (por exemplo)". Feita a configuração, acesse o menu de usuários. A formula será executada nesse momento, **antes** de preencher o DataSet com a consulta padrão do RM e suas propriedades, ou seja, nenhuma Propriedade será retornado na FV.

* **Gatilho Após a Leitura das Propriedades:** Utilizando o gatilho "Após a Leitura do DataSet", a fórmula visual será executada no momento em que o usuário clicar na visão (Assim que as propriedades forem criadas, exibido nos detalhes da exceção).

**Exemplo:**Na edição da fórmula criada, configure o gatilho "Cadastros | Após da Leitura da Visão" com a action "GlbUsuario (por exemplo)". Feita a configuração, acesse o menu de usuários. A formula será executada nesse momento, **após** o preenchimento do DataSet e criação das propriedades, ou seja, os dados do DataSet e as propriedades será retornado na FV.

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.44 ou Superiores

false

**Processo:** Gatilhos de Cadastros

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
