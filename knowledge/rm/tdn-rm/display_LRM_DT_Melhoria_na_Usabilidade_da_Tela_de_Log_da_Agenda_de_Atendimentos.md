---
content_hash: 020a727592f9b1ddf7ea02d4ca5bc4e8b160f432494edc715409adca5583451d
fetched_at: '2026-06-29T00:08:07.770258+00:00'
page_id: '237389135'
product: rm
source: tdn-rm
title: DT_Melhoria_na_Usabilidade_da_Tela_de_Log_da_Agenda_de_Atendimentos
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Melhoria_na_Usabilidade_da_Tela_de_Log_da_Agenda_de_Atendimentos
version: 118
---

# Melhoria na Usabilidade da Tela de Log da Agenda de Atendimentos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Log da Agenda de Atendimentos |  |  | | --- | | **Rotina envolvida** | | Agenda de Atendimentos | |
| **Requisito (ISSUE):** | PCREQ-10898 |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL Server®, Oracle®. |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Melhoria na usabilidade da tela de log da Agenda de Atendimentos, alterada a grid utilizada pela grid padrão dos produtos da Linha RM.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.11 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.11.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:

   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).

   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros:

   a. Linha: RM

   b. Versão: RM 12.1.11

   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.

**Importante**: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

## Procedimento para Utilização

1. Acesse o menu **Atendimento / Agendamento / Agenda de Atendimentos** e selecione uma agenda qualquer em uma data que contenha agendamentos.
2. Clique no ícone  (no centro da tela). A tela do log de agendamentos, com a nova grid abrirá.
3. Verifique se os controles da grid estão se comportando adequadamente.

divs
