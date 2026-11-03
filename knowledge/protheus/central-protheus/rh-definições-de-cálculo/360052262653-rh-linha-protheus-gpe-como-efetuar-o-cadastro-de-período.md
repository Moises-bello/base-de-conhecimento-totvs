---
article_id: 360052262653
category: RH - Definições de Cálculo
content_hash: 8584692f78198b65209211338842746cf3d7e9c8414aec5128f24f105ce4258e
fetched_at: '2026-06-28T22:43:22.380988+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Como efetuar o cadastro de período
type: support-article
updated_at: '2025-09-30T11:34:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052262653-RH-Linha-Protheus-GPE-Como-efetuar-o-cadastro-de-per%C3%ADodo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:04:00 min**

**Dúvida**Como efetuar o cadastro de período?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
1. Antes de iniciar o cadastro de períodos é necessário possuir:

* **Processos cadastrados:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082273913/mceclip0.png)**

O processo, para o módulo SIGAGPE, define em que cálculo se enquadra o funcionário. Ele serve como agrupador no momento da realização dos cálculos.

Por exemplo: funcionários celetistas mensalistas, celetistas semanalistas, autônomos mensalistas, autônomos semanalistas.

O sistema traz, por padrão, esses quatro processos já cadastrados. Porém, se desejar, é possível cadastrar qualquer processo.

* **Roteiros de cálculo:**

É necessário possuir os roteiros carregados em **Atualizações / Definições de Cálculo / Roteiros de Cálculos:**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081165934/mceclip2.png)**

* **Parâmetros definidos:**

Parâmetro **MV\_DIASPER:** Define como será a regra de calculo em relação aos dias do mês, se será considerado o divisor por 30 dias ou a quantidade dias do mês. [RH - Linha Protheus - GPE - Como configurar o parâmetro MV\_DIASPER para definir regra de calculo](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjBLjXVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBpWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1OTMxNzk1My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb25maWd1cmFyLW8tcGFyJUMzJUEybWV0cm8tTVYtRElBU1BFUi1wYXJhLWRlZmluaXItcmVncmEtZGUtY2FsY3VsbwY7CFQ6DnNlYXJjaF9pZEkiKWQ5OGI4ODZmLWU0ZWQtNGNiZC05NWMxLWE2N2QxZmYxNzA5NQY7CEY6CXJhbmtpCToLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiD01WX0RJQVNQRVIGOwhUOhJyZXN1bHRzX2NvdW50aQLZBA%3D%3D--80f984956f76eaa1c9eb2283f0bbe7659e97af49)

Parâmetro **MV\_TPCALEN:** Indica o tipo de edição para o calendário do período. O valor padrão é 1 que indica calendário analítico ou 2 calendário sintético. [RH - Linha Protheus - GPE - Como configurar o parâmetro MV\_TPCALEN](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhDkiLHGgA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBiGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExNTAxMDA4MTM0Ny1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb25maWd1cmFyLW8tcGFyJUMzJUEybWV0cm8tTVYtVFBDQUxFTi0GOwhUOg5zZWFyY2hfaWRJIik5YWM3ZjZiZS1lZTk2LTRmM2ItOGI0Yi1lYTU3M2NmMGY1NjkGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIg9NVl9UUENBTEVOBjsIVDoScmVzdWx0c19jb3VudGkC2QQ%3D--7b7013be5c3a73694df2bf8373994ca77e786afc)

2. Para cadastrar o período acesse: **Atualizações/ Definições de Cálculo/ Períodos** e selecione a opção Incluir. Preencha os campos obrigatórios e cadastre um Roteiro de cálculo conforme regra da Empresa e selecione a opção Confirmar.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10759495802775)

Para ativar o roteiro, o campo **Per Ativo** deve ser alterado para **1-Sim**

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10760055013399)**

3. Finalizado o cadastro ficará da seguinte forma:

* **Processos na parte superior e Períodos na parte inferior**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10759696086679)

* **Aba Cadastro de Calendário (Parâmetro MV\_TPCALEN: 1)**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10759875222039)

