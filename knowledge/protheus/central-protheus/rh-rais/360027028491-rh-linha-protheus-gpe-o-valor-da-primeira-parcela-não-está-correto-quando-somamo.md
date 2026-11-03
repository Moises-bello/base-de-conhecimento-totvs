---
article_id: 360027028491
category: RH - RAIS
content_hash: 7ad488965311ff4ee685dead65575eb32afeb8c29871d5b0606168b0c8111d41
fetched_at: '2026-06-28T22:44:05.709823+00:00'
product: protheus
section_id: 360000030327
source: central-protheus
title: RH - Linha Protheus - GPE - O valor da primeira parcela não está correto quando
  somamos a incidência “B” para a RAIS.
type: support-article
updated_at: '2025-09-04T20:24:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027028491-RH-Linha-Protheus-GPE-O-valor-da-primeira-parcela-n%C3%A3o-est%C3%A1-correto-quando-somamos-a-incid%C3%AAncia-B-para-a-RAIS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34708520688535) Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**

O valor da primeira parcela não está correto quando somamos a incidência “B” para a **RAIS**.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal –  Todas as versões  
  
**Solução**

Cenário:

Roteiro 131 mês de pagamento novembro (tem direito a 12/12 avos)

Salário - campo RA\_SALARIO R$3.580,00

Adicional cargo de confiança R$2.00,00

Calculo primeira parcela na versão 12

Verba 200 1ª parcela de 13º (id 0022)  = R$1.790,00

Verba 201 Adic. Cargo de confiança 1ª parcela 13º (id 1636) = R$1.000,00

Verba 202 Prêmio (verba sem identificador de cálculo) \* =  R$800,00 (valor equivalente a primeira parcela)

Verba 999 Liquido primeira parcela 13º (id 0678) = R$3.590,00

Se na segunda parcela de décimo terceiro a empresa pagar a mesma verba 202 Prêmio “sem id”,  e está verba ter a incidência somente “C” para o campo RAIS na aba anuais o sistema irá somar o valor somente para a segunda parcela, este valor não irá entrar para a primeira parcela o que irá causar diferença no valor total.

Neste caso deverá informar a incidência ‘B” para o sistema entender e levar corretamente a parcela de 13º

Este problema não irá ocorrer para verbas que tem identificador de cálculo, pois atualmente temos verbas para primeira e segunda parcela.

Na **RAIS** é possível ter duas incidências que no caso para a verba 202 teria C e B

**Neste item a empresa precisa ter atenção a duas coisas importantes:**

1ª) No cálculo da primeira parcela quando existe verba informada ou gerada pelo usuário, o sistema não consegue calcular o valor devido, o usuário deverá informar a parte que cabe a primeira parcela)

2ª) A verba que será informada na primeira parcela tem que ter atenção para não ser a mesma da segunda parcela, por causa das incidências para o eSocial a primeira parcela tem tributação somente de FGTS.

**Saiba Mais**  
[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
