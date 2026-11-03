---
content_hash: 91a338c8d68d973ca58399708b3043fc59449f78b7c9794fd982d3265271f2b1
fetched_at: '2026-06-29T00:11:36.527882+00:00'
page_id: '772831859'
product: rm
source: tdn-rm
title: Exemplos de apurações do Simples com Redistribuição do ISS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=772831859
version: 10
---

#f5f5f5#363636noneExemplosAtenção

Para a correta apuração do Simples Nacional, quando utilizado a 6ª faixa de faturamento, é necessário que a 5ª faixa esteja corretamente preenchida no cadastro de alíquotas do Simples, pois será utilizada no cálculo.

Imagem Exemplo

**01. Exemplos**

* **Cenário 1 - Faturamento ultrapassou o sublimite:**  
    

  RBT12 = R$ 4.500.000,00  
  RBA = R$ 4.000.000,00  
  RPA = R$ 1.000.000,00

  Sublimite = R$ 3.600.000,00  
  Parcela da RPA que não excedeu o sublimite (P1) = (1.000.000,00 – 400.000,00) = 600.000,00  
  Parcela da RPA que excedeu o sublimite (P2) = (4.000.000,00 – 3.600.000,00) = 400.000,00  
    
  Alíquota Efetiva = ((RBT12 x alíquota nominal da respectiva faixa) - parcela a deduzir da faixa) / RBT12

Imagem - Cadastro de Alíquotas

Alíquota efetiva : ((4.500.000,00 x 33,00%) - 648.000,00) / 4.500.000,00 = 18,60%  
Percentual do ISS na 5ª faixa = (((RBT12 x Alíquota Nominal da 5ª faixa)-Valor a Deduzir da 5ª faixa)/RBT12) x alíquota do ISS da 5ª faixa  
Percentual do ISS na 5ª faixa = (((4.500.000,00 x 21%) - 125.640,00) / 4.500.000,00) x 33,5% = 6,09968%  
Valor devido P1 = 600.000 x (alíquota efetiva da 6ª faixa + percentual ISS da 5ª faixa)  
Valor devido P1 = 600.000 x (18,60% + 6,09968%) = 600.000 x 24,69968% = **148.198,08**

Alíquota Efetiva do Excesso Apurado = ((Sublimite x Alíquota Nominal Aplicada) - Parcela a Deduzir) / Sublimite  
Alíquota Efetiva do Excesso Apurado: 15% = ((3.600.000,00 x 33%) - 648.000,00) / 3.600.000,00  
Valor do Excesso Apurado = Alíquota Efetiva do Excesso Apurado x Parcela excedente (P2)  
Valor do Excesso Apurado: 60.000,00 = 15% x 400.000,00  
  
Valor Total = Valor do Excesso Apurado + Valor devido (P1)  
Valor Total: **208.198,08** = 60.000,00 + 148.198,08  
  
Alíquota demonstrada no período = Valor Total / RPA  
Alíquota demonstrada no período: 208.198,08 / 1.000.000,00 = **20,82%**  
 

Imagem - Período de Apuração

* **Cenário 2 - Faturamento não ultrapassou o sublimite:**  
    
  RBT12 = R$ 3.721.877,25  
  RBA = R$ 3.000.000,00  
  RPA = R$ 266.493,64  
    
  Sublimite = R$ 3.600.000,00  
  Parcela da RPA que excedeu o sublimite (P2) = (3.000.000,00 – 3.600.000,00) = **"Não excedeu o sublimite"**  
    
  Alíquota Efetiva = ((RBT12 x alíquota nominal da respectiva faixa) - parcela a deduzir da faixa) / RBT12

Imagem - Cadastro de Alíquotas

Alíquota efetiva : ((3.721.877,25 x 33,00%) - 648.000,00) / 3.721.877,25 = 15,5894%  
Percentual do ISS na 5ª faixa = (((RBT12 x Alíquota Nominal da 5ª faixa)-Valor a Deduzir da 5ª faixa)/RBT12) x alíquota do ISS da 5ª faixa  
Percentual do ISS na 5ª faixa = (((3.721.877,25 x 21%) - 125.640,00) / 3.721.877,25) x 33,5% = 5,90414%  
  
Valor Total Devido = 266.493,64 x (15,5894% + 5,90414%) = 266.493,64  x 21,49354% = **57.278,99**

Imagem - Período de Apuração
