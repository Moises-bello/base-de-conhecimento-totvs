---
content_hash: 6899285d55853a7ba1ec5a25ed9a80e0ace0d7834fd2275ee988f8739f19be7d
fetched_at: '2026-06-29T00:09:14.734350+00:00'
page_id: '421385244'
product: rm
source: tdn-rm
title: Fatos e Indicadores
type: documentation
url: https://tdn.totvs.com/display/LRM/Fatos+e+Indicadores
version: 2
---

**Fato de Custo Previsto (HZA)**  
 Extrai informações sobre o Custo do cronograma previsto conforme o período definido no plano de extração. Os valores são quebrados por empresa, filial, moeda, projeto de construção e período. Para a correta visualização das informações no TOTVS Smart Analytics, fica obrigatório o preenchimento dos campos "Empresa" (que corresponde à coligada do TOTVS Obras e Projetos) ou "Estabelecimento" que é o campo filial no Construção & Projetos, e dos campos "Moeda" e "Projeto de Construção" . Além disso, é importante que no projeto do TOTVS Smart Analytics o filtro de "Período (Datas)" esteja dentro dos períodos do cronograma selecionado.

|  |  |
| --- | --- |
| Campo | Descrição |
| Empresa (HZA\_EMPRES) | Código da coligada |
| Estabelecimento (HZA\_ESTABL) | Código da filial |
| Moeda (HZA\_MOEDA) | Moeda do Projeto |
| Data (HZA\_DATA) | Data do custo previsto |
| Projeto (HZA\_PROJCO) | Projeto de construção |
| Tarefa (HZA\_TAREPC) | Tarefa |
| Valor (HZA\_VLPREV) | Valor do custo previsto da tarefa |

**Processamento:** Tabela de Destino: HZA  
 **Indicadores Diretos:** • Valor do Custo Previsto (HZA\_VLPREV) - Indicativo do custo previsto da tarefa é o valor do cronograma previsto da mesma. Esse valor é calculado para cada período parametrizado para o projeto.   **Fato de Avanço Físico (HZB)**  
 Extrai informações sobre o Avanço Físico do projeto conforme o período definido no plano de extração. Os valores são quebrados por empresa, filial, moeda, projeto de construção e período. Para correta visualização das informações no TOTVS Obras e Projetos) ou "Estabelecimento" que é o campo filial no Construção & Projetos, e dos campos "Moeda" e "Projeto de Construção" . Além disso, é importante que no projeto do TOTVS Smart Analytics o filtro de "Período (Datas)" esteja dentro dos períodos do cronograma selecionado.

|  |  |
| --- | --- |
| Campo | Descrição |
| Empresa (HZB\_EMPRES) | Código da coligada |
| Estabelecimento (HZB\_ESTABL) | Código da filial |
| Data (HZB\_DATA) | Data do avanço físico |
| Projeto (HZB\_PROJCO) | Projeto de construção |
| Tarefa (HZB\_TAREPC) | Tarefa |
| Percentual Realizado (HZB\_REALIZ) | Percentual de avanço físico da tarefa |

**Processamento:** Tabela de Destino: HZB  
 **Indicadores Diretos:** • Percentual Realizado da Tarefa (HZB\_REALIZ) - Indica o percentual do avanço físico da tarefa em relação à obra. O valor deste campo em percentual é obtido da seguinte fórmula: (Percentual da tarefa do cronograma realizado \* Percentual da tarefa na Planilha) / 100. Esse valor é calculado para cada período parametrizado para o projeto.
