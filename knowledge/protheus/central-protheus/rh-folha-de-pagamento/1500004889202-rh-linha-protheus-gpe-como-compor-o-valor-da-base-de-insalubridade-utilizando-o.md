---
article_id: 1500004889202
category: RH - Folha de Pagamento
content_hash: fd4069c521917475d201fcbd6fc0b33f12ae36f4ac186a90f96b218ed1acf6a9
fetched_at: '2026-06-28T22:44:13.228353+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como compor o valor da base de insalubridade utilizando
  o parâmetro MV_INSALVH e o mnemônico P_VALHOADIC
type: support-article
updated_at: '2025-08-12T14:21:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004889202-RH-Linha-Protheus-GPE-Como-compor-o-valor-da-base-de-insalubridade-utilizando-o-par%C3%A2metro-MV-INSALVH-e-o-mnem%C3%B4nico-P-VALHOADIC
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34123853381527) Tempo aproximado para leitura: 00:04:00 min**

**Dúvida**Como compor o valor da base de insalubridade utilizando o parâmetro MV\_INSALVH e o mnemônico P\_VALHOADIC

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17

**Solução**Quando temos o parâmetro MV\_INSALVH = H e o mnemônico P\_VALHOADIC=.T. o sistema recalcula os valores para montar a base da insalubridade da seguinte forma:

Cadastro do sindicato:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006454442)

Cadastro do funcionário:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006614121)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006614061)

Cálculo da folha demonstrando o adicional + as verbas de composição do cálculo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006613161)  
  
Ele pega o valor do salário mínimo R$ 1.100,00 (pela definição no cadastro de sindicato) e divide pela quantidade de horas do funcionário 220, chegando a um valor de 5,50.  
  
O mnemônico valoriza a quantidade de horas lançadas de acordo com o percentual da verba 55%. Logo ao invés de 10 horas teremos 15,50 horas. Lembrando que essa valorização ocorre apenas para a verba de H.E. a de DSR continua com a mesma referência trazida pelo sistema.  
  
Logo:  
15,50 \* 5,00 = 77,50  
2,98 \* 5,00 = 14,90  
  
1100,00 + 77,50 + 14,90 = 1192,40 - valor base da insalubridade.  
  
1192,40 \* 20% = 238,48 - valor de insalubridade.  
  
Para encontrar a referência de horas geradas na insalubridade o sistema aplica os 20% sobre as 220 horas que é igual a 44 conforme apresentado no cálculo.

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[RH - Linha Protheus - GPE - Insalubridade sobre salario mínimo + verbas - MV\_INSALVH = H com faltas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwidOLnUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBomh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MTE5NDAxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtSW5zYWx1YnJpZGFkZS1zb2JyZS1zYWxhcmlvLW0lQzMlQURuaW1vLXZlcmJhcy1NVi1JTlNBTFZILUgtY29tLWZhbHRhcwY7CFQ6DnNlYXJjaF9pZEkiKWY1OTIwOTc3LTAwN2QtNDFlYi05YWM3LTRjMzc2MmI3Y2Y2OQY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiaVJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBJbnNhbHVicmlkYWRlIHNvYnJlIHNhbGFyaW8gbcOtbmltbyArIHZlcmJhcyAtIE1WX0lOU0FMVkggPSBIIGNvbSBmYWx0YXMGOwhUOhJyZXN1bHRzX2NvdW50aQLoAw%3D%3D--d8844584f9178c57b4e9013dfc552b06ddf15dba)  
[RH - Linha Protheus - GPE - Para que serve o mnemônico P\_VALHOADIC](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj%2Bu63UUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBh2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDQ0MTIxNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUGFyYS1xdWUtc2VydmUtby1tbmVtJUMzJUI0bmljby1QLVZBTEhPQURJQwY7CFQ6DnNlYXJjaF9pZEkiKTMwZmQwYTFmLWIyN2YtNDU5Mi1hMmRkLWJkYjM5MjBlNDNlMAY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiSFJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBQYXJhIHF1ZSBzZXJ2ZSBvIG1uZW3DtG5pY28gUF9WQUxIT0FESUMGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--f4de231a058975456a13259ab40ed48207436fda)
