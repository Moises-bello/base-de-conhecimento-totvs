---
article_id: 360037036014
category: RH - Rescisão
content_hash: e3977883a4c7493bbc6588a8184f895fc25cccf3ca0ab832c3feb264227c6eb4
fetched_at: '2026-06-28T22:43:49.654282+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Criação do campo RR_VALORI ( valor Orginal) para
  rescisões complementares
type: support-article
updated_at: '2025-05-07T11:23:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037036014-RH-Linha-Protheus-GPE-Cria%C3%A7%C3%A3o-do-campo-RR-VALORI-valor-Orginal-para-rescis%C3%B5es-complementares
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26439059433239)***Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como conferir numa rescisão complementar os valores que ja foram calculados na rescisão principal?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) GPE - Gestão de Pessoal – A partir da versão 12.1.17

**Solução**

Criação do campo RR\_VALORI (Valor Original), onde será gravado, no cálculo da rescisão complementar, o valor original da verba calculada na rescisão anterior, facilitando a conferência dos valores gerados na rescisão complementar.

Este campo será exibido em tela apenas no cálculo ou visualização de rescisões complementares.

Para que a melhoria esteja disponível faz-se necessário a utilização do [UPDDISTR](http://tdn.totvs.com/x/nJLYCg) (somente p/ release 12.1.17) com o diferencial constante no pacote de atualização.

**Importante**

-Nas rescisões complementares dendro do mesmo mês da rescisão principal o campo não sera apresentado ou preenchido

-A verba com ID 0318- Salario Base não terá o campo RR\_VALOR preenchido

**Calculo da Rescisão principal  em 01/2019**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048571594)

**Calculo da complementar por alteração salarial, mês seguinte 02/2019.**

RR\_VALORI (Valor Original), com os valores gerados na rescisão principal.

Verba de Id 0318- Salário Base, valor = 0,00

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049466653)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048571974)

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
