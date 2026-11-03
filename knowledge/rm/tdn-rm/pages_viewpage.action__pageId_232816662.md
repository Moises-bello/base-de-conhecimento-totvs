---
content_hash: 5986f58b92047340f07ad2870822b8662ff276cf78d24c34421ebc7c43f66483
fetched_at: '2026-06-29T00:06:27.231054+00:00'
page_id: '232816662'
product: rm
source: tdn-rm
title: DT_Gestão_de_Entrega_da_2ª_Via_de_Laudo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=232816662
version: 123
---

# Gestão de Entrega da 2ª Via de Laudo

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | Rotina | | Controle de Pedidos de Exames | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL, Oracle |
| **Tabelas Utilizadas:** | SZHISTORICOSTATUS |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Esta implementação tem como objetivo possibilitar ao usuário, a visualização do responsável pelo recebimento de um exame.

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
2. Selecione um pedido de exames qualquer e abra a edição do registro.
3. Avance até emitir o Resultado.
4. Selecione a ação “**Entregar Exame**” e clique em **Salvar**.
5. Preencha o nome do **Responsável pela Retirada** do Exame e clique em **OK**.
6. Acesse a aba **Histórico de Controle** e clique sobre o registro de Entrega do Exame. O Nome da pessoa que retirou o Exame será exibido.
7. Selecione a ação “**Cancelar Entrega de Exame**” e clique em **Salvar.**
8. Neste momento é possível emitir a segunda via do Exame, através da ação **Reemitir Exame**.
9. Selecione novamente a ação “**Entregar Exame**” e clique em **Salvar**.
10. Preencha novamente o nome do **Responsável pelo** **Recebimento** e cliqueem **OK**.
11. Acesse novamente a aba “**Histórico de Controle**”, clique sobre o registro e verifique:

divs
