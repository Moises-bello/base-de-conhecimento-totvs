---
content_hash: f5a1b7d6e9641650893ea86a7e76147772c3fdd3c77c32dfd4c63ecf3c823849
fetched_at: '2026-06-29T00:09:14.301760+00:00'
page_id: '421385188'
product: rm
source: tdn-rm
title: Orçamento de Montagem
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385188
version: 2
---

---

Os parâmetros citados abaixo, consistem em ratear o valor de determinadas tarefas (etapa ou obra também), entre outras tarefas dados pré-selecionadas e seguindo alguns critérios de rateio pré-definidos. Na verdade, a base para o rateio será a quantidade, e é utilizado o valor nesse primeiro exemplo somente para simplificar a explicação.

Ex:

|  |  |  |
| --- | --- | --- |
| 001.01.01 | Tarefa 1 | R$ 500,00 |
| 001.01.02 | Tarefa 2 | R$ 350,00 |
| 001.01.03 | Tarefa 3 | R$ 170,00 |
| 001.01.04 | Tarefa 4 | R$ 900,00 |
|  | **Total** | **R$ 1920,00** |

A tarefa 4 será rateada entre as outras tarefas dado o seguinte critério de rateio:

001.01.01 – 50%

001.01.02 – 30%

001.01.03 – 20%  
    
 Nesse exemplo teremos:

|  |  |  |
| --- | --- | --- |
| 001.01.01 | Tarefa 1 | R$ 950,00 |
| 001.01.02 | Tarefa 2 | R$ 620,00 |
| 001.01.03 | Tarefa 3 | R$ 350,00 |
|  | **Total** | **R$ 1920,00** |

O rateio sob uma visão mais simples trata exatamente isso, ele divide algum valor entre outras tarefas e retira do calculo a tarefa que originou o rateio. Como aconteceu no exemplo, os R$ 900,00 foram rateados entre as outras tarefas, e a tarefa 001.01.04 sumiu do calculo.

**Critérios de rateio**

Os critérios de *rateio* determinam como o valor será rateado entre as tarefas selecionadas, e com exceção do critério "Informado manualmente", todos os outros são feitos de forma automática.  
 Os critérios são:

* Proporcional ao homem-hora  
  O valor que cada tarefa receberá do rateio será referente à proporção que ela representa, essa proporção é dada pelo seu consumo de homem-hora. E esse consumo será definido via formula.
* Proporcional ao peso

            O valor que cada tarefa receberá do rateio será referente à proporção que ela representa, essa proporção é dada pelo seu peso. E esse consumo será definido via formula.

**Fórmula do cálculo do homem-hora**

Esta funcionalidade se resume em informar uma fórmula para se calcular a proporção do consumo homem-hora em uma atividade.

**Fórmula de cálculo do peso**

Esta funcionalidade se resume em informar uma fórmula para se calcular a proporção do consumo do peso em uma atividade.

---
