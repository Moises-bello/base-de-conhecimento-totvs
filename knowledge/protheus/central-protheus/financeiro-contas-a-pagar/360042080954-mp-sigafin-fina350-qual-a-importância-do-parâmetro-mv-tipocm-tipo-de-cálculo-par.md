---
article_id: 360042080954
category: Financeiro - Contas a Pagar
content_hash: 29670a417aff174027a07c2c9e0abdb59ae7010c2da5ea774706840d51a94cae
fetched_at: '2026-06-28T22:38:09.994013+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: MP- SIGAFIN - FINA350 - Qual a importância do parâmetro MV_TIPOCM (Tipo de
  cálculo para correção monetária)
type: support-article
updated_at: '2022-04-01T21:21:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042080954-MP-SIGAFIN-FINA350-Qual-a-import%C3%A2ncia-do-par%C3%A2metro-MV-TIPOCM-Tipo-de-c%C3%A1lculo-para-corre%C3%A7%C3%A3o-monet%C3%A1ria
---

**Ocorrência**A correção monetária no momento da baixa pode ser calculada sobre o valor total do título sem considerar descontos, juros, multas e impostos configurando parâmetro **MV\_TIPOCM** como **O**(Original). Para que o cálculo considere estes valores este parâmetro deve estar configurado como **T**(Total).

**Causa**Ao utilizar a configuração do parâmetro como **T**(Total), o valor para cálculo da correção monetária será o valor resultante no momento da baixa na moeda do título, ou seja considerando os descontos, juros, multas e retenções, este valor calculado será convertido para a moeda padrão utilizando a taxa da inclusão e a taxa da baixa para que seja gerado a correção monetária.

**Ambiente**  
Microsiga Protheus – Financeiro – A partir da versão 12.1.25  
   
**Solução:**

## EXEMPLO DE UTILIZAÇÃO

Exemplo 01:

**MV\_TIPOCM = T**

Baixa de título em dólar (moeda 2) com decréscimo informado na inclusão do título.

Taxa de inclusão R$3,7236

Título em dólar (Moeda 2):  
Valor: $180,00  
Decréscimo: $28,00

O valor do título considerando o decréscimo: R$565,99

Taxa do dia da baixa R$ 4,0745

Valor na moeda do título: $152,00  
Valor na moeda forte: R$ 619,32

|  | $ | R$ (Taxa inclusão) | R$ (Taxa dia da baixa) |
| --- | --- | --- | --- |
| Valor do título | 180,00 | 670,25 | 733,41 |
| Decréscimo | 28,00 | 104,26 | 114,09 |
| Total | 152,00 | 565,99 | 619,32 |

**Correção monetária:**

152 \* 4.0745 = 619.32

152 \* 3.7236 = 565.99

619.32 - 565.99 = 53.34

CM = R$ 53.34

Exemplo 02:

**MV\_TIPOCM = T**

Baixa de um título em dólar (moeda 2) informando desconto no momento da baixa.

Taxa de inclusão R$3,7236

Título em dólar(Moeda 2):  
Valor: $180,00

Taxa do dia da baixa R$ 4,0745

Desconto: R$28,00 (o valor informado no campo de desconto é na moeda do banco, para este exemplo é a moeda padrão - Moeda 1)

Valor na moeda do título: $173,13  
Valor na moeda forte com desconto: R$ 705,41

|  | $ | R$ (Taxa inclusão) | R$ (Taxa da baixa) |
| --- | --- | --- | --- |
| Valor do título | 180 | 670,25 | 733,41 |
| Desconto | 6,87 | 25,58 | 28,00 |
| Total | 173,13 | 644,67 | 705,41 |

**Correção monetária:**

173,13 \* 4,0745 = 705,41

173,13 \* 3,7236 = 644,67

705,41 - 644,67 = 60,74

CM = R$ 60,74

Exemplo 03:

**MV\_TIPOCM = O**

Baixa de título em dólar (moeda 2) com decréscimo informado na inclusão do título.

Taxa de inclusão R$3,7236

Título em dólar(Moeda 2):  
Valor: $180,00  
Decréscimo: $28,00

O valor do título considerando o decréscimo: R$565,99

Taxa do dia da baixa R$ 4,0745

Valor na moeda do título: $152,00  
Valor na moeda forte: 619,32

|  | $ | R$ (Taxa inclusão) | R$ (Taxa dia da baixa) |
| --- | --- | --- | --- |
| Valor do título | 180,00 | 670,25 | 733,41 |
| Decréscimo | 28,00 | 104,26 | 114,09 |
| Total | 152,00 | 565,99 | 619,32 |

**Correção monetária:**

180 \* 4,0745 = 733,41

180 \* 3,7236 =670,25

**733,41 - 670,25 = 63,16**

**CM = R$ 63,16**Exemplo 04:

**MV\_TIPOCM = O**

Baixa de um título em dólar (moeda 2) informando desconto no momento da baixa.

Taxa de inclusão R$3,7236

Título em dólar(Moeda 2):  
Valor: $180,00

Taxa do dia da baixa R$ 4,0745

Desconto: R$28,00 (o valor informado no campo de desconto é na moeda do banco, para este exemplo é a moeda forte-Moeda 1)

Valor na moeda do título: $173,13  
Valor na moeda forte com desconto: R$ 705,41

|  | $ | R$ (Taxa inclusão) | R$ (Taxa da baixa) |
| --- | --- | --- | --- |
| Valor do título | 180 | 670,25 | 733,41 |
| Desconto | 6,87 | 25,58 | 28,00 |
| Total | 173,13 | 644,67 | 705,41 |

**Correção monetária:**

180 \* 4,0745 = 733,41

180 \* 3,7236 =670,25

**733,41 - 670,25 = 63,16**

**CM = R$ 63,16**

**Importante:**Os exemplos usados são baixas realizadas em banco na moeda padrão para que ocorra o cálculo de correção monetária.
