---
content_hash: cfd009978681878bbe4d64870e64c02ced9aff3babb719c3fcb5f64b3a508ffd
fetched_at: '2026-06-29T00:08:05.320537+00:00'
page_id: '235594370'
product: rm
source: tdn-rm
title: DT_Dispensação_Modelo_Otimizado_Separação_Prévia
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235594370
version: 119
---

# Dispensação - Modelo Otimizado Separação Prévia

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar. |
| **Rotina:** | |  | | --- | | **Rotina** | | Mapa de Dispensação. |  |  | | --- | | **Rotina(s) envolvida(s)** | | Recebimento pela Enfermagem. | |
| **Requisito (ISSUE):** | [PCREQ-10750](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10750 "PCREQ-10750") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle®, MSSQL® |
| **Tabelas Utilizadas:** | SZAPRAZAMENTO |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Esta implementação tem como objetivo disponibilizar para os usuários, um novo fluxo de separação prévia de medicamentos que irão compor um pacote a ser entregue no leito do paciente.

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

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse o menu **Opções/Parâmetros/Parâmetros Gerais**, aba **Estoques II** e marque os parâmetros **Utiliza dispensação horária por requisição** e **Utiliza Modelo Otimizado de Separação Prévia**.
2. Selecione o relatório correspondente à etiqueta de pacote.

## Procedimento para Utilização

1. Acesse o menu **Prontuário** e selecione um paciente que esteja internado e ocupando um leito.
2. Prescreva um item para o paciente e clique em **Conclui**.
3. Acesse o menu **Estoques/Mapa de Dispensação**.
4. Inclua um filtro que permita visualizar a prescrição recém feita.
5. Selecione a linha desejada e clique em **Gerar Mapa**, na parte superior da tela. Sistema deverá atribuir aos itens um ID de Mapa.
6. Caso esteja com o relatório de mapa corretamente configurado, clique em **Imprimir Mapa**, na parte superior da tela. Sistema deverá imprimir todos os itens que tem aquele ID de Mapa.
7. Dê um duplo clique em um dos itens da prescrição. Na tela de detalhe, selecione os itens desejados e clique em **Processar**. Sistema processará a requisição e gerará um "CODPACOTE", para cada item.
8. Ao final do processo, sistema automaticamente gerará a etiqueta que corresponde aos itens do pacote.
9. Acesse o menu **Estoques/Recebimento Pela Enfermagem**.
10. Nesta tela, deverá ser "bipado" o código de barras correspondente ao pacote, para que os itens sejam listados e confirmados pela enfermagem.
11. Para efeito de testes, pode ser digitado o código do pacote, seguido de um "0", por exemplo: Pacote "000013", deverá ser digitado "0000130".
12. Confirme todos os itens e clique em **Avançar**.

divs
