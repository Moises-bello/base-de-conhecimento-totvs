---
content_hash: 42ca1d19893d7948dc64d06312b89ee24673da2e4f8558b50ea863909ed94661
fetched_at: '2026-06-29T00:08:36.882530+00:00'
page_id: '284480491'
product: rm
source: tdn-rm
title: DT Vínculo de Unidades de Atendimento com Produto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284480491
version: 103
---

# Disponibilizar a opção de Vincular Unidade de Atendimento - Cadastro de Produtos/Informações do TOTVS Saúde

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Prontuário Eletrônico/Prescrição Médica | SadProntuarioEletronico.pas | | Movimentação de Estoque | SadMovEstoque.pas | | Elaboração de Contas | PSAFT001.pas |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Produto - Informações RM Saúde | SauPRDAction | |
| **Cadastros Iniciais:** | Cadastros -> Estoques / Produto / Anexo: Produto - Informações RM Saúde: Vincular unidades de atendimento a um produto |
| **Parâmetro(s):** | *Opções -> Parâmetros / Parâmetros Gerais - aba Estoques: "Filtra Produtos por Unidade de Atendimento"* |
| **Tickets relacionados** | [Ticket #866546](https://totvssuporte.zendesk.com/agent/tickets/866546 "Open ticket in Zendesk Support") |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-1125 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Tabelas Utilizadas:** | SZPRDUNIDATEND |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Esta atividade foi desenvolvida com intuito de permitir o vínculo de unidades de atendimento a um produto. Dessa forma, ao realizar uma prescrição, elaborar uma conta e/ou movimentar estoque, só será possível visualizar os produtos que terão vínculo com a unidade de atendimento em questão.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados, bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

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

1. Acesse **Opções / Parâmetros / Parâmetros Gerais**, aba Estoques.
2. Marque o parâmetro *“Filtra Produtos por Unidade de Atendimento”.*
3. Acesse **Cadastros / Estoques / Produto**. Selecione um produto para configurar as unidades de atendimento.
4. Acesse **Anexos: Informações – TOTVS Saúde.** Na aba *“Unidades de Atendimento vinculadas ao produto”,* configure as unidades que poderão utilizar o produto em questão.
5. Acesse o Prontuário Eletrônico e selecione um paciente.
6. Acesse a aba Prescrição Médica e realize uma Nova Prescrição.
7. Pesquise um item pela Pesquisa direta.
8. **Resultado com o parâmetro marcado:**
9. **Resultado com o parâmetro desmarcado:**
10. O filtro também será aplicado para as opções de materiais e medicamentos abaixo:
11. Acesse **Estoques / Movimentação de Estoque.** Selecione a prescrição realizada ou crie uma nova movimentação qualquer.
12. Clique em Incluir e pressione TAB para que a tela de pesquisa de produtos seja mostrada. Pesquise um dos itens parametrizados.
13. **Resultado com o parâmetro marcado**
14. **Resultado com o parâmetro desmarcado**
15. Este filtro também funcionará para a **Elaboração de Contas,**na aba *MatMed.*

divs
