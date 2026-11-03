---
article_id: 360026130474
category: RH - Rescisão
content_hash: d6dadb44cf83b22229abb0fa9ab64d60b9e192b1a97e0e2b0f4121417511ab5a
fetched_at: '2026-06-28T22:43:49.770991+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Médias na rescisão maiores que o demonstrativo
  de médias
type: support-article
updated_at: '2025-05-07T11:22:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026130474-RH-Linha-Protheus-GPE-M%C3%A9dias-na-rescis%C3%A3o-maiores-que-o-demonstrativo-de-m%C3%A9dias
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26439101629847)***Tempo aproximado para leitura:**00:01:00 min**

**Dúvida**Na conferência da rescisão, ao verificar o demonstrativo de médias com os valores de médias da rescisão, estas médias apresentam valores maiores que o demonstrativo de médias  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) GPE - Gestão de Pessoal - A partir da Versão 11.8  
  
**Solução**As médias do cálculo da rescisão podem ficar maiores que as médias que constam no demonstrativo quando na rotina Manutenção Tabelas, na Tabela S043 as colunas DSR MEDIA FER, DSR MEDIA 13ª e DSR MEDIA AV.PREVIO estão preenchidas com S, pois o sistema irá calcular um DSR sobre as médias do demonstrativo, e esse DSR sobre as médias será pago na verba da própria média, fazendo com que os valores fiquem maiores. Abaixo exemplo com média de 13ª rescisão:  
  
Tabela S043 da rotina Manutenção Tabelas, onde para o Tipo de Rescisão 24 as colunas DSR MEDIA FER, DSR MEDIA 13ª e DSR MEDIA AV.PREVIO estão com S:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040741594)  
Linha MEDIA PGTO do demonstrativo de média:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040741074)  
Então o sistema calculará um DSR sobre o valor da linha MEDIA PGTO de acordo com o cadastro de Períodos:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040742114)  
  
Valor MEDIA PGTO / 27 \* 4, então temos:  
268,77 / 27 \* 4 = 38,82  
Então para a média de 13º na rescisão, além do valor que consta no demonstrativo, será pago também na mesma verba o valor de R$ 38,82, então na verba de MEDIA 13ª RESCISÃO será pago o valor total de R$ 308,59:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040742614)  
Essa mesma fórmula de cálculo se aplica para as médias de férias e médias de aviso.  
  
E deve ser considerado para esse mesmo cálculo a configuração da proporcionalização do DSR na rescisão, pois se o DSR da rescisão estiver configurado para ser calculado proporcionalmente, o DSR das médias também será proporcional.  
  
**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
