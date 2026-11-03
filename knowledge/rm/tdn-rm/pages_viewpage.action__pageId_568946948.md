---
content_hash: 361e5e5305e0d9c7369484f631a79a2aa5f3ff0325cfc6add94f208084f53536
fetched_at: '2026-06-29T00:10:51.579194+00:00'
page_id: '568946948'
product: rm
source: tdn-rm
title: FISCAL01-14028 DT Lançamento de Ajuste x Atividade Econômica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=568946948
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Encerramento do Período CPRB |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14028 |

## **02. SITUAÇÃO/REQUISITO**

No período de Apuração os valores do Lançamento de DC devem afetar o código de atividade Econômica no qual ele pertence. Os valores de ajustes passam a afetar a Base de Cálculo e não o valor do imposto diretamente.

**Verificar estória completa no épico**

Critérios de aceite:

* Atualizar o valor da Base de Cálculo na atividade para considerar os valores dos Lançamentos de ajuste
* Quando não for preenchido o código de atividade econômica no Lançamento de ajuste deve ser mantido o comportamento atual.
* Este comportamento deverá afetar apenas períodos de 2020 ou superiores

## **03. SOLUÇÃO**

Na apuração do tributo CPRB será considerado o código da atividade vinculado ao lançamento de outros débitos e créditos CPRB;

Quando não informado o código de atividade econômica no lançamento de outros débitos e créditos na apuração o lançamento será considerado o comportamento anterior.

O Lançamento de Ajuste afetará a Base de Cálculo na apuração da atividade e consequentemente o Valor da Contribuição.

A implementação tem efeito em períodos CPRB a partir de 01/2020.
