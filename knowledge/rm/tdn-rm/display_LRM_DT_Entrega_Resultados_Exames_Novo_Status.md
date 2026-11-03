---
content_hash: 2a20a34416d3b725b990510b61903cf075c1cd511fc4830abe4180888e7030ca
fetched_at: '2026-06-29T00:08:16.999611+00:00'
page_id: '249955052'
product: rm
source: tdn-rm
title: DT_Entrega_Resultados_Exames_Novo_Status
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Entrega_Resultados_Exames_Novo_Status
version: 113
---

# Entrega de resultados de exames com novo status

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Controle de Pedidos de Exames | |
| **Parâmetro(s):** | Utiliza Status Liberado Recepção |
| **Requisito (ISSUE):** | SAUHRM01-565 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada a opção de utilizar status **Liberado para recepção** no **Controle de Pedido de Exames**.

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

1. Acesse**Opções/Parâmetros/Parâmetros Gerais**.
2. Na aba **Unidade Diagnóstico II** , marque o parâmetro **Utiliza Status Liberado Recepção**.

* + **Não:** Processo de controle de exames não utilizará esse status.
  + **Antes da impressão do resultado:** Marque caso o fluxo seja de imprimir na área que gera o resultado do exame.
  + **Depois da impressão do resultado:** Marque caso a recepção seja responsável por imprimir o resultado do exame.

****CONFIGURAÇÃO DE PERFIL****

1. Acesse  **Cadastros/Segurança/Perfis**.
2. Selecione um perfil e acesse **Anexos/Parâmetros RM Saúde**.
3. Marque os parâmetros **Libera resultado para recepção** e **Cancela Liberação resultados para recepção**.

## Procedimento para Utilização

1. Acesse o menu **Unidade de Diagnóstico / Controle de Pedidos de Exames**.

* Processo com o parâmetro setado como Antes da impressão do resultado.

              Quando um exame está com status liberado, as possíveis ações são:

              Ao liberar para recepção, o status do exame passa para O.

Quando um exame liberado para recepção, as possíveis ações são:

* + Cancelar liberação para recepção: Ao efetuar a ação, o status passa a ser retorno para correção.

* + Entregar exame: Entregar ao responsável o resultado.

* Processo com o parâmetro setado como **Depois da impressão do resultado**

Quando um exame está com status **liberado**, as possíveis ações são:

* + Retornar Liberado para correção.
  + Emitir resultado.

Quando um exame está com status **emitido**, as possíveis ações são:

Quando um exame está **liberado para a recepção**, as possíveis ações são:

divs
