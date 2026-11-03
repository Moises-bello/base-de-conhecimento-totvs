---
content_hash: f89b1b662c3cef7b6a665d10208633a7b1a3573e2c49f337c3598b7a3e0b3bb4
fetched_at: '2026-06-29T00:06:21.317098+00:00'
page_id: '223168383'
product: rm
source: tdn-rm
title: TTQMIC_DT_Pesquisa_Responsável_Técnico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223168383
version: 2
---

# Pesquisa por Responsável Técnico

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Totvs Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Controle de Pedidos de Exames. |  |  | | --- | | **Rotina(s) envolvida(s)** | | Liberação de Laudos. | |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL Server, Oracle. |
| **Sistema(s) Operacional(is):** | Windows. |
| **Versões/Release:** | 12.1.8. |

## Descrição

   Ajustes para melhoria de usabilidade na grid de seleção de responsáveis técnicos, no controle de pedidos de exames.

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

1. Acesse o menu **Unidades Diagnóstico \ Controle de Pedidos de Exames.**
2. Selecione um filtro que permita a visualização de um pedido que tenha laudo preenchido, ou à preencher:
3. Acesse o laudo para edição.
4. Movimente o Laudo até o status “**Liberar Após Retorno**”. Ao clicar em “**Salvar**”, o sistema exibirá a tela de seleção do responsável técnico:
5. A Grid agora encontra-se em ordem alfabética.
6. Digite o **Nome do Responsável** selecionado e verifique se a grid filtra de acordo:

divs
