---
content_hash: e35f6631d6a92091166b41558d94caad8e9b7ff3dca3d41e1bdc7159c6943eae
fetched_at: '2026-06-29T00:06:27.516091+00:00'
page_id: '232824033'
product: rm
source: tdn-rm
title: DT_Adequação_Visão_Controle_de_Pedidos_de_Exames
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=232824033
version: 10
---

# Adequação da Visão de Controle de Pedidos de Exames

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | Rotina | | Controle de Pedidos de Exames | |
| **Requisito (ISSUE):** | PCREQ-1000 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL, Oracle |
| **Tabelas Utilizadas:** | SZPEDEXAMEITEM |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Esta melhoria tem como objetivo adequar a visão da tela de controle de pedidos de exames, para permitir ao usuário visualizar o profissional executante relacionado à cada exame.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):  
   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.10 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.10.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.10

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Acesse o menu **Unidades Diagnóstico / Controle de Pedidos de Exames**.
2. Aplique um filtro qualquer que permita a visualização de um ou mais itens.
3. Verifique a existência da última coluna da grid (Médico Executante).
