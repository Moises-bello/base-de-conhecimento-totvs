---
content_hash: a6f7e697d3537b224c4d42d71f193a2c6a4d538ae408b604c8cfdaddc1a892af
fetched_at: '2026-06-29T00:09:13.414623+00:00'
page_id: '419550764'
product: rm
source: tdn-rm
title: Criação de Preço Médio de Insumo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=419550764
version: 3
---

Esta funcionalidade tem como finalidade a criação de um novo preço médio considerando os preços existentes para o (s) Insumo (s) selecionado (s).

Este processo pode ser encontrado em Menu Orçamento | Insumos | Cadastro (ou atalho F8) | Processos | Criação de Preço Médio de Insumos ou ainda na edição do Insumo, para executa-lo deve-se selecionar ao menos um Insumo que receberá o preço médio, se não houver seleção de Insumo, por padrão será sugerido para todos os Insumos.

Para executar o processo deve-se obrigatoriamente informar o intervalo de datas **"Data de Atualização Inicial"** e **"Data de Atualização Final"** para que se crie o preço médio a partir dos preços que forem encontrados dentro deste intervalo de datas. A data de seleção do preço é o campo **"Data Atualização"** do cadastro do preço do Insumo.

O cálculo do preço médio se dá a partir do somatório dos preços dentro do intervalo informado / (dividido) pela quantidade dos preços dentro do intervalo informado. Exemplo:

* **Preço 1:** 25,62
* **Preço 2:** 32,59
* **Preço 3:** 57,45
* **Preço Médio:** ((25,62 + 32,59 + 57,45) /3) = 38,55

Se durante o processo o mesmo for executado com a opção **"Ativar o Novo Preço"** habilitado o preço médio será criado como ativo, caso contrário o preço médio será criado como inativo.

A descrição do preço médio criado obedecerá ao seguinte padrão: *Preço Médio em (Data Atual) do período de (Data de Atualização Inicial) e (Data de Atualização Final)*. Exemplo:

* Preço Médio em 08/10/2018 do período de 08/10/2017 a 08/10/2018.

Caso exista um preço com a mesma descrição o processo irá atualizar o valor do preço e o seu preço não será considerado no cálculo.

O processo criar preço médio tanto para insumos locais quanto para insumos globais.
