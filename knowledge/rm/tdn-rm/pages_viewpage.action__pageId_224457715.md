---
content_hash: 456a7f74f5090de6309889cf7d160b13ff440032061850d85ab67cc13a78aa6e
fetched_at: '2026-06-29T00:06:26.281487+00:00'
page_id: '224457715'
product: rm
source: tdn-rm
title: DT_Restrições_por_Grupo_de_Exames
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224457715
version: 126
---

# Restrições por Grupo de Exames

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Agenda de atendimento | Agendamento de exames | |
| **Requisito (ISSUE):** | [PCREQ-9951](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-9951) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | SZCLASSEXAME e SZGRUPOEXAMES |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Esta implementação consiste em permitir o cadastro grupos de exames, definir quantidade máxima para agendamento por dia e restringir o agendamento de um exame do mesmo grupo caso a quantidade seja ultrapassada.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.9 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.9.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).
2. Faça o login, com seu E-mail e Senha.
3. Na barra de menu superior, clique em DOWNLOAD.
4. No boxe Central de Downloads aplique os filtros conforme campos abaixo:  
   1. Linha: RM
   2. Versão: RM 12.1.9
   3. Tipo: Patch

Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.  
   Importante: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

* Cadastro do grupo de exames:
  1. Acesse o menu **Cadastros/Unidades de Diagnóstico/Classificação de Exames**.
  2. Preencha os campos obrigatórios. O campo "**Qtd. Máxima**" indica a quantidade de agendamentos que este grupo pode ter por dia.
  3. Na aba "**Grupo de Exames**", escolha quais os exames farão parte deste grupo.
* Agendamento de exames:
  1. Quando algum destes exames do grupo for agendado, o sistema validará se a algum deles já foi agendado para o mesmo dia. Se sim, o sistema soma a quantidade agendada para todos os exames do grupo e verifica se atingiu o limite definido no cadastro. Caso já tenha atingido, uma mensagem informando que não será possivel agendar será exibida. A validação ocorre tanto no agendamento normal quanto no wizard de agendamento de exames.

divs
