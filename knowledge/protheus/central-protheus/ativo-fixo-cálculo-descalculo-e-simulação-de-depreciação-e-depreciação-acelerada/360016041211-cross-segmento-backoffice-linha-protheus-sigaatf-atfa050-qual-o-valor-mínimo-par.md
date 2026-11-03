---
article_id: 360016041211
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: 57cce9e501bf884e56e59e30ef143b237467d60ff291b27f4daa6552192db09c
fetched_at: '2026-06-28T22:41:43.263124+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA050 - Qual o valor
  mínimo para cálculo de depreciação '
type: support-article
updated_at: '2021-09-01T10:47:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016041211-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA050-Qual-o-valor-m%C3%ADnimo-para-c%C3%A1lculo-de-deprecia%C3%A7%C3%A3o
---

**Dúvida**ATFA050 Qual o valor mínimo para cálculo de depreciação ?

**Ambiente**Cross Segmento - Backoffice Linha Protheus – Ativo Fixo – A partir da versão 11.80.

**Conceito**

A Rotina **ATFA050** trata conforme conceito abaixo o processo para os valores de calculo de depreciação, quando valor menor que R$1,00.

Não existe cenário que se aplique uma depreciação de 10% ao ano para um bem no valor de R$ 1,00. isto de acordo com o Art. 301 do RIR/99.   
  
II - Bens cujo custo unitário de aquisição não seja superior a R$326.61 (trezentos e vinte e seis reais e sessenta e um centavos), ainda que o prazo de vida útil seja superior a um ano.  
  
Exemplo:  
Valor do bem: 26,83  
Valor depreciado/mes: 0,22  
Valor acumulado: 25,71  
Formula: (Valor do bem) - (Valor acumulado) - (Valor depreciado)  
Valores: 26,83 - 25,71 - 0,22  
Saldo: 0,90  
  
Este saldo será acumulado ao valor a depreciar no mês, somando um valor de 1,12 unidades monetárias.

Sendo assim, caso o valor restante a depreciar seja inferior a 1 (uma) unidade monetária, será adicionado este valor a cota atual de depreciação.
