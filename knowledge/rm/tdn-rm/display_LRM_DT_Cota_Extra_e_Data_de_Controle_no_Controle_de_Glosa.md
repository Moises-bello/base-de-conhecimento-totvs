---
content_hash: 72ee4b3c6ae4776e5909c712c7381f346c0436b4a4a5a112f78186f992cdca88
fetched_at: '2026-06-29T00:08:16.932309+00:00'
page_id: '248583561'
product: rm
source: tdn-rm
title: DT_Cota_Extra_e_Data_de_Controle_no_Controle_de_Glosa
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Cota_Extra_e_Data_de_Controle_no_Controle_de_Glosa
version: 114
---

# Cota-extra e Data de Controle no Controle de Glosa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Controle de Glosa |  |  | | --- | | **Rotina envolvida** | | Controle de Recebimento | |
| **Cadastros Iniciais:** | Elaboração de Contas, Faturamento de Contas |
| **Requisito (ISSUE):** | SAUHRM01-326 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® e Oracle® |
| **Tabelas Utilizadas:** | SZCONTROLEGLOSA |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Esta implementação consiste em disponibilizar na conclusão do controle de glosa os campos de **cota-extra** e **data de controle**. A cota-extra consiste no valor que "sobrou", ou seja, que não foi identificado no controle de glosa. Os valores identificados a maior em cada item devem ser informados no controle do item. Somente os valores não identificados são considerados como cota-extra. O valor da cota-extra será incluído no valor a maior das informações da glosa.

A data de controle serve para cada cliente e normalmente é a data do recebimento, a data em que o depósito do valor foi feito pelo Convênio.

Além desses novos campos, foram incluídas novas funcionalidades, como:

* Glosa Automática total.
* Estorno de cota-extra.
* Inclusão da data de entrada do paciente nas contas da fatura.
* Inclusão do valor da conta no botão "Pesquisa conta".

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

1. Acesse o menu **Faturamento / Controle de Glosa**.
2. Informe os filtros desejados e selecione uma remessa.
3. Selecione algumas contas (ou todas) e clique no botão **Glosa Total Automática** para realizar a glosa das contas e ter a possibilidade de realizar o recurso delas.
4. Ao clicar no botão de **Glosa Total Automática**, será exibida a tela abaixo solicitando informações da glosa e da data de controle.
5. No botão de **Liberação Automática**, também será solicitado a Data de controle e o valor da cota-extra (caso exista).
6. Uma vez informado o valor da Cota-extra, o sistema habilitará o botão "**Estorno de Cota-extra**", onde o usuário poderá informar o valor do estorno e o sistema já preenche a data e o usuário que realizou o estorno.
7. Verifique na imagem abaixo, a informação da data de Entrada do paciente nas contas da fatura.
8. Verifique na imagem abaixo, a informação do valor da conta, na pesquisa de contas.

divs
