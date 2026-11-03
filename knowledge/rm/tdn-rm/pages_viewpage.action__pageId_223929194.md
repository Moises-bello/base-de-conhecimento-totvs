---
content_hash: 062f1e5cdf753b5f13157f018944c9e48d114c02a038dc7f79012d888e24139c
fetched_at: '2026-06-29T00:06:23.031840+00:00'
page_id: '223929194'
product: rm
source: tdn-rm
title: DT_Transferência_de_Atendimento_Externo_Para_Interno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223929194
version: 124
---

# Transferência de Atendimento Externo para Interno

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | RM Saúde |
| **Rotina:** | |  | | --- | | **Rotina** | | Atendimento |  |  | | --- | | **Rotina(s) envolvida(s)** | | Internação. | |
| **Requisito (ISSUE):** | [PCREQ-9191](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-9191 "PCREQ-9191") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL, Oracle |
| **Sistema(s) Operacional(is):** | Windows. |
| **Versões/Release:** | 12.1.9 |

## Descrição

  Esta implementação tem por objetivo a criação de um fluxo alternativo na transferência de atendimento Externo para Interno, permitindo que os itens da parcial origem sejam automaticamente copiados para a parcial destino e seu cancelamento realizado.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):  
   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.9 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.9.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.9

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse o menu "**Opções / Parâmetros / Parâmetros Gerais / Registro de Atendimento**" e marque o checkbox  "**Cancela Primeira Parcial ao Mudar o Tipo de Atendimento**".

## Procedimento para Utilização

1. Acesse o menu "**Opções / Parâmetros / Parâmetros Gerais / Registro de Atendimento**" e marque o checkbox "**Cancela Primeira Parcial ao Mudar o Tipo de Atendimento**".
2. Registre um novo atendimento externo.
3. Acesse a **Elaboração de Contas** para o atendimento e inserir alguns itens, como MatMed, Diagnose e Terapia, Taxas, Etc.
4. Acesse o menu "**Atendimento / Internação / Transferência de Externo para Interno**" e selecione o atendimento externo criado.
5. Preencha todos os dados obrigatórios para o registro do atendimento interno e registre o atendimento.
6. Acesse novamente a elaboração de contas (**Ctrl+L**) e verifique as parciais. A primeira parcial estará cancelada e vazia, enquanto a segunda parcial deverá conter todos os itens de débito da conta.
8. O log dessa transação será salvo na tabela "**SZLOGATENDIMENTO**", com o tipo **15** (quando a transferência for de Interno para Externo, o tipo será o 14).

divs
