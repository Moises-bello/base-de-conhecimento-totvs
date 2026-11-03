---
content_hash: c18a6d109d3b20de805c8a7caceb20471faa94b06f53288c5385250fa99a41b9
fetched_at: '2026-06-29T00:10:03.659052+00:00'
page_id: '452719118'
product: rm
source: tdn-rm
title: D.S.R
type: documentation
url: https://tdn.totvs.com/display/LRM/D.S.R
version: 1
---

**D.S.R**   
**Paga D.S.R:** Ao selecionar este campo, está sendo definido que o cálculo do D.S.R feito pelo Totvs Automação de Ponto substituirá o cálculo que é feito pelo Totvs Folha de Pagamento.   
O cálculo considera o período de apuração de ponto para gerar os eventos com o número de horas de D.S.R e D.S.R Perdido.   
   
**Número de Horas do D.S.R:** Neste campo é cadastrado o número de horas de D.S.R a ser lançado para o funcionário (este é o valor de cada D.S.R).  
   
**Número de Horas do D.S.R Proporcional:** Neste campo Deverá ser informado o valor proporcional a ser descontado do D.S.R para cada dia que definirá esta perda, ou seja, para um D.S.R de 8 horas, cada dia da semana (considerando 5 dias de trabalho) corresponderá a 01:36 de D.S.R.  
Caso o funcionário falte (ou tenha um atraso que leve a perda do D.S.R) duas vezes na semana e utilize o D.S.R proporcional, serão descontadas 03:12 de D.S.R. (01:36 para cada falta / atraso).  
   
**Número de Horas de D.S.R do Feriado:** Neste campo é cadastrado o número de horas de D.S.R a ser lançado para o funcionário em dias de feriado.   
Caso o parâmetro do sindicato *Considera os feriados para o cálculo de D.S.R* esteja marcado, o sistema lança um número de horas de D.S.R de feriado.  
Este número de horas será o cadastrado neste parâmetro e, caso ele esteja com o valor 00:00, será lançado o número de horas da jornada no dia de feriado.
