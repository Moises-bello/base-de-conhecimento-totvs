---
article_id: 360054370694
category: RH - Dissídio
content_hash: 52925c04d7a2abc38de2c233832b6a9059fe503848a2e82a1c3487d2e7c230d2
fetched_at: '2026-06-28T22:43:43.272603+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir média de férias  dentro do cálculo
  de dissídio
type: support-article
updated_at: '2025-08-08T14:54:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054370694-RH-Linha-Protheus-GPE-Como-conferir-m%C3%A9dia-de-f%C3%A9rias-dentro-do-c%C3%A1lculo-de-diss%C3%ADdio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17322839650455) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como conferir média de férias dentro do cálculo de dissídio?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**  
1. Saber a categoria, salário e horas mensais do funcionário:

Acesse: Atualizações > Funcionários > Funcionários  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094224993)  
  
2. A média é composta por uma hora extra paga na competência de Julho.  Por esse motivo, é preciso saber a quantidade de dias úteis e DSR:

Atualizações >  Definições de cálculo > Período  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094225033)  
  
3. Certificar-se que o valor de hora extra pago na folha de pagamento está correto:  
Consulta > Cadastros > Recibo de pagamento  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094225053)  
  
Cálculo de hora extra  
Salário (2.000,00/ 220) \* 40 horas extras = 363,63  
Valor hora 363,63 + 100% = 727,28  
  
Cálculo do DSR  
Hora extra (727,28/ 27) \* 4 = 107,75  
  
4. Cálculo das férias do funcionário e demonstrativo de médias:  
Miscelânea/ Cálculo/ Férias  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092017214)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092017234)  
  
A soma das verbas 151 e 215 corresponde ao valor demonstrado no demonstrativo de médias.  
  
**Atenção**É muito importante que este demonstrativo de médias, retirado no momento do cálculo das férias, seja guardado. Existe uma rotina de dissídio retroativo que permite a impressão do relatório, mas o valor apresentado dependerá de todas as informações colocadas nos parâmetros de impressão e a configuração atual de verbas.  
Então, se entre o cálculo de férias e o cálculo do dissídio existir alteração no cadastro das verbas que tem incidência de médias, o valor não será o mesmo.  
Não tem como realizar a conferência de médias dentro do dissídio sem saber exatamente as verbas que estavam compondo as médias no cálculo das férias.  
  
5. Cálculo de dissídio:  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094225113)  
  
Como o sistema chegou no valor de médias de horas no valor de 66,67 e médias em valor de 9,88?  
  
Internamente o sistema refaz das verbas com sim para médias utilizando o novo salario.  
Cálculo de hora extra  
Salário (2.200,00/ 220) \* 40 horas extras = 400,00  
Valor hora 400,00 + 100% = 800,00  
Hora extra 800,00/ 12 = **66,67**  
  
Cálculo do DSR  
Hora extra (800/ 27) \* 4 = 118,52  
DSR 118,52/ 12 =  **9,88**  
  
Depois de encontrar os valores corrigidos o sistema subtraí o que foi pago na época e gera o valor de diferença.  
  
**Saiba mais**:

[RH - Linha Protheus - GPE - As férias mês seguinte devem ser recalculadas no dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16180159912727-RH-Linha-Protheus-GPE-As-f%C3%A9rias-m%C3%AAs-seguinte-devem-ser-recalculadas-no-diss%C3%ADdio?source=search)

[RH - Linha Protheus - GPE - Dissídio retroativo, o que analisar quando não calcula valores de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007824751-RH-Linha-Protheus-GPE-Diss%C3%ADdio-retroativo-o-que-analisar-quando-n%C3%A3o-calcula-valores-de-f%C3%A9rias?source=search)

[RH - Linha Protheus - GPE - Cálculo de dissídio retroativo com férias em dobro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407244881303-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-diss%C3%ADdio-retroativo-com-f%C3%A9rias-em-dobro?source=search)

[RH - Linha Protheus - GPE - Como funciona o mnemônico P\_LMEDFERD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054270134-RH-Linha-Protheus-GPE-Como-funciona-o-mnem%C3%B4nico-P-LMEDFERD?source=search)

[RH - Linha Protheus - GPE - Verbas de férias não são demonstradas no cálculo de dissídio retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059630173-RH-Linha-Protheus-GPE-Verbas-de-f%C3%A9rias-n%C3%A3o-s%C3%A3o-demonstradas-no-c%C3%A1lculo-de-diss%C3%ADdio-retroativo?source=search)