**Saiba mais:**

[RH - Linha Protheus - GPE - Parâmetros utilizados para o cadastro de período GPEA400](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiX6TKcqQc6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBn2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzg0MjUwNTE0NDk3NTEtUkgtTGluaGEtUHJvdGhldXMtR1BFLVBhciVDMyVBMm1ldHJvcy11dGlsaXphZG9zLXBhcmEtby1jYWRhc3Ryby1kZS1wZXIlQzMlQURvZG8tR1BFQTQwMAY7CFQ6DnNlYXJjaF9pZEkiKWI0NDg1MDk4LWYzN2EtNDAzYi05NDlhLTMwOGVmNTg0ZmNiNQY7CEY6CXJhbmtpCzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiGGNhZGFzdHJvIGRlIHBlcmlvZG8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--678dd5afc1d79d8660a806a5be5197b48e9326d0)  
[RH - Linha Protheus - GPE - Tabelas utilizadas para o Cadastro de Período GPEA400](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXxuXhqQc6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBl2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzg0MjYyMjA3OTk1MTEtUkgtTGluaGEtUHJvdGhldXMtR1BFLVRhYmVsYXMtdXRpbGl6YWRhcy1wYXJhLW8tQ2FkYXN0cm8tZGUtUGVyJUMzJUFEb2RvLUdQRUE0MDAGOwhUOg5zZWFyY2hfaWRJIiliNDQ4NTA5OC1mMzdhLTQwM2ItOTQ5YS0zMDhlZjU4NGZjYjUGOwhGOglyYW5raQ46C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhhjYWRhc3RybyBkZSBwZXJpb2RvBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--417e061b2b0b54a320565f374db611834d850829)  
[RH - Linha Protheus - GPE - Como configurar o compartilhamento das tabelas do Cadastro de Períodos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgcWbbSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBp2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNzQ1MTI5Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb25maWd1cmFyLW8tY29tcGFydGlsaGFtZW50by1kYXMtdGFiZWxhcy1kby1DYWRhc3Ryby1kZS1QZXIlQzMlQURvZG9zBjsIVDoOc2VhcmNoX2lkSSIpNjA1YzJiNmQtMmJlYS00N2NiLWJmZTUtYWI4ZDhiNzA4OWQ5BjsIRjoJcmFua2kHOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIYY2FkYXN0cm8gZGUgcGVyaW9kbwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--80624d584bce37464d0018b7e4ac42330f76ff76)  
[RH - Linha Protheus - GPE - Funcionalidade do campo RHC\_STATUS no cadastro de períodos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXPH4hogk6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzEwNTkxOTUxMjczMTExLVJILUxpbmhhLVByb3RoZXVzLUdQRS1GdW5jaW9uYWxpZGFkZS1kby1jYW1wby1SSEMtU1RBVFVTLW5vLWNhZGFzdHJvLWRlLXBlciVDMyVBRG9kb3MGOwhUOg5zZWFyY2hfaWRJIik2MDVjMmI2ZC0yYmVhLTQ3Y2ItYmZlNS1hYjhkOGI3MDg5ZDkGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhhjYWRhc3RybyBkZSBwZXJpb2RvBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--c21b9591b369a86dcd8eca7bd42ae93f42f87af9)

[RH - Linha Protheus - GPE - Como configurar bloqueio de período na rotina GPEA400 - Cadastro de Períodos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgFNdzUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBsGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzQ4Njg1My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb25maWd1cmFyLWJsb3F1ZWlvLWRlLXBlciVDMyVBRG9kby1uYS1yb3RpbmEtR1BFQTQwMC1DYWRhc3Ryby1kZS1QZXIlQzMlQURvZG9zBjsIVDoOc2VhcmNoX2lkSSIpYjQ0ODUwOTgtZjM3YS00MDNiLTk0OWEtMzA4ZWY1ODRmY2I1BjsIRjoJcmFua2kMOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIYY2FkYXN0cm8gZGUgcGVyaW9kbwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--8899c032783d6c312261f19e94c0d49698f60b17)
