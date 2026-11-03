---
article_id: 360028983511
category: RH - Dissídio
content_hash: 025a5ca355dd93c70226463e9fbd9f12bc541905fd6f9aa5578f22177fe90757
fetched_at: '2026-06-28T22:43:44.288181+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Nunca fiz dissidio, qual a configuração inicial
type: support-article
updated_at: '2025-08-20T14:31:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028983511-RH-Linha-Protheus-GPE-Nunca-fiz-dissidio-qual-a-configura%C3%A7%C3%A3o-inicial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34317243416983) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Nunca fiz dissidio, qual a configuração inicial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**A primeira situação a ser analisada são as configurações das verbas:

No cadastro de verbas > aba dissidio, verifique se as verbas que devem entrar para o cálculo de dissidio estão com SIM e se estão amarradas corretamente a verba para cálculo

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029807691)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029807731)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029817632)

As verbas estando cadastradas corretamente, pode-se efetuar o cálculo utilizando a rotina de dissidio retroativo.  
  
Verifique principalmente as **verbas de férias mês seguinte**, pois essas verbas não devem entrar para cálculo do dissidio, pois o sistema vai calcular de acordo com as verbas mês geradas na SRD. Então por exemplo, as férias calculadas em abril geraram verbas de férias mês e mês seguinte e em maio as verbas mês seguinte de abril se transformam em verbas mês e serão calculadas no dissidio retroativo.  
  
O sistema buscará a informação de salário para calcular o dissidio retroativo através do campo **Salário Base Dissidio no cadastro do funcionário**. Caso esse campo esteja em branco ou com valor diferente do esperado, deve ser ajustado para que no cálculo do dissidio o sistema busque a informação correta.   
  
Antes de calcular o dissidio retroativo, analise o cadastro de verbas afim de assegurar a parametrização e cálculo correto para o dissidio retroativo.

Mais informações sobre a configuração das verbas, acesse o link abaixo:

<http://tdn.totvs.com/pages/releaseview.action?pageId=220889925>

Saiba Mais:  
[Página Centralizadora do Dissídio (GPEM690)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
