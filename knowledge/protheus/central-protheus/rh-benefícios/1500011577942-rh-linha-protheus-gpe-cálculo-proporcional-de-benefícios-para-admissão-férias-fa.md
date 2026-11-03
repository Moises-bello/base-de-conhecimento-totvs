---
article_id: 1500011577942
category: RH - Benefícios
content_hash: b12f1caa3b904aa098e5f3c5280547d4a492e8e4692fc50c62d19b5da0f0184f
fetched_at: '2026-06-28T22:44:03.607799+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo proporcional de benefícios para admissão,
  férias, faltas e afastamentos
type: support-article
updated_at: '2026-05-19T11:02:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011577942-RH-Linha-Protheus-GPE-C%C3%A1lculo-proporcional-de-benef%C3%ADcios-para-admiss%C3%A3o-f%C3%A9rias-faltas-e-afastamentos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31937698439191) Tempo aproximado para leitura: 00:01:00 min**  
  
**Dúvida**  
Como fazer o cálculo de benefício VT/VR/VA normalmente para funcionários afastados?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

**-Roteiros VTR, VRF e VAL**  
  
Para que **não seja calculado** proporcional ao afastamento, existe uma pergunta nos parâmetros de cálculo dos benefícios, chamada Prop. Férias/Afast. ?  
  
Acesse: **Atualizações**> **Benefícios> VT/VR/VA**> **Cálculo.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39480925940887)**​**  
  
Abaixo detalhes de como funciona o cálculo dependendo do conteúdo selecionado  
  
**Ambos -** Será calculado proporcional a férias e afastamentos  
**Nenhum** - O sistema não abaterá Férias Calculadas e Afastamentos lançados, ou seja, calculará integral.  
**Férias** - O sistema só abaterá dias de Férias, ou seja, cálculo proporcional para funcionários com férias e integral para funcionários com afastamentos  
**Afastamento**- O sistema só abaterá dias de Afastamento, ou seja, cálculo proporcional para funcionários com afastamento e integral para funcionários com férias

Caso queira também descontar **faltas** dentro do período, deixe a pergunta **Descontar Faltas ? = Sim**

**-Roteiro BEN**  
  
Em **Definição de Benefício**, informe no campo Propoc. (RIS\_PROPOR) se o benefícios deverá ser calculado deduzindo os dias afastados.   
  
Acesse: **Atualizações> Benefícios> Outros Benefícios> Definição de Benefícios.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39480925943831)

**Saiba Mais**  
[RH - Linha Protheus - GPE - Como Cadastrar e Calcular o Vale Refeição](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgAU2TTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBj2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyODg1Mjk5Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1DYWRhc3RyYXItZS1DYWxjdWxhci1vLVZhbGUtUmVmZWklQzMlQTclQzMlQTNvBjsIVDoOc2VhcmNoX2lkSSIpNGQwMGNmNGItMGRlYy00MGY5LWFjZDYtNTQ3YTM5YTgzMDg0BjsIRjoJcmFua2kKOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIcY2FsY3VsYSB2YWxlIHJlZmVpw6fDo28GOwhUOhJyZXN1bHRzX2NvdW50aQLVAQ%3D%3D--b5b4bb9a9393a80b92959670aff748735c3584ac)  
[RH - Linha Protheus - GPE - Como Cadastrar e Calcular o Vale Transporte](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjTIWfTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBh2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyOTAzNzAxMS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1DYWRhc3RyYXItZS1DYWxjdWxhci1vLVZhbGUtVHJhbnNwb3J0ZQY7CFQ6DnNlYXJjaF9pZEkiKWQ3ZmQ0MDIzLTZhNzAtNDJmZS04N2UwLTJiMmVlNmYyNjU2NgY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiH0NvbW8gQ2FkYXN0cmFyIGUgQ2FsY3VsYXIgBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--ebfc8c700536653af51214c903779584c3dc958c)  
[RH - Linha Protheus - GPE - Cadastro e Cálculo do Vale Alimentação](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhIMmXTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBkWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyODkxMDE1Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ2FkYXN0cm8tZS1DJUMzJUExbGN1bG8tZG8tVmFsZS1BbGltZW50YSVDMyVBNyVDMyVBM28GOwhUOg5zZWFyY2hfaWRJIik3ODI4ODdmZC1lM2IyLTQ3YzktOWZiOC00MDU2YzY1Yjg0NjgGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIjFDb21vIENhZGFzdHJhciBlIENhbGN1bGFyIHZhbGUgYWxpbWVudGHDp8OjbwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--0b96cb78ef8001cd7a9194f524f272bc0674b828)  
[RH - Linha Protheus - GPE - Como abater as Faltas no cálculo de Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhoRV%2FTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBlWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyODUyMTgzMi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1hYmF0ZXItYXMtRmFsdGFzLW5vLWMlQzMlQTFsY3Vsby1kZS1CZW5lZiVDMyVBRGNpb3MtBjsIVDoOc2VhcmNoX2lkSSIpZmQ0MmM2ZTgtNjg4Yi00NjBhLWJjMTUtMjc1MTNiY2M5Y2U1BjsIRjoJcmFua2kIOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIYYmVuZWZpY2lvcyBhZmFzdGFkbwY7CFQ6EnJlc3VsdHNfY291bnRpApAH--4b8b1896368d201f19339bc9d2529cc8e96d5b85)
