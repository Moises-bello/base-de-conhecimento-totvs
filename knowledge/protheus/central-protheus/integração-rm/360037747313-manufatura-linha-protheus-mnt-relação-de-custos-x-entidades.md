---
article_id: 360037747313
category: Integração RM
content_hash: 0e0de55e083670b437c7f63afea7258389c06419546adf46104e11d89c958cb7
fetched_at: '2026-06-28T22:42:36.939940+00:00'
product: protheus
section_id: 360012117913
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Relação de Custos x Entidades
type: support-article
updated_at: '2021-10-29T11:34:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037747313-Manufatura-Linha-Protheus-MNT-Rela%C3%A7%C3%A3o-de-Custos-x-Entidades
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:00 min**  
**Dúvida**Como funciona a relação de **Custos** e **Entidades**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integração RM - Todas as versões  
  
**Solução**A tabela abaixo demonstra como deve funcionar a relação de custos x entidades.

| Custo Extraído | Tabela | Descrição Tabela |
| --- | --- | --- |
| **InputCost** | **STL** | **Insumos da Ordem de Serviço** |
| **LaborCost** | **STL** | **Insumos da Ordem de Serviço** |
| **ThirdPartCost** | **STL** | **Insumos da Ordem de Serviço** |
| **ToolCost** | **STL** | **Insumos da Ordem de Serviço** |
| **IncidentCost** | **TRH** | **Registro Comunicado Sinistro** |
| **TRK** | **Cargas Afetadas pelo Sinistro** |
| **TRO** | **Veículos Terceiros no Sinistro** |
| **TRL** | **Imóveis Terceiros Env. Sinistro** |
| **TRV** | **Complemento do Sinistro** |
| **TRM** | **Vítimas do Sinistro** |
| **PenaltyCost** | **TRX** | **Cadastro de Multas** |
| **PaperCost** | **TS2** | **Documentos a Pagar** |

Segue abaixo detalhamento dos custos que serão enviados na mensagem:

| Tipo de Custo | Descrição | Observação |
| --- | --- | --- |
| **LaborCost** | **Custo Mão de Obra** | Custo de mão de obra aplicado nas **O.S. - Ordem de serviço**. Aplicará à essa *tag* o custo gerado nos insumos de tipo **Mão de Obra**, de uma **O.S.** já finalizada. |
| **InputCost** | **Custo Materiais aplicados** | Custo de peças, produtos, lubrificantes, aplicados na **O.S.** Aplicará à essa *tag* o custo gerado nos insumos de tipo **Produto**, de uma **O.S.** já finalizada. |
| **ThirdPartCost** | **Custo com Terceiros** | Custo com serviços de terceiros que trabalharam na **O.S.** Aplicará à essa *tag* o custo gerado nos insumos de tipo **Produto**, de uma **O.S.** já finalizada |
| **ToolCost** | **Custo de Ferramentas** | Custo com **Ferramentas** aplicadas na **O.S.** Aplicará à essa *tag* o custo gerado nos insumos de tipo **Ferramenta**, de uma **O.S.** já finalizada. |
| **FuelCost** | **Custo do consumo de combustível** | Custo com os abastecimentos realizados no mês |
| **PenaltyCost** | **Custo com multas** | Custo com multas pagas no mês. |
| **IncidentCost** | **Custo com Acidentes** | Custo com acidentes ocorridos no mês |
| **PaperCost** | **Custo com Documentos** | Custo com documentos realizados  no mês |
| **RentCost** | **Custo Fixo de locação do Equipamento** | Custo de locação do equipamento fixo, calculado pelo Sistema de **Manutenção de Ativos**. |
| **TotalRentCost** | **Custo total de locação do equipamento** | Custo total de locação do equipamento, calculado pelo Sistema de **Manutenção de Ativos** mensalmente. |
| **HourRentCost** | **Custo Hora de locação do Equipamento** | Custo hora de locação do equipamento, calculado pelo Sistema de **Manutenção de Ativos** |
| **RealHourRentCost** | **Custo Hora Real de locação do equipamento** | Custo hora real de locação do equipamento, calculado pelo Sistema de **Manutenção de Ativos** mensalmente |
| **BilledRentCost** | **Valor Faturado** | Valor faturado pela locação do equipamento |
| **UnproductiveHoursAmount** | **Horas Improdutivas** | Quantidade de horas improdutivas apontadas no mês na frente de trabalho |
| **UnproductiveHoursCost** | **Valor Horas Improdutivas** | Valor das horas improdutivas no mês. Calculado da seguinte forma: **Valor improdutivo = (custo hora da máquina parada \* quantidade de horas paradas).** O somatório das horas paradas é apurado com base nas horas lançadas nas atividades improdutivas |
| **ProductiveHoursAmount** | **Horas Produtivas** | Quantidade de horas produtivas apontadas no mês na frente de trabalho |
| **ProductiveHoursCost** | **Valor Horas Produtivas** | Valor de horas produtivas |
