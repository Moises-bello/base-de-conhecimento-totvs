---
content_hash: e5a7b09fa236926bf97a331979eeb6b5d9ab9f15b48ccbf832286ea4522e472f
fetched_at: '2026-06-29T00:06:00.248749+00:00'
page_id: '195300168'
product: rm
source: tdn-rm
title: RMFIS00001_06.001 - Perguntas e Respostas
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00001_06.001+-+Perguntas+e+Respostas
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão: todas** |
| **Processo** | **:** | ECF - Escrituração Contábil Fiscal |
| **Subprocesso** | **:** | ECF - Escrituração Contábil Fiscal |
| **Data da publicação** | **:** | 27/07/2015 |

## **A DRE será desenvolvida pelo cliente?**

Sim, a inclusão e parametrização da DRE será realizada pelo Cliente. Caso já exista alguma DRE montada para entrega da ECD, poderá ser utilizada sem necessidade de criar uma nova.

## **Quem já possui uma DRE parametrizada para emissão...poderá utiliza a mesma base ou será necessário cia uma nova para gerar esta rotina do ECF?**

Pode sim. Lembrando que a DRE é utilizada na apuração dos tributos e deve ser associada ao Evento Tributário. A DRE em si não é enviada para a ECF.

## **Usamos a DRE por estrutura disponibilizada pela TOTVS. Teremos que parametrizar a DRE nas Demonstrações?**

Sim. O Evento Tributário para o Lucro Real utiliza a nova ferramenta de Demonstrações Contábeis. Para acessá-la na nova MDI:

Backoffice | Gestão Contábil – Escrituração Contábil | Demonstração Contábil.

## **As adições não deveriam ser com base na DRE e sim diretamente no plano de contas, pois a DRE está resumida.**

As adições no Evento Tributário não possuem sua origem na DRE. O Item do Evento Tributário possui três opções para buscar o valor: i) Conta Contábil, ii) Lalur – Parte B e iii) Lançamentos Fiscais.
