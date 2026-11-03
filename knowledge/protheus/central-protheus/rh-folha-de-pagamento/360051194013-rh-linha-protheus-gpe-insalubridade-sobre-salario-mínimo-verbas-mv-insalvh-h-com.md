---
article_id: 360051194013
category: RH - Folha de Pagamento
content_hash: b014a6d5bc20f8ec78fecde8ea64039b67c8261848bb7d79bb293173e98ea1ea
fetched_at: '2026-06-28T22:44:15.016137+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Insalubridade sobre salario mínimo + verbas - MV_INSALVH
  = H com faltas
type: support-article
updated_at: '2025-08-12T12:46:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051194013-RH-Linha-Protheus-GPE-Insalubridade-sobre-salario-m%C3%ADnimo-verbas-MV-INSALVH-H-com-faltas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26334462540823)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Insalubridade sobre salario mínimo + verbas - MV\_INSALVH = H com faltas.   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

Quando o parâmetro MV\_INSALVH está configurado com H, a base da insalubridade é o salario mínimo + verbas recalculadas baseadas no salario mínimo e não no salario contratual, obedecendo as seguintes regras.

* verbas devem ser do do Tipo "H"
* incidência para Insalubridade
* incidência para Hora Extra
* verba de DSR(ID 0035) sempre entra
* verbas de Faltas/Atrasos

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078400273)  
  
**Importante**

As horas extras não são valorizadas neste caso, é usado apenas a referência conforme a fórmula: ( Salário Minimo / Horas do Mês ) \* Horas Extras => ( 880 / 220 ) \* 50 => 200,00

Para que as horas sejam valorizadas deverá alterar o conteúdo do parâmetro P\_VALHOADIC

**Saiba Mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Para que serve o mnemônico P\_VALHOADIC](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj%2Bu63UUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBh2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDQ0MTIxNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUGFyYS1xdWUtc2VydmUtby1tbmVtJUMzJUI0bmljby1QLVZBTEhPQURJQwY7CFQ6DnNlYXJjaF9pZEkiKTE3MDVlY2RmLTdkMDItNGU4ZC04NTM3LWVmZWQzYzE0ZGUyNwY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiSFJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBQYXJhIHF1ZSBzZXJ2ZSBvIG1uZW3DtG5pY28gUF9WQUxIT0FESUMGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--c38cfcbe32b6127bd2bd62ad630d1d1a515b169c)
