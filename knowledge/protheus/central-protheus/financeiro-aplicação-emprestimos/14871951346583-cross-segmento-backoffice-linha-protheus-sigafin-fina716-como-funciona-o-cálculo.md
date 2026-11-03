---
article_id: 14871951346583
category: Financeiro - Aplicação / Emprestimos
content_hash: bc866ee0de371c1a67c0900d17fa1f488ace41223e1d023866f0c3e9b6873694
fetched_at: '2026-06-28T22:37:59.434040+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmento - Backoffice linha Protheus - SIGAFIN - FINA716 - Como funciona
  o cálculo come-cotas, cálculo rendimento, IR nas apropriações e resgate na Aplicação
  FAF
type: support-article
updated_at: '2024-08-29T20:31:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14871951346583-Cross-Segmento-Backoffice-linha-Protheus-SIGAFIN-FINA716-Como-funciona-o-c%C3%A1lculo-come-cotas-c%C3%A1lculo-rendimento-IR-nas-apropria%C3%A7%C3%B5es-e-resgate-na-Aplica%C3%A7%C3%A3o-FAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22979856681111) Tempo aproximado para leitura: **00:15:00 min****Dúvida**Como funciona o cálculo come-cotas, cálculo rendimento, IR nas apropriações e resgate na Aplicação FAF?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**O mês do come-cotas é definido no parâmetro **MV\_10892**=05#11 , onde no meu exemplo irá ocorrer nos meses de maio e novembro  
  
**MV\_RENAPL4**=1   
Tipo de rendimento da apropriação de aplicação por cotas (1=Acumulado;2=Mensal)  
  
**MV\_APIRTAB** = .T.  
Define alíquota de IR para os meses não come-cotas .T. - será considerada tabela regressiva de IR .F. - considera 15% longo prazo e 20% curto prazo;  
  
**Contrario Bancário (FINA120)** - Cadastrar um contrato informando banco, agência e conta, e o número do contrato, e informar o valor unitário de 1 cota.  
  
