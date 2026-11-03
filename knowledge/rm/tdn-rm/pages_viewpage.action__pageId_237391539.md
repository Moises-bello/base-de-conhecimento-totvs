---
content_hash: c4897d6fb8a06a4a7a28b6e6f40547a1cd03f418d546db5e93f3c9fdedb1afe1
fetched_at: '2026-06-29T00:08:07.823306+00:00'
page_id: '237391539'
product: rm
source: tdn-rm
title: DT_Validação_Controle_de_Documentos_por_Parcial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=237391539
version: 117
---

# Validação por Parcial no Controle de Documentos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Controle de Documentos | |
| **Requisito (ISSUE):** | [PCREQ-10899](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10899 "PCREQ-10899") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle®/ SQL Server® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

 Implementada a  validação de inclusão de documentos de um mesmo tipo, por parcial.

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

1. Acesse o menu **Opções / Parâmetros / Parâmetros Gerais** e marcar a opção **"Apenas um Documento por Parcial"**.

## Procedimento para Utilização

1. Acesse o menu **Faturamento / Controle de Documentos.**
2. Inclua um novo documento para um paciente.
3. Inclua novamente um documento do mesmo tipo para o paciente. O sistema deverá alertar o usuário e caso o mesmo deseje prosseguir, deverá permitir a inclusão do documento.
4. Acesse o menu **Opções / Parâmetros / Parâmetros** Gerais e marcar a opção "**Apenas um Documento por Parcial**".
5. Execute novamente os passos de 1 a 3. O sistema não permitirá que o documento seja incluído, alertando o usuário sobre a parametrização realizada.

divs
