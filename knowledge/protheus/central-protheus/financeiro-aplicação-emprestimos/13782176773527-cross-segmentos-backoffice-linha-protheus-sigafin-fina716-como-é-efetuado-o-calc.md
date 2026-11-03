---
article_id: 13782176773527
category: Financeiro - Aplicação / Emprestimos
content_hash: b6f8798cc6c4096554cb45757be07eefd391eea011c637841037565600d846ed
fetched_at: '2026-06-28T22:37:59.496001+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA716 - Como é efetuado
  o calculo do juros nas parcelas
type: support-article
updated_at: '2026-01-22T16:44:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13782176773527-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA716-Como-%C3%A9-efetuado-o-calculo-do-juros-nas-parcelas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20862607752215) Tempo aproximado para leitura: **00:30:00 min**  
  
**Dúvida**  
Como é efetuado o cálculo do juros nas parcelas?  
Tenho um contrato de empréstimo **SAC** no valor de R$ 3.897.774,00, com liberação no dia 14/06/2022 com juros a.a. (ao ano) de 16,00% em 11 parcelas, onde as parcelas estão gerando juros de:  
  
Parcela - Data Vencimento - Valor Juros  
1 - 20/07/2022 - R$ 57.477,96  
2 - 20/08/2022 - R$ 44.949,55  
3 - 20/09/2022 - R$ 40.454,60  
  
Como faço o cálculo para chegar no valor do juros de R$ 57.477,96?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210  
  
**Solução**

```
Valor do Empréstimo = R$ 3.897.774,00
Data da Inclusão = 14/06/2022
Juros a.a. = 16,00%
Parcelas  = 11
Juros a.d.  (ao dia) = ?
Vencimento da primeira parcela = 20/07/2022
```

Segue o cálculo da **amortização SAC**

```
Valor do empréstimo / quantidade de parcelas 
R$ 3.897.774,00 / 11 = R$ 354.343,09
```

1) Encontrar o **juros ao dia**, segue a **fórmula de conversão:**

```
(1+TAXA)^(1/365)-1
```

**Importante:** O conteúdo **365** é o número de dias do ano e isso poderá conter no contrato que poderá utilizar 360 ou 365 dias, e o sistema irá obter essa informação do parâmetro **MV\_DIASCTB**

![formula_conversao_juros_ano_mes_dia.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/13781650549527)

Cálculo realizado:

```
((1+TAXA)^(1/365))-1 = Resultado 

((1+16%)^(1/365))-1 
((1+0,16)^(1/365))-1 
((1,16)^(0,002739))-1 =
(1,0004066 - 1) =0,000406713
```

2) Calcular quantos dias entre a **inclusão do empréstimo** até a data da primeira parcela

```
20/07/2022 - 14/06/2022 = 36 dias
```

3) Calcular os juros da primeira parcela

```
J = (Valor do debito  x  ( (1 + taxa do dia )^dias entre uma parcela e outra ) ) - Valor do debito
J = ( R$ 3.897.774,00  *  ( (1 + 0,000406713)^36 dias ) ) - R$ 3.897.774,00 
J = ( R$ 3.897.774,00  *  ( 1,0,000406713 ^36 dias ) )   - R$ 3.897.774,00 
J =  (R$ 3.897.774,00  * 1,014746362 )  - R$ 3.897.774,00 
J = R$ 3.955.251,74 -  R$ 3.897.774,00 
J = R$ 57.477,96
```

**Cálculo da coluna "Valor do Debito"**

```
Valor emp. atualizado - amortização = Valor do Debito
R$ 3.897.774,00 - 354.343,09 = R$ 3.543.430,91
```

4) Calcular os juros da segunda parcela

```
20/08/2022 - 20/07/2022 = 31 dias
```

```
J = (Valor do debito  x  ( (1 + taxa do dia )^dias entre uma parcela e outra ) ) - Valor do débito
J = ( R$ 3.543.430,91 *  ( (1 + 0,000406713) ^ 31 dias ) ) - R$ 3.543.430,91 
J = ( R$ 3.543.430,91  *  ( 1,000406713 ^31 dias ) )   - R$ 3.543.430,91
J =  (R$ 3.543.430,91 * 1,012685319)  - R$ 3.543.430,91
J = R$ 3.588.380,46 - R$ 3.543.430,91
J = R$ 44.949,55
```

Cálculo da coluna **"Valor do Debito"**

```
Valor emp. atualizado - amortização = Valor do Debito
R$ 3.543.430,91 - 354.343,09 = R$ 3.189.087,82
```

5) Calcular os juros da terceira parcela

```
20/08/2022 - 20/09/2022 = 31 dias
```

```
J = (Valor do debito  x  ( (1 + taxa do dia )^dias entre uma parcela e outra ) ) - Valor do debito
J = ( R$ 3.189.087,82 *  ( (1 + 0,000406713) ^ 31 dias ) ) - R$ 3.189.087,82
J = ( R$ 3.189.087,82  *  ( 1,000406713 ^31 dias ) )   - R$ 3.189.087,82
J =  (R$ 3.189.087,82 * 1,012685319)  - R$ 3.189.087,82
J = R$ 3.229.542,42 - R$ 3.189.087,82
J = R$ 40.454,60
```

Cálculo da coluna **"Valor do Debito"**

```
Valor emp. atualizado - amortização = Valor do Debito
R$ 3.189.087,82 - 354.343,09 = R$ 2.834.744,73
```

Fazendo o processo pela **rotina FINA716 - Aplicação / Empréstimo**

 A) **Inclusão do Empréstimo SAC**

**![2_inclusao.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/13783688493847)![3_inclusao.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/13783656269847)**

 B) **Geração das parcelas**

[**![4_parcelas.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/13783688375319)**](https://centraldeatendimento.totvs.com/hc/article_attachments/13783688375319)

**Importante:** Na Projeção de valores da parcela o valor de **juros é recalculado** quando utiliza o tipo **"SAC"**  
Paraotipo **"PRICE":** Os juros **não são recalculados**, pois as prestações são fixas. Dependendo da data inserida, os juros podem exceder o valor da prestação fixa, o que contraria as regras do sistema PRICE.

**Saiba mais**  
[Aplicações e Empréstimos - Financeiro P12](https://tdn.totvs.com.br/pages/releaseview.action?pageId=392500138)  
[Empréstimos - FINA716](https://tdn.totvs.com.br/pages/releaseview.action?pageId=684987254)  
  
**How to -** **FINA716 - Calculo do juros nas parcelas**
