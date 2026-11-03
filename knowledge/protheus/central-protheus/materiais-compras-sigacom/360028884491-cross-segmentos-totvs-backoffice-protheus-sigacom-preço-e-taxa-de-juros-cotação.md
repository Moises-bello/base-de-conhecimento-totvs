---
article_id: 360028884491
category: Materiais - Compras (SIGACOM)
content_hash: 3f853772fbdc0c8cb1036d106276dc7becbb3f19699d0307261ef1c5e10ad7fb
fetched_at: '2026-06-28T22:41:24.043187+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Preço e Taxa de Juros
  Cotação
type: support-article
updated_at: '2023-11-16T20:00:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028884491-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Pre%C3%A7o-e-Taxa-de-Juros-Cota%C3%A7%C3%A3o
---

**Dúvida**O que é valor presente (Analise de Cotação) ?

**Ambiente**Protheus – SIGACOM – A partir da versão 11.80

**Solução**

O cálculo deste valor sofre influência da Taxa de Juros do sistema (oportunidade de mercado) utilizada para cálculo de deflação de valores ao valor presente. MV\_JUROS.

O valor apresentado na analise de cotação serve como referência ao valor A Vista conforme a **taxa de juros** + **condição de pagamento** utilizada na cotação.  
A seguir a demonstração da fórmula utilizada para o cálculo:

**Exemplo:**  
Em uma Cotação com :  
Qtde = 100  
Valor Unitário = R$ 9,00  
Valor Total = R$ 900,00  
Condição de Pagamento = 30 dias  
Taxa Financeira = 5.00%  
Alíquota de ICMS = 18,00%  
  
Na Analise de Cotações o**valor presente** será = **R$ 858,54**  
  
Porque :  
ValPres :=  900,00 / (  (  1 + ( 5 / 100 ) ) \*\*  (**29**/ 30 ) )  
ValPres :=  900,00 /  (  1.05  \*\*  ( 0.96666667 ) )  
ValPres :=  900,00 /  1.04829373  
**ValPres :=  858.54**  
  
Quanto ao ICMS quando houver, após o calculo do valor presente deve-se deduzir o mesmo. EX.:  18% de 900.00 = 162.00    
  
Valpres := 858.54 – 162,00  
**Valpres := 696.54**  
  
***OBS***. Em uma condição de pagamento onde o campo E4\_DDD “Dias da Condição de Pagamento”  esteja com o conteúdo “D” = Data do dia o valor será 29 dias, se quiser que seja 30 dias deverá alterar esse campo para “Fora o dia”, neste caso o calculo seria este:  
  
ValPres :=  900,00 / (  (  1 + ( 5 / 100 ) ) \*\*  (**30**/ 30 ) )  
ValPres :=  900,00 /  (  1.05  \*\*  ( 1 ) )  
  
ValPres :=  900,00 /  1.05  
ValPres :=  857.14  
Valpres := 857.14 – 162,00  
**Valpres := 695.14  
  
  
*OBS*:** Na tela da rotina de Análise de Cotação, o **Valor Presente** da Cotação poderá ser visualizado através do Campo de **Valor Total** da Proposta, conforme exemplo abaixo:

![](https://tdn.totvs.com/download/attachments/514728443/image2019-9-6_16-50-5.png?version=1&modificationDate=1567799405127&api=v2)

Cálculo da mesma cotação utilizando uma condição de pagamento com 3 parcelas iguais de 30,60 e 90 dias :  
  
O cálculo é realizado em cada parcela de 300,00 e depois somado:  
ValPres1Parc :=  300,00 / (  (  1 + ( 5 / 100 ) ) \*\*  (**30**/ 30 ) )  
ValPres1Parc :=  300,00 /  (  1.05  \*\*  ( 1 ) )  
ValPres1Parc :=  300,00 /  1.05  
  
**ValPres1Parc :=  285.71428571**  
  
ValPres2Parc :=  300,00 / (  (  1 + ( 5 / 100 ) ) \*\*  (**60**/ 30 ) )  
ValPres2Parc :=  300,00 /  (  1.05  \*\*  ( 2 ) )  
ValPres2Parc :=  300,00 /  1.1025000  
  
**ValPres2Parc :=  272.10884354**  
  
ValPres3Parc :=  300,00 / (  (  1 + ( 5 / 100 ) ) \*\*  (**90**/ 30 ) )  
ValPres3Parc :=  300,00 /  (  1.05  \*\*  ( 3 ) )  
ValPres3Parc :=  300,00 /  1.157625000  
  
**ValPres3Parc :=  259.15127956**  
  
**VALOR PRESENTE = 285.71428571 + 272.10884354 + 259.15127956**  
**VALOR PRESENTE = 816,97 – 162,00 (ICMS) se houver**  
**VALOR PRESENTE = 654,97**  
  
***SINTAXE DA FÓRMULA***  
Valor Presente da parcela = Valor da parcela / ( ( 1+ ( Tx juros )  ) \*\* ( Prazo da parcela / 30 ) )  
Valor Presente Final = a soma do valor presente das parcelas

OBS : Taxa de Juros Percentual (Opcional)?  
Quando informada a taxa, será considerada esta para o cálculo do valor presente na análise das cotações. Caso contrário, o sistema busca o conteúdo do parâmetro "MV\_JUROS".  
  
A150Monta GetMV(" MV\_JUROS"),SC8->C8\_TAXAFIN)  
A160MontVe GetMV("MV\_JUROS")/100

Por padrão o sistema traz os valores para a mesma data, para que usuário possa comparar, por isso dependendo da condição de pagamento o valor pode variar,

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[PCOM10012 - Como é efetuado o cálculo do Valor Presente na Análise de Cotação?](https://tdn.totvs.com/pages/releaseview.action?pageId=514728443)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
