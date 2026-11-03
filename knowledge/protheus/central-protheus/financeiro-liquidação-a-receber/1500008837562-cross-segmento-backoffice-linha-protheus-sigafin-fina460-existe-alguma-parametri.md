---
article_id: 1500008837562
category: Financeiro - Liquidação a Receber
content_hash: 8fca63c5d3f804c3ca15fc18a490952e33f1b2d6ad97b6bf81d550de15e246e2
fetched_at: '2026-06-28T22:37:42.247587+00:00'
product: protheus
section_id: 33830247616663
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA460 - Existe alguma
  parametrização para títulos não vencidos
type: support-article
updated_at: '2026-03-31T17:53:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008837562-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA460-Existe-alguma-parametriza%C3%A7%C3%A3o-para-t%C3%ADtulos-n%C3%A3o-vencidos
---

**Dúvida**  
Existe alguma parametrização específica para permitir a liquidação de títulos ainda não vencidos na rotina FINA460?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA460 - A partir da versão 12.1.25  
  
**Solução**

Para títulos **a vencer**, **não há parâmetro padrão** que permita o cálculo de **juros**.

Durante uma **negociação** que envolva títulos **vencidos e a vencer**, a rotina, por padrão, **não calcula juros** e **não permite** a edição manual do campo **Valor Juros (FO1\_VLJUR)** na grid **"Títulos Selecionados"** para títulos ainda não vencidos.

A edição do campo **Valor Juros** para títulos a vencer **não é permitida**, com o objetivo de **preservar a integridade dos dados**.

Para atender a necessidade de inserção de valores adicionais em negociações envolvendo títulos a vencer, foi implementado o campo **Valor Adicional Negociado (FO1\_VLADIC)** na mesma grid. Esse campo possibilita informar um valor adicional por título negociado.

Na contabilização da baixa dos títulos negociados (LPs de código 520), o valor informado neste novo campo é disponibilizado por meio da variável **FO1VADI**.

**Exemplo**  
**![](https://totvssuporte.zendesk.com/attachments/token/jb5LaKSm7x6hm3D9l0E7oEoYK/?name=inline1564164178.png)**

**Importante**  
O campo e variável estarão disponíveis para uso a partir da versão12.1.25​  
  
**Saiba Mais**  
[Melhoria para: adicionar valor na negociação e na validação TIN RM / Correção no cálculo de Valores Acessórios e Cancelamento de Liquidação](https://tdn.totvs.com/pages/releaseview.action?pageId=464953881)  
[FINA460 - Liquidação a receber - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=545236275)
