---
article_id: 360059185253
category: RH - Rescisão
content_hash: 03f6008b2839ac55bd7ff304a57a9688759409155b39b72d165e636c501a8961
fetched_at: '2026-06-28T22:43:52.130232+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Configuração de verbas de desconto de 13º salário
  na rescisão
type: support-article
updated_at: '2026-04-27T18:55:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059185253-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-de-verbas-de-desconto-de-13%C2%BA-sal%C3%A1rio-na-rescis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15862390134679) Tempo aproximado para leitura: 01:00 min**  
  
**Dúvida**  
Como configurar as verbas de desconto de 13º salário na rescisão (ID 0116, 0183 e 0247)?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
Para rescisões calculadas após o pagamento da 2ª parcela do 13º salário, é necessário descontar os valores já pagos anteriormente.  
Por esse motivoa verba **0116 – Desconto 13º salário rescisão** tornou-se obrigatória.

A incidência para FGTS da verba **0247 – Desconto líquido 13º 2ª parcela rescisão**, passou a ser controlada internamente pelo sistema de acordo com o tipo de rescisão a ser calculada, a saber:

• Rescisões com recolhimento de GRFC/GRRF: a incidência para FGTS será considerada como **NÃO**.

• Rescisões sem recolhimento de GRFC/GRRF: a incidência para FGTS será considerada como  **SIM**.  
  
Para que os valores de INSS, FGTS e IRRF fiquem corretos na rescisão, é necessário que alguns campos das verbas de ID abaixo estejam configurados com **Não** para INSS e IR e com **SIM** para FGTS e Ref. a 13º.

* **0116- Desconto 13º salário rescisão**,
* **0247- Desconto Líquido 13º 2ª parcela rescisão**
* **0183- Desconto ant. 13º na 2ª parcela**

Para envio ao esocial , os identificadores dessas verbas devem estar com **IncFGTS = 12**

No cálculo da rescisão, após o calculo da 2ª parcela do 13º salário, INSS e FGTS serão recalculados **somente se houver diferença a recolher**  
Lembrando que, para o IRRF sempre será **Recalculado** e abatido o valor já descontado no cálculo da 2ª parcela do 13º salário.  
  
**Observação:** A verba **0116 – Desconto 13º salário rescisão**, deve possuir as mesmas incidências da verba **0183 – Desc. ant. 13º na 2ª parcela**.

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Calculo de 13º intermitente X indeterminado](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgX7OetAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDk1NTQxMDMzMTktUkgtTGluaGEtUHJvdGhldXMtR1BFLUNhbGN1bG8tZGUtMTMlQzIlQkEtaW50ZXJtaXRlbnRlLVgtaW5kZXRlcm1pbmFkbwY7CFQ6DnNlYXJjaF9pZEkiKWU0NWYxMGE1LTRjMmQtNDk1Yi1iNWJiLWE1NWRmMmVkYjFjZgY7CEY6CXJhbmtpCDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDGlkIDAxODMGOwhUOhJyZXN1bHRzX2NvdW50aQLdBA%3D%3D--5fc10145fc804966b6bddb9cf76cbc034d9c12a8)  
[RH - Linha Protheus - GPE - Como Conferir a Base de FGTS 13º Salário 2ª Parcela](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwg1Dv0%2BXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBn2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDAzNTc5NDEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tQ29uZmVyaXItYS1CYXNlLWRlLUZHVFMtMTMlQzIlQkEtU2FsJUMzJUExcmlvLTIlQzIlQUEtUGFyY2VsYQY7CFQ6DnNlYXJjaF9pZEkiKWU0NWYxMGE1LTRjMmQtNDk1Yi1iNWJiLWE1NWRmMmVkYjFjZgY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDGlkIDAxODMGOwhUOhJyZXN1bHRzX2NvdW50aQLdBA%3D%3D--94f6b91fe29cc59e596b1655357cd8d9085e00ea)  
[RH - Linha Protheus - GPE - Por que rescisão gera id 1672 indevidamente quando a data de demissão contabiliza 12/12 avos de 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXxIHFDwo6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB3Wh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExMDYyODU0NDAzMDk1LVJILUxpbmhhLVByb3RoZXVzLUdQRS1Qb3ItcXVlLXJlc2NpcyVDMyVBM28tZ2VyYS1pZC0xNjcyLWluZGV2aWRhbWVudGUtcXVhbmRvLWEtZGF0YS1kZS1kZW1pc3MlQzMlQTNvLWNvbnRhYmlsaXphLTEyLTEyLWF2b3MtZGUtMTMlQzIlQkEtc2FsJUMzJUExcmlvBjsIVDoOc2VhcmNoX2lkSSIpNWU3YzdlMzItOWQzZC00YWU5LTlhMGUtZGM5YmU3MmE5MDI2BjsIRjoJcmFua2kIOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIMaWQgMDExNgY7CFQ6EnJlc3VsdHNfY291bnRpAt0E--9c372224c1a96033ec887c615d398deb5db0dd20)
