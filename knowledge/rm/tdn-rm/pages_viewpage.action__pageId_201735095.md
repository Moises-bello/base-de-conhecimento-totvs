---
content_hash: a8b859cae0a83c2ad1898cd30962ced70dcc10c83dcf88c38fa0a330bfad9138
fetched_at: '2026-06-29T00:06:07.093915+00:00'
page_id: '201735095'
product: rm
source: tdn-rm
title: DT_Link_de_Exames_para_Cópia_de_Laudo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201735095
version: 10
---

# Cópia (Link) de Laudos de Exames

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Unidade de Diagnóstico |
| **Rotina:** | |  | | --- | | **Rotina** | | Link de Exames |  |  | | --- | | **Rotina(s) envolvida(s)** | | Controle de Pedidos de Exames | |
| **Chamados relacionados** | TRAYU0 |
| **Requisito (ISSUE):** | [PCREQ-6798](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-6798 "PCREQ-6798") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas utilizadas:** | SZLINKEXAMES |
| **Sistema(s) operacional(is):** | Windows |
| **Versões/Release:** | 12.1.7 |

## Descrição

   Implementada melhoria que consiste em “linkar” laudos de médicos, para que quando um laudo for digitado e salvo, o sistema realiza a cópia deste laudo para todos os outros exames que estão “linkados”.

## Procedimento para Implantação

   Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):  
   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.7 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.7.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:  
   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).   
   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros conforme campos abaixo:  
   a. Linha: RM  
   b. Versão: RM 12.1.7  
   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.  
   Importante: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Acesse o menu **Unidades Diagnóstico / Controle de Pedidos de Exames**.
2. Selecione o filtro "**Em digitação**", selecione um pedido e clique em "**Link Laudos**”, na barra superior da view.
3. Será exibida para selecionar exames, selecione mais de um exame (segure a tecla*ctrl* e clique nos exames).
4. Clique em **Relacionar**.
5. Novamente na **View**, selecione um dos exames que foram 'linkados', digite o laudo e conclua a digitação.
6. Acesse o outro exame e verifique que o laudo digitado no primeiro exame foi replicado.
