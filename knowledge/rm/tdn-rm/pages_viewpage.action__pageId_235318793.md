---
content_hash: 2fef7106d496f8fa95c44f47d47e43f89d97e8ab9c861b1785947e0e51880157
fetched_at: '2026-06-29T00:06:30.297666+00:00'
page_id: '235318793'
product: rm
source: tdn-rm
title: DT_Inteligência_na_Gestão_de_Filas_do_Pronto_Socorro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235318793
version: 117
---

# Inteligência na Gestão de Filas do Pronto Socorro

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Painel de Classificação de Riscos. |  |  | | --- | | **Rotina(s) envolvida(s)** | | Cadastro e Parametrização de Riscos | |
| **Requisito (ISSUE):** | [PCREQ-9985](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-9985 "PCREQ-9985") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL, Oracle |
| **Tabelas Utilizadas:** | SZGESTAOFILAATEND |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

   Esta implementação tem como objetivo alterar o funcionamento da gestão das filas de atendimento, para que o sistema valide a parametrização referente à quantidade de pacientes que serão chamados para cada diferente classificação.

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

1. Acesse o menu **Opções / Parâmetros / Parâmetros Gerais**, na aba **Classificação de Riscos** e verifique o parâmetro “**Utiliza registro de atendimento ANTES da classificação de risco**”.
2. Este parâmetro determinará o fluxo que o Painel de Classificação de Riscos seguirá. Caso ele esteja marcado, o fluxo começará na aba **Registro de Atendimento**, caso contrário na aba **Registro de Triagem**.
3. Acesse o menu **Cadastros / Registro e Controle / Toten**.
4. Configure um totem qualquer com uma unidade que realize atendimentos externos de urgência.
5. Acesse o menu **Atendimento / Pronto Atendimento/Ambulatório / Painel de Classificação de Riscos**.
6. Acesse a aba **Plantão** e configure um plantão na mesma unidade de atendimento parametrizada para o totem, incluindo o médico e a especialidade desejados.
7. Acesse o menu **Cadastros / Uso Geral / Classificação de Risco / Cadastro e Parametrização de Riscos**.
8. Selecione um dos itens e clique em **Anexos / Critérios de Chamada de Atendimento**.
9. Este cadastro permitirá informar a quantidade de pacientes que serão chamados em uma determinada classificação, antes que um paciente de uma classificação inferior seja chamado.
10. Realize esta parametrização para todas as classificações existentes.

## Procedimento para Utilização

1. Acesse o menu **Atendimento / Pronto Atendimento/Ambulatório / Totem de Pronto Atendimento**.
2. Selecione o Totem configurado e gere algumas senhas para a unidade de atendimento configurada.
3. Acesse novamente o menu **Atendimento / Pronto Atendimento/Ambulatório / Painel de Classificação de Riscos**.
4. Selecione a unidade de atendimento configurada e navegue até a aba **Registro de Atendimento** ou **Registro de Triagem**, dependendo da parametrização realizada no início deste documento.
5. Para que o teste possa ser realizado considerando todas as diferentes classificações, chame um número de senhas maior que o número parametrizado para as classificações, selecionando as classificações desejadas para cada senha, na aba registro de triagem, informando também o médico do plantão.
6. Entre no sistema com o médico configurado no plantão, acesse novamente o Painel de Classificação de Riscos e chame 9 senhas, através do botão chamar da aba “Atendimento Médico”.
7. Considerando a fila acima, e que foi configurada a quantidade 2 para cada classificação nesta unidade de atendimento, a ordem de chamada das 9 primeiras senhas deve ser a seguinte.

divs
