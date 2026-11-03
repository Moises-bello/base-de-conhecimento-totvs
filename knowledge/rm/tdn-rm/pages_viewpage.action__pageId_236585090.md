---
content_hash: 274f1b994b120a8e612a3c8f50e6e9ef982ac05036216bcee0166b1ff0fb0bdc
fetched_at: '2026-06-29T00:08:06.136632+00:00'
page_id: '236585090'
product: rm
source: tdn-rm
title: DT_Utilitário_Exportação_Dados_Prontuário_Eletrônico_do_Paciente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=236585090
version: 114
---

# Utilitário de Exportação de Dados do Prontuário RM para a Central de Documentos Prontuário Eletrônico do Paciente (PEP 2.0)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Utilitários | Utilitário de exportação de dados do PEP RM para a central de documentos | |
| **Requisito (ISSUE):** | PCREQ-10857 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server®, Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementado utilitário para exportação dos dados do Prontuário da linha RM através do RM Reports para a central de documentos do Prontuário Eletrônico do Paciente (PEP 2.0).

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

1. Acesse o menu **Utilitários/Utilitários do RM Saúde/Assistente de exportação de dados para a Central de Documentos** (PEP 2.0).
2. Leia as orientações.
3. Selecione o tipo de relatório, o relatório e informe o nome da pasta de armazenamento na **Central de Documento**. Clique em **Avançar** e o sistema gerará os relatórios para todos os pacientes da base de dados.
4. Verifique o documento na central de documento do Prontuário Eletrônico do Paciente.

divs
