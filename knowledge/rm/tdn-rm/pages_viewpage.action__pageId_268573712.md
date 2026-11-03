---
content_hash: 27ef24935b53ca1f5f2b9ba3ec466afdb7cd74d392ca04e25f78f6730b2ece0c
fetched_at: '2026-06-29T00:08:20.253632+00:00'
page_id: '268573712'
product: rm
source: tdn-rm
title: DT_Migração_Faturamento_Registro_de_Entrega_de_Faturas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268573712
version: 114
---

# Migração para .Net - Faturamento - Registro de Entrega de Faturas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Faturamento para Convênios | |
| **Requisito (ISSUE):** | SAUHRM02-187 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada a migração da rotina do Faturamento de **Registro de Entrega de Faturas** da tecnologia Delphi para a tecnologia .Net. Rotina incluída no Faturamento para Convênios. 

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

1. Acesse a nova **MDI RM.exe / Faturamento / Faturamento para Convênios**.
2. Para registrar a entrega de fatura, acesso o processo **Registro de Entrega de Faturas**.
3. Informe a data da entrega e quem esta recebendo.
4. Para registrar o  estorno do registro de entrega da  fatura, acesse o processo **Estorna Registro de Entrega**.
5. Informe o motivo.
6. Para verificar o  histórico do registro de entrega da fatura, acesse o anexo **Histórico Estorno Fatura**.

divs
