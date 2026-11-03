---
article_id: 1500006362581
category: RH - 13º salário
content_hash: f3d350b54effa9a4f17255a0c620614c4a2db9e8ca1261e02cab275ae2d28ec0
fetched_at: '2026-06-28T22:44:00.506987+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Como antecipar o 13º Salario nas férias
type: support-article
updated_at: '2026-06-26T17:38:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006362581-RH-Linha-Protheus-GPE-Como-antecipar-o-13%C2%BA-Salario-nas-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16032469672599) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como realizar a antecipação de 13º Salario nas férias individuais?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Acesse o caminho **Miscelânea > Cálculos > Férias (GPEM030)**, selecione o **funcionário** e clique em **Calculo**.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008519821)  
  
O sistema carregará o cabeçalho de férias, onde é possível informar o percentual de antecipação do 13º no campo **%13 Salario** (RH\_PERC13S).  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008326982)  
  
Após calcular, confira se o sistema gerou a **verba de Identificador de Cálculo 0022**.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008519981)

**Importante**

* Caso o funcionário receba **adicionais**, como periculosidade, por exemplo, o sistema incluirá **automaticamente** o valor proporcional desses adicionais na antecipação da primeira parcela do 13º salário, na verba de ID 0022.
* Para que seja calculado as **médias** de 13º, é necessário habilitar o parâmetro**[MV\_MED1OP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053499193-RH-Linha-Protheus-GPE-Como-calcular-m%C3%A9dias-da-1%C2%AA-parcela-13-sal%C3%A1rio-no-c%C3%A1lculo-das-f%C3%A9rias)**, que também serão pagas na verba ID 0022.
* Dessa forma, quando o calcular o roteiro 131 e 132, o sistema levará em conta o valor já antecipado na verba 0022 — tanto os **adicionais** quanto as **médias** — garantindo que esses valores não sejam pagos em duplicidade.

**Saiba Mais**

[RH - Linha Protheus - GPE - Como gerar antecipação de 13º pela rotina de Férias Programadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052058514-RH-Linha-Protheus-GPE-Como-gerar-antecipa%C3%A7%C3%A3o-de-13%C2%BA-pela-rotina-de-F%C3%A9rias-Programadas)  
[RH - Linha Protheus - GPE - Como imprimir recibo de antecipação de 13º nas férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjh7xzVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBpWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NzcyODk5My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1pbXByaW1pci1yZWNpYm8tZGUtYW50ZWNpcGElQzMlQTclQzMlQTNvLWRlLTEzJUMyJUJBLW5hcy1mJUMzJUE5cmlhcwY7CFQ6DnNlYXJjaF9pZEkiKTg4ZGQwMzMzLTc1NjMtNDVlNC05MmRjLTg2MDA5MzYyYjQxNgY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiEDEzwrogZmVyaWFzBjsIVDoScmVzdWx0c19jb3VudGkCxQU%3D--934cbdfc28d82123a8e390927c31520475b62e0f)  
[RH - Linha Protheus - GPE - Como calcular médias da 1ª parcela 13° salário no cálculo das férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053499193-RH-Linha-Protheus-GPE-Como-calcular-m%C3%A9dias-da-1%C2%AA-parcela-13-sal%C3%A1rio-no-c%C3%A1lculo-das-f%C3%A9rias)  
[RH - Linha Protheus - GPE - Como contabilizar provisão de férias e 13º separadas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiNXFY%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBoWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDYyMTA3MDEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tY29udGFiaWxpemFyLXByb3ZpcyVDMyVBM28tZGUtZiVDMyVBOXJpYXMtZS0xMyVDMiVCQS1zZXBhcmFkYXMtBjsIVDoOc2VhcmNoX2lkSSIpY2UyNTViZmUtZmFjZS00OWU2LTlhN2EtZDg0NDUyOTZjNDE3BjsIRjoJcmFua2kPOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIQZmVyaWFzIDEzwroGOwhUOhJyZXN1bHRzX2NvdW50aQLFBQ%3D%3D--08bda3450c0a279adf7bf892bed6965d902cdf7c)  
[RH - Linha Protheus - GPE - Como é calculado a antecipação de 13º nas férias quando há licença maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXXvCUAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBzmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDkxMzUyMjY1MTktUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tJUMzJUE5LWNhbGN1bGFkby1hLWFudGVjaXBhJUMzJUE3JUMzJUEzby1kZS0xMyVDMiVCQS1uYXMtZiVDMyVBOXJpYXMtcXVhbmRvLWglQzMlQTEtbGljZW4lQzMlQTdhLW1hdGVybmlkYWRlBjsIVDoOc2VhcmNoX2lkSSIpODhkZDAzMzMtNzU2My00NWU0LTkyZGMtODYwMDkzNjJiNDE2BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIQMTPCuiBmZXJpYXMGOwhUOhJyZXN1bHRzX2NvdW50aQLFBQ%3D%3D--b317dbc12a973c07cb4eb7a32808e3867f8ae3b1)
