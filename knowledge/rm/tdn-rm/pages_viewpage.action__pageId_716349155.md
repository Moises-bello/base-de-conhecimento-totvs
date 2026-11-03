---
content_hash: 64c4e17034181652676e7d658deb6e393b7382a439164a943d61a473813f9ba6
fetched_at: '2026-06-29T00:11:26.357364+00:00'
page_id: '716349155'
product: rm
source: tdn-rm
title: RRA - Geração do XML de Rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=716349155
version: 16
---

## **Conceito**

O eSocial, recorrentemente, vem passando por modificações e adaptações, a fim de receber as informações referente ao Imposto de Renda na sua versão simplificada de escrituração. 

A partir de 16/01/2023 o leiaute S-1.1 passa a ser aceito no ambiente de produção do eSocial, onde contemplará as informações sobre os Rendimentos Recebidos Acumuladamente (RRA).

Para geração das informações do RRA, foi necessário adequação da geração do XML do evento S-1200.

falseImportante!

1. Para a correta geração do XML é necessário que:
   1. o parâmetro "Utiliza Cálculo RRA" existente em Configurações | Parametrizador | Folha Normal | Geral 2/2 esteja marcado.
   2. o histórico de RRA esteja devidamente preenchido, sendo obrigatório o preenchimento dos campos " Tipo do Processo" e "Natureza / Descrição RRA";

      2. As verbas calculadas referente ao RRA serão lançadas no período informado em Configurações | Parametrizador | Folha Normal | Geral 2/2.

**Exemplo de XML da Rescisão**

  Mês competência: **02/2022**

  Diferença retroativa a: **12/2021**

  Pensão: **Sim**

  IR: **Sim**

  Ficha financeira do mês 02/2022 - **Período 300**

**Período 1:**

**Período 300: Rescisão RRA**

  Geração do XML: Eventos de IRRF

   Mês 12/2021 - Verbas geradas por diferença:

Geração do XML:
