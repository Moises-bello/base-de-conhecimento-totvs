---
article_id: 360016647531
category: RH - Rescisão
content_hash: 1ac18b201284d0c869fe26ebd5e28332cd9c95b13a90c191da57ecd3bfebcf6e
fetched_at: '2026-06-28T22:43:48.373549+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE -  Dias de Faltas injustificadas não estão abatendo
  nas Férias da Rescisão
type: support-article
updated_at: '2025-09-08T18:45:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016647531-RH-Linha-Protheus-GPE-Dias-de-Faltas-injustificadas-n%C3%A3o-est%C3%A3o-abatendo-nas-F%C3%A9rias-da-Rescis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34788846795927)** **Tempo aproximado para leitura: 00:03:00 min****Ocorrência**Ao tentar realizar o Cálculo de Rescisão (GPEM040) para funcionários que possuem faltas injustificadas nos acumulados (SRD), não estão sendo abatidos dos dias de direito de Férias.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Solução**Para solucionar essa ocorrência, verifique os seguintes dados:  
  
1. A verba de Faltas com **ID 0054** deve conter no campo Médias Férias o conteúdo S;   
2. Para abater os dias de Férias deverá conter mais de 6 faltas injustificadas dentro do mesmo período aquisitivo;  
3. Observar se o campo **RF\_DFALVAT** do Controle Dias de Direito contem o número de faltas injustificadas;  
4. Criado o parâmetro **MV\_SEGFALT** que define se gera as faltas de forma analítica, onde se utilizado o conteúdo .F. é olhado o campo **RD\_DATARQ** e se utilizado o conteúdo .T. é olhado o campo RD\_DTREF.

**Saiba Mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)

[RH - Linha Protheus - GPE - Abatimento faltas nos avos férias proporcionais rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXpox9Gww6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBoGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzEzMzEyMjEwMDE5OTkxLVJILUxpbmhhLVByb3RoZXVzLUdQRS1BYmF0aW1lbnRvLWZhbHRhcy1ub3MtYXZvcy1mJUMzJUE5cmlhcy1wcm9wb3JjaW9uYWlzLXJlc2NpcyVDMyVBM28GOwhUOg5zZWFyY2hfaWRJIikzNzcxN2JjYy1mMGQ5LTQ5OWQtYjY1ZS1iMzIxMzk2NTAwYTAGOwhGOglyYW5raQk6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhVmYWx0YXMgcmVzY2lzw6NvBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--92592c363c15ce2890a9d5f00aa5c526cd5ac6f4)  
[RH - Linha Protheus - GPE - Funcionamento do parâmetro MV\_SEGFALT nas faltas no Controle Dias de Direito](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgayLLUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBrWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDc3MTk5NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtRnVuY2lvbmFtZW50by1kby1wYXIlQzMlQTJtZXRyby1NVi1TRUdGQUxULW5hcy1mYWx0YXMtbm8tQ29udHJvbGUtRGlhcy1kZS1EaXJlaXRvBjsIVDoOc2VhcmNoX2lkSSIpZTFlNGNjODYtYmE4ZS00ODc0LThkYmEtYzA4NDI4OTEzOTNkBjsIRjoJcmFua2kJOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIPTVZfU0VHRkFMVAY7CFQ6EnJlc3VsdHNfY291bnRpAvME--9a9c167b7ec1f9659f159dda3932dd9f873b5137)  
[RH - Linha Protheus - GPE - Como fazer a contagem dos avos de férias vencidas e proporcionais na rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiUq0HSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBs2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAwOTgwNDY5Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1mYXplci1hLWNvbnRhZ2VtLWRvcy1hdm9zLWRlLWYlQzMlQTlyaWFzLXZlbmNpZGFzLWUtcHJvcG9yY2lvbmFpcy1uYS1yZXNjaXMlQzMlQTNvBjsIVDoOc2VhcmNoX2lkSSIpOTk5OWI4ODctMzZlZS00NjMxLWI5MmQtYTc2ZTBhZDMwN2I0BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJwUkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIENvbW8gZmF6ZXIgYSBjb250YWdlbSBkb3MgYXZvcyBkZSBmw6lyaWFzIHZlbmNpZGFzIGUgcHJvcG9yY2lvbmFpcyBuYSByZXNjaXPDo28GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--87ed95f25dac1ca62b66cccdd089e811a4403be4)  
[RH - Linha Protheus - GPE - Por que o sistema está considerando as faltas para abatimento de avos mesmo alterando a quantidade na rotina de Controle de Dias de Direito?](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhteNLTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB7Wh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAzNjA3MTUzMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUG9yLXF1ZS1vLXNpc3RlbWEtZXN0JUMzJUExLWNvbnNpZGVyYW5kby1hcy1mYWx0YXMtcGFyYS1hYmF0aW1lbnRvLWRlLWF2b3MtbWVzbW8tYWx0ZXJhbmRvLWEtcXVhbnRpZGFkZS1uYS1yb3RpbmEtZGUtQ29udHJvbGUtZGUtRGlhcy1kZS1EaXJlaXRvLQY7CFQ6DnNlYXJjaF9pZEkiKTM3NzE3YmNjLWYwZDktNDk5ZC1iNjVlLWIzMjEzOTY1MDBhMAY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiFWZhbHRhcyByZXNjaXPDo28GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--84a32366abffb89d0bbe531fc88388eade29c76b)
