---
content_hash: e575022e7a719e85611fe5556622090bc6734b4225aa71a7e8df92bc9e87c2b5
fetched_at: '2026-06-29T00:08:45.630545+00:00'
page_id: '311635287'
product: rm
source: tdn-rm
title: DT Vínculo de Itens de Enfermagem x Unidades de Atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=311635287
version: 2
---

# Vínculo de Itens de Enfermagem x Unidades de Atendimento: Integração - Prontuário Eletrônico do Paciente

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Itens de Enfermagem | Cadastro de sinais vitais | |
| **Chamado****:** | [1474663](https://totvssuporte.zendesk.com/agent/tickets/1474663 "Open ticket in Zendesk Support") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Melhoria na integração entre TOTVS Gestão Hospitalar e Prontuário Eletrônico do Paciente, possibilita filtro de Sinais Vitais cadastrados pela Unidade de Atendimento selecionada.

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):

   Realize a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

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

**Exemplo:**

1. Acesse **Cadastros/Cuidados com o Paciente/Prescrição Médica/Itens de Enfermagem**.
2. Cadastre um item do tipo **Sinais Vitais**.
3. Na aba **Unidade de Atendimento**, selecione as unidades nas quais o item ficará disponível.
4. No **Prontuário Eletrônico do Paciente**, em **Registros de Enfermagem**, caso seja selecionada a mesma unidade de atendimento na qual os itens foram cadastrados, eles serão apresentados na listagem.
5. Na aleta **Prescrição Médica/Painel Rotinas**, **Cuidados, Monitorizações e Sinais Vitais**, os itens que são apresentados, são os cadastrados para aquela unidade de atendimento. Os que tem o checkbox “**Padrão**” marcado no cadastro do **TOTVS Gestão Hospitalar**, já são selecionados no **Prontuário Eletrônico do Paciente**.

No cadastro dos itens de enfermagem, é necessário informar pelo menos uma unidade de medida, clicando em **Anexos/Unidades**.
