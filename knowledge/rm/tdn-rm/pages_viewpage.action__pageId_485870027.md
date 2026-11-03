---
content_hash: 50d15533348c10755a54bb5ffde7125412446fba4c9dc5687f40fbae3e598f2b
fetched_at: '2026-06-29T00:10:20.105241+00:00'
page_id: '485870027'
product: rm
source: tdn-rm
title: Execução de Relatórios com Procedure pela MDI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=485870027
version: 17
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       Este documento tem objetivo de orientar qual estrutura se deve utilizar em relatórios Delphi que possua Stored Procedures contendo passagem de parâmetro, para que sejam executados via MDI (RM.exe).

# Introdução:

---

       Relatórios Delphi contendo procedures com passagem de parâmetros e que são configuradas para executar antes da geração do relatório, necessitam de alteração na sua estrutura para que possam executar pela MDI.

false

 Para acessar esta configuração, pela estrutura do relatório Delphi, vá no menu: “*Configurar | Dados do Relatório*”.

       O nome da Procedure deve ser removido da configuração “Stored Procedure”, na estrutura do relatório deve-se incluir no primeiro grupo do relatório o controle “Stored Procedure”.

 

       Caso o controle “Stored Procedure” seja incluso em um grupo com outros controles, será necessário ajustar a ordenação de execução destes controles, para isso selecione o grupo e acesse suas propriedades, guia “Campos”.

       Controles que passam valores para procedure ou um espelho que recebe valores de um campo que repassa como parâmetro para procedure devem ser posicionados para executar antes da procedure.

       Com esta estrutura o relatório poderá ser executado pela Visão.Net sem problemas.

       Lembramos que o Gerador de Relatórios é uma das ferramentas obsoletas do sistema RM. Por isso, pequenos ajustes que referenciam essa ferramenta não serão realizados.

---

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Relatórios com Procedure

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
