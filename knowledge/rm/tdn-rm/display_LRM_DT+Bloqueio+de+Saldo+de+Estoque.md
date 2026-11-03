---
content_hash: 5069385db48a20822f4a138a7560a16f1accc43029c68615ff103dfb9b6cc22e
fetched_at: '2026-06-29T00:08:36.946853+00:00'
page_id: '284857770'
product: rm
source: tdn-rm
title: DT Bloqueio de Saldo de Estoque
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Bloqueio+de+Saldo+de+Estoque
version: 101
---

# Não exibir produtos que possuem saldo menor ou igual a zero no estoque

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Prontuário Eletrônico/Prescrição Médica | SadProntuarioEletronico.pas | | Movimentação de Estoque | SadMovEstoque.pas | | Elaboração de Contas | PSAFT001.pas |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Produto - Informações RM Saúde | SauPRDAaction | |
| **Parâmetro(s):** | Opções -> Parâmetros / Parâmetros Gerais - aba Estoques: *"*Não exibe produtos sem saldo no estoque*"* |
| **Tickets relacionados** | [Ticket #892201](https://totvssuporte.zendesk.com/agent/tickets/892201 "Open ticket in Zendesk Support") |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-1126 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

O objetivo desta implementação é filtrar os itens que possuem saldo zerado no estoque. Dessa forma, ao pesquisar um item, serão mostrados os itens que possuem saldo no estoque. Caso nenhum item seja retornado na pesquisa, uma mensagem será mostrada para o usuário.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realize a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.18 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.18.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.18

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Acesse **Opções / Parâmetros / Parâmetros Gerais,** aba Estoques.
2. Marque o parâmetro *“Não exibe produtos sem saldo no estoque”.*
3. Acesse o Prontuário Eletrônico e selecione um paciente.
4. Acesse a aba Prescrição Médica e realize uma Nova Prescrição.
5. Veja o exemplo abaixo:
6. Ao pesquisar um dos itens pela Pesquisa direta, apenas o item com saldo será mostrado.
7. **Resultado com o parâmetro marcado:**
8. ****Resultado com o parâmetro desmarcado:****
9. O filtro também será aplicado para as opções de materiais e medicamentos abaixo:
10. Acesse **Estoques / Movimentação de Estoque.** Selecione a prescrição realizada ou crie uma nova movimentação qualquer.
11. Clique em Incluir e pressione TAB para que a tela de pesquisa de produtos seja mostrada.
12. Veja os itens abaixo:
13. **Resultado com o parâmetro marcado**
14. **Resultado com o parâmetro desmarcado**
15. Em **Tesouraria / Lançamentos na Conta do Paciente**, aba MatMed, a mesma rotina é aplicada na pesquisa, ao ativar o parâmetro mostrado anteriormente.

divs
