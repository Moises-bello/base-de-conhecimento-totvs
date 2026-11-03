---
content_hash: e0127e84f5a79768ffef5302d0f32b49ae983787a5065df37183017c1acb0366
fetched_at: '2026-06-29T00:08:49.706807+00:00'
page_id: '331856320'
product: rm
source: tdn-rm
title: DT Análise de Orçamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=331856320
version: 1
---

# Análise de Orçamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Folha de Pagamento |
| **Módulo:** | Orçamento |
| **Função:** | Análise de Orçamento Previsto x Realizado |
| **Situação/Requisito:** | Análise de orçamento |
| **Solução/Implementação:** | O processo de "Gerar Dados Realizado" tem o intuito de gerar os dados para comparação entre registros reais e os previstos pelo orçamento. Os dados gerados são de cunho Financeiro (valores) e Headcount (amostragem de pessoas).    Visão informativa com os dados previstos e realizados para amostragem de pessoas que foram admitidas, demitidas e transferidas. |
| **Requisito:** | FOPCALCULO01-1780 |

**Análise Previsto x Realizado**

**Definição do processo:**

Idealizado para facilitar avaliações gerencias por parte das empresas, permitindo Analisar o Previsto x Realizado em um determinado período.

**Gerar Dados Previsto x Realizado:**

Na geração de Dados Previsto x Realizado, é possível salvar um perfil.

**1 – Parâmetros**

**Orçamento**: Informar o orçamento que será comparado com os dados reais.

**Revisão**: Informar qual revisão será utilizada em relação ao orçamento selecionado.

**Tipo de análise**:

* **Financeiro** - A análise será feita para dados relativos aos valores de movimentações da ficha financeira, ou seja, valores que efetivamente foram realizados.
* **Headcount** - A análise será feita para dados relativos à contagem de admissões, transferências e demissões que efetivamente foram realizados.

**Período**: Período ao qual serão gerados os dados.

* **Atual** - O período de análise será para a competência atual.
* **Anterior** - O período de análise será para a competência anterior.

**Período** - O período de análise será uma data de início e uma data de fim estipulada pelo usuário. Tais datas devem ser coerentes com as datas de início e fim do orçamento e competência atual.

**Análise HeadCount Previsto x Realizado:**

Visão informativa com os dados previstos e realizados para amostragem de pessoas que foram admitidas, demitidas e transferidas.

Na tela à esquerda mostra a quantidade de funcionários que entraram e saíram filtrados por Orçamento, Revisão, Competência, Seção e Função. Mostrando o total de Previsto e Realizado.

Na tela a direita mostra detalhes do item a esquerda agrupados por tipo de movimentação (Admissão, Transferência Entrada, Demissão, Transferência Saída e Afastado).

Ao abrir o item da direita, é possível ver os funcionários que foram realizados para aquele tipo de movimentação.
