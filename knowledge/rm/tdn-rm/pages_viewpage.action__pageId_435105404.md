---
content_hash: 3b2f95bc47bb383e48fd5ce3b95a04b829498c41531c2f29adbe328c7863cade
fetched_at: '2026-06-29T00:09:50.117335+00:00'
page_id: '435105404'
product: rm
source: tdn-rm
title: Contabilização do Contrato de Locação - Anexo - Linearização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105404
version: 2
---

A linearização consiste em utilizar o valor médio em cada período para realizar as contabilizações, mesmo que haja diferenças no valor cobrado mês a mês, seja por descontos, carências ou qualquer outro motivo que afete os valores.

* **Ajustes:**

* + Caso alguma alteração gere impacto nos valores linearizados, seja por alterar algum valor, seja por alterar o prazo do contrato, serão feitos os ajustes, onde a diferença da linearização será acertada no período em que houve a alteração e nos meses posteriores, até o final do contrato.

* **Tratamento das operações contábeis:**

* + Serão gravados os IDs das operações contábeis para cada processo que realizar contabilização. Foram criadas tabelas onde é possível amarrar os dados do contrato, o período (mês e ano) e a operação contábil para os processos.

* **Tratamento dos Escalonamentos:**

* + Os escalonamentos possuem tratamentos diferenciados, com relação a terem sidos criados antes ou após a efetivação do contrato de locação:

* + - **Escalonamentos criados ANTES da efetivação do contrato de locação:** Estes serão identificados através de um campo interno e serão considerados desde o início do Contrato, no cálculo dos valores lineares.
    - **Escalonamentos criados APÓS a efetivação do contrato de locação:** Estes serão identificados através de um campo interno e serão considerados apenas para o período do escalonamento, no cálculo dos valores lineares.
