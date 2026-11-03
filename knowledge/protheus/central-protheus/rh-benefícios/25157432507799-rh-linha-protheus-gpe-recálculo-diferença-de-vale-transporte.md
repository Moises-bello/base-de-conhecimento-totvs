---
article_id: 25157432507799
category: RH - Benefícios
content_hash: 4eff53d5b286365d16445e78b22bec80e972c90d3e8f582f2633c0e96ca894cd
fetched_at: '2026-06-28T22:44:04.760658+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Recálculo (Diferença) de Vale Transporte
type: support-article
updated_at: '2025-08-21T20:00:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25157432507799-RH-Linha-Protheus-GPE-Rec%C3%A1lculo-Diferen%C3%A7a-de-Vale-Transporte
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25157399096471) Tempo aproximado para leitura: 00:03:00 min****Dúvida**É possível calcular a diferença de Vale Transporte referente ao mês anterior?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.2210  
  
**Solução**Foi implementada a possibilidade de efetuar o recálculo do VT realizado no período anterior, e **compensar eventual diferença no cálculo atual.**O recálculo é efetuado quando ocorrem situações não previstas no momento do cálculo do VT, como: **afastamentos e trocas de escala.**  
Para isso, é necessário ativar o Mnemônico **P\_RECALCVT:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25157399097239)**

**> Exemplo** de cálculo de Vale Transporte **pago a mais:**O funcionário recebeu um total de 40 vales (20 dias) no período 06/2024:  
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdx4KEo4osEvyAYIWG8uU8BS3IhaCXIJEYQFeE7zerzntQnywETV5ixDuFIEcpGPn0yPT34iYsB8pFJ4SoLzrPGFZULiQEs4miSyl6ZfGpV4qphUQcYsSydbCZJ3tCLz7LRXCpubzDAFTF2_mJgtq6uKBDKR64=s2048?key=2PBQSi-PxUEixmvMklSqXw)**

Após o cálculo, foi incluído um **afastamento** de 5 dias dentro do período 06/2024:  
![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUf78D0NDhU2zV5wZi2f__jABHqJvh5t4R3vNoOuGZ4gdXBp1HfTc3Y5E5S_sgofzb66s2P4t-NJ0wnwbeiuqaH_eMDWEj2qChkD43rq0waluWCPMpA4P8QNRphnesPS3-nq_ssGm61JV0dtyjjd97f_EVzsioSP=s2048?key=2PBQSi-PxUEixmvMklSqXw)

No cálculo do período 07/2024, foram considerados 23 dias úteis, porém, foi efetuada a **dedução da diferença paga a mais** do período anterior:  
![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUcSMrtztw581gDCEn-oFDUPS664tPdUuYQAY5eBo9cWERpCQmKIkH2zdPDtGyW-bVeU5ygyPNx-JN3wBKHpfoVA1m2z0ZRpoPbedS7ZMUsX8eciZgyTmn3AOuYfLWG2ZlF6BfddHvi9WrwjDnFq9I5zOf2UgB5T=s2048?key=2PBQSi-PxUEixmvMklSqXw)

- **5 dias de afastamento** do período 06/2024 (10 vales) = R$ 45,00  
**- Campo Vlr Anterior:** 23 dias úteis do período 07/2024 = R$ 207,00  
**- Campo Valor Calc:** Total pago no período = R$ 162,00 (R$ 207,00 - R$ 45,00)

**Saiba Mais**[Documento Técnico - Recálculo do VT](https://tdn.totvs.com/pages/releaseview.action?pageId=839961057#exemplos-exemplo2)  
[RH - Linha Protheus - GPE - Cálculo e Integração de benefício considerando os dias do próximo período da folha](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgX8X5XyQ46D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBzmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE2MjU3OTE5MTUyNDA3LVJILUxpbmhhLVByb3RoZXVzLUdQRS1DJUMzJUExbGN1bG8tZS1JbnRlZ3JhJUMzJUE3JUMzJUEzby1kZS1iZW5lZiVDMyVBRGNpby1jb25zaWRlcmFuZG8tb3MtZGlhcy1kby1wciVDMyVCM3hpbW8tcGVyJUMzJUFEb2RvLWRhLWZvbGhhBjsIVDoOc2VhcmNoX2lkSSIpYmVmYzEwMDctMTc4ZC00NGEzLTk0ZmEtMzJmOWYxZjVlYTAwBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJ5UkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIEPDoWxjdWxvIGUgSW50ZWdyYcOnw6NvIGRlIGJlbmVmw61jaW8gY29uc2lkZXJhbmRvIG9zIGRpYXMgZG8gcHLDs3hpbW8gcGVyw61vZG8gZGEgZm9saGEGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--ee2d8aeb668d1f9d24dd99a02a032e98e9b67a7c)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
