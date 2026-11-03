---
article_id: 1500009448741
category: RH - Consulta Cálculo
content_hash: 557f97c30260a28edae76a1b13a3a33daed28e74d4a394e224dadb499e5a21f2
fetched_at: '2026-06-28T22:43:13.536870+00:00'
product: protheus
section_id: 360010855834
source: central-protheus
title: RH - Linha Protheus - GPE - Calculo de id 0318 para funcionário desligado
type: support-article
updated_at: '2024-07-10T15:37:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009448741-RH-Linha-Protheus-GPE-Calculo-de-id-0318-para-funcion%C3%A1rio-desligado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24790619334039) Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**  
Como evitar a geração do id 0318 na folha de funcionário desligado no mês anterior?

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Solução:**

Quando o sistema gerar cálculo de folha com id 0318 para funcionário desligado, verifique se o campo

RA\_DTGERAR  da rescisão está preenchendo dentro do período da rescisão. O mesmo deve estar preenchido conforme o help de campo:

Neste campo deve ser digitada a Data de  
Geração na Folha. Deve estar dentro do  
mesmo Mês/Ano da Folha em Aberto e/ou  
não pode ser maior que o Mês/Ano da Data  
de Demissão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24790619345943)

Exemplo:

Se a rescisão ocorrer em 31/03/2021 a sua data geração não pode ser maior que a data de demissão, pois desta forma quando executar o cálculo da folha no mês 04 o sistema irá gerar o id 0318 para o funcionário demitido.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014345402)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014625841)  
  
**Saber Mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
