---
content_hash: 5fbba9199450df05a1e608176bf47214f54d8f88d4fb0577b017c08431aef9a1
fetched_at: '2026-06-29T00:08:13.958791+00:00'
page_id: '244434768'
product: rm
source: tdn-rm
title: DT_Controle_Exames_Movimentação_Status
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244434768
version: 112
---

# Controle de Exames e Movimentação de Status

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Controle de Pedidos de Exames | |
| **Requisito (ISSUE):** | SAUHRM01-34 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada a validação de status e movimentação de exames com laudo lincado.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.13 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.13.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.13

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

       1.    Acesse o menu****Unidade de Diagnóstico / Controle de Pedidos de Exames****.

               Realize o "link" de alguns exames. Verifique que os status  'X' ,  'M', 'T'  e   'F' apresentam mensagem que o status é inválido.

              

   2. Mova o status de um dos exames. Verifique se todos exames lincados mudam de status.

divs
