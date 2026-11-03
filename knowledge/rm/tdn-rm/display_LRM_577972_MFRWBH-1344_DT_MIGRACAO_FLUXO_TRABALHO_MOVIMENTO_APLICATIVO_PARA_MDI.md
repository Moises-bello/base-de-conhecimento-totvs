---
content_hash: 6250edc0c6e714ca0cb1057d79717e4a78bc3a7352c540eebb596e1cef0d0d04
fetched_at: '2026-06-29T00:08:29.752776+00:00'
page_id: '272162549'
product: rm
source: tdn-rm
title: 577972_MFRWBH-1344_DT_MIGRACAO_FLUXO_TRABALHO_MOVIMENTO_APLICATIVO_PARA_MDI
type: documentation
url: https://tdn.totvs.com/display/LRM/577972_MFRWBH-1344_DT_MIGRACAO_FLUXO_TRABALHO_MOVIMENTO_APLICATIVO_PARA_MDI
version: 107
---

# 577972\_MFRWBH-1344\_DT\_MIGRACAO\_FLUXO\_TRABALHO\_MOVIMENTO\_APLICATIVO\_PARA\_MDI

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e projetos.* |
| **Módulo:** | **Gestão de estoque compras e faturamento*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Conversor Fluxo de Atendimento para nova MDI .Net* | **Conversor Fluxo de Atendimento para nova MDI .Net*.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **NA*.* | *NA.* | |  |  | |
| **Cadastros Iniciais:** | *Criar fluxos de trabalhos globais nos tipos de movimentos apresentados na versão Delphi.* |
| **Parâmetro(s):** | *NA.* |
| **Ponto de Entrada:** | *Processo do aplicativo RMNucleus.exe.* |
| **Tickets relacionados** | [577972](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%22577972%22 "577972") |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [MFRWBH-1344](http://jiraproducao.totvs.com.br/browse/MFRWBH-1344) |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | * *Oracle* * *SQL SERVER.* |
| **Tabelas Utilizadas:** | * *GDATASERVERWORKFLOW.* * *GDATASERVERWORKFLOWITEM* |
| **Sistema(s) Operacional(is):** | *-.* |

## Descrição

Foi criado o processo "Conversor Fluxo de Atendimento para nova MDI .Net" dentro do aplicativo RMNucleus.exe com o intuito de migrar as configurações de fluxos de trabalhos criadas nesse aplicativos, e atendimentos relacionados aos movimentos gerados por essas mesmas configurações, dessa forma, após executa-ló, o cliente poderá usar todas suas configurações criadas no RMNucleus.exe na nova estrutura de tipos de movimento presentes na nova MDI.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

**As permissões destacadas abaixo devem ser habilitadas:**

***Obs: Ambas as permissões destacadas compartilham os mesmos privilégios de segurança, ou seja, se uma for desabilitada, as duas deixarão de funcionar.***

## Procedimento para Utilização

O processo "Conversor Fluxo de Atendimento para nova MDI .Net" deve ser executado em uma base de dados que já estiver configurada para utilizar o fluxo de trabalho global, basta executar e ele irá realizar todas as conversões necessárias para as configurações já existentes, assim como todos os atendimentos já criados, passem a funcionar dentro da estrutura revisada utilizada na nova MDI. Seguem abaixo detalhes técnicos das tabelas alteradas pelo processo:

A coluna ACTION de ambas as tabelas GDATASERVERWORKFLOW e GDATASERVERWORKFLOWITEM, será atualizada de acordo com a classificação de cada movimento criado usando o fluxo de trabalho no aplicativo RMNucleus.exe, segue abaixo a relação entre qual nova action deve ser atribuída de acordo com sua classificação:

divs
