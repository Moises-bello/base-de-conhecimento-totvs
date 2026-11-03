---
content_hash: 678c54a11ec7276cdfb97ce642cd714d3ebf5ae78ad0c0ffd5914a787c4de2e5
fetched_at: '2026-06-29T00:06:18.651204+00:00'
page_id: '219684846'
product: rm
source: tdn-rm
title: DT_Periodo_letivo_encerrado_geracao_lancamento
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Periodo_letivo_encerrado_geracao_lancamento
version: 2
---

# Período letivo encerrado para geração de lançamento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Geração de lançamentos | Geração de lançamentos financeiros |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Período Letivo | Cadastro de período letivo | | Parâmetros Educacionais | Cadastro de parâmetros educacionais | |
| **Cadastros Iniciais:** | Cadastro de período letivo e parâmetros educacionais por perfil de usuários, módulo Educacional. |
| **Parâmetro(s):** | Parâmetros educacionais por perfil de usuários |
| **Requisito (ISSUE):** | [PCREQ-8593](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-8593) |
| **País(es):** | Brasil |
| **Tabelas Utilizadas:** | SPLETIVO, SPARAMPERFIL |
| **Versões/Release:** | *12.1.19* |

## Descrição

Explicar a necessidade dos clientes e detalhar o comportamento do TOTVS Educacional com o novo parâmetro do cadastro do período letivo, relacionado ao processo de geração de lançamentos financeiros.

# Período letivo encerrado para geração de lançamentos

Surgiu a necessidade dos clientes do TOTVS Educacional realizarem a geração de lançamentos para contratos de períodos letivos já encerrados, seja por inadimplência dos alunos ou outro motivo.

Para atender esta demanda, foi adicionado mais um campo ao cadastro de período letivo, de nome “Período letivo encerrado para geração de lançamentos”.

Este novo campo, terá impacto somente em rotinas financeiras (Geração de Lançamento em massa e geração de lançamento por parcela).

**Detalhamento das alterações**

1-     Quando o novo parâmetro “Período letivo encerrado para geração de lançamentos” no cadastro do Período letivo estiver **habilitado,** não será possível gerar lançamentos financeiro para parcelas de contratos vinculados ao período letivo que teve o parâmetro habilitado. Em algumas funcionalidades o mesmo não estará disponível para seleção.  
 Quando o parâmetro estiver **desabilitado**, será possível gerar lançamentos financeiro para parcelas de contratos vinculados ao período letivo que está com o parâmetro desabilitado.

Observações:

* O parâmetro “Período letivo encerrado” não será mais responsável por validar a permissão/bloqueio da geração de lançamentos financeiro, essa funcionalidade sai do seu conjunto de validações e passa a ser do parâmetro “Período letivo encerrado para geração de lançamentos”.
* O nome “Período encerrado para pagamento” será alterado para “Período letivo encerrado para pagamento de professores”, para instruir melhor ao usuário o comportamento do sistema.
* Todas as outras validações que o parâmetro “Período letivo encerrado” trata quando está habilitado continuarão sendo tratadas.

2-     Foi criado o parâmetro “Permitir gerar lançamentos para períodos letivos encerrados para geração financeira” no cadastro de parâmetros educacionais do perfil de usuário.  
 Esse parâmetro, quando habilitado, permitirá usuários vinculados ao perfil gerar lançamentos financeiros para períodos letivos encerrados para geração financeira.

3-     A geração de lançamento passou a bloquear a geração de financeira para contratos com períodos letivos com este novo parâmetro marcado. Não será possível gerar lançamento pelo processo de geração de lançamento em lote ou por parcela.

4-     O bloqueio da geração de lançamento passou a ser feito pela regra geral de lançamentos, uma vez marcado o parâmetro “período letivo encerrado para geração financeira”, somente usuários com o perfil de acesso parametrizado para “permitir gerar lançamentos para períodos letivos encerrados” estarão aptos para a geração.

divs
