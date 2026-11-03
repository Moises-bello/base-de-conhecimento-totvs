---
content_hash: 583d11d86ffbfba3da2027453cbbfcd4259563d431557357ca7c69fec00a1d9b
fetched_at: '2026-06-29T00:08:21.387268+00:00'
page_id: '268818083'
product: rm
source: tdn-rm
title: DT_Leito_do_Paciente_no_Filtro_de_Movimentaçao_de_Estoque
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268818083
version: 115
---

# Leito do paciente no filtro de movimentação de estoque

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Movimentação do Estoque | |
| **Chamados Relacionados** | TVGZEQ |
| **Requisito (ISSUE):** | SAUHRM02-68 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada coluna **Leito** com o número do leito do paciente na tela de Movimentação do Estoque.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.14 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.14.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.14

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Acesse o menu **Estoques******/** Movimentação do Estoque.**
2. Verifique a coluna indicando o leito do paciente na listagem das movimentações do estoque.

divs
