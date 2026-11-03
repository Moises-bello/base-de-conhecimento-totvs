---
article_id: 5433568249751
category: RH - Provisão
content_hash: ef4594736107a6ff6f4e8d28aa926292873c1f5da320616dcc0bf22174fba070
fetched_at: '2026-06-28T22:43:55.657807+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo da provisão com lançamento manual de verba
  de insalubridade que incorpora e entra para média
type: support-article
updated_at: '2025-10-24T12:32:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5433568249751-RH-Linha-Protheus-GPE-C%C3%A1lculo-da-provis%C3%A3o-com-lan%C3%A7amento-manual-de-verba-de-insalubridade-que-incorpora-e-entra-para-m%C3%A9dia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32998257680791) Tempo aproximado para leitura: **06:00:00 min** **Dúvida**Cálculo da provisão com lançamento manual de verba de insalubridade que incorpora e entra para média.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Solução****01. Situação/Requisito:**

Quando a verba de insalubridade possui configuração para incorporação e para médias e é incluída manualmente na folha do funcionário sendo que o mesmo não possui configuração no cadastro de que recebe o adicional, ao efetuar o cálculo da provisão ocorre o provisionamento duplicado do valor, pois provisiona tanto o valor como média quanto o valor de incorporação da verba.

**02. Solução:**

Ajuste no cálculo de provisão para não considerar incorporação de verbas de insalubridade/periculosidade quando estas forem incluídas manualmente e possuírem configuração para incorporação e médias, além do funcionário não possuir configuração para recebimento do adicional no cadastro, uma vez que o valor deverá ser apurado como média, assim como determina o artigo 142, parágrafo 6 da CLT.

Para detalhar o ajuste, segue exemplificação abaixo do cenário alterado:

Parametrização:

Configuração da verba:

* Codigo Verba (RV\_COD): 119;
* Id.p/Calculo (RV\_CODFOL): 0038;
* Incorp. Sal. (RV\_INCORP): S
* Media Ferias (RV\_MEDFER): S
* Media 13o. (RV\_MED13): S

Configuração do funcionário:

* Salário (RA\_SALARIO): R$ 2.000,00;
* Hrs. Insal. (RA\_INSMAX): 0,00

Parâmetro MV\_MEDDIRE: N.

No período de 01/2021, foi feito a inclusão da verba 119 conforme abaixo:

| Cod Verba | Valor |
| --- | --- |
| 119 | R$ 88,88 |

No período de 02/2021, foi feito a inclusão da verba 119 conforme abaixo:

| Cod Verba | Valor |
| --- | --- |
| 119 | R$ 161,60 |

Atualmente, a provisão efetua o provisionamento dos valores de verbas incluídas manualmente com configuração para incorporação conforme regra: valor incorporado ÷ 12 X avos de direito, e também provisiona o valor das médias conforme configuração de sindicato, configuração de verbas que entram para média, parâmetros e etc..

Na configuração de verba e funcionário citado no início, segue antes e depois para exemplificar a diferença na provisão de 13º:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5433596995607)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5433598684951)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5433653305367)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5433618718871)

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)

[Orientações Consultoria de Segmentos TIHIDZ e TIHKU3 – Insalubridade e Periculosidade em Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=126718423).
