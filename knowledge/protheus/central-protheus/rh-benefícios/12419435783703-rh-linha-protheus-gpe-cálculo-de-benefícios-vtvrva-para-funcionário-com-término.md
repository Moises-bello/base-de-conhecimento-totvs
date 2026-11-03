---
article_id: 12419435783703
category: RH - Benefícios
content_hash: aeeaa1d983af61b4f25dde813dfec5533d59867e293f51f4bb6efc5e2a063c83
fetched_at: '2026-06-28T22:44:03.578768+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de benefícios (Vt/Vr/Va) para funcionário
  com término de contrato determinado
type: support-article
updated_at: '2026-06-24T18:50:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12419435783703-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-benef%C3%ADcios-Vt-Vr-Va-para-funcion%C3%A1rio-com-t%C3%A9rmino-de-contrato-determinado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31914668674455) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como é realizado o cálculo de benefícios para o funcionário com término de contrato de determinado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.33.  
  
**Solução**

Foi liberado no pacote de expedição a partir de 13/01/2023, a possibilidade de configurar nas perguntas do cálculo se deve verificar a data de término de contrato determinado.   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12418801362199)  
  
Se definido com **Não**, será calculado o mês completo.   
Se definido com **Sim**, o cálculo será limitado à data definida no campo RA\_DTFIMCT no cadastro de funcionário:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12419214017047)

**Obs:** A melhoria depende da aplicação da atualização e execução do **UPDDISTR** com o dicionário diferencial   
  
Estrutura dos grupos de perguntas criados:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12419112760087)  
  
  
  
**Saiba Mais:**[RH - Linha Protheus - GPE - Como Cadastrar e Calcular o Vale Transporte](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjTIWfTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBh2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyOTAzNzAxMS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1DYWRhc3RyYXItZS1DYWxjdWxhci1vLVZhbGUtVHJhbnNwb3J0ZQY7CFQ6DnNlYXJjaF9pZEkiKWZhN2Y4Y2MwLTQwMzYtNDlmMy04NzA4LTljZDVmY2E1ZDA0NAY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiHmNvbW8gY2FkYXN0cmFyIGUgY2FsY3VsYXIGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--5c106323abfddb25cfe6563a7eb07021a5f9ece0)  
[RH - Linha Protheus - GPE - Como Cadastrar e Calcular o Vale Refeição](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgAU2TTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBj2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyODg1Mjk5Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1DYWRhc3RyYXItZS1DYWxjdWxhci1vLVZhbGUtUmVmZWklQzMlQTclQzMlQTNvBjsIVDoOc2VhcmNoX2lkSSIpZmE3ZjhjYzAtNDAzNi00OWYzLTg3MDgtOWNkNWZjYTVkMDQ0BjsIRjoJcmFua2kHOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIeY29tbyBjYWRhc3RyYXIgZSBjYWxjdWxhcgY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--472130df488a66f4f186fe6600cafb9ce2cc28e0)  
[RH - Linha Protheus - GPE - Cadastro e Cálculo do Vale Alimentação](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhIMmXTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBkWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyODkxMDE1Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ2FkYXN0cm8tZS1DJUMzJUExbGN1bG8tZG8tVmFsZS1BbGltZW50YSVDMyVBNyVDMyVBM28GOwhUOg5zZWFyY2hfaWRJIik2MjhkODM2MC04YzhhLTRlMTgtOGVkZC1hZWUyNDU1ODY4M2QGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhd2YWxlIGFsaW1lbnRhw6fDo28GOwhUOhJyZXN1bHRzX2NvdW50aQIHBg%3D%3D--cc398bc2c4e0d29e4b8546c1c58c7422d24e187e)  
[RH - Linha Protheus - GPE - Rotinas envolvidas nos cálculos de Benefícios - VR/VA/VT](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjp%2B67UUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDUyMzExMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUm90aW5hcy1lbnZvbHZpZGFzLW5vcy1jJUMzJUExbGN1bG9zLWRlLUJlbmVmJUMzJUFEY2lvcy1WUi1WQS1WVAY7CFQ6DnNlYXJjaF9pZEkiKTBiYTRlMWUwLWU4NjEtNGVmYi1hNzA5LTMxZTQ3YWQyZjUyNgY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiW1JIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBSb3RpbmFzIGVudm9sdmlkYXMgbm9zIGPDoWxjdWxvcyBkZSBCZW5lZsOtY2lvcyAtIFZSL1ZBL1ZUBjsIVDoScmVzdWx0c19jb3VudGkCZgY%3D--33860da00f7afd57d14bb2f035827c8e41ade7aa)  
[RH - Linha Protheus - GPE - Mapa de vale refeição/alimentação/transporte em planilha (GPER009)](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiWwtzUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBsWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzUyMzA5NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTWFwYS1kZS12YWxlLXJlZmVpJUMzJUE3JUMzJUEzby1hbGltZW50YSVDMyVBNyVDMyVBM28tdHJhbnNwb3J0ZS1lbS1wbGFuaWxoYS1HUEVSMDA5LQY7CFQ6DnNlYXJjaF9pZEkiKTBiYTRlMWUwLWU4NjEtNGVmYi1hNzA5LTMxZTQ3YWQyZjUyNgY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiW1JIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBSb3RpbmFzIGVudm9sdmlkYXMgbm9zIGPDoWxjdWxvcyBkZSBCZW5lZsOtY2lvcyAtIFZSL1ZBL1ZUBjsIVDoScmVzdWx0c19jb3VudGkCZgY%3D--2a2863a1505d0b5daf117e8927e01f757724eccf)  
[RH - Linha Protheus - GPE - Como calcular benefícios para dias Não Trabalhados, Feriados ou Compensados](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjYbGPTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBsGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyODc5NDA3Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jYWxjdWxhci1iZW5lZiVDMyVBRGNpb3MtcGFyYS1kaWFzLU4lQzMlQTNvLVRyYWJhbGhhZG9zLUZlcmlhZG9zLW91LUNvbXBlbnNhZG9zBjsIVDoOc2VhcmNoX2lkSSIpNjI4ZDgzNjAtOGM4YS00ZTE4LThlZGQtYWVlMjQ1NTg2ODNkBjsIRjoJcmFua2kHOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIXdmFsZSBhbGltZW50YcOnw6NvBjsIVDoScmVzdWx0c19jb3VudGkCBwY%3D--f9fcb102b17b802adb3a7ef03e30609da34b123a)
