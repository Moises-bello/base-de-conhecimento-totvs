---
content_hash: b1aaf0cc09b8e1aa950b55d3958d21eda52274e99032389b1ace87e032e145bc
fetched_at: '2026-06-29T00:06:23.007472+00:00'
page_id: '223927904'
product: rm
source: tdn-rm
title: DT_Transferência_de_Atendimento_Interno_para_Externo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223927904
version: 122
---

# Transferência de Atendimento Interno para Externo

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | RM Saúde |
| **Rotina:** | |  | | --- | | **Rotina** | | Atendimento |  |  | | --- | | **Rotina(s) envolvida(s)** | | Elaboração de Contas. | |
| **Requisito (ISSUE):** | [PCREQ-9192](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-9192 "PCREQ-9192") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL, Oracle |
| **Sistema(s) Operacional(is):** | Windows. |
| **Versões/Release:** | 12.1.9 |

## Descrição

   Esta implementação tem como objetivo disponibilizar ao usuário a funcionalidade de transferência de um atendimento do tipo Interno para o tipo Externo.

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

1. Acesse o menu "**Opções / Parâmetros / Parâmetros Gerais / Registro de Atendimento**" e marque o checkbox  "**Cancela Primeira Parcial ao Mudar o Tipo de Atendimento**":

## Procedimento para Utilização

1. Registre um novo atendimento interno.
2. Acesse a **Elaboração de Contas** para o atendimento e insira alguns itens, como MatMed, Diagnose e Terapia, Taxas, entre outros.
3. Acesse o menu "**Atendimento / Pronto Atendimento / Ambulatório / Transferência de Interno para Externo**" e selecione o atendimento interno criado.
4. Preencha todos os dados obrigatórios para o registro do atendimento externo e registre o atendimento.
5. Acesse novamente a elaboração de contas (**Ctrl+L**) e verifique as parciais. A primeira parcial estará cancelada e vazia, enquanto a segunda parcial deverá conter todos os itens de débito da conta.

divs
