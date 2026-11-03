---
content_hash: 6379094d4aafa1bbbf75562a0a06e4383d30397ca6f5702a3e4a4756bc0578cc
fetched_at: '2026-06-29T00:08:41.325976+00:00'
page_id: '286720509'
product: rm
source: tdn-rm
title: DT Histórico Alteração de Boletos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286720509
version: 8
---

# HISTÓRICO DE ALTERAÇÕES NO BOLETO

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| **Segmento Executor:** | Construção e Projetos. | | |
| **Módulo:** | Totvs Gestão Financeira. | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Boletos.* | *Histórico de Boletos.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Baixa | Baixa de lançamentos. | | Código de Barras | Geração de código de barras | | Nosso número | Geração de nosso número | | Parametrização | Parametrização do Financeiro | | Remessa | Remessa bancária | | Retorno | Retorno bancário | | Registro online | Registro online de boletos | | Desconto duplicata | Efetivação de desconto de duplicatas | | Lançamento | Processo de alteração de cliente/forncedor de lançamento | | | |
| **Requisito/Story/Issue:** | FINANCEIRO01-1883*.* | | |
| **País:** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

### Objetivo

Gravar registro de histórico de alteração de boletos. Toda alteração de um registro na tabela de boletos deve gerar um novo registro que conterá a cópia dos dados após a execução do processo.

## Definição da Regra de Negócio

Os processos do Totvs Gestão Financeira que alteram dados do boleto devem chamar o serviço para inclusão do histórico do mesmo após a execução do processo. A tabela FBOLETOHISTORICO contém todos os campos existentes na tabela de boleto (FBOLETO) além de um campo, de nome *Origem da Gravação*, que indica qual processo chamou a alteração, que pode ser:

* Efetivação Desconto Duplicata
* Alteração do boleto via interface
* Alteração Conta Caixa e Convênio do boleto
* Alteração Lançamento financeiro
* Alteração Vencimento do boleto
* Cancelamento Acordo de lançamentos do Educacional
* Cancelamento Baixa
* Cancelamento Remessa de boleto
* Cancelamento Boleto
* Exclusão Lançamento do Boleto
* Geração Código de Barras via fórmula (função de fórmula CODBARRABOLETO ou CODBARRABOLETODATA)
* Geração IPTE via fórmula (função de fórmula , IPTEBOLETO ou IPTEBOLETODATA)
* Geração Nosso Número
* Inclusão Baixa
* Inclusão de lançamento em Boleto
* Parametrização Financeiro: ocorre ao alterar o parâmetro "Usar dados bancários global do Cli/For" no parametrizador do Financeiro**.**
* Processo Alteração Cli/For Lançamento (chamdo pelo Totvs Processo Seletivo)
* Registro Online
* Remessa de boleto
* Retorno Bancário
* Portal TIN.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parametrizador Financeiro | Alteração | Ambiente -> Parâmetros -> Totvs Gestão Financeira | - |
| Execução de Fórmulas | Envolvida |  | Execução de fórmula com uma das seguintes função de fórmula CODBARRABOLETO, CODBARRABOLETODATA, IPTEBOLETO, IPTEBOLETODATA. |
| Inclusãlo de lançamento ao boleto | Alteração | Contas a Pagar / Receber -> Lançamentos -> Processos -> Boleto | - |
| Desvincular lançamento do boleto | Alteração | Contas a Pagar / Receber -> Lançamentos -> Processos -> Boleto |  |
| Cancelamento de boleto | Alteração | Contas a Pagar / Receber -> Boleto-> Processos |  |
| Alterar Conta Caixa e Convênio | Alteração | Contas a Pagar / Receber -> Boleto-> Processos -> Manutenção de Boletos |  |
| Alterar Data de Vencimento | Alteração | Contas a Pagar / Receber -> Boleto-> Processos -> Manutenção de Boletos |  |
| Geração Nosso Número | Envolvida |  |  |
| Remover Código de Barras | Alteração | Contas a Pagar / Receber -> Boleto-> Processos |  |
| Registro Online | Envolvida |  | O registro online altera os dados do boleto. |
| Alteração de lançamento | Alteração | Contas a Pagar / Receber -> Lançamentos |  |
| Baixar lançamento | Alteração | Contas a Pagar / Receber -> Lançamentos -> Processos -> Baixa |  |
| Cancelamento de baixa | Alteração | Contas a Pagar / Receber -> Lançamentos -> Processos -> Baixa |  |
| Remessa | Alteração | Movimentações Bancárias -> Cadastro Bancário |  |
| Cancelamento de Remessa | Alteração | Contas a Pagar / Receber -> Lançamentos -> Processos |  |
| Retorno Bancário | Alteração | Movimentações Bancárias -> Retorno Bancário |  |
| Cancelar Acordo | Alteração | Contas a Pagar / Receber -> Acordo -> Gerenciar Acordo -> Processos |  |
| Efetivar Desconto de duplicata | Alteração | Contas a Pagar / Receber -> Lançamentos -> Processos -> Duplicatas |  |
| Processo Seletivo | Envolvido |  | Alteração de cliente/fornecedor de lançamento altera os dados do boleto vinculado. |

Criado anexo ***Histórico de Alterações*** na visão de boletos que irá exibir todos os registros de histórico do boleto. O mesmo tem a mesma permissão de menu do cadastro de boletos e não permite incluir, editar ou excluir registros.

O parâmetro ***Gravar Histórico de boleto ao gerar código de barras/IPTE via fórmual***(passo 02.02.02.01 do parametrizador do Totvs Gestão Financeira) deixa de existir, o histórico será sempre gravado ao ser realizada qualquer alteração no registro de boleto.

**Tabelas Utilizadas**

* FBOLETOHISTORICO– Histórico de alteração do Boleto
