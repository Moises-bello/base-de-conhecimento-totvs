---
article_id: 19199294827799
category: RH - Benefícios
content_hash: 64388a1f42e07a3e403adf63d9b3f4455c6a985b7600cc5cd160e49922fef31e
fetched_at: '2026-06-28T22:44:04.764515+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Referência de vale transporte vem dobrado na folha
  de pagamento.
type: support-article
updated_at: '2025-09-26T14:42:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19199294827799-RH-Linha-Protheus-GPE-Refer%C3%AAncia-de-vale-transporte-vem-dobrado-na-folha-de-pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19199294800407) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Referência de vale transporte (Roteiro VTR) vem dobrado na folha de pagamento.   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.2210  
  
**Solução**A rotina foi atualizada para levar a **quantidade total de vales** como referência. O Sistema busca a quantidade no campo **R0\_QDIACAL** no cálculo dos roteiros VTR/VAL/VRF.  
Como geralmente o Roteiro VTR é configurado para pagar ida e volta, essa quantidade de vales é dobrada. 

**-Cálculo VTR  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19199272243479)  
  
-Integração com a folha  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19199301967255)**

**Saiba Mais:**[DT Dedução de vales - VT, VR e VA](https://tdn.totvs.com/pages/viewpage.action?pageId=784232321)  
[RH - Linha Protheus - GPE - Rotinas envolvidas nos cálculos de Benefícios - VR/VA/VT](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjp%2B67UUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDUyMzExMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUm90aW5hcy1lbnZvbHZpZGFzLW5vcy1jJUMzJUExbGN1bG9zLWRlLUJlbmVmJUMzJUFEY2lvcy1WUi1WQS1WVAY7CFQ6DnNlYXJjaF9pZEkiKWIwNGE0NGRmLTY0NjItNDNmZi1hZjlmLTNjMmY0MGFlYzk0ZAY7CEY6CXJhbmtpDzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDXZ0L3ZyL3ZhBjsIVDoScmVzdWx0c19jb3VudGlF--3c09f8adf1cdecea06f3e72010612e121a03b337)  
[RH - Linha Protheus - GPE - Como utilizar parâmetro MV\_CVTUSO no cálculo do vale transporte](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgzE4%2FSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBpWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNDg3NzQ5MS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby11dGlsaXphci1wYXIlQzMlQTJtZXRyby1NVi1DVlRVU08tbm8tYyVDMyVBMWxjdWxvLWRvLXZhbGUtdHJhbnNwb3J0ZQY7CFQ6DnNlYXJjaF9pZEkiKWJkOTlmM2E2LTVlZTktNDFmNS1hZGMzLTY3MDFiN2I5YjUxZgY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiRFJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBDb21vIHV0aWxpemFyIHBhcsOibWV0cm8gTVZfQ1ZUUFJPUAY7CFQ6EnJlc3VsdHNfY291bnRpAugD--097112952cf001bf376de53ef5abbfae651469ef)  
[RH - Linha Protheus - GPE - Cálculo e Integração de benefício considerando os dias do próximo período da folha](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgX8X5XyQ46D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBzmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE2MjU3OTE5MTUyNDA3LVJILUxpbmhhLVByb3RoZXVzLUdQRS1DJUMzJUExbGN1bG8tZS1JbnRlZ3JhJUMzJUE3JUMzJUEzby1kZS1iZW5lZiVDMyVBRGNpby1jb25zaWRlcmFuZG8tb3MtZGlhcy1kby1wciVDMyVCM3hpbW8tcGVyJUMzJUFEb2RvLWRhLWZvbGhhBjsIVDoOc2VhcmNoX2lkSSIpNGUyOGY2ZGItOGFmNC00M2I4LWFhZGQtMDI3NWU1M2RiNjQ3BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJ5UkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIEPDoWxjdWxvIGUgSW50ZWdyYcOnw6NvIGRlIGJlbmVmw61jaW8gY29uc2lkZXJhbmRvIG9zIGRpYXMgZG8gcHLDs3hpbW8gcGVyw61vZG8gZGEgZm9saGEGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--ceebece337986ac810d815e208b9ababc7fbfd3e)  
[RH - Linha Protheus - GPE - Cálculo de benefícios (Vt/Vr/Va) para funcionário com término de contrato determinado](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgX5g6gSws6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBxWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzEyNDE5NDM1NzgzNzAzLVJILUxpbmhhLVByb3RoZXVzLUdQRS1DJUMzJUExbGN1bG8tZGUtYmVuZWYlQzMlQURjaW9zLVZ0LVZyLVZhLXBhcmEtZnVuY2lvbiVDMyVBMXJpby1jb20tdCVDMyVBOXJtaW5vLWRlLWNvbnRyYXRvLWRldGVybWluYWRvBjsIVDoOc2VhcmNoX2lkSSIpYjA0YTQ0ZGYtNjQ2Mi00M2ZmLWFmOWYtM2MyZjQwYWVjOTRkBjsIRjoJcmFua2kLOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSINdnQvdnIvdmEGOwhUOhJyZXN1bHRzX2NvdW50aUU%3D--b8c9240d64a66ca6d0dfb0edbf65b6dcfbe1a832)
