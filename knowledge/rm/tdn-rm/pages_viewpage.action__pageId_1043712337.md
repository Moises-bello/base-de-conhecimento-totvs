---
content_hash: 4472b69af6198c3ed098c5f3059e5242a9cb35891e31879b87e9751ddbe00cb6
fetched_at: '2026-06-29T00:05:50.869745+00:00'
page_id: '1043712337'
product: rm
source: tdn-rm
title: Código De Cálculo 492 - Base Excedente FGTS 13º a Compensar no FGTS Folha
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1043712337
version: 3
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Evento base de cálculo estorna FGTS. Calculará automaticamente a base do FGTS se já foi recolhido sobre o adiantamento maior que o valor calculado na rescisão, o excedente deverá ser acumulado nesse código de cálculo.

## **02. EXEMPLO DE UTILIZAÇÃO**

Dados fictícios

Supondo um funcionário que recebeu a primeira parcela do décimo terceiro em fevereiro

Em abril foi demitido

Demonstrativo do cálculo na Rescisão com data de demissão **30/04**:

* + **R$ 1.064,27** – Provento de 13º salário proporcional *(codIncFGTS = 12)*
  + **R$ 1.596,40** – Desconto da 1ª parcela do 13º *(codIncFGTS = 12)*
  + **R$ 3.192,80** – Provento de saldo de salário *(codIncFGTS = 11)*
  + **R$ 532,13** – Base de Cálculo de FGTS *(codIncFGTS = 11 | Tipo 4 – Dedutora) -***NOVA VERBA COM CC 492**

Nesse cenário, as bases serão:

• **Base de FGTS de 13º Salário:** R$ 0,00 *(R$ 1.064,27 − R$ 1.596,40)*  
• **Base de FGTS:** R$ 2.660,67 *(R$3.192,80 - R$532,13)*

O código de cálculo 26 - FGTS QUITACAO será calculado considerando o desconto do código de cálculo 492 - Base Excedente FGTS 13º a Compensar no FGTS Folha

Dica:

Veja mais informações em:

* [FGTS Digital - Compensação do valor pago a título de 13º Maior do que a rescisão](https://tdn.totvs.com/pages/releaseview.action?pageId=877870673)
* [Nota Orientativa nº 11/2025 - Leiaute S-1.3 - FGTS DIGITAL](https://tdn.totvs.com/pages/releaseview.action?pageId=1024335823)

## **03.** **TABELAS UTILIZADAS**

* PFPERFF
* PFFINANC
