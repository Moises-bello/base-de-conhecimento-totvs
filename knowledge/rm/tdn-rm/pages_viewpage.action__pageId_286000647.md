---
content_hash: 9a348e8965c1e1275e5ec86a2b21fda3a2ec06ea217e67556cf386a20ead5c9f
fetched_at: '2026-06-29T00:08:38.917335+00:00'
page_id: '286000647'
product: rm
source: tdn-rm
title: DT Restrição de Abas no Prontuário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286000647
version: 3
---

# Restrição de abas no PEP

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Cadastros/Segurança/Perfil/Selecione um perfis/Anexos/Parâmetros do RM Saúde/Restrição Abas PEP RM |  |  | | --- | | **Rotina(s) envolvida(s)** | | Prontuário Eletrônico/Prontuário Eletrônico do Paciente | |
| **Tickets relacionados** | [Ticket #875326](https://totvssuporte.zendesk.com/agent/tickets/875326 "Open ticket in Zendesk Support") |
| **Requisito:** | [SAUHRM02-1121](http://jiraproducao.totvs.com.br/browse/SAUHRM02-1121) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® e Oracle® |
| **Tabelas Utilizadas:** | SZRESTRICAOABASPEPRM |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Realizadas alterações no cadastro de perfil dos usuários do RM Saúde, para que seja possível informar quais serão as abas restritas no Prontuário do TOTVS Gestão Hospitalar.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realize a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.18 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.18.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.18

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

**Registrar Abas que serão restritas para o PEP RM**

1. Acesse **Cadastros / Segurança / Perfil**.
2. Selecione um perfil e acesse **Anexos / Parâmetros do RM Saúde.**
3. A tela de Parâmetros RM Saúde abrirá.
4. Inclua um novo registro.
5. Selecione a aba que deseja restringir o acesso e a Unidade de Atendimento.
6. Salve o Registro.
7. O registro será adicionado na tabela da aba **Restrição de Abas PEP RM**.
8. Para verificar a restrição acesse o Prontuário.
9. Note que as abas Sumário de Atendimentos e Sumário de Alta não estão mais disponíveis:
