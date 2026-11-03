---
article_id: 360046160214
category: Faturamento - Cenários de Venda
content_hash: 8b743b87a358c4cf0e5121b39d2ee46f2ff147fd9b0ecfe7b3c689158a93ceb1
fetched_at: '2026-06-28T22:38:33.954435+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Para que serve
  o campo Vigência (DA1_DATVIG) na tabela de preço (OMSA010)?
type: support-article
updated_at: '2023-05-11T18:42:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046160214-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Para-que-serve-o-campo-Vig%C3%AAncia-DA1-DATVIG-na-tabela-de-pre%C3%A7o-OMSA010
---

**Dúvida**Para que serve o campo **Vigência** (**DA1\_DATVIG**) na **Tabela de Preço** (**OMSA010**)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**O campo **Vigência** (**DA1\_DATVIG**), serve para informar o valor do produto no pedido de venda a partir da data de vigência informada.   
  
Exemplo:

Tenho o produto 001 informado na tabela de preço com o valor de R$ 1.000,00 e com a data vigente de 01/01/2020 preenchido no campo **"Vigência (DA1\_DATVIG)"**. Então a partir dessa data o produto 001 vai custar R$ 1.000,00 quando for utilizar essa **Tabela de Preços** (**OMSA010**) nas operações do sistema;

Caso eu coloque o mesmo produto 001 com a data 01/02/2020 preenchido no campo **"Vigência (DA1\_DATVIG)"** e com o valor de R$ 1.200,00, quer dizer que a partir dessa data o sistema vai considerar o novo valor e desconsiderar o anterior da data 01/01/2020. Sendo assim a partir da data 01/02/2020 o produto 001 vai custar R$ 1.200,00 quando for utilizar essa **Tabela** **de Preços** (**OMSA010**) nas operações do sistema;

Mais informações sobre a tabela de preço:

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Precificação no módulo Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014623071-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Precifica%C3%A7%C3%A3o-no-m%C3%B3dulo-Faturamento)**

**[MP - FAT - Limite de Itens da tabela de preços - OMSA010](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042569273-MP-FAT-Limite-de-Itens-da-tabela-de-pre%C3%A7os-OMSA010)**

**[MP-FAT-Dúvida sobre a falta de título no browser da rotina OMSA010](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033884113-MP-FAT-D%C3%BAvida-sobre-a-falta-de-t%C3%ADtulo-no-browser-da-rotina-OMSA010)**
