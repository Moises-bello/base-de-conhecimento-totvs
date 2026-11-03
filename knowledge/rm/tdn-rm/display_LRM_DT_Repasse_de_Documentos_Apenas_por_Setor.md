---
content_hash: 03fc181323c887bccac6d4a401416c504b349474be100956f001aaf65667dccb
fetched_at: '2026-06-29T00:08:07.843524+00:00'
page_id: '237392348'
product: rm
source: tdn-rm
title: DT_Repasse_de_Documentos_Apenas_por_Setor
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Repasse_de_Documentos_Apenas_por_Setor
version: 115
---

# Repasse de Documentos apenas por Setor

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Controle de Documentos |  |  | | --- | | **Rotina(s) envolvida(s)** | | Parâmetros Gerais | |
| **Requisito (ISSUE):** | [PCREQ-10900](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10900 "PCREQ-10900") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle®/ SQL Server® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

 Implementado repasse de documentos apenas por setor.

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

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse o menu **Opções / Parâmetros / Parâmetros Gerais - Aba Faturamento** e marcar a opção**"Repasse de Documentos Apenas Por Setor"**.

## Procedimento para Utilização

1. Acesse o menu **Faturamento/Controle de Documentos**.
2. Inclua um novo documento e clique em **Processos - Repasse**.
3. Caso o parâmetro **Repasse de Documentos Apenas Por Setor** estiver marcado, o lookup de usuário será exibido desabilitado.
4. Selecione o setor para onde o documento será repassado e efetue o processo normalmente.

divs
