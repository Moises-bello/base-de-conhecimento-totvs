---
article_id: 22658839180311
category: RH - Férias
content_hash: b03a8c95f85494b7c9e2cba113acd61b79a0e950286b7e6d7a4785eda032bca8
fetched_at: '2026-06-28T22:43:58.211916+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Como verificar qual tipo de Férias foi calculada
  para o Funcionário
type: support-article
updated_at: '2025-07-28T17:28:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22658839180311-RH-Linha-Protheus-GPE-Como-verificar-qual-tipo-de-F%C3%A9rias-foi-calculada-para-o-Funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22658826972951) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como verificar qual tipo de Férias foi calculada para o Funcionário?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O histórico das Férias é gravado na tabela SRH, e nela existe o campo **Tipo de Cálculo (RH\_TIPCAL),** que pode ser gravado com as seguintes legendas:  
**> N - Férias normais/individuais** calculadas pela rotina GPEM030 **> P - Férias Programadas** calculadas pela rotina GPEM060 com a opção Férias Programadas **> C - Férias Coletivas** calculadas pela rotina GPEM060 com a opção Férias Coletivas  
  
Ao gerar a [Consulta Genérica](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052080693-RH-Linha-Protheus-GPE-Consulta-de-informa%C3%A7%C3%B5es-em-arquivos-por-Consulta-Gen%C3%A9rica) da tabela SRH, é possível visualizar o campo e seu conteúdo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22658839160599)

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Como calcular férias na versão 12](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj3%2FJrSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBh2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNTY1ODIzMS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jYWxjdWxhci1mJUMzJUE5cmlhcy1uYS12ZXJzJUMzJUEzby0xMgY7CFQ6DnNlYXJjaF9pZEkiKWMwMTk3NTIwLTY2MDItNDJhOC05ZmQ1LTQ4ZWIxYTc2ZDViZgY7CEY6CXJhbmtpCDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiFWNhbGN1bGFyIGbDqXJpYXMGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--df0b5327749f69ba442cc71343d9b4f4ea0ff88d)  
[RH - Linha Protheus - GPE - Como calcular férias coletivas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhZJfk%2BXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBgGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDAxMDE3MjEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tY2FsY3VsYXItZiVDMyVBOXJpYXMtY29sZXRpdmFzBjsIVDoOc2VhcmNoX2lkSSIpYzAxOTc1MjAtNjYwMi00MmE4LTlmZDUtNDhlYjFhNzZkNWJmBjsIRjoJcmFua2kHOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIVY2FsY3VsYXIgZsOpcmlhcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--685e7e005fadc9001ae63645a62a6a6757f54c3d)  
[RH - Linha Protheus - GPE - Como calcular férias programadas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwitBzY%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBgmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDQwOTE4MjEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tY2FsY3VsYXItZiVDMyVBOXJpYXMtcHJvZ3JhbWFkYXMGOwhUOg5zZWFyY2hfaWRJIiljMDE5NzUyMC02NjAyLTQyYTgtOWZkNS00OGViMWE3NmQ1YmYGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhVjYWxjdWxhciBmw6lyaWFzBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--ee480e05a0ce6876172314a6d3d5fc4b343387ab)  
[RH - Linha Protheus - GPE - Como visualizar histórico de férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXqHR5bxM6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBi2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzIxMzY5NDk5OTg2MDcxLVJILUxpbmhhLVByb3RoZXVzLUdQRS1Db21vLXZpc3VhbGl6YXItaGlzdCVDMyVCM3JpY28tZGUtZiVDMyVBOXJpYXMGOwhUOg5zZWFyY2hfaWRJIikzMTNkOTZmMS1lYzJjLTRlMTEtYmE3ZS0xNTlkOTMxYjljMjAGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhpoaXN0w7NyaWNvIGRlIGbDqXJpYXMGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--234ff53b3a00100010b38487891e3eb0ccbd9c42)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
