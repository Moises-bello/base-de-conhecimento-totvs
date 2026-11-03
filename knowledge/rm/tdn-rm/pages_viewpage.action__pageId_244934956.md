---
content_hash: 444c4cb6a9eae94a5336832806868da2ef9ae7b938216f1a6f74ffe79d491906
fetched_at: '2026-06-29T00:08:16.277663+00:00'
page_id: '244934956'
product: rm
source: tdn-rm
title: DT_Ação_na_Interação_Medicamentosa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244934956
version: 110
---

# Ação na Interação Medicamentosa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Interação Medicamentosa | |
| **Requisito (ISSUE):** | SAUHRM01-662 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® |
| **Tabelas Utilizadas:** | SZCADINTMED |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Alteração dos labels "**Classificação de Risco**" e "**Observação**" para "**Classificação de Risco / Nível de Interação**" e "**Observação / Risco**", implementado o campo "**Ação**" na tela de **Interações Medicamentosas**.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.13 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.13.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.13

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Acesse o menu **Cuidados com o Paciente / Prescrição Médica / Interações Medicamentosas**.
2. Selecione um registro e acesse a tela de edição dele. Verifique os labels dos campos “**Classificação de Risco / Nível de Interação**” e “**Observação / Risco**” aparecem com o novo texto, e o campo de “**Ação**” está disponível na tela.
3. Na tela de listagem, a coluna "**Ação**" já está devidamente configurada.

divs
