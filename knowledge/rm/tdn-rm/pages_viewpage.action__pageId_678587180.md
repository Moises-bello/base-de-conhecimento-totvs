---
content_hash: 2aa9cafde1eee75cb6c7583bf56e3df5941d6edc7d6bbf5b2ee9008581cc7866
fetched_at: '2026-06-29T00:11:17.268111+00:00'
page_id: '678587180'
product: rm
source: tdn-rm
title: 06 - Regras para habilitar a inscrição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=678587180
version: 13
---

## 

## **01. Regras**

Para que a opção "**Inscrições**" seja exibida, será considerado o período de inscrição definido no calendário do cadastro do processo seletivo e também a data de inscrição que poderá ser cadastrada para as áreas ofertadas do processo seletivo e o período defino para a "Forma de inscrição".

Será possível informar a data de inscrição para área de interesse ofertada somente a partir da versão 12.1.2205

Independente do período de inscrição do processo seletivo ou área de interesse ofertada, para que a opção "**Inscrições**" seja disponibilizada, é necessário que o processo seletivo tenha cadastrado pelo menos uma forma de inscrição com um período válido em relação a data atual.

Processo seletivo com período de inscrição preenchido

* A opção "**Inscrições**" ficara disponível somente se a data atual estiver entre o período de inscrição

* Serão apresentadas somente as áreas ofertadas em que o período de inscrição não esteja preenchido, ou se o período de inscrição da área ofertada estiver válido considerando a data atual.

Processo seletivo que não possui o período de inscrição preenchido

* A opção "**Inscrições**" ficara disponível somente se existir ao menos uma área ofertada para o processo seletivo que possua o período de inscrição preenchido, e que esteja válido considerando a data atual.
* Serão disponibilizadas para inscrição somente as áreas ofertadas que possuir um período de inscrição válido.
Forma de inscrição do processo seletivo

Sempre ao cadastrar ou alterar a data de inicio ou término de  uma **forma de inscrição** no processo seletivo serão aplicadas as seguintes regras de validação:

* A data de início e término da forma de inscrição deverá estar entre o período de inscrição do processo seletivo (quando preenchida)
* Se a área ofertada cadastrada para o processo seletivo possuir uma data de inscrição, deverá existir pelo menos uma **forma de inscrição** cadastrada com uma data de inicio e término que considere o período de inscrição da área ofertada.

**Por exemplo:**

**Cenário 01 (Válido)**

Forma de inscrição "Online" - Período: 01/01/2022 á 31/12/2022.

Área ofertada:  Administração / Comércio Exterior - Período de inscrição: 01/01/2022 á

**Cenário 02 (Inválido)**

Forma de inscrição "Online" - Período: 01/01/2022 á 31/03/2022.

Área ofertada:  Administração / Comércio Exterior - Período de inscrição: 01/01/2022 á

Para este cenário o sistema apresentará  uma mensagem de validação

Esta mesma regra será aplicada se o usuário estiver executando manutenção no cadastro de uma área ofertada.
