---
content_hash: ea1a4f52b92611002c7563eee4ea9e67c9376503246fa4358e2624a52f815226
fetched_at: '2026-06-29T00:10:27.148582+00:00'
page_id: '516621035'
product: rm
source: tdn-rm
title: Definição de período para corte de curto prazo e longo prazo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=516621035
version: 32
---

Será possível definir como o sistema irá consistir o período de corte para o processo de Contabilização de Curto e Longo prazo. É necessário acessar os parâmetros do Totvs Incorporação através da aba ‘Ambiente’>>Parâmetros>>Totvs Incorporação. Após selecione a opção ‘Integração Contábil’ e avance.

**Ação dos parâmetros:**

|  |  |
| --- | --- |
| **Utilizar Período Contábil para calcular os valores de curto e longo prazo** | Essa opção não pode ser marcada, sempre o sistema irá considerar como data inicial do curto prazo a data da Venda, Aditivo, Reajuste, Seguro Prestamista ou Distrato.  Habilitado, define que o sistema irá considerar o período contábil como base para a data inicial do prazo curto e a data se atualiza conforme o processo executado (Venda ou Reajuste). Desmarcado o sistema irá considerar como data inicial do curto prazo a data da venda. |
| **Período limite curto prazo (Em meses)** | Define a quantidades de meses que o sistema considerar como curto prazo. |
| **Período de Apuração da Transferência (Em meses)** | A apuração sempre é mensal não tem a opção de alterar   Define o período (meses) que os valores serão transferidos das contas de longo prazo para o curto prazo. |

**Por Default o sistema irá apresentar as opções da seguinte forma:**

* ‘Utilizar Período Contábil para calcular os valores de curto e longo prazo’ habilitado.
* Período limite curto prazo (Em meses) como 24 ou 12.
* Período de Apuração da Transferência (Em meses) como 12 ou 1.

**Parâmetro: Essa opção está desativada**

5
complete
**Utilizar Período Contábil para calcular os valores de curto e longo prazo**

Considerando 3 vendas distintas, com o período contábil de de 2 anos. As vendas foram criadas com datas diferentes para demonstrar a evolução dos períodos. conforme tabela a seguir:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Vendas** | **Data da Venda** | **Data Limite Curto** | **Período de curto** | **Período de Transferência Apuração** |
| **A** | 02/01/2019 | 31/12/2020 | 24 | 12 |
| **B** | 01/02/2019 | 31/12/2020 | 24 | 12 |
| **C** | 01/03/2020 | 31/12/2021 | 24 | 12 |

**Parâmetro:**

6
incomplete
 **Utilizar Período Contábil para calcular os valores de curto e longo prazo**

Considerando 3 vendas distintas, com um plano de financiamento de 12 parcelas. As vendas foram criadas com datas diferentes para demonstrar a evolução dos períodos. conforme tabela a seguir:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Vendas** | **Data da Venda** | **Data Limite Curto** | **Período de Curto** | **Período de Transferência Apuração** | **Parcelas** |
| D | 10/01/2019 | 31/04/2019 | 3 | 1 | 12 |
| E | 15/02/2019 | 30/05/2019 | 3 | 1 | 12 |
| F | 09/03/2019 | 31/06/2019 | 3 | 1 | 12 |

**Importante:**

* **O processo de Reajuste irá atualizar os períodos, seguindo o mesmo raciocínio da venda, será considerado a data do reajuste.**
* **O sistema não trava a alteração da parametrização, necessário extremo cuidado antes de qualquer alteração.**
