---
article_id: 360036671094
category: RH - Dissídio
content_hash: fe5a4bd097273c54ddea0f58a7cb4fce89d917134b0b914f1ccc941012de3196
fetched_at: '2026-06-28T22:43:43.495821+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de dissídio para funcionários que tiveram
  antecipação e aumento salarial anteriormente
type: support-article
updated_at: '2025-08-20T14:32:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036671094-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-diss%C3%ADdio-para-funcion%C3%A1rios-que-tiveram-antecipa%C3%A7%C3%A3o-e-aumento-salarial-anteriormente
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34317249366807) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como é realizado o cálculo de dissídio retroativo para funcionários que tiveram antecipação de % do dissídio e aumento salarial antes do % de dissídio ser finalizado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
 **Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
1. Cadastro do funcionário:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047990574)  
  
2. Foi realizada a antecipação salarial de acordo com o link abaixo: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016825391>  
  
Após o histórico salarial ficou da seguinte forma:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048861233)  
  
3. No mês seguinte a antecipação de salário, o funcionário teve uma promoção salarial. O histórico ficou da seguinte forma:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047991034)  
  
Nesse passo, é necessário atualizar o campo salário e salário base dissídio, pois o cálculo de dissídio será realizado também sobre o novo salário.  
  
4. No mês seguinte, cálculo de dissídio:  
  
Observe aqui, que o sistema para competência 06/2019 repeitou o salário anterior - somente com a antecipação salarial. Nessa competência foi adiantado 2% do percentual total de 3,48% e por esse motivo como diferença foi pago apenas 1,48%.  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048861653)  
  
Para competência 07/2019, onde houve a promoção o sistema reajustou o percentual total de dissídio - 3,48% sobre o salário atualizado nesta competência:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048861713)  
  
Caso o salário base dissídio não seja atualizado no momento da promoção (passo 3), o salário do funcionário na competência 07/2019, mês que houve a promoção ficará negativo e o funcionário será prejudicado, por isso é necessário aplicar o percentual sobre o salário atualizado do funcionário.  
  
O processo de cálculo da antecipação e configuração do dissídio estão no manual, deixarei o link abaixo:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=220889925>

Saiba Mais:  
[Página Centralizadora do Dissídio (GPEM690)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
