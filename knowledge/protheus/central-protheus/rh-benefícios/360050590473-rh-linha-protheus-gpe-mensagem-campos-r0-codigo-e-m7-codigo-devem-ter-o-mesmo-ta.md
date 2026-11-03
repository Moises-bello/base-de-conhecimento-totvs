---
article_id: 360050590473
category: RH - Benefícios
content_hash: 2b997328127e07ba701ab5abefa69ba8c858330409e6fa93720282d9900ccf90
fetched_at: '2026-06-28T22:44:04.709596+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: 'RH - Linha Protheus - GPE - Mensagem: Campos R0_CODIGO e M7_CODIGO devem ter
  o mesmo tamanho, verifique com o administrador do sistema'
type: support-article
updated_at: '2025-09-08T19:20:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050590473-RH-Linha-Protheus-GPE-Mensagem-Campos-R0-CODIGO-e-M7-CODIGO-devem-ter-o-mesmo-tamanho-verifique-com-o-administrador-do-sistema
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34790096208791) Tempo aproximado para leitura: 00:01:00 min  
  
Ocorrência**Ao tentar acessar a rotina de **Atualização de Vales (GPEA133)** dentro de benefícios é apresentada a mensagem: Campos R0\_CODIGO e M7\_CODIGO devem ter o mesmo tamanho, verifique com o administrador do sistema

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075217994)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17

**Causa**Esse incidente ocorre, pois o tamanho dos campos estão diferentes.

**Solução**Para ajustar, acessar o módulo Configurador **(SIGACFG)** em **Base de Dados> Dicionário> Base de Dados** Clique em **Dicionário de Dados**, procure a tabela SR0 e selecione o campo **R0\_CODIGO** para edição e ajuste o tamanho para 3.   
Realizar o mesmo processo para o campo **M7\_CODIGO**.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076417273)

**Saiba Mais**[RH - Linha Protheus - GPE - Conversão tabelas SR0/SM7](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwi6uajUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSJ%2FaHR0cHM6Ly9jZW50cmFsZGVhdGVuZGltZW50by50b3R2cy5jb20vaGMvcHQtYnIvYXJ0aWNsZXMvMzYwMDUwMTEyOTU0LVJILUxpbmhhLVByb3RoZXVzLUdQRS1Db252ZXJzJUMzJUEzby10YWJlbGFzLVNSMC1TTTcGOwhUOg5zZWFyY2hfaWRJIikyOWM2MjExNi1kMjcyLTQwMDctODc2YS04YTYwNTAzYzViNmUGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIghTTTcGOwhUOhJyZXN1bHRzX2NvdW50aRI%3D--00d143ff78338d545801e14c8c074f94ac3e1fb8)  
[RH - Linha Protheus - GPE - Atualização da rotina de Benefícios o layout - VT/VR/VA](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiyv6DUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBoGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA0OTU5MDE5NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQXR1YWxpemElQzMlQTclQzMlQTNvLWRhLXJvdGluYS1kZS1CZW5lZiVDMyVBRGNpb3Mtby1sYXlvdXQtVlQtVlItVkEGOwhUOg5zZWFyY2hfaWRJIikyOWM2MjExNi1kMjcyLTQwMDctODc2YS04YTYwNTAzYzViNmUGOwhGOglyYW5raQk6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIghTTTcGOwhUOhJyZXN1bHRzX2NvdW50aRI%3D--b6ef28a846a6b513c4f130f1cc1aa6bf179ba572)  
[RH - Linha Protheus - GPE - Rotinas envolvidas nos cálculos de Benefícios - VR/VA/VT](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjp%2B67UUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDUyMzExMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUm90aW5hcy1lbnZvbHZpZGFzLW5vcy1jJUMzJUExbGN1bG9zLWRlLUJlbmVmJUMzJUFEY2lvcy1WUi1WQS1WVAY7CFQ6DnNlYXJjaF9pZEkiKTI5YzYyMTE2LWQyNzItNDAwNy04NzZhLThhNjA1MDNjNWI2ZQY7CEY6CXJhbmtpDzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiCFNNNwY7CFQ6EnJlc3VsdHNfY291bnRpEg%3D%3D--4bc14fb2af698f011a56ce24205386d2080d324b)
