---
content_hash: d1098d3feadb9722b25ec51f9344dca691583515bfa87391878d1f1c5e110e2a
fetched_at: '2026-06-29T00:10:12.627923+00:00'
page_id: '454831887'
product: rm
source: tdn-rm
title: Conversor Histórico Rateio Tomador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454831887
version: 6
---

Este processo tem o objetivo de preencher o histórico de tomador de serviço conforme opções abaixo:

Nessa tela é possível realizar a seleção dos funcionários e a forma de conversão.

* **Considerar apenas rateio atual:** O sistema irá verificar o cadastro do rateio de tomador atual e preencherá o histórico.
* **Considerar movimento distribuído de competências anteriores:** O usuário deverá informar a**"Competência Inicial"** e o "**Evento base para Rateio**", com isso o sistema irá alimentar o histórico a partir da competência informada até a competência anterior a atual com os tomadores encontrados no Movimento Distribuído por Tomador para o evento selecionado. Para a competência atual o sistema alimenta o histórico com o rateiro atual de tomador.
* **Regerar histórico:** Está opção deleta todos os históricos existentes, conforme filtro cadastrado e refaz o processo de conversão conforme opções acima.

**Observações:** Para preenchimento do campo "Competência Inicial" no histórico o sistema verifica a opção selecionada, conforme abaixo:

* Ao selecionar a opção "Considerar apenas rateio atual" preencherá com o mês e ano da competência atual.
* Ao selecionar a opção "Considerar movimento distribuído de competências anteriores" preencherá com o mês e ano competência existente no movimento do tomador, para a competência atual o sistema alimenta com o mês e ano competência atual.

Caso seja necessária alguma alteração poderá ser feita manualmente pelo histórico ou pela importação de dados.
