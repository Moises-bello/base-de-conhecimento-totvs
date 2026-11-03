---
content_hash: b935d59bee1eb0b298edd534518c9ce92942e0f23efb47c554ae33fbc48607db
fetched_at: '2026-06-29T00:08:07.703725+00:00'
page_id: '237385093'
product: rm
source: tdn-rm
title: DT_Prontuário_Alerta_Exames_Liberados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=237385093
version: 125
---

# Alerta de Exame com Status Liberado

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Prontuário Eletrônico do Paciente | |
| **Requisito (ISSUE):** | [PCREQ-9998](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-9998 "PCREQ-9998") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server®, Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementado alerta na tela do Prontuário Eletrônico do Paciente (PEP), quando há exame com status "**Liberado**" cujo médico solicitante seja aquele vinculado ao usuário logado no sistema.

Ao clicar no alerta, é exibida tela com todos os exames "Liberados" para que o usuário selecione um dos registros e seja carregado no Prontuário Eletrônico do Paciente o registro do paciente.

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

1. Ao abrir o **Prontuário Eletrônico do Paciente**, caso exista algum exame com status "Liberado", cujo médico solicitante seja aquele vinculado ao usuário logado no sistema, será exibido um alerta, conforme destacado na imagem.
2. Ao clicar no alerta, será exibida uma tela com a lista de todos os exames com status "**Liberado**".
3. Selecione o exame e clique em **OK**, serão carregados os dados do paciente no Prontuário Eletrônico.

divs
