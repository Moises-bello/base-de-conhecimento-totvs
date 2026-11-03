---
content_hash: 257b16e07b6438c772e2891de36970cf159aa8064f826b4caf4244833bc83e6d
fetched_at: '2026-06-29T00:08:42.916827+00:00'
page_id: '301171612'
product: rm
source: tdn-rm
title: DT Pesquisa Itens por período
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=301171612
version: 4
---

# Opção de Pesquisa por Período na Elaboração de Contas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Pesquisa item por grupo de gasto | SauPesquisaItensAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Elaboração de Contas | PSAFT001 | |
| **Tickets relacionados** | [296570](https://totvssuporte.zendesk.com/agent/tickets/296570 "Open ticket in Zendesk Support") |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [SAUHRM02-1292](http://jiraproducao.totvs.com.br/browse/SAUHRM02-1292) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® e Oracle® |
| **Tabelas Utilizadas:** | SZATENDHONORARIO, SZATENDDIARIA, SZATENDTAXASERV, SZATENDSADT, SZATENDMATMED |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Na funcionalidade da Elaboração de Contas, na pesquisa de Itens por grupo de gasto foi incluída a opção de filtrar por período. Implementada a possibilidade de não exibir os itens estornados e incluidas as colunas: número da requisição, local de uso, centro de custo, hora de realização

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realize a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.18 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.18.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.18

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Acesse o menu **Faturamento / Particular e Convênios / Elaboração de Contas**.
2. Clique no botão **Pesquisa Atend**.
3. Selecione um atendimento.
4. Clique na aba **Matmed**
5. Clique no botão com o ícone de um binóculo com a descrição **Pesquisa de itens por grupo de gasto**.
6. Será exibida a tela abaixo com algumas opções de filtros. A própria grid já fornece algumas opções de filtro.
