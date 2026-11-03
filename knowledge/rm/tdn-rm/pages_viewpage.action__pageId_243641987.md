---
content_hash: cee37b17ab6e82eb85f08f8f8aa72e0db81a9363d78c847dc7b77bbcdb5fd891
fetched_at: '2026-06-29T00:08:12.266440+00:00'
page_id: '243641987'
product: rm
source: tdn-rm
title: DT_Parametrização_de_KITs_e_Materiais_associados_por_Unidade_e_Via_de_Acesso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243641987
version: 114
---

# Parametrização de KITs e Materiais associados por Unidade e Via de acesso

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Padrão de Prescrição |  |  | | --- | | **Rotina envolvida** | | Princípio Ativo | |
| **Cadastros Iniciais:** | Princípio Ativo |
| **Requisito (ISSUE):** | SAUHRM01-76 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL®, Oracle® |
| **Tabelas Utilizadas:** | SZDOSAGEMUNIDATEND |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada a opção de adicionar uma Unidade de Atendimento à um padrão de prescrição.

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

## Procedimento para Utilização

**Exemplo:**

       1. Acesse o menu **Cadastros / Cuidados com o paciente / Prescrição Médica / Padrões de Prescrição**.

       2. Selecione um Princípio Ativo, e dentro dele, um Padrão de Prescrição.

       3.  Na tela de **Concentração**, na aba de **Padrão de Prescrição**, selecione um item, ou crie um novo.

       4. Na aba de **Unidade de Atendimento**, selecione a unidade desejada.

divs
