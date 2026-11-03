---
content_hash: b85a643414359dda14e325d32fc01808de9dfdbda99d22fbbc3f2b5675074b9e
fetched_at: '2026-06-29T00:06:26.498034+00:00'
page_id: '225268723'
product: rm
source: tdn-rm
title: DT_Restrições_por_Exame_Dia_Horário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=225268723
version: 118
---

# Restrições por Exame Dia/Horário

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Agenda de Atendimentos | Agendamento de Exames | |
| **Requisito (ISSUE):** | [PCREQ-9952](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-9952 "PCREQ-9952") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | SZHORARIOSPERMITIDOSEXAME |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

A implementação consiste em possibilitar a restrição do agendamento de exames por dia e horário.

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

* Cadastro de horários permitidos para o exame
  1. Acesse o menu **Cadastros / Unidades de Diagnóstico / Exames e Serviços**.

2. Selecione o exame e clique duas vezes para editar.

3. Na aba **Horários Permitidos**, defina o dia e a faixa horária que será permitida para a realização do exame.

4. Ao tentar realizar o agendamento fora do horário definido, o sistema exibe a mensagem de alerta e não permite o agendamento. A mensagem aparece tanto no agendamento normal quanto no Wizard de agendamento de exames.

5. Nos outros dias da semana, o sistema permite o agendamento normalmente. Para restrigir o horário para os outros dias, repita os 2 e 3, selecionando os outros dias da semana conforme necessário.

divs
