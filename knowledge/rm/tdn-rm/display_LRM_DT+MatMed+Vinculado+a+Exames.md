---
content_hash: a29e97491a20f1fb7fc2d850a9d8da08ccd678a5fa2800d13430dfb82c0e726a
fetched_at: '2026-06-29T00:08:29.555671+00:00'
page_id: '272152433'
product: rm
source: tdn-rm
title: DT MatMed Vinculado a Exames
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+MatMed+Vinculado+a+Exames
version: 117
---

# MatMed Vinculado a Exames

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Exames e Serviços - Anexo MATMED associado a Exames | | Pedido de Exames | | Avaliações Complementares - Solicitação de Exames | |
| **Tickets relacionados** | 197777 |
| **Requisito****:** | SAUHRM02-592 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Tabelas Utilizadas:** | SZEXAMEMATMED – Cadastro de MatMed associado a exames  SZRELEXAMEMATMEDCONTA – relacionamento do exame e o MatMed lançados na conta do paciente  SZATENDMATMED - Lançamento de MatMed na conta do paciente  SZMOVIESTOQUEITEM - Item da requisição  SZRELEXAMEMOVIESTOQUE  - relacionamento do exame e MatMed relacionados à movimentação de estoque |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

A implementação possibilita o vinculo de exames com os materiais necessários para sua realização. No momento do vinculo, será possível optar entre requisitar os itens na farmácia, ou somente cobrar na conta do paciente na solicitação de exame.

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

1. No menu**Cadastros/Unidade de Diagnóstico/ Exames e Serviços**crie ou altere um exame ou serviço.
2. Clique em **Anexos/ Exame MatMed** para vincular o exame e os materiais.
3. No momento do vinculo, opte entre **Gera movimentação de estoque** (requisitar os itens para a  farmácia) ou **Somente lançar na conta do paciente**(cobrar na conta do paciente) na solicitação de exame e informar a quantidade do produto na mesma unidade de medida que a unidade de controle de estoque.
4. Em um mesmo exame, pode-se vincular materiais com opções distintas, conforme imagem de exemplo abaixo.
5. No menu**Unidade de Diagnóstico/Pedido de Exames Paciente Interno**crie ou edite um pedido.
6. Para os exames solicitados no pedido, os seguintes materiais foram associados.
7. Acesse **Estoques/Movimentação do Estoque**  para verificar se materiais vinculados que estão com a opção **Gera movimentação de estoque** marcada foi gerada a Movimentação de Estoque.
8. Para verificar quais itens foram lançados, acesse a aba **Itens da Movimentação**.
9. Acesse **Unidade de Diagnóstico/Lançamentos na conta do Paciente**e verifique que os materiais vinculados ao exame que estão com a opção  **Somente lança na conta do paciente**marcada, foram lançados na conta do paciente.
10. Para verificar quais itens foram lançados, acesse a aba **MatMed**.
11. Cancele alguns itens do pedido.
12. Ao cancelar um exame, os materiais com solicitação de movimentação de estoque são estornados automaticamente.
13. Ao cancelar um exame, os materiais lançados na conta do paciente são estornados automaticamente.
14. Para solicitar exames no menu **Prontuário** acesse um prontuário, clique na guia **Avaliações Complementares**, e no botão **Solicitação de Exame**.
15. Inclua exames e confirme.
16. Cancele alguns exames.
17. Ao cancelar um exame, os materiais com solicitação de movimentação de estoque são estornados automaticamente
18. Ao cancelar um exame, os materiais lançados na conta do paciente são estornados automaticamente.

divs