No exemplo do Contrato abaixo:  
Emissão: 22/10/2020  
Vlr. Cota/Tit. : R$ 75,00 (Preço 1 cota)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/14871893667479)](https://centraldeatendimento.totvs.com/hc/article_attachments/14871893667479)

**FINA716 Cadastrar a aplicação FAF -** Inserir o contrato e a quantidade de cotas a serem obtidas  
Modelo: APL - Aplicação  
Operação: FAF  
Dt. Operação: 22/10/2020  
Qtd. Cota/Tit: 1.000,00  
Vlr. Operação: R$ 75.000,00

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/14872147078679)](https://centraldeatendimento.totvs.com/hc/article_attachments/14872147078679)  
 **Contrario Bancário (FINA120)** - Atualizar a cota no contrato bancário  
31/10/2020 - Preço 1 cota R$ 76,00

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/14872897912471)](https://centraldeatendimento.totvs.com/hc/article_attachments/14872897912471)

**Efetuar a apropriação (FINA716)**

```
Total da operação R$ 76.000,00 = R$ 76,00 * 1000,00 cotas   
Rendimento R$ 1.000,00 = (R$ 76.000,00 - R$ 75.000,00)  
IR até 180d 22,5% R$ 225,00 = (R$ 1.000,00 * 22,5%)
```

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/14872980839831)](https://centraldeatendimento.totvs.com/hc/article_attachments/14872980839831)

**Mês come-cotas****Contrario Bancário (FINA120)** - 30/11/2020  Preço 1 cota R$ 77,00   
**Efetuar a apropriação** **(FINA716)**

```
Total da operação R$ 77.000,00 = R$ 77,00 * 1000,00 cotas   
Rendimento R$ 2.000,00 = (R$ 77.000,00 - R$ 75.000,00)  
IR come-cotas 15%  R$ 300,00  = (R$ 2.000,00 * 15%)  
Cotas Retidas 3,89610390 =  R$ 300 / R$ 77,00    
Saldo em Cotas 996,10389610 = (1000,00 cotas ant. - 3,89610390 cotas retidas)
```

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/14873340718871)](https://centraldeatendimento.totvs.com/hc/article_attachments/14873340718871)

31/12/2021-  Preço 1 cota R$ 78,00   
**Apropriação (FINA716)**

```
Total da operação R$ 77.696,10 = R$ 78,00 * 996,10389610 cotas  
Rendimento R$ 2.996,10 = ((R$ 78,00 * 996,10389610) + R$ 300,00 IR come-cotas 15% 30/11/20 ) - (R$ 75,00 vlr. unitário da cota inicial  * 1.000,00 cotas que eu tinha)  
IR 22,5%  R$ 374,12 = (R$ 2.996,10 * 22,5% IR)  - R$ 300,00
```

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/26005769604375)](https://centraldeatendimento.totvs.com/hc/article_attachments/26005769604375)

31/01/2021-  Preço 1 cota R$ 79,00   
**Apropriação (FINA716)**

```
Total da operação R$ 78.692,21 =79,00*996,10389610  
Rendimento R$ 3.992,21 =((79,00*996,10389610)+300,00)-(75,00*1000)  
IR 22,5% R$ 598,25 =(3992,21*22,5%)-300,00
```

28/02/2021 -  Preço 1 cota R$ 80,00   
**Apropriação (FINA716)**

```
Total da operação R$ 79.688,31  =80,00*996,10389610  
Rendimento R$ 4.988,31 =((80,00*996,10389610)+300,00)-(75,00*1000)  
IR 22,5% R$ 822,37  =(4988,31*22,5%)-300,00
```

31/03/2021 -  Preço 1 cota R$ 81,00

**FINA716 Apropriação**

```
Total da operação R$ 80.684,42  =81,00*996,10389610  
Rendimento R$ 5.984,42  =((81,00*996,10389610)+300,00)-(75,00*1000)  
IR 22,5% R$ 1.046,49  =(5984,42*22,5%)-300,00
```

30/04/2021 -  Preço 1 cota R$ 82,00  (190 dias, tabela IR muda para 20,0%)

**Apropriação (FINA716)**

```
Total da operação R$ 81.680,52  =82,00*996,10389610  
Rendimento R$ 6.980,52  =((82,00*996,10389610)+300,00)-(75,00*1000)  
IR 20,0%  R$ 1.096,10   =(6980,52*20,0%)-300,00
```

**Mês come-cotas**31/05/2021  Preço 1 cota R$ 83,00  
  
**FINA716 Apropriação**

```
Total da operação R$ 82.676,62 = R$ 83,00 * 996,10389610 cotas   
Rendimento R$ 7.976,62  =((83*996,1038961)+300)-(75*1000)  
IR come-cotas 15%  R$ 896,49  = (R$ 7.976,62 * 15% ) - R$ 300,00 IR  
Cotas Retidas 10,80112658 = R$ 896,49  /  R$ 83,00    
Saldo em Cotas 985,30276952 = (996,1038961 cotas ant. - 10,80112658 cotas retidas)
```

```
 
```

30/06/2021-  Preço 1 cota R$ 84,00

**Resgate (FINA716)**

```
Total da operação R$ 82.765,43 = R$ 84,00 * 985,30276952 cotas  
Rendimento R$ 8.961,93 = (R$ 82.765,43+ R$ 300,00 IR Come Cotas 15% ref.30/11/20 +  R$ 896,49 IR Come Cotas 15% ref.31/05/21) - (R$ 75,00 vlr. unitário da cota inicial * 1.000,00 cotas que eu tinha)  
IR 20% R$ 595,90 = (R$ 8.961,93 * 20% ir) - (300,00 IR Come-Cotas + 896,49 IR Come-Cotas )
```

**Saiba mais**

[1 - FINA716 Como é contabilizado pelo LP 582 e 585 na apropriação e no resgate dos rendimentos mês a mês de uma aplicação por cotas FAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14683550030487)

[2 - Exemplo de utilização do parâmetro MV\_RENAPL4](https://tdn.totvs.com/pages/releaseview.action?pageId=571786367)

[3 - Pagina oficial da rotina FINA716](https://tdn.totvs.com.br/pages/releaseview.action?pageId=684987254)  
[4 - Lançamentos padrões e sintaxe Aplicação Empréstimo](https://tdn.totvs.com/pages/releaseview.action?pageId=236430682)

[5 - Conceitos Aplicações Empréstimos](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=392500138)
