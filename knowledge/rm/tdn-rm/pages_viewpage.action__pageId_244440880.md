---
content_hash: 35a6915ada99da5db986b8f63e71622f14d1dcbf4cd3e6f2d22750f9b037fee6
fetched_at: '2026-06-29T00:08:14.092167+00:00'
page_id: '244440880'
product: rm
source: tdn-rm
title: DT_Classificação_de_Risco_Parâmetros_por_Estação_de_Trabalho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244440880
version: 113
---

# Classificação de Risco - Parâmetros por estação de trabalho

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Classificação de Risco | |
| **Chamados Relacionados** | TUDAB0 |
| **Requisito (ISSUE):** | SAUHRM01-286 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Tabelas Utilizadas:** | SZPARAMESTACAO |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementado o campo **Sala** na tela de **Classificação de Risco**, que possibilita ao médico confirmar ou alterar a sala que utilizará.

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

1. Acesse o menu **Opções / Parâmetros / Parâmetros Gerais**.
2. Na aba “**Geral**”, selecione a opção de parâmetros por usuário.
3. Acesse o menu **Atendimento / Pronto Atendimento/Ambulatório / Painel de Classificação de Risco**.
4. O campo para alteração da sala será exibido na parte superior da tela.
5. No menu **Opções / Parâmetros / Parâmetros por Estação de Trabalho**, o campo **“Nº do guichê/Sala**” tem o mesmo valor preenchido na tela anterior.
6. Nos **Parâmetros** **Gerais**/ aba **Geral**, ao selecionar os parâmetros por estação de trabalho (passo 3), o campo de sala é ocultado na tela do **Painel de Classificação de Risco**.

divs
