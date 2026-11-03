---
content_hash: b2bad02d8f97b5083b7cdababd05065d335056f676899da300fe36f6f0b00105
fetched_at: '2026-06-29T00:08:56.923135+00:00'
page_id: '351386151'
product: rm
source: tdn-rm
title: DT Bloco K - Gerar SPED Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=351386151
version: 8
---

# Processo de geração de SPED Contábil

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Gestão Contábil*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | SPED Contábil | CtbSpedContabilProcessAction | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A.* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [CONTROLADORIA01-1204](http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-1204);[CONTROLADORIA01-1279](http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-1279);[CONTROLADORIA01-1280](http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-1280);[CONTROLADORIA01-1283](http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-1283) |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *SQLSever / Oracle* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *Windows.* |

## Descrição

Para possibilitar a geração do Bloco K foi disponibilizado o campo Plano Consolidado - Bloco K.

**SPED Contábil**

O processo de geração do SPED Contábil, existente na aba obrigações acessórias, recebeu o campo Plano Consolidado - Bloco K. Ele irá listar todos os planos de contas paralelos, existentes na coligada corrente, cuja "Instituição Responsável / Finalidade" seja  "Bloco K - Plano de Contas Consolidado".

O campo Plano Referencial também foi alterado para exibir somente os planos de conta paralelos, existentes na coligada corrente, cuja "Instituição Responsável / Finalidade" seja diferente de "Bloco K - Plano de Contas Consolidado".

**Registro K100**

O SPED Contábil foi alterado para gerar o registro K100, que identifica as empresas que fazem parte da escrituração contábil consolidada. Para gerá-lo é necessário incluir, no cadastro de controladas, as coligadas controladas pelo coligada corrente.

**Registro K200**

O SPED Contábil foi alterado para gerar o registro K200, que apresenta o plano de contas utilizado nas escriturações contábeis consolidadas.

**Registro K210**

O SPED Contábil foi alterado para gerar o registro K210, apresenta o mapeamento das contas do plano de contas consolidado informado no registro K200 para as contas dos planos de contas das empresas consolidadas.

**Registro K300**

O SPED Contábil foi alterado para gerar o registro K300, que apresenta o saldo das contas consolidadas.

**Registro K310**

O SPED Contábil foi alterado para gerar o registro K300, que apresenta as empresas detentoras das parcelas do valor eliminado total, com os respectivos valores eliminados.

**Registro K315**

O SPED Contábil foi alterado para gerar o registro K300, que apresenta as empresas contrapartes das parcelas do valor eliminado total, com os respectivos valores eliminados.

Obs: Controladas inativas não irão participar do cálculo ou da composição dos registros citados anteriormente.
