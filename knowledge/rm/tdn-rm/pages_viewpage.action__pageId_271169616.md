---
content_hash: a10e2d3479448e8247dbd226b5a28438f91349f8640495d434183e7f17c212d1
fetched_at: '2026-06-29T00:08:26.250764+00:00'
page_id: '271169616'
product: rm
source: tdn-rm
title: DT Histórico de Atualização do Laudo de imagem
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271169616
version: 5
---

# Histórico de Atualização do Laudo de Imagem

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Nome Técnico** | | Controle de Pedido de Exames | |
| **Cadastros Iniciais:** | Relacione os cadastros necessários que precisam ser preenchidos antes da utilização desse requisito. |
| **Requisito (informe o requisito relacionado):** | SAUHRM02-332 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle® e SQL Server® |
| **Tabelas Utilizadas:** | SZPEDEXAMERESULTMODLOG |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Esta funcionalidade tem o objetivo de manter todo o histórico das alterações no laudo de exames de imagem.

Somente a partir desta versão é que o histórico passará a ser salvo.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.15 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.15.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em "DOWNLOAD".

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM;

   b. Versão: RM 12.1.15;

   c. Tipo: Patch.

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Criar o pedido de exame de diagnóstico de imagem.
2. Acessar o Menu "**Unidades Diagnósticos -> Controle de Pedido de Exames**".
3. Selecione um exame de imagem. Para acessar o histórico das alterações do laudo, clique no botão em destaque na imagem abaixo.
4. Dar um duplo clique para preencher o laudo.
5. Ao concluir a digitação, o sistema salva o laudo na nova tabela.
6. Gravação do histórico.
7. Alteração do laudo.
8. Histórico da alteração.
