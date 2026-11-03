---
content_hash: 0091c665859b1fb514a4b1efb6326ab48288823d94cfab697efc0defab5a6adf
fetched_at: '2026-06-29T00:08:29.485248+00:00'
page_id: '272147151'
product: rm
source: tdn-rm
title: DT Tipos de Movimento para a CME
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Tipos+de+Movimento+para+a+CME
version: 13
---

# Tipos de Movimento para o CME

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Movimentação de Estoque |  |  | | --- | | **Rotina(s) envolvida(s)** | | Unidades CME | | Parâmetros de Integração / Parâmetros RM Nucleus | |
| **Cadastros Iniciais:** | Locais de Estoque, Produtos Esterilizáveis |
| **Parâmetro(s):** | Tipos de movimento relacionados ao CME |
| **Tickets relacionados:** | 198174 |
| **Requisito****:** | SAUHRM02-791 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server®, Oracle® |
| **Tabelas Utilizadas:** | SZMOVIESTOQUE - Movimentação de estoque  SZMOVIESTOQUEITEM - Itens da movimentação de estoque  SZCMEMOV - Movimentação do CME   ``` SZCMEHISTORICO - Histórico de movimentação dos itens ```   SZLOCALESTCME - Locais de estoque que tratam itens do CME |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

A implementação possiblita o funcionamento do módulo do Central de Material Esterilizado (CME) através de **tipos de movimento de Requisição para o CME** e o **movimento de Devolução para o CME**.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.16 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.16.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.16

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Acesse o menu **Opções / Parâmetros / Integração RM Nucleus**, página **Locais de Estoque do CME**. Neste cadastro, informe os locais de estoque que requisitarão materiais do CME. O próprio local de estoque do CME deve ser cadastrado. Somente esses locais serão exibidos nos tipos de movimento para o CME (Requisição e devolução para o CME).
2. Na página **Tipos de Mov. Estoque**, configure os dois novos tipos **Requisição para o CME** e **Devolução para o CME**. No tipo de movimento do RM Nucleus, informe o de transferência. É no tipo de transferência que a movimentação de estoque está baseada.
3. Para liberar o acesso a esses tipos de movimento, é necessário acessar o menu de segurança para definir o acesso dos perfis.
4. Acesse o menu **Cadastros / CME / Unidades CME**. Deve-se cadastrar pelo menos uma unidade cujo local de estoque definido para o Expurgo seja igual ao local de estoque para o qual as unidades solicitarão os materiais. No exemplo abaixo, o local de estoque que deverá ser selecionado na Requisição para o CME é o local CME. Se for selecionado um outro, no momento da devolução para o CME, o sistema acusará o erro de que não existe Unidade CME definida para o local de estoque selecionado.
5. Acesse o menu **Estoques / Movimentação de Estoque** e crie uma novo movimento do tipo **Requisição para o CME**.
6. Na requisição, deve-se informar o**Local de estoque do CME** e para onde os itens devem ser enviados, ou seja, de quem está requisitando. O usuário do CME é quem deve ter permissão de processar a requisição.
7. Na inclusão de itens são aceitos somente itens esterilizáveis. No cadastro do produto, informe o **Tipo de material esterilizável**. Somente itens que possuem esta informação preenchida é que serão considerados no CME.  
     
     
     
   Itens configurados como esterilizáveis:  
     
   Tentativa de incluir um item comum:  
     
   Requisição com o item esterilizável:

Saldo do item antes do processamento:

Movimentação de estoque processada:

Saldo do item após o processamento:

Movimentação  nas tabelas do CME:

Devolução  para o CME:

Processamento da devolução:

Saldo do item após o processamento da devolução:

Execução das fases de Entrada no expurgo e Conferência.

Como foram devolvidos 5 unidades, o sistema confirmou os 5 e gerou uma pendência dos outro 5.

Como foram solicitados 10 e devolvidos 5, o usuário só poderá devolver no máximo 5 unidades da próxima vez.
