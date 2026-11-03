---
content_hash: 2ad0cfc5f9a43f4a357bc9e15ef978a8d3faa379a31cf5e2b000164c1e8035b6
fetched_at: '2026-06-29T00:08:15.508873+00:00'
page_id: '244742383'
product: rm
source: tdn-rm
title: DT_Condições_Contratuais_com_Convênio_Período_de_Retorno_Consultas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244742383
version: 113
---

# Condições Contratuais com Convênio - Período de Retorno Consultas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Condições Contratuais com Convênios | |
| **Chamados Relacionados** | TUTEZZ |
| **Requisito (ISSUE):** | SAUHRM01-288 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER®, ORACLE® |
| **Tabelas Utilizadas:** | SZCONDCONTRATRETORNO |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Melhoria na rotina de Condições Contratuais com Convênios, implementado campo para vincular uma condição contratual a uma Unidade de Atendimento.

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

**Exemplo:**

1. Acesse o menu **Cadastros / Faturamento / Condições Contratuais com Convênios**.
2. Selecione um registro e na tela que é exibida, acesse o menu **Anexos / Retorno de Consulta**.
3. Na aba de **Retorno de Consulta**, selecione **Novo** (ícone Página).
4. Na tela de **Retorno de Consulta**, a opção de selecionar uma Unidade de Atendimento estará disponível.
5. Após salvar, na aba de **Retorno de Consulta** também será possível visualizar o valor selecionado.

divs
