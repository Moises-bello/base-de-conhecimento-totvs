---
article_id: 360018462732
category: RH - Rescisão
content_hash: 854cb80ac36711020d41f2d5bd6fe27eabda7da6615a30cc4ab3b95a9fc415a3
fetched_at: '2026-06-28T22:43:49.665799+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - De onde o sistema busca as informações dos campos
  Horas Normais e Horas DSR do cabeçalho da Rescisão
type: support-article
updated_at: '2025-09-09T15:10:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018462732-RH-Linha-Protheus-GPE-De-onde-o-sistema-busca-as-informa%C3%A7%C3%B5es-dos-campos-Horas-Normais-e-Horas-DSR-do-cabe%C3%A7alho-da-Rescis%C3%A3o
---

**Dúvida**De onde o sistema busca as informações dos campos **Horas Normais** e **Horas DSR** do cabeçalho da Rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Os campos são montados de acordo com dois registros: O campo **Horas Dia (RA\_HRSDIA)** do cadastro do **Funcionário** e os campos **Dias Úteis** e **Dias DSR** do cadastro de **Períodos**.  
Sistema faz a multiplicação dos campos Dias Úteis e Dias de DSR com o campo Horas Dia.  
  
Exemplo:  
Campo Horas dia no cadastro do Funcionário = 7,3333  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10985424565143)  
  
Dias Úteis = 26  
Dias de DSR = 4  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10985461064983)

**Horas Normais = Dias úteis \* horas dia =  7,3333 \* 26 = 190,6658**

**Horas DSR = Dias DSR \* horas dia =  7,3333 \* 4 = 29,3332  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10985531949079)**

Saiba mais:

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
