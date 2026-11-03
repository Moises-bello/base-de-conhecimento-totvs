---
content_hash: ff999f256ce400a8cc95866472b651099aabe5b354747ce030e961d3f1a1be83
fetched_at: '2026-06-29T00:08:09.238509+00:00'
page_id: '239030742'
product: rm
source: tdn-rm
title: ER_SAUHRM01-50_LOG_processos_Exportação_e_Importação_MATRIX
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=239030742
version: 116
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS HOSPITALAR | **Módulo** | RM SAUDE |
| **Segmento Executor** | SAÚDE | | |
| **Projeto1** | SAUHRM01 | **IRM1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-36 |
| **Requisito1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-50 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-215 |
| **Chamado2** |  | | |
| **País** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### **Objetivo**

    Esta especificação tem como objetivo detalhar a melhoria à ser implementada na funcionalidade de Controle de Pedidos de Exames, onde serão implementados registros do histórico do status para os processo de importação e exportação do Controle de Pedidos de Exames para o MATRIX.

## Definição da Regra de Negócio

***RN001 -***Quando ocorrer a troca de informações com o Matrix, s*erá criado um registros do histórico do status durante os processos, permitindo assim verificar que o processo foi exportado/importado**.*

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Troca de Informações com o Matrix] | [Alteração] | [Unidade Diagnóstico > Controle de Pedido de Exame > Troca de Informações com o Matrix > Exportar Pedido] | RN001 |

***Exemplo de Aplicação:***

* *Toda vez que for realizada a importação/exportação do Controle de Pedidos de Exames para o Matrix, esse processo irá registrar o histórico do status na tabela SZHISTORICOSTATUS.*

***Tabelas Utilizadas***

* **SZHISTORICOSTATUS*– Histórico*

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
