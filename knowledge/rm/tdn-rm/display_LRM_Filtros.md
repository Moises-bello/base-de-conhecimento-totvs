---
content_hash: e41878e93557c5888ccea98080188764e62a833ff915bec9a4d40a7d49075438
fetched_at: '2026-06-29T00:11:02.562341+00:00'
page_id: '61932706'
product: rm
source: tdn-rm
title: Filtros
type: documentation
url: https://tdn.totvs.com/display/LRM/Filtros
version: 18
---

Índice

---

.\*ndice:

# Introdução

---

       A execução de processos na linha RM foi modificada estruturalmente para trazer benefícios e possibilidades ao processamento das tarefas e processos. Isso foi possível graças à mudança da arquitetura de Win32 para .Net.

# Objetivo

---

      Os filtros são utilizados para melhorar a visualização dos registros em uma visão ou mesmo trazer aqueles que lhe fazem necessidade.

# 1.Exemplos de Filtros

---

        Para criar um filtro na visão dos sistemas clique no botão Filtrar | Novo Filtro.  Para mais informações veja o [WikiHelp](http://wikihelp.totvs.com.br/WikiHelp/GLB/Glb.Filtros.aspx).

**Opções do item Selecionado:** São os campos da visão que estão disponíveis para filtrar.

**Operador:** São os tipos de condições que o usuário consegue adicionar para filtrar os dados da visão.

**Expressão:** É onde se encontram as condições cadastradas no filtro selecionado.

## 1.1 **Filtros utilizando LIKE:**

---

 Action de Movimento.

**Expressão**: Fornecedor LIKE [CODCFO]

 Action de Movimento.

**Expressão**: Fornecedor LIKE [FORNECEDOR]

 Action de Movimento

**Expressão**: Fornecedor LIKE [] %

## 1.2 **Filtro usando IS NOT NULL (Todos - Retorna todos os registros da visão):**

---

Action de Funcionários

**Expressão**: Chapa IS NOT NULL

## 1.3 **Filtro u**sando operador "=" (igual)****

---

 Action de Funcionários

**Expressão**: Situação = A

## 1.4 **Filtro u**sando uma consulta SQL (IN SQL):****

---

  Action de Funcionários

**Expressão**: Chapa IN (SelecaoCodSit)

## 1.5 **Filtro **variáveis de contexto ( $Hoje):****

---

**Action de Gerenciamento de Jobs**

**Expressão**: Criado EM = $Hoje

# 2.Informações sobre Filtros

---

Para que um determinado filtro seja sempre aplicado no momento da abertura de uma visão (tela), basta que seja marcada a opção"Sempre usar            este filtro ao abrir a visão.

## 2.1 ****Copia de filtros entre coligadas****

---

Para copiar um filtro entre coligadas é necessário Selecionar o Filtro e Clicar em Copiar Filtro.

Após clicar em **não** basta selecionar as coligadas que o filtro será replicado

## 2.2 ******Filtro Global******

---

Para adicionar um filtro como Global é necessário selecionar o Filtro, clicar com o botão direito do mouse e selecionar a opção filtro global.

## 2.3 ******Permissão para Filtro Global******

---

Para ter acesso ao Filtro Global, é necessário que o usuário tenha permissão no item "Filtros Globais" no perfil do módulo em que ele deseja utilizar os filtros Globais.  
  
Exemplo: Para ter acesso aos Filtros Globais no módulo RM Nucleus, o usuário deve estar associado à um perfil do RM Nucleus que tenha permissão no item "Filtros Globais" no "Acesso a Menus".

Atenção

Versões anteriores à 12.1.21:  
  
Para ter acesso ao item Filtro Global em qualquer módulo, é necessário que o usuário tenha em seu acesso algum perfil do módulo "Serviços Globais" que possua permissão no item "Filtros Globais".

## 2.4 **Enviar para barra de Ferramentas**

---

A Opção de Enviar para a barra de ferramentas, disponibiliza o filtro na barra de ferramentas, seja ele por Usuário ou Global, respeitando o escopo do filtro.

Atenção

Filtros Globais só podem ser adicionados na barra de ferramentes por usuários que possuírem permissão em filtros globais conforme item 2.3 desta documentação.

Os Filtros Globais irão aparecer na barra de ferramentas para todos os usuários caso o mesmo seja habilitado.

 

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Filtros de Visão

falsefalse

**Status:** Finalizado

false

**Data:** 18/10/2018

false

**Autores:**
