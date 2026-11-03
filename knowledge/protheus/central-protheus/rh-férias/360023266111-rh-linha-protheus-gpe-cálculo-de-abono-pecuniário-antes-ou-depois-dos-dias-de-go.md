---
article_id: 360023266111
category: RH - Férias
content_hash: 3cb58243f9d5dcbd8c75d23c9ff1c1dbe129dedfc4aa52df6e7ab682bce60459
fetched_at: '2026-06-28T22:43:57.974895+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de abono pecuniário antes ou depois dos
  dias de Gozo das férias
type: support-article
updated_at: '2025-08-21T19:53:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023266111-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-abono-pecuni%C3%A1rio-antes-ou-depois-dos-dias-de-Gozo-das-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34354673561111) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Cálculo de abono pecuniário antes ou depois dos dias de Gozo das férias  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**No momento do cálculo das férias, no cabeçalho do cálculo existe o campo **Per. de Abono** (RH\_ABOPEC), que pode ser definido como **Antes** ou **Depois**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10605801864727)

Quando definido que o abono ocorre **antes**, apenas será permitida a geração do abono se **o período todo do abono estiver no mesmo mês de início das férias**.

O cálculo da Folha não tem como gerar dias de abono que ocorreram no mês anterior, que já foi **calculado e pago**, e mesmo que o período anterior esteja em **aberto**, **não será** **permitido.**

**Exemplos:**

* 10 dias de abono e férias com **início em 12/12** é correto, pois os dias de abono fazem parte do mesmo mês.
* 10 dias de abono e férias com **início em 06/12** não será permitido, pois o abono iniciaria no mês anterior (26/11).

Portanto, **não existe nenhuma forma de quebrar a quantidade de dias de abono** para essa situação.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10605829751319)  
  
Para que seja possível calcular o abono antes das férias, ajuste o Parâmetro **MV\_ABOPEC** - Parâmetro que libera a opção de cálculo do Abono Pecuniário respeitando a regra acima.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10605885109271)

**Saiba Mais**[RH - Linha Protheus - GPE - Como calcular e parametrizar o abono pecuniário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXzBQHAwQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBkmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MTEwNTAyMTY0NzEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tY2FsY3VsYXItZS1wYXJhbWV0cml6YXItby1hYm9uby1wZWN1bmklQzMlQTFyaW8tBjsIVDoOc2VhcmNoX2lkSSIpNjI4MWI4YjYtMTMzOS00MThmLWE2MmMtNTc3NWE1Y2UzN2FjBjsIRjoJcmFua2kIOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIWYWJvbm8gcGVjdW5pw6FyaW8GOwhUOhJyZXN1bHRzX2NvdW50aQL0AQ%3D%3D--ab02437712aca601d9d0a375ff1877602e42f109)  
[RH - Linha Protheus - GPE - Como imprimir relatório de memória de cálculo das férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhZUsrUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjMxNDcxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1pbXByaW1pci1yZWxhdCVDMyVCM3Jpby1kZS1tZW0lQzMlQjNyaWEtZGUtYyVDMyVBMWxjdWxvLWRhcy1mJUMzJUE5cmlhcwY7CFQ6DnNlYXJjaF9pZEkiKWFkNjZmMGY4LTlmYjctNDdiNy1iZjkwLTIzYjI4NGQ3ZGVjZAY7CEY6CXJhbmtpDToLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiGWNvbW8gY2FsY3VsYXIgZmVyaWFzBjsIVDoScmVzdWx0c19jb3VudGkC6wY%3D--46159d5fc82a41c9e32631151a48ed03ea48be8c)  
[RH - Linha Protheus - GPE - Cálculo de Abono Pecuniário sem o cálculo de Dias de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiCgiPTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBq2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyNDYwNTMxNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQyVDMyVBMWxjdWxvLWRlLUFib25vLVBlY3VuaSVDMyVBMXJpby1zZW0tby1jJUMzJUExbGN1bG8tZGUtRGlhcy1kZS1GJUMzJUE5cmlhcwY7CFQ6DnNlYXJjaF9pZEkiKTYyODFiOGI2LTEzMzktNDE4Zi1hNjJjLTU3NzVhNWNlMzdhYwY7CEY6CXJhbmtpDjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiFmFib25vIHBlY3VuacOhcmlvBjsIVDoScmVzdWx0c19jb3VudGkC9AE%3D--d57028f833859ea052e29f7fdadf2ade60a5c056)  
[RH - Linha Protheus - GPE - Valor de 1/3 de abono de férias não está correto o que verificar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024602612-RH-Linha-Protheus-GPE-Valor-de-1-3-de-abono-de-f%C3%A9rias-n%C3%A3o-est%C3%A1-correto-o-que-verificar)
