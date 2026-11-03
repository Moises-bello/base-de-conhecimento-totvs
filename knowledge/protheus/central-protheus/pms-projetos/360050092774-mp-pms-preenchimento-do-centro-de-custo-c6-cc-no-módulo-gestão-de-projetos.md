---
article_id: 360050092774
category: PMS - Projetos
content_hash: 188b3e0d704328c7101a040c803f5df287f189e4b1406bbc1437ca47cba29caf
fetched_at: '2026-06-28T22:37:15.037422+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: MP - PMS - PREENCHIMENTO DO CENTRO DE CUSTO C6_CC NO MÓDULO GESTÃO DE PROJETOS
type: support-article
updated_at: '2021-04-29T21:12:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050092774-MP-PMS-PREENCHIMENTO-DO-CENTRO-DE-CUSTO-C6-CC-NO-M%C3%93DULO-GEST%C3%83O-DE-PROJETOS
---

**Dúvida**

Quando Faturo um projeto através do módulo PMS, o sistema não leva o centro de custo no pedido de venda, mesmo que o produto tenha o **B1\_CC** preenchido.  
   
 **Ambiente**

Protheus -  A partir da versão 11.  
  
**Solução**

Ao faturar um projeto através da rotina **PMSA600** ( Programa de faturamento de projetos), realmente o centro de custo  campo **C6\_CC** (Centro de custo) não é levado ao pedido de venda. Esta tratativa é exclusiva para os pedidos incluídos direto no módulo de Faturamento, através do **MATA410**. 

Uma alternativa é avaliar a possibilidade de utilizar os pontos de entrada abaixo:

**PMA600COL** - Armazena valores **gravados**  
**<https://tdn.totvs.com/display/public/mp/PMA600COL+-+Armazena+valores+gravados>**

**PMSA600AF** - Insere **itens**  
**<https://tdn.totvs.com/display/public/mp/PMSA600AF+-+Insere+itens>**

**PMSA600PV** - Manipula faturamento do **projeto**  
**<https://tdn.totvs.com/display/public/mp/PMSA600PV+-+Manipula+faturamento+do+projeto>**

**Observação:**Quando utiliza integração via **EAI** com o ***TOP da RM*** e ***Protheus***, aconselhamos a utilizar o ponto de entrada **MT410EAI** - Edição dos Arrays de cabeçalho e itens antes da gravação - Integração.

[**https://tdn.totvs.com/x/D4TYCg**](https://tdn.totvs.com/x/D4TYCg)
