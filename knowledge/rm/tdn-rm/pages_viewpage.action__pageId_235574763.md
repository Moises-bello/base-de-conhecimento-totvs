---
content_hash: 2a4c9805eab6591850ff8ce11333d7c17685134d4b8dfe0b1e3bc0c6b34a6117
fetched_at: '2026-06-29T00:08:04.559212+00:00'
page_id: '235574763'
product: rm
source: tdn-rm
title: DT_Fluxo_Medicamento_de_Uso_Comum/Medicamento_Uso_Individual/Medicamento_do_Paciente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235574763
version: 114
---

# Fluxo PEP 2 - Medicamento de Uso Comum/Medicamento Uso Individual/Medicamento do Paciente

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Integração Prontuário Eletrônico do Paciente (PEP 2) & TOTVS Gestão Hospitalar |  |  | | --- | | **Rotina(s) envolvida(s)** | | Registro de Atendimento | | Prontuário Eletrônico | |
| **Requisito (ISSUE):** | [PCREQ-10754](http://jira.totvs.com.br/browse/PCREQ-10754) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MSSQL®/Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Esta implementação tem como objetivo garantir o funcionamento da integração entre Prontuário Eletrônico do Paciente (PEP 2.0) e o TOTVS Gestão Hospitalar (RM Saúde), durante a Checagem de Medicamentos e Liberação de Aprazamento.

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

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse o menu **Cadastros/Cuidados com o Paciente/Prescrição Médica/Padrões de Prescrição**.
2. Caso já exista algum medicamento configurado, valide se na aba **Anexos/Padrão de Prescrição**existe configuração.
3. Caso não esteja configurado, realize a configuração para o medicamento desejado.
4. Acesse o menu **Cadastros/Estoques/Produto** e busque pelo Produto recém configurado.
5. Acesse o menu **Anexos/Anexos/Informações - TOTVS Saúde**.
6. Na aba **Identificação**,marque as opções ******Item fracionado de uso individual que é faturado na checagem******e ******Item de uso coletivo que é faturado somente na checagem******.

## Procedimento para Utilização

1. No **TOTVS Gestão Hospitalar**, acesse o menu **Atendimento/Pronto Atendimento / Ambulatório/Registro de Atendimentos Externos**e registre um novo atendimento em alguma unidade de atendimento que esteja configurada para utilização no **Prontuário Eletrônico do Paciente** (PEP 2).
2. Acesse o **Prontuário Eletrônico do Paciente** (PEP 2) na mesma Unidade de Atendimento na qual o novo atendimento foi inserido.
3. Acesse a aba **Evolução Médica** e insira uma nova Evolução.
4. Acesse a aba **Prescrição Médica** e lance uma nova prescrição com o medicamento configurado.
5. Clique em **Liberar Prescrição**. A prescrição será incluída na aba **Planejamento Terapêutico**.
6. Acesse a aba **Planejamento Terapêutico** e clique em **Liberar Aprazamento**. Neste momento, caso esteja corretamente configurado, o **Prontuário Eletrônico do Paciente** (PEP 2) efetuará a checagem de todos os itens que foram aprazados.
7. Acesse novamente o **TOTVS Gestão Hospitalar** (RM Saúde**)** e verifique a conta do paciente. Caso o medicamento lançado seja um **Item fracionado de uso individual que é faturado na checagem** ou **Item de uso coletivo que é faturado somente na checagem**, o sistema terá lançado o item na conta do paciente.
8. Acesse novamente o **Prontuário Eletrônico do Paciente** (PEP 2) e acesse a aba **Planejamento Terapêutico,** no atendimento do mesmo paciente.
9. Clique sobre um dos aprazamentos que estão com o ícone  e clique em **Desfazer Checagem**.
10. Informe a justificativa e acesse novamente a conta do paciente, no **TOTVS Gestão Hospitalar** (RM Saúde). O sistema deverá ter realizado o estorno do item.

divs
