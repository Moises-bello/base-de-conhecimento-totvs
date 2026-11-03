---
content_hash: 65f54cee0f9a2a40e072c38d5d989ed04ddad0f6db2ca9cd85fa2f9e5ec1b762
fetched_at: '2026-06-29T00:11:26.345673+00:00'
page_id: '716349098'
product: rm
source: tdn-rm
title: RRA - Geração do XML da Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=716349098
version: 31
---

## **Conceito**

O eSocial, recorrentemente, vem passando por modificações e adaptações, a fim de receber as informações referente ao Imposto de Renda na sua versão simplificada de escrituração. 

A partir de 16/01/2023 o leiaute S-1.1 passa a ser aceito no ambiente de produção do eSocial, onde contemplará as informações sobre os Rendimentos Recebidos Acumuladamente (RRA).

Para geração das informações do RRA, foi necessário adequação da geração do XML do evento S-1200.

falseImportante!

1. Para a correta geração do XML é necessário que:
   1. o parâmetro "Utiliza Cálculo RRA" existente em Configurações | Parametrizador | Folha Normal | Geral 2/2 esteja marcado.
   2. o histórico de RRA esteja devidamente preenchido, sendo obrigatório o preenchimento dos campos " Tipo do Processo" e "Natureza / Descrição RRA";

      2. As verbas calculadas referente ao RRA serão lançadas no período informado em Configurações | Parametrizador | Folha Normal | Geral 2/2.

**Exemplo do XML de Folha RRA**

  Mês competência: **02/2022**

  Diferença retroativa a: **12/2021**

  Pensão: **Sim**

  IR: **Sim**

  Preenchimento da aba "Verbas Geradas" da ficha financeira **(PFVERBASDIS)** do mês 12/2021:

 Geração do XML do evento S-1200:

  Envelope de Pagamento referente ao mês 02/2022 onde foi calculado a diferença que não são consideradas como RRA.

  Período: 1

 Período 100 com os valores calculados de RRA:

Funcionários | Anexos | Históricos | Histórico de RRA

Este histórico é criado quando é realizado o calculo de diferença de RRA.

  Geração do XML do evento S-1200:
