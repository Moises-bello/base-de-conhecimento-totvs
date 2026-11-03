---
content_hash: fc7ea2d84094714c8e6d1b4f723c9f8106b0db8e774310101e3918bd7ddc765a
fetched_at: '2026-06-29T00:08:14.202299+00:00'
page_id: '244442772'
product: rm
source: tdn-rm
title: DT_Controle_Pedidos_Exames_Reduzir_Quantidade_de_Status
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Controle_Pedidos_Exames_Reduzir_Quantidade_de_Status
version: 110
---

# Controle de Pedidos de Exames Reduzir Quantidade de Status

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Controle de Pedidos de Exames | |
| **Parâmetro(s):** | Suprime Confirmação F4 e OK na Digitação do Resultado |
| **Requisito (ISSUE):** | SAUHRM01-372 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada a opção de suprimir os processos de confirmação(Salvar) e OK na Digitação de Resultados.

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

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse **Opções/Parâmetros/Parâmetros Gerais**.  
   Marque o parâmetro “**Suprime Confirmação F4 e OK na Digitação do Resultado** ”.

## Procedimento para Utilização

1. Na digitação de resultado de exames mova o status e verifique que não são habilitados os botões **Salvar** (F4) e **OK**.

divs
