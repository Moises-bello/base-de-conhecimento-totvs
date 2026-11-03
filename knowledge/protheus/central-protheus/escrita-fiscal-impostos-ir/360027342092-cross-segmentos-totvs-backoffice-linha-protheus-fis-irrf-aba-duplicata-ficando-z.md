---
article_id: 360027342092
category: Escrita Fiscal - Impostos - IR
content_hash: 562df261d92f4ead395e1cb5c2b338b8a0422c93ebc3a2b3b49123cbc7d215ad
fetched_at: '2026-06-28T22:39:31.849261+00:00'
product: protheus
section_id: 1500001549802
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  IRRF - aba duplicata
  ficando zerada após a gravação do documento quando o valor do Impostos é inferior
  a 10,00
type: support-article
updated_at: '2021-06-17T13:03:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027342092-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-IRRF-aba-duplicata-ficando-zerada-ap%C3%B3s-a-grava%C3%A7%C3%A3o-do-documento-quando-o-valor-do-Impostos-%C3%A9-inferior-a-10-00
---

**Ocorrência**

Cliente destaca que ao lançar uma nota fiscal de entrada com IRRF abaixo de dez reais, o sistema calcula o impostos mas não mantém o mesmo na aba duplicatas, assim que a nota é salva.   
  
**Ambiente**

Protheus - MATA103 - A partir da versão 11.80

**Solução**

Quando ocorre a escrituração de uma nota fiscal de serviço com IRRF o sistema apresenta duas fases:

**Cálculo do Imposto:**

O sistema faz o cálculo do IRRF de qualquer valor.

**Retenção do imposto:**

O sistema faz a retenção conforme a condição do parâmetro MV\_VLRETIR = 10.00 (É dispensado a retenção do IR em até dez reais). Caso o IRRF seja abaixo de dez reais ele não leva para o financeiro, destaca na aba impostos mas "apaga" assim que você salva a nota e visualiza a nota escriturada no módulo de compras.

**E por quê calcula:**

O sistema precisa calcular esse impostos, pois há o fator da cumulatividade, caso você entre com outra nota com mesma data de emissão o sistema vai recuperar aquele imposto calculado/armazenado (que não havia superado os dez reais) e soma com essa segunda nota e gera retenção no financeiro.

**Na pratica, ficaria deste modo na tabela SE2 com base em duas notas fiscais:**

*A primeira nota fiscal o valor do IRRF ficou em sete reais;*

E2\_VRETIRF = 7.00 (este campo armazena o cálculo)

E2\_IRRF = 0.00 (este campo é o IR retido que leva o tipo TX no financeiro)

*Segunda nota o valor do IRRF ficou em cinco reais (mesma data de emissão);*

E2\_VRETIRF = 5.00 (armazenou o cálculo da nota atual)

E2\_IRRF = 12.00 (gerou retenção, pois no somatório das notas superou o valor de dez reais 7,00 + 5,00).
