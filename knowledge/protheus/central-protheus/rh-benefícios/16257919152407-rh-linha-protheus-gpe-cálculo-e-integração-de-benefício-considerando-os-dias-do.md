---
article_id: 16257919152407
category: RH - Benefícios
content_hash: 4f4888e6001e75b250c858c7e00d88d4ebd18245c1885db0a619f77ec81babcd
fetched_at: '2026-06-28T22:44:03.603089+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo e Integração de benefício considerando
  os dias do próximo período da folha
type: support-article
updated_at: '2025-09-26T13:37:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16257919152407-RH-Linha-Protheus-GPE-C%C3%A1lculo-e-Integra%C3%A7%C3%A3o-de-benef%C3%ADcio-considerando-os-dias-do-pr%C3%B3ximo-per%C3%ADodo-da-folha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16257955124119) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como realizar o cálculo e integração dos roteiros de benefícios (VA, VR e VT) considerando os dias do próximo período da folha?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.33  
  
**Solução**

Foi implementado possibilidade, através da configuração do mnemônico P\_INTPERAT, para que a integração dos roteiros de benefícios (VA, VR e VT) seja efetuada no período da folha que está em aberto.

**P\_INTPERAT configurado com .F. (padrão)**

Período da folha ativo: **07/2023**Período dos benefícios (VA, VR e VT) ativo: **08/2023.**

Os lançamentos serão integrados no roteiro da folha do período **08/2023**, que é o **período dos benefícios.**

**P\_INTPERAT configurado com .T.**

Período da folha ativo: **07/2023**Período dos benefícios (VA, VR e VT) ativo: **08/2023.**

Os lançamentos serão integrados no roteiro da folha do período **07/2023**, que é o **período em aberto da Folha.**

**Exemplo:**-Folha 07/2023 aberta e roteiro VTR inativo ![](https://centraldeatendimento.totvs.com/hc/article_attachments/16284881902871)

-Roteiro VTR 08/2023 ativo  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16285036047255)

-Cálculo com base no VTR de 08/2023

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16284700822423)

-Integração com a folha do mês 07/2023, vem os valores do roteiro VTR de 08/2023  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16284557772823)

**Saiba Mais:**[RH - Linha Protheus - GPE - Como descontar valor Fixo de Vale Transporte](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXmi7qAQQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBiWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDYyNzA0MDEwNDctUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tZGVzY29udGFyLXZhbG9yLUZpeG8tZGUtVmFsZS1UcmFuc3BvcnRlBjsIVDoOc2VhcmNoX2lkSSIpYzhlMDFiYWYtZjY3MC00MzE5LTkyYjItYzAyMTFiY2E2ZjczBjsIRjoJcmFua2kKOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIUdmFsZSB0cmFuc3BvcnRlBjsIVDoScmVzdWx0c19jb3VudGkCegE%3D--48c00fc62a224125b1d08a0f7d67d326d9100d31)  
[RH - Linha Protheus - GPE - Rotinas envolvidas nos cálculos de Benefícios - VR/VA/VT](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjp%2B67UUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDUyMzExMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUm90aW5hcy1lbnZvbHZpZGFzLW5vcy1jJUMzJUExbGN1bG9zLWRlLUJlbmVmJUMzJUFEY2lvcy1WUi1WQS1WVAY7CFQ6DnNlYXJjaF9pZEkiKWIwNGE0NGRmLTY0NjItNDNmZi1hZjlmLTNjMmY0MGFlYzk0ZAY7CEY6CXJhbmtpDzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDXZ0L3ZyL3ZhBjsIVDoScmVzdWx0c19jb3VudGlF--3c09f8adf1cdecea06f3e72010612e121a03b337)  
[RH - Linha Protheus - GPE - Como utilizar parâmetro MV\_CVTUSO no cálculo do vale transporte](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgzE4%2FSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBpWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNDg3NzQ5MS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby11dGlsaXphci1wYXIlQzMlQTJtZXRyby1NVi1DVlRVU08tbm8tYyVDMyVBMWxjdWxvLWRvLXZhbGUtdHJhbnNwb3J0ZQY7CFQ6DnNlYXJjaF9pZEkiKWJkOTlmM2E2LTVlZTktNDFmNS1hZGMzLTY3MDFiN2I5YjUxZgY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiRFJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBDb21vIHV0aWxpemFyIHBhcsOibWV0cm8gTVZfQ1ZUUFJPUAY7CFQ6EnJlc3VsdHNfY291bnRpAugD--097112952cf001bf376de53ef5abbfae651469ef)  
[RH - Linha Protheus - GPE - Como calcular benefícios para dias Não Trabalhados, Feriados ou Compensados](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjYbGPTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBsGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyODc5NDA3Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jYWxjdWxhci1iZW5lZiVDMyVBRGNpb3MtcGFyYS1kaWFzLU4lQzMlQTNvLVRyYWJhbGhhZG9zLUZlcmlhZG9zLW91LUNvbXBlbnNhZG9zBjsIVDoOc2VhcmNoX2lkSSIpYzhlMDFiYWYtZjY3MC00MzE5LTkyYjItYzAyMTFiY2E2ZjczBjsIRjoJcmFua2kLOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIUdmFsZSB0cmFuc3BvcnRlBjsIVDoScmVzdWx0c19jb3VudGkCegE%3D--3f39536ad92d6f4ff6c4c8995f49406e728af7b3)   
[RH - Linha Protheus - GPE - Cálculo de benefícios (Vt/Vr/Va) para funcionário com término de contrato determinado](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgX5g6gSws6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBxWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzEyNDE5NDM1NzgzNzAzLVJILUxpbmhhLVByb3RoZXVzLUdQRS1DJUMzJUExbGN1bG8tZGUtYmVuZWYlQzMlQURjaW9zLVZ0LVZyLVZhLXBhcmEtZnVuY2lvbiVDMyVBMXJpby1jb20tdCVDMyVBOXJtaW5vLWRlLWNvbnRyYXRvLWRldGVybWluYWRvBjsIVDoOc2VhcmNoX2lkSSIpYjA0YTQ0ZGYtNjQ2Mi00M2ZmLWFmOWYtM2MyZjQwYWVjOTRkBjsIRjoJcmFua2kLOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSINdnQvdnIvdmEGOwhUOhJyZXN1bHRzX2NvdW50aUU%3D--b8c9240d64a66ca6d0dfb0edbf65b6dcfbe1a832)
