---
content_hash: b0ae2d77f8635d24fca6566e2d00537247913ba9b1874a0aecfe234d8de1c995
fetched_at: '2026-06-29T00:06:24.031329+00:00'
page_id: '224110470'
product: rm
source: tdn-rm
title: DT_Farmácia_OFFLINE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224110470
version: 129
---

# Farmácia OFFLINE

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Estoque | Movimentação de Estoque | |
| **Cadastros Iniciais:** | Integração de estoque com EMS ou Protheus |
| **Requisito (ISSUE):** | [PCREQ-4656](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-4656) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | SZMOVIESTOQUE e SZMOVIESTOQUEITEM |
| **Sistema(s) Operacional(is):** | Windows |
| **Versões/Release:** | 12.1.10 |
| **Versão Expedida:** | 12.1.10 |

## Descrição

Esta implementação consiste em permitir que uma requisição seja processada mesmo que a integração do estoque com o EMS ou o Protheus esteja offline (inativa).

Para que seja permitido, deve-se habilitar um parâmetro para indicar que a conexão (integração) esteja OFFLINE.

Ao processar uma requisição no modo OFFLINE, o sistema realiza o lançamento na conta do paciente e libera o aprazamento normalmente, mas marca esta requisição, assim como seus itens, com o status de "Processado OFFLINE" para que, quando a conexão (integração) com o EMS ou Protheus seja re-estabelecida, seja possível reprocessar, realizando assim a baixa no estoque.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.9 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.9.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).
2. Faça o login, com seu E-mail e Senha.
3. Na barra de menu superior, clique em DOWNLOAD.
4. No boxe Central de Downloads aplique os filtros conforme campos abaixo:  
   1. Linha: RM
   2. Versão: RM 12.1.9
   3. Tipo: Patch

Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.  
   Importante: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Ao perceber que a integração do estoque entre RM e EMS ou Protheus esteja instável ou inativa, é necessário habilitar o parâmetro "Estoque OFFLINE" disponível em: "Ambiente/Parâmetros/Gestão Hospitalar/Integrações/Integração Backoffice/" aba "Configurações Gerais 3/5"
2. Com o parâmetro marcado, ao acessar as telas "Movimentação de estoque", "Mapa de dispensação" e suas respectivas telas de edição, será exibida uma label informando que o estoque encontra-se offline
3. Com o estoque offline, ao processar uma requisição os itens são lançados na conta e o aprazamento é liberado normalmente mas a requsição é marcada com o status "Offline" e não é realizada a baixa no estoque. A baixa só será realizada quando a integração com o EMS  ou Protheus for reativada e o usuário realizar novamente o processamento da requisição.
4. Ao tentar processar uma requisição no modo offline que já tenha sido processada, o sistema exibirá um aviso informando que só é possível processar novamente com a integração Online.
5. Quando a integração for reativada, o processamento seguirá normalmente apenas para a baixa no estoque, já que os lançamentos e aprazamentos foram liberados anteriormente.

divs
