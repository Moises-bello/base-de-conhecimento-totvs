---
content_hash: 8370a001b87eabc67482be5e51e5155c387f79a10f2a15c6c66b8a2e80dd1e17
fetched_at: '2026-06-29T00:08:09.265662+00:00'
page_id: '239032184'
product: rm
source: tdn-rm
title: DT_Tag_Controle_Acesso
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Tag_Controle_Acesso
version: 115
---

# Tag Controle de Acesso

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotinas** | | Lançamentos na Conta do Paciente | | Registro de Atendimentos Externos | | Registro de Internações | |
| **Cadastros Iniciais:** | Perfil / Parâmetros RM Saúde |
| **Parâmetro(s):** | Altera data de um atendimento Externo  Altera data de um atendimento Interno |
| **Requisito:** | RHRM01-46 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle®/ SQL Server® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementação do controle de acesso na Elaboração de Contas, página "Especial". Ao restringir acesso à determinadas páginas da Elaboração de Contas, o sistema passa a desabilitar o lançamento delas na página "Especial". Foi implementado também o controle da permissão da alteração da data de entrada após o registro do atendimento.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.12 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.12.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.12

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse o menu **Cadastros/Segurança/Perfil/ Parâmetros RM Saúde** e marque as opções**"Altera data de um atendimento Externo"** e **"Altera data de um atendimento Interno"**.

## Procedimento para Utilização

1. Acesse**Tesouraria/Lançamentos na Conta do Paciente**.

           Na aba **Especial**, os tipos de Lançamento que devem estar habilitados são de acordo com a permissão de cada uma das demais abas.

2. Acesse **Atendimento/Pronto Atendimento/Ambulatório/ Registro de Atendimentos Externos** e verifique se está habilitada ou desabilitada a alteração da data de atendimento em um registro existente.

3. Acesse **Atendimento/ Internação / Registro de Internações**e verifique se está habilitada ou desabilitada a alteração da data de atendimento em um registro existente.

divs
