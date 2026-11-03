---
article_id: 360057631754
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 93eeede555627e276a23a8216bc9f55d0c695ff30c865b5d7527e7d0adb85043
fetched_at: '2026-06-28T22:38:45.217174+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: MP-FAT-Como calcular o valor da fatura, quando o parâmetro MV_TPDPIND=1
type: support-article
updated_at: '2021-04-28T15:12:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057631754-MP-FAT-Como-calcular-o-valor-da-fatura-quando-o-par%C3%A2metro-MV-TPDPIND-1
---

**Dúvida**Como calcular o valor da fatura, quando o parâmetro MV\_TPDPIND=1.  
  
**Ambiente**Protheus – Faturamento – A partir da versão 11.80  
  
**Solução**

CENÁRIO :  
1º Item com TES (501) que gera duplica com valor de  100,00  
2º Item com TES(557) que não gera duplica com valor de  200,00  
3- No pedido de venda preencher o campo C5\_DESCONT= 10,00  
Veja que o VALOR FATURA=96,67

Se o seu parâmetro está configurado para todos os itens  (MV\_TPDPIND=1) , ele irá ratear o valor entre todos os itens, como ja diz o próprio parâmetro.  
Ou seja, neste caso ele rateia os 10,00 entre os 100,00 do primeiro item, mais os 200,00 do segundo item,**logo chegamos à seguinte conclusão:**

Primeiro item = R$ 3,33      -  100,00, ou seja ele é equivale a 33,3333% do total do pedido  
Segundo ítem = R$ 6,67    -  200,00 do segundo item, ou seja ele equivale a 66,6666% do total do pedido  
Totalizando os itens acima, chegamos aos R$ 10,00 contidos no C5\_DESCONT.  
Logo somente o primeiro item gera duplicata, e o valor do mesmo é de 100,00.  Aplicando o desconto proporcional  que é R$ 3,33  chegamos ao resultado:

**R$100,00 - R$3,33 =  Valor da fatura R$ 96,67**
