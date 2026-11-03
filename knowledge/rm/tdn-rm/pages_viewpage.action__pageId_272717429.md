---
content_hash: e37c1bbe8334ea0b11b5bd202100ec05d6117a6834403c15c05866ef30340d56
fetched_at: '2026-06-29T00:08:31.123898+00:00'
page_id: '272717429'
product: rm
source: tdn-rm
title: DT Rastreabilidade do Recebimento de Lotes Guias / Recurso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272717429
version: 119
---

# Rastreabilidade do Recebimento de Lotes Guias / Recurso

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Faturamento para Convênios / Recebimento de Lotes Guias/Recurso  Faturamento para Convênios / Rastreabilidade de Recebimento de Lotes Guias/Recurso | |
| **Tickets relacionados** | [98738](https://totvssuporte.zendesk.com/agent/tickets/198738 "Open ticket in Zendesk Support") |
| **Requisito****:** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-589 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Tabelas Utilizadas:** | SZARQUIVOCONVENIO, SZLOGIMPRECGLOSAERRO, SZITENSDIARIAARQUIVO, SZITENSHONORARIOARQUIVO, SZITENSMATMEDARQUIVO, SZITENSSADTARQUIVO, SZITENSTAXASERVICOSARQUIVO |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

A melhoria possibilita a Rastreabilidade do processo de Recebimento Lotes Guias e Recursos para a funcionalidade de Faturamento para Convênios e possibilita a rastreabilidade dos itens processados por arquivo e suas respectivas falhas, durante a importação do XML de Retorno de Pagamento, com o objetivo de agregar melhoria operacional ao sistema.

Importante

Esta melhoria contempla a versão 3 da TISS.

## Tabelas para geração de relatórios

Além da informações apresentadas neste documento, esta funcionalidade disponibilizou a rastreabilidade dos itens importados através do banco de dados, para fins de geração de relatórios. Cada item processado e importado com sucesso é salvo nas seguintes tabelas, de acordo com seu respectivo grupo de gasto.

* SZITENSDIARIAARQUIVO: Tabela para armazenar os itens do grupo de gasto Diária.
* SZITENSHONORARIOARQUIVO: Tabela para armazenar os itens do grupo de gasto Honorário.
* SZITENSMATMEDARQUIVO: Tabela para armazenar os itens do grupo de gasto MAT/MED.
* SZITENSSADTARQUIVO: Tabela para armazenar os itens do grupo de gasto SADT.
* SZITENSTAXASERVICOSARQUIVO: Tabela para armazenar os itens do grupo de gasto Taxas/Serviços.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.16 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.16.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.16

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

## Processar remessa

1. Na MDI nova (RM.exe) acesse **Faturamento****/ Faturamento para Convênios**.
2. Selecione a opção de **filtro** desejado, como por exemplo Remessa.
3. Informe o número da remessa, conforme o XML que será utilizado no processo.
4. Selecione um registro.
5. Clique em **Processos** / **Recebimento de Lotes Guia / Recurso.**
6. Siga as seguintes etapas do processo.
7. Avance a primeira etapa.
8. Preencha os campos necessários / Avance o processo.  
   * **Unidade de Faturamento:**Unidade de faturamento da Remessa
   * **Convênio:** Convênio da remessa
   * **Caminho do Arquivo:**Caminho do arquivo que será processado
9. Execute o processo.
10. Após o processamento a seguinte mensagem de sucesso será apresentada.

## Rastreabilidade do Recebimento de Lotes Guias / Recurso

1. Na MDI nova (RM.exe) acesse **Faturamento / Outros / Outros / Rastreabilidade do Recebimento de Lote guias/Recursos**.
2. Selecione e/ou abra o arquivo.
3. Acesse **Anexos / Itens não encontrados na Importação de Lote guias/Recursos**.
4. O sistema pode apresentar os seguintes cenários:

* + Quando todos os itens do arquivo são importados, não haverá nenhum registro no anexo.
  + Quando algum item não foram importado, ele será apresentado nesta tela.

divs
