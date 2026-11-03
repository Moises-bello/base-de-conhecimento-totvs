---
content_hash: 1b23908330bcbc99eb4516e22863a2e20043bd675e97e88cbde83f3af75abd5a
fetched_at: '2026-06-29T00:08:20.986279+00:00'
page_id: '268800590'
product: rm
source: tdn-rm
title: DT_Informações_SZLOGATENDIMENTO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268800590
version: 114
---

# Informações SZLOGATENDIMENTO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Painel de Classificação de Risco | |
| **Requisito (ISSUE):** | SAUHRM02-71 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada geração de novas informações na tabela SZLOGATENDIMENTO.

* Gravar o codpaciente, codatendimento na tabela SZLOGATENDIMENTO nas fases Inicio da Triagem e Término da Triagem quando a triagem for feita após o registro de atendimento.
* Gravar a Data/Hora atual (ServerNow) caso qrypfhd0024.FieldByName('DATASENHAATENDIMENTO').Value venha nulo em PSARC023 => BTNGravaClick no status "Paciente gerou nova senha de Atendimento".

Essa informações serão necessárias para elaboração de relatórios estatísticos para controle da rotina de Classificação de Risco.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.14 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.14.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.14

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Gere senha de atendimento em **Atendimento / Pronto Atendimento/Ambulatório/ Toten de Pronto Atendimento.**
2. Acesse o ícone  do **Painel de Classificação de Risco.**
3. Na aba **Registro de Atendimento**, dê duplo clique na senha a ser chamada para criação do registro de atendimento.
4. Para efetuar o registro de Triagem, acesse a aba **Registro de Triagem** e dê duplo clique na senha a ser chamada para Triagem.
5. Preencha os dados de triagem.

divs
