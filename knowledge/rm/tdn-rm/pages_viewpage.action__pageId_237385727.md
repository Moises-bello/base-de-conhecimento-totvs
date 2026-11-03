---
content_hash: 6cf3b6026a35157e9a6566a14f6527910be7846c7c2ae27b6454329aa1f84db4
fetched_at: '2026-06-29T00:08:07.720489+00:00'
page_id: '237385727'
product: rm
source: tdn-rm
title: DT_Indicação_de_Médico_Cooperado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=237385727
version: 120
---

# Indicação de Médico Cooperado

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Credenciamento de Prestador x Convênios |  |  | | --- | | **Rotina(s) envolvida(s)** | | Registro de atendimento interno e externo | | Elaboração de Contas | |
| **Requisito (ISSUE):** | [PCREQ-10897](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10897 "PCREQ-10897") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server®, Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

No credenciamento do prestador, existe um campo (checkbox) para informar se naquele credenciamento o prestador é ou não COOPERADO.

Ao selecionar o prestador, o sistema valida essa informação e caso seja COOPERADO, será exibida uma mensagem na tela apenas para informação. Por default, no cadastro o campo fica desmarcado.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.11 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.11.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo: 

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.11

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Acesse o menu **Cadastros/Uso geral/Prestador/Anexos/Credenciamento**.
2. Marque o campo "**Cooperado**".
3. No registro de atendimento interno ou externo, ao escolher o campo "**Médico Responsável**", o sistema valida o credenciamento do prestador e caso o campo esteja marcado, exibe a mensagem "O médico é cooperado para este credenciamento".
4. Na **Elaboração de Contas**, ao lançar algum item no qual o médico solicitante seja cooperado, também será exibida a mensagem "O médico é cooperado para este credenciamento".

divs
