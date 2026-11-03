---
article_id: 4404413683351
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 815229ec5afe44d4220e33f2c8ade1479fb5375f867cfe85977f10d701a68304
fetched_at: '2026-06-28T22:40:48.934341+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - TAF - TAFA438 - Cadastro de vigência
  do evento tributário
type: support-article
updated_at: '2021-07-16T10:39:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404413683351-Cross-Segmento-Backoffice-Linha-Protheus-TAF-TAFA438-Cadastro-de-vig%C3%AAncia-do-evento-tribut%C3%A1rio
---

**Dúvida**TAFA438 - Cadastro de vigência do evento tributário  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus- TAF - Todas as versões  
  
**Solução**

A rotina de apuração (TAFA444) só será processada se houver o cadastro de Vigência.

O cadastro de vigência é o relacionamento do evento tributário (TAFA433) com o período que será apurado. [Evento Tributário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404225269527-Cross-Segmento-Backoffice-Linha-Protheus-TAF-TAFA433-Cadastro-do-Evento-tributario-BLOCO-M-e-BLOCO-N)

Cadastro de Vigência:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404397076119/mceclip1.png)

A Rotina de Evento tributário (TAFA433) é Baseada na "Tributação CSLL/IRPJ" para cada apuração, há um código.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024454392/mceclip2.png)

Para apuração do **Lucro Real Anual,** deverá conter 12 cadastro mensais de vigência (TAFA438) relacionados ao evento tributário (TAFA433) "Tributação CSLL/IRPJ":

* Evento tributário código 000002- Lucro Real, Estimativa por levantamento de Balanço e/ou
* Evento tributário código 000003- Estimativa por Receita Bruta

Mais uma vigência referente ao  Ajuste anual ( 01/jan/xx à 31/12/xx)

* Evento tributário código 000001- LUCRO REAL (Ajuste anual)

Totalizando 13 cadastros de vigência (TAFA438)

Empresas de **Lucro Real Trimestral**, terão 4 cadastros de Vigência no período, relacionados somente ao

* Evento tributário código 000002- Lucro Real, Estimativa por levantamento de Balanço

Empresas de **Lucro Presumido**, terão 4 cadastros de Vigência no período, relacionados somente ao

* Evento tributário código 000003- Estimativa por Receita Bruta

**Saiba Mais**

Base de calculo do LALUR**: [Base de calculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063097093-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS300-TAFA344-Quais-valores-o-TAF-considera-para-Base-de-c%C3%A1lculo-IRPJ-CSLL-)**

Cadastro Evento Tributário: [Evento Tributário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404225269527-Cross-Segmento-Backoffice-Linha-Protheus-TAF-TAFA433-Cadastro-do-Evento-tributario-BLOCO-M-e-BLOCO-N)

Simulação LALUR: [Simulação apuração IRPJ/CSLL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402387769623-Cross-Segmento-Backoffice-Linha-Protheus-TAF-TAFA433-Simula%C3%A7%C3%A3o-apura%C3%A7%C3%A3o-LALUR)
