---
article_id: 38690065257751
category: Financeiro - Liquidação a Receber
content_hash: f6b1f39e278419b69137e0cafa6c55b8cc7e14e87cf52da6b1469f289ad5dd29
fetched_at: '2026-06-28T22:37:42.301596+00:00'
product: protheus
section_id: 33830247616663
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA460 - Parâmetro
  MV_VL460NT
type: support-article
updated_at: '2026-02-27T19:01:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38690065257751-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA460-Par%C3%A2metro-MV-VL460NT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38690056753815) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Qual a funcionalidade do parâmetro **MV\_VL460NT**?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.

**Solução**  
Criado o parâmetro **MV\_VL460NT**, este permitirá ao cliente escolher como o sistema irá gerar os títulos de impostos de retenção.

**MV\_VL460NT = 1** – Informará ao sistema que, no momento da liquidação, os títulos de abatimentos (impostos) serão gerados de acordo com a natureza informada.

Exemplos:

**Caso 01**

Considerando 3 títulos a receber liquidados, sendo:

| LIQ | LIQ001 | R$ 1.000,00 | com IR na emissão |
| --- | --- | --- | --- |
| LIQ | LIQ002 | R$ 2.000,00 | sem retenção de impostos |
| LIQ | LIQ003 | R$ 3.000,00 | Com IR na baixa. |
|

**Liquidados em um título com natureza que calcule PCC e IR.**

Será realizada a baixa dos títulos liquidados (LIQ001, LIQ002 e LIQ003) juntamente com seus impostos e gerado um novo título no valor de R$ 6.000,00.

A base de cálculo dos impostos (PCC e IR) será o valor total liquidado, isto é, R$ 6.000,00.

Total dos novos títulos = R$ 6.000,00

Base de cálculo do IR = R$ 6.000,00.

Base de cálculo do PCC = R$ 6.000,00.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38690056754839)

### 

**Caso 02**

**Não calcula X não calcula**

Caso um título origem tenha uma natureza que não calcula impostos, e a natureza usada para liquidação também seja uma natureza que não calcula impostos, a rotina somente irá baixar o título origem e gerar os novos títulos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38690065224215)

**Caso 03**

**Não calcula x calcula**

Caso um título origem tenha uma natureza que não calcula impostos, e a natureza usada para liquidação seja uma natureza que calcula impostos (INSS, ISS, IRRF, PCC), a rotina irá baixar o título origem, gerar os novos títulos e gerará também os títulos de impostos para os novos títulos.

**Observações:**

* Se a natureza usada na liquidação for para cálculo de impostos como INSS, ISS ou IRRF, os títulos de impostos serão gerados somente em 01 parcela, mesmo que a condição de pagamento seja em várias parcelas.
* Se a natureza usada na liquidação for para cálculo de impostos de PCC e a condição de pagamento usada para liquidação for em várias parcelas, os títulos de impostos PCC serão gerados de acordo com o número de parcelas definidas na condição de pagamento.

Exemplo de natureza que calcula IR:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38690056756503)

Exemplo de natureza que calcula PCC e condição de pagamento de 3 parcelas:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38690056757655)

**Caso 04**

**Calcula x Não calcula**

Caso um título de origem tenha uma natureza que calcula impostos (INSS, ISS, IRRF, PCC), e a natureza usada para liquidação seja uma natureza que não calcula impostos, a rotina irá baixar tanto o título de origem quanto seus títulos de impostos e irá gerar os novos títulos com o valor já líquido, isto é, já descontando as retenções.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38690065231383)

**Caso 05**

**Calcula x calcula.**

Caso um título origem tenha uma natureza que calcula impostos (INSS, ISS, IRRF, PCC), e a natureza usada para liquidação seja uma natureza que também calcula impostos, a rotina irá baixar o título origem e seus impostos e gerará os novos títulos tomando como base o valor total dos títulos baixados, e gerará também os impostos dos novos títulos de acordo com a natureza usada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38690065232791)

**MV\_VL460NT = 2** – Informará ao sistema que, no momento da liquidação, os títulos de abatimentos (impostos) serão gerados com os mesmos valores e base de cálculo dos títulos que estão sendo baixados.

Exemplos:

**Caso 01**

Considerando 3 títulos a receber liquidados, sendo:

| LIQ | LIQ001 | R$ 1.000,00 | Com IR na emissão. |
| --- | --- | --- | --- |
| LIQ | LIQ002 | R$ 2.000,00 | sem retenção de impostos |
| LIQ | LIQ003 | R$ 3.000,00 | Com IR na baixa. |
|

**Liquidados em um título com natureza que calcule PCC e IR**

Será realizada a baixa dos títulos liquidados (LIQ001, LIQ002 e LIQ003) juntamente com seus impostos e gerado um novo título no valor de R$6.000,00.

