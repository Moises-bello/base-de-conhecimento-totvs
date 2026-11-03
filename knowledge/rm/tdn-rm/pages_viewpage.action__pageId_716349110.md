---
content_hash: 6dbd180fb32edec3496b0a5a4c897ab4aabb98e76caa40598e0cec7e8d822ac9
fetched_at: '2026-06-29T00:11:26.349724+00:00'
page_id: '716349110'
product: rm
source: tdn-rm
title: RRA - Geração do XML da Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=716349110
version: 8
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

**Exemplo de XML Férias RRA**

  Mês competência: **02/2022**

  Diferença retroativa a: **12/2021**

  Pensão: **Sim**

  IR: **Sim**

  Ficha financeira do mês 02/2022 - **Período 100**

 Geração do XML contendo as informações no grupo <**infoperApur>**referente ao **Período 100**:****

 O IR considerado no grupo **<infoperApur>** será o que tem código de calculo "211-IRRF RRA FERIAS".

 Geração do XML contendo as informações no grupo <**infoperAnt>**

Neste grupo serão consideradas as verbas de folha de pagamento são oriundas da aba "verbas geradas por diferenças" e as verbas de férias da aba "Detalhamento verbas geradas pela diferença de férias(Envelope)"

**Verbas geradas por diferenças**

**Detalhamento verbas geradas pela diferença de férias(Envelope)**
