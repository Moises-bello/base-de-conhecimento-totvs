---
content_hash: 1a80af67b846993d18e7832eddb81a110168cc71daf4e05f39a3c1ddeb4e04c0
fetched_at: '2026-06-29T00:08:13.987292+00:00'
page_id: '244436047'
product: rm
source: tdn-rm
title: DT_Tipo_de_Guia_na_Central_de_Autorização_para_Padrões_que_a_Utilizam
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244436047
version: 112
---

# Tipo de guia na central de autorização para padrões que a utilizam

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Central de Autorização | |
| **Chamados Relacionados** | TTYUPC |
| **Requisito (ISSUE):** | SAUHRM01-285 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL®, Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Melhoria na tela de Central de Autorizações, foi excluída a exigência de tipo de guia para autorizar lançamentos nos convênios em que o padrão de codificação é diferente de ANS/TISS.

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

**Exemplo:**

       1.            Acesse o menu **Faturamento/Central de Autorizações**.

       2.            Selecione o registro a ser autorizado.

       3.            Clique em **Processos/Realizar Autorização dos Lançamentos.**

       4.            Confirme a autorização na janela que é exibida.

divs
