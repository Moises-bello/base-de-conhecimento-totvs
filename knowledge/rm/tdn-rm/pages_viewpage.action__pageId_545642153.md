---
content_hash: 74d8085d35bb959d39e35082a5ce121fe7efc407d85a62889dddf57a4585ae72
fetched_at: '2026-06-29T00:10:39.041469+00:00'
page_id: '545642153'
product: rm
source: tdn-rm
title: Log do Aditivo - Utiliza Mês Comercial.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=545642153
version: 1
---

Criado um parâmetro para se utilizar Mês comercial em Aditivo de alteração de vencimento.

Mes comercial - Utiliza 30 dias de todos os meses.

Não Utiliza o Mês Comercial  - Utiliza o Mês cheio.

## **Log do aditivo de alteração de vencimento. ( Prorrrogação / Antecipação )**

Novo Parâmetro : Usa Mês Comercial Aditivo Vencimento como Cálculo em Meses.

Parâmetro Desmarcado - Não utiliza mês comercial para cálculo em meses.

Incluindo Aditivo - Alteração de Vencimento.

# **1.  Prorrogação**

Parcela com vencimento dia **20/04/2020** e jogando para **08/12/2028.**

**Observação sobre o****Tipo de Cálculo Vencimento.**

Para o calculo, são utilizados 4 tipos calculo de vencimento.

* Valor futuro meses
* Valor futuro meses parcial
* N de meses percentual
* N de meses valor

Após Aplicar e Calcular - Clicar em LOG Parcela.

**O Log mostra que o Parâmetro não encontra-se marcado e mostra o número de Meses da Prorrogação**

Marcando o Parâmetro - Usa Mês Comercial Aditivo Vencimento com Cálculo em Meses.

**O Log mostra que o Parâmetro encontra-se marcado e mostra o número de Meses da Prorrogação**

# **2. Antecipação.**

Parâmetro Marcado.

Parcela com vencimento dia **20/11/2028** e antecipando para **20/04/2020.**

**O Log mostra que o Parâmetro encontra-se marcado e mostra o número de Meses da Antecipação.**

Parâmetro desmarcado

**O Log mostra que o Parâmetro encontra-se Desmarcado e mostra o número de Meses da Antecipação.**