A base de cálculo do PCC (Imposto que não está presente nos títulos liquidados) será o valor total liquidado, isto é, R$ 6.000,00.

A base de cálculo do IR (presente nos títulos LIQ001 e LIQ002) será calculada de acordo com os títulos liquidados que possuem esses impostos (LIQ001 e LIQ003), isto é, R$ 4.000,00.

Total dos novos títulos = R$ 6.000,00

Base de cálculo do IR = R$ 4.000,00

Base de cálculo do PCC = R$ 6.000,00

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38690056765591)

**Caso 02**

**Ex.: Títulos** do mesmo cliente a serem liquidadas.

| SIM | FIN460120 | R$ 10.000,00 | sem retenções |
| --- | --- | --- | --- |
| CIM | FIN460120 | R$ 10.000,0 | com retenção de PCC |
|

**PIS** – R$ 65,00  
**Base PIS** – R$ 10.000,00

**COFINS** – R$ 300,00  
**Base Cofins** – R$ 10.000,00

**CSLL** – R$ 100,00  
**Base CSLL** – R$ 10.000,00

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38690065235607)

**Novo título gerado na negociação:**

| LIQ | FIN460120 | R$ 20.000,00 | com retenção de PCC |
| --- | --- | --- | --- |
|
|  |

**PIS** – R$ 65,00  
**Base PIS** – R$ 10.000,00

**COFINS** – R$ 300,00  
**Base Cofins** – R$ 10.000,00

**CSLL** – R$ 100,00  
**Base CSLL** – R$ 10.000,00

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38690065237655)

**Caso 03**

Considerando 2 títulos a receber liquidados, sendo:

| NF1 | NF0000001 | R$ 10.000,00 | PCC e IRRF na baixa. Título com duas baixas parciais, 1ª baixa de R$ 3.000,00 2º baixa de R$ 5.000,00  Saldo do título R$ 1508,00 |
| --- | --- | --- | --- |
| NF2 | NF0000002 | R$ 5.000,00 | PCC e IRRF na baixa Título sem baixa parcial. |
|

**Liquidados em um título com natureza que calcule PCC e IR**

Será realizada a baixa dos títulos liquidados (NF1 e NF2) juntamente com seus impostos e gerado um novo título no valor de R$6.508,00.

O novo título gerado na liquidação, terá como base de cálculo dos impostos PCC e IRRF o valor de **R$ 7.000,00.**

**Observação**

Se no momento da liquidação for usada uma natureza que calcule impostos que não existam nos títulos que estão sendo liquidados, o sistema irá **manter os valores das retenções e valores da base de cálculo dos existentes** e irá calcular os novos impostos para a somatória dos valores dos títulos em liquidação.

Para que as retenções não sejam geradas, e desde que o ambiente tenha o cálculo do PCC pelo regime Caixa (na baixa), o parâmetro **MV\_VL460NT** deve estar com o conteúdo igual a **'3'.**

**MV\_VL460NT = 3** – Informará ao sistema que, no momento da liquidação, os títulos de abatimentos (impostos) serão gerados de acordo com o valor dos títulos, levando em conta apenas os impostos por eles retidos. Caso seja informada uma natureza com retenção de impostos que não são retidos pelos títulos pais, essas retenções são desconsideradas.

**Importante**: Essa opção de parâmetro (MV\_VL460NT = 3) não deve ser usada em ambiente em que o PCC é gerado na baixa do título (MV\_BR10925 = 1).

Considerando 3 títulos a receber liquidados, sendo:

| LIQ | LIQ001 | R$ 1.000,00 | com IR na emissão |
| --- | --- | --- | --- |
| LIQ | LIQ002 | R$ 2.000,00 | sem retenção de impostos |
| LIQ | LIQ003 | R$ 3.000,00 | com IR na baixa |
|

**Liquidados em um título com natureza que calcule PCC e IR**

Será realizada a baixa dos títulos liquidados (LIQ001, LIQ002 e LIQ003) juntamente com seus impostos e gerado um novo título no valor de R$6.000,00. Apenas os impostos presentes nos títulos-pais serão considerados, e terão sua base de cálculo baseada nos títulos liquidados (LIQ001 e LIQ003).

Total dos novos títulos = R$ 6.000,00

Base de cálculo do IR = R$ 4.000,00.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38690056770583)

**Saiba mais**

[Fina460 - Liquidação a receber](https://tdn.totvs.com/pages/releaseview.action?pageId=545236275#FINA460Liquida%C3%A7%C3%A3oareceberP12-01.VIS%C3%83OGERAL)

[MP - SIGAFIN - FINA460 - Gerar liquidação com natureza diferente do título pai que calcula impostos na emissão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002710662-MP-SIGAFIN-FINA460-Gerar-liquida%C3%A7%C3%A3o-com-natureza-diferente-do-t%C3%ADtulo-pai-que-calcula-impostos-na-emiss%C3%A3o)
