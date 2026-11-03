---
content_hash: 59bec00f267d8840c05bcf829add47ea401d979efd3e902fecf9e2c93ff2f04d
fetched_at: '2026-06-29T00:08:07.736903+00:00'
page_id: '237385991'
product: rm
source: tdn-rm
title: DT_Processamento_de_Requisição_na_Tela_de_Edição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=237385991
version: 118
---

# Processamento de Requisição na tela de Edição

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Movimentação de Estoque | |
| **Requisito (ISSUE):** | [PCREQ-10895](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10895 "PCREQ-10895") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server®, Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Na tela de edição da movimentação de estoque, foi implementado o botão "Processa" que possui o mesmo funcionamento do botão de mesmo nome na tela de visão da movimentação de estoque, ou seja, que realiza o processamento da requisição.

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

1. Acesse o menu **Estoques/Movimentação de Estoque**.
2. Preencha o filtro de acordo com a necessidade, para que sejam exibidas as requisções pendentes.
3. Selecione uma das requisições e editar ou clicar duas vezes sobre a linha para que seja aberta a tela de edição.
4. O botão **Processa**está posicionado na barra de ações inferior.
5. Ao clicar neste botão, o TOTVS Gestão Hospitalar realizará o processamento da requisição.

divs
