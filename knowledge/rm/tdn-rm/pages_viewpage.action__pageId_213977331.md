---
content_hash: e47d46f1cd6a754d3d7a38787fbbb02df0856d6e9f49aefe67a57dc3190d14fa
fetched_at: '2026-06-29T00:06:17.521531+00:00'
page_id: '213977331'
product: rm
source: tdn-rm
title: TTKAQM_DT_Permitir_Visualização_do_Laudo_em_Controle_de_Pedidos_de_Exames
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=213977331
version: 2
---

# Permitir Visualização do Laudo no Controle de Pedidos de Exames

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Unidade de Diagnóstico |
| **Rotina:** | |  | | --- | | **Rotina** | | Unidade de Diagnóstico |  |  | | --- | | **Rotina(s) envolvida(s)** | | Controle de Pedidos de Exames | |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | MSSQL/Oracle |
| **Sistema(s) Operacional(is):** | Windows |
| **Versões/Release:** | 12.1.8 |

## Descrição

   Implementada rotina no botão Imprimir, da tela de **Controle de Pedidos de Exames**, que permite ao usuário efetuar a visualização do Laudo, independentemente da etapa atual.

## Procedimento para Implantação

 Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):  
   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.8 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.8.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:  
   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).   
   2. Faça o login, com seu E-mail e Senha.  
   3. Na barra de menu superior, clique em DOWNLOAD.  
   4. No boxe Central de Downloads aplique os filtros conforme campos abaixo:  
   a. Linha: RM  
   b. Versão: RM 12.1.8  
   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.  
   Importante: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Acesse o menu **Unidade de Diagnóstico / Controle de Pedidos de Exames**.
2. Filtre os exames buscando por algum exame que possua modelo de laudo pré-cadastrado.
3. Acesse qualquer exame da grid.
4. Na aba **Laudo**, clique no ícone da impressora, no canto superior direito da tela.
5. Sistema realizará a impressão do laudo, independente do status atual do exame.

divs
