---
content_hash: 1ca74630c05388ba5d798f3538b4893542cce707baecaa11961e4799848dc6ee
fetched_at: '2026-06-29T00:08:07.937938+00:00'
page_id: '237397800'
product: rm
source: tdn-rm
title: DT_Alertas_Encerramento_de_Contas_com_Valores_Inferiores_a_X_Reais
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Alertas_Encerramento_de_Contas_com_Valores_Inferiores_a_X_Reais
version: 110
---

# Alertas encerramento de contas com valores inferiores a X reais

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Parâmetros Gerais | | Elaboração de Contas | |
| **Requisito (ISSUE):** | [PCREQ-10846](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10846 "PCREQ-10846") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL®, Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementação de alertas no encerramento de contas com valores inferiores a X reais, onde o objetivo é criar um conjunto de parâmetros que alterem o comportamento da rotina de encerramento de contas, levando em consideração um valor mínimo para cada Item de Débito.

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

1. Acesse o menu **Opções / Parâmetros / Parâmetros Gerais**, aba **Faturamento II**.
2. Marque o checkbox **Utiliza verificação de valor mínimo no encerramento** e parametrize as demais opções conforme desejado:

## Procedimento para Utilização

1. Acesse o menu **Atendimento/Pronto Atendimento / Ambulatório /Registro de Atendimentos Externos**.
2. Inclua um novo atendimento.
3. Na aba **Guia/Autorização**, inclua uma guia para o paciente.
4. Acesse a **Elaboração de Contas do Paciente** e lance alguns itens de SADT, MatMed, Honorários, Diárias e Taxas/Serviços na conta do paciente.
5. Encerre a conta e verifique se o sistema respeitou as regras parametrizadas:

divs
