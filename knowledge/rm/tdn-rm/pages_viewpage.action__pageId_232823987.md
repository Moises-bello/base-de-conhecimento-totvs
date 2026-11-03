---
content_hash: 08a9ad942eb820af0e5c74c9c9936ab2eeda27854d5e70115bf6316986f9ae41
fetched_at: '2026-06-29T00:06:27.510834+00:00'
page_id: '232823987'
product: rm
source: tdn-rm
title: DT_Campo_Alterar_o_Título_do_Exame
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=232823987
version: 120
---

# **Campo Alterar o Título do Exame**

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Controle de Pedidos de Exames | |
| **Requisito (ISSUE):** | PCREQ-10002 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL, Oracle |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Esta implementação tem como objetivo possibilitar ao usuário a alteração de um grupo de exames que possuam link.

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
2. Aplique um filtro que liste pelo menos um dos exames do paciente desejado.
3. Selecione o registro e clique no botão “**Link laudos**”, no cabeçalho da grid. Serão listados nesta tela, todos os itens de pedidos de exames relacionados ao paciente e que **não possuam** os seguintes status:  

   **'X' – Cancelado;**

   **'M' – Registro Médico;**

   **'T' – Execução Externa;**

   **'F' – Entrega.**
4. Selecione os Exames que deseja linkar (segurando a tecla CTRL) e clique em “**Relacionar**”. O sistema deverá solicitar o nome que será dado para o relacionamento entre os exames:  
     
   **Importante:** Este é o nome que será exibido na impressão. Caso ele não seja preenchido, cada exame terá seu nome exibido, como acontece normalmente.
5. Selecione um dos exames linkados e avance o mesmo até a etapa de emissão. Como o exame possui link, o sistema dá a opção de que o laudo todo seja replicado, portanto deve-se ter atenção às mensagens do sistema durante o processo, um exemplo é esta mensagem exibida ao passar para o Status Digitar Exame:
6. Avançar até a emissão do laudo e conferir a impressão:

divs
