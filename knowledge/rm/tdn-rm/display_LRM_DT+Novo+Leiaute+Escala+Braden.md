---
content_hash: d5ee6d470de230b67fbd4587b64bde02a8eab1f2a4aa5a3a431b493981bfa5ac
fetched_at: '2026-06-29T00:08:38.347128+00:00'
page_id: '285648792'
product: rm
source: tdn-rm
title: DT Novo Leiaute Escala Braden
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Novo+Leiaute+Escala+Braden
version: 102
---

# Novo Leiaute Escala Braden

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Prontuário Eletrônico/Enfermagem Aba Scores, sub aba Escala Braden | |
| **Tickets relacionados** | [Ticket #197604](https://totvssuporte.zendesk.com/agent/tickets/197604 "Open ticket in Zendesk Support") |
| **Requisito****:** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-1211 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® e Oracle® |
| **Tabelas Utilizadas:** | SZBRADEN |
| **Sistema Operacional:** | Windows® |

## Descrição

Realizadas alterações no leiaute da escala de Braden no Prontuário, com novas descrições, inclusão da opção Excelente em Nutrição e alteração do campo Total para Classificação.

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

1. Acesse **Prontuário**.
2. Selecione um paciente cadastrado, clique em **OK***.*
3. Acesse a aba Enfermagem/ Scores/ Escala de Braden.
4. Clique no botão **Adicionar** (+).
5. Verifique as alterações na imagem abaixo.
6. Para salvar o preenchimento, clique em **OK**.

divs
