---
content_hash: a57630bbedec2ab40100eced639166ce4f638395eccd41d4b08c0686d2938746
fetched_at: '2026-06-29T00:11:26.353358+00:00'
page_id: '716349137'
product: rm
source: tdn-rm
title: RRA - Geração do XML de 13ºsalário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=716349137
version: 6
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

**Exemplo de calculo de diferença de 13º Salário RRA com Pensão:**

  Mês competência: **03/2022**

  Diferença retroativa a: **12/2021**

  Pensão: **Sim**

  IR: **Sim**

  Preenchimento da aba "Verbas Geradas" da ficha financeira **(PFVERBASDIS)**do mês 12/2021:

Envelope de pagamento referente ao mês 03/2022, onde foi calculado a diferença.

**Período: 200**

Funcionários | Anexos | Históricos | Histórico de RRA

Geração do XML do evento S-1200:
