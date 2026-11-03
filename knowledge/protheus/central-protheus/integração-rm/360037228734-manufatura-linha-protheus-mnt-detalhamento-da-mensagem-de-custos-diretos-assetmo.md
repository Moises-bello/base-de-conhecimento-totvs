---
article_id: 360037228734
category: Integração RM
content_hash: 7b12bc8be9c8fcfa7e934cae1c86ee4b59e2ccedde7f2b0e5603c17843a3b65e
fetched_at: '2026-06-28T22:42:36.884920+00:00'
product: protheus
section_id: 360012117913
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Detalhamento da mensagem de custos diretos
  AssetMonthlyDirectCosts
type: support-article
updated_at: '2021-08-30T20:15:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037228734-Manufatura-Linha-Protheus-MNT-Detalhamento-da-mensagem-de-custos-diretos-AssetMonthlyDirectCosts
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Qual o detalhamento da mensagem de custos diretos **AssetMonthlyDirectCosts**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integração RM - Todas as versões  
  
**Solução**Abaixo segue o detalhamento da mensagem de custos diretos **AssetMonthlyDirectCosts:**

| Mensagem Única | MNT | | Observação |
| --- | --- | --- | --- |
| **Descrição** | **Tabela** | **Coluna** |
| **BusinessContentType** | | | |
| **CompanyId** |  | **cEmpAnt** | **Código da coligada/empresa** |
| **CompanyInternalId** |  |  | **Internal ID do código da Coligada/Empresa** |
| **BranchId** |  | **cFilAnt** | **Código da filial** |
| **AssetInternalId** |  | **cEmpAnt| cFilAnt| T9\_CODBEM** | **Internal ID bem/equipamento** |
| **MonthYear** |  |  | **Ano mês da ocorrência dos custos** |
| **ListOfDirectCost** | | | |
| CostCenterCode |  |  | **Código do Centro de Custo/Frente de Trabalho** |
| InternalId |  |  | **Internal ID da entidade** |
| UnproductiveHoursAmount |  |  | **Quantidade de Horas Improdutivas apontadas no mês para a Frente de Trabalho/Centro de Custo** |
| UnproductiveHoursCost |  |  | **Valor das horas improdutivas no mês. Calculado da seguinte forma. Valor Improdutivo = (custo hora da maquina parada \* quantidade de horas paradas). O somatório das horas paradas será apurado com base nas horas lançadas nas atividades improdutivas** |
| ProductiveHoursAmount |  |  | **Quantidade de Horas Produtivas apontadas no mês para a Frente de Trabalho/Centro de Custo** |
| ProductiveHoursCost |  |  | **Valor das Horas Produtivas** |
| **oApportionmentProductiveHursCost** |  |  | **Valor das horas produtivas recalculada após rateio das horas improdutivas. Processo de rateio distribui as horas improdutivas com base na quantidade de horas produtivas por frente de trabalho. Então a quantidade de horas produtivas vai aumentar, e consequentemente o valor também vai aumentar, após o rateio. Este campo representa este novo valor.** |
| **ListOfAppointment** | | | |
| **InternalId** |  |  | **Internal ID do apontamento** |
| **TaskProjectInternalId** |  |  | **Internal id do ID da tarefa** |
| **TaskProjectId** |  |  | **ID Tarefa** |
| **StartDateTimeAppointment** |  |  | **Data/Hora Inicial do apontamento** |
| **EndDateTimeAppointment** |  |  | **Data/Hora Final do apontamento** |
| **ActivityCode** |  |  | **Código da Atividade** |
| **ActivityInternalId** |  |  | **Internal ID da Atividade** |
