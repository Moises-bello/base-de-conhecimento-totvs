---
article_id: 360037748673
category: Integração RM
content_hash: d215f36e68b93a6ff4061a819596cef12dc59e6b1e4b8689632ecef8f8a1b96e
fetched_at: '2026-06-28T22:42:36.895855+00:00'
product: protheus
section_id: 360012117913
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Detalhamento da mensagem de custos indiretos
  AssetMonthlyUndirectCosts
type: support-article
updated_at: '2021-09-02T16:51:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037748673-Manufatura-Linha-Protheus-MNT-Detalhamento-da-mensagem-de-custos-indiretos-AssetMonthlyUndirectCosts
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Qual o detalhamento da mensagem de custos indiretos **AssetMonthlyUndirectCosts?**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integração RM - Todas as versões  
  
**Solução**Abaixo segue o detalhamento da mensagem de **Custos indiretos - AssetMonthlyUndirectCosts**:

| **Mensagem Única** | **Observação** |
| --- | --- |
| **Tag** |
| **BusinessContentType** | |
| **CompanyId** | Código da empresa/coligada |
| **CompanyInternalId** | *Internal* **ID - Identificação** da chave completa da empresa |
| **BranchId** | Código da Filial |
| **AssetInternalId** | *Internal* **ID** do Código do Bem |
| **MonthYear** | Ano mês da ocorrência dos custos |
| **ListOfIndirectCost** | |
| **InternalId** | *Internal* **ID** da entidade |
| **CostCenterCode** | Código do centro de custo |
| **LaborCost** | Custo da mão-de-obra aplicado na **OS - Ordem de serviço** |
| **InputCost** | Custo de peças, produtos, lubrificantes, aplicados na **OS** |
| **ThirdPartCost** | Custo com serviços de terceiros que trabalharam na **OS** |
| **ToolCost** | Custo com ferramentas aplicadas na **OS** |
| **RentCost** | Custo de locação do equipamento fixo, calculado pelo Sistema de **Manutenção de ativos** |
| **PenaltyCost** | Custo com multas pagas no mês, podemos considerar somente multas por culpa da empresa |
| **IncidentCost** | Custo com acidentes ocorridos no mês |
| **PaperCost** | Custo com documentos realizados no mês |
| **FuelCost** | Custo com os abastecimentos realizados no Mês |
| **TotalRentCost** | Custo total de locação do equipamento, calculado pelo Sistema de **Manutenção de ativos** mensalmente |
| **HourRentCost** | Custo hora de locação do equipamento, calculado pelo Sistema de **Manutenção de ativos** |
| **RealHourRentCost** | Custo hora real de locação do equipamento, calculado pelo Sistema de **Manutenção de ativos** mensalmente |
| **BilledRentCost** | Valor faturado pela locação do equipamento |
