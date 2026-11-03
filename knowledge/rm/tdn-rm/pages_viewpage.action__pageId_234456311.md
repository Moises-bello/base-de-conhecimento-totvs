---
content_hash: 8e4dcb40f96ee991906917170096efe278dadfb1254070e61363998a3b81c880
fetched_at: '2026-06-29T00:06:29.263262+00:00'
page_id: '234456311'
product: rm
source: tdn-rm
title: DT_Adaptação_Atendimentos_ELETIVOS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=234456311
version: 115
---

# Adaptação Atendimentos ELETIVOS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Painel de Atendimentos Eletivos |  |  | | --- | | **Rotina(s) envolvida(s)** | | Painel de Classificação de Riscos | | Registro de Atendimentos Externos | | Cadastro de Unidades de Atendimento | | Agenda de Atendimentos | |
| **Requisito (ISSUE):** | [PCREQ-10197](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10197 "PCREQ-10197") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL, Oracle |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Esta implementação tem como objetivo disponibilizar para o usuário a funcionalidade "**Painel de Atendimentos Eletivos**".

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):  
   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.10 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.10.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.10

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse **Cadastros / Uso Geral / Unidades de Atendimento**, selecione uma unidade de atendimento cuja classificação Default de atendimentos seja "**Eletivo**" e marque a opção **Inclui Atendimentos Eletivos no Painel**.
2. Acesse **Atendimento / Pronto Atendimento / Painel de Atendimentos Eletivos.**
3. Selecione a unidade de atendimento e acesse a aba **Plantão**.
4. Na grid inferior, cadastre uma nova especialidade para a unidade de atendimento.
5. Na grid superior, clique no botão "**+**" e inclua um novo plantão.
6. Acesse o menu **Cadastros / Registro e Controle / Totem**.
7. Inclua um Totem para a unidade de atendimento desejada.

## Procedimento para Utilização

1. Acesse o menu **Atendimento / Agendamento / Agenda de Atendimentos**.
2. Efetue os agendamentos desejados.
3. Acesse o menu **Atendimento / Pronto Atendimento / Ambulatório / Totem de Pronto Atendimento** e abra o totem cadastrado.
4. Clique na unidade cadastrada e a Especialidade do plantão cadastrado.
5. Imprima algumas senhas.
6. Acesse o menu **Atendimento / Pronto Atendimento / Ambulatório / Painel de Atendimentos Eletivos**.
7. Selecione a unidade para a qual as senhas foram impressas e acesse a aba "**Registro de Atendimento**".
8. Clique no botão **Chamar**, e confirme o início do registro do atendimento. A tela da Agenda abrirá.
9. Selecione o agendamento realizado, indo até a agenda desejada, ou clicando no botão **Pesquisar** e buscando pelo paciente agendado.
10. Com o agendamento selecionado, clique no botão "**Atendimento Externo**".
11. Registre o atendimento externo. Após isso o atendimento passará para a aba "**Registro de Triagem**", ou "**Atendimento Médico**", dependendo das opções marcadas no cadastro da especialidade.
12. Acesse a aba correspondente, conforme parametrizado, selecione o registro desejado e clique em  "**Chamar**".
13. No caso de Classificação de Risco, preencha as informações necessárias e clique em "**Salvar**". O registro aparecerá na aba atendimento médico.
14. Entre no sistema com o usuário médico responsável pelo atendimento.
15. Dê um duplo clique sobre o registro desejado e clique em "**Chamar**".
16. Confirme a finalização do atendimento.

divs
