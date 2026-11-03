---
article_id: 360024752653
category: RH - Provisão
content_hash: 73f0f32daaad1876cbe0d05d60ed9d386fb8ebdd0ad1dcdda992a63f191229e5
fetched_at: '2026-06-28T22:43:55.900366+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Ferias partidas na provisão parâmetro MV_TPBXFER
type: support-article
updated_at: '2025-11-03T12:02:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024752653-RH-Linha-Protheus-GPE-Ferias-partidas-na-provis%C3%A3o-par%C3%A2metro-MV-TPBXFER
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32903306439191)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como é utilizado o parâmetro **MV\_TPBXFER** na baixa das férias?   
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**O parâmetro **MV\_TPBXFER** indica se a baixa será feita total ou parcial quando funcionário possuir férias partidas.

**Habilitado com  1** - Indica que a baixa de provisão será feita em sua totalidade no mês de saída.

**Obs:** Este conceito é o padrão do sistema, portanto, para os clientes que não possuírem o parâmetro, a baixa da provisão será feita em sua totalidade no primeiro mês de férias.

**Exemplo:**  
Funcionário com gozo de Férias de 03/10/2022 à 01/11/2022.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14228126683415)

Veja que com o parâmetro configurado com 1, é realizada toda a Baixa de Férias no mês inicial.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14228693313559)

Quando o parâmetro é **habilitado com 2** - Indica que o valor de baixa de provisão será feito dentro do mês e também no mês seguinte respeitando assim a quebra das férias.  
  
Exemplo:

Funcionário com gozo de Férias de 03/10/2022 à 01/11/2022.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14228126683415)

Veja que a Baixa é Partida entre o mês e mês seguinte, quando o parâmetro está configurado com 2.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14228513897495)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14229102595479)

**Saiba Mais:**  
[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
