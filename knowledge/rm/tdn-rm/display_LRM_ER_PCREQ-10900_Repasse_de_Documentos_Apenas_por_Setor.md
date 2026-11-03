---
content_hash: 0e367c3d58a4899589931babeb738a63d1857917562caa933545aa8008cd4917
fetched_at: '2026-06-29T00:08:07.829967+00:00'
page_id: '237391839'
product: rm
source: tdn-rm
title: ER_PCREQ-10900_Repasse_de_Documentos_Apenas_por_Setor
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-10900_Repasse_de_Documentos_Apenas_por_Setor
version: 120
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | Saúde |
| **Projeto** | * [R\_SAU\_RM\_V12\_1516](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12_1516 "R_SAU_RM_V12_1516") | **IRM** | * [PCREQ-10841](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-10841 "PCREQ-10841") |
| **Requisito** | * [PCREQ-10900](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10900 "PCREQ-10900") | **Subtarefa** | * [SAU\_DEV-4786](http://jira.totvs.com.br/browse/SAU_DEV-4786) |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

    Este documento tem como objetivo especificar o requisito de repasse de documentos apenas por setor.

## Definição da Regra de Negócio

  **RN001**

* Criar um parâmetro para que, quando marcado, o processo de Repasse de Documento deixe de exigir informação "**usuário**".

   **RN002**

* Modificar o processo de repasse de documentos, fazendo que passe a verificar o parâmetro criado na **RN001** e quando ele estiver marcado, o campo "**usuário**" seja ocultado.

|  |  |  |  |
| --- | --- | --- | --- |
| Rotina | Tipo de Operação | Opção de Menu | Regras de Negócio |
| Parâmetros | Alteração | Opções > Parâmetros > Parâmetros Gerais | **RN001** |
| Repasse de Documentos | Alteração | Faturamento > Controle de Documentos > Processos - Repasse | **RN002** |

**Exemplo de Aplicação:**

1. Acessar o menu "**Opções > Parâmetros > Parâmetros Gerais**";
2. Marcar a opção "**Repasse apenas por Setor**";
3. Acessar o menu "**Faturamento > Controle de Documentos**";
4. Incluir um novo documento e clicar em "**Processos - Repasse**";
5. Selecionar o Setor para onde o documento será repassado.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
