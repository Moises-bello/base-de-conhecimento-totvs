---
content_hash: d0039a82a3c20dbed1c8b74ea114d6e026b19a651f0e787ad625a30c0c8a1f01
fetched_at: '2026-06-29T00:06:07.086950+00:00'
page_id: '201735064'
product: rm
source: tdn-rm
title: ER_PCREQ-6798_Link_de_Exames_para_Cópia_de_Laudo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201735064
version: 3
---

# Linkar exames para replicar o Laudo

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

# 

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS HOSPITALAR | **Módulo** | UNIDADE DE DIAGNÓSTICO |
| **Projeto1** | * [R\_SAU\_RM\_V12](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12 "R_SAU_RM_V12") | **IRM1** | * [PCREQ-6791](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-6791 "PCREQ-6791") |
| **Requisito1** | * [PCREQ-6798](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-6798 "PCREQ-6798") | **Subtarefa1** | 1. [SAU\_DEV-2791](http://jira.totvs.com.br/browse/SAU_DEV-2791) |
| **Chamado2** | TRAYU0 | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | 12.1.8 |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

   Possibilitar para o usuário, linkar exames, para que quando um laudo for digitado para um dos exames linkados, ele seja replicado para todos os outros.

## Definição da Regra de Negócio

Ao acessar o menu "Unidade de Diagnóstico > Controle de Pedidos de Exames", é disponibilizado ao usuário um novo botão, que permite linkar os exames relacionados com aquele que está selecionado na view.

   Ao selecionar um exame e clicar no botão, é disponibilizado para o usuário uma tela onde todos os exames passíveis de serem relacionados são disponibilizados, usuário então deve linkar os exames que desejar.

   Ao editar um dos exames que foram linkados e alterar o seu laudo, sistema, ao salvar, avisa o usuário que existem exames linkados e se ele deseja replicar o laudo apra todos os exames linkados. Caso o usuário confirme a réplica, todos os outros laudos serão sobrescritos pelo laudo que o usuário acabou de salvar.

*<Na tabela abaixo informe quais são as rotinas envolvidas, o tipo de operação, a opção de menu e se necessário uma breve descrição das regras de negócio relacionadas a rotina>.*

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Unidade de Diagnóstico] | [Alteração] | [Unidade de Diagnóstico > Controle de Pedidos de Exames] | - |

***Exemplo de Aplicação:***

* Logar no RM Saúde com o usuário "mestre";
* Acessar o menu "Unidades Diagnóstico > Controle de Pedidos de Exames";
* Selecionar o filtro "Em digitação", selecionar um pedido qualquer e clicar no botão "Link Laudos”, na barra superior da view;
* Na tela qua abrir, selecionar mais de um exame (Segurando ctrl e clicando nos mesmos) e clicar em relacionar;
* Novamente na view, selecionar um dos exames que foram 'linkados', digitar o laudo e concluir a digitação;
* Acessar um dos outros exames e verificar se o laudo digitado no primeiro foi replicado.

***Tabelas Utilizadas***

* *SZLINKEXAMES - Link de exames*

### Opcional

## Protótipo de Tela

**Protótipo 01**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
