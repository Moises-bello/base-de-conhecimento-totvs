---
article_id: 360036186414
category: RH - Benefícios
content_hash: 1681e7835ad2d6aafb10b5e497ae77803b35ee97e2ca6ce485099c7c425013c4
fetched_at: '2026-06-28T22:44:04.892721+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Importação de variáveis Coparticipação, dependentes
  ficam deletados na RHO
type: support-article
updated_at: '2025-09-29T12:52:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036186414-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-Coparticipa%C3%A7%C3%A3o-dependentes-ficam-deletados-na-RHO
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:01:00 min**

**Ocorrência**Ao importar um arquivo de coparticipação, o sistema grava na tabela RHO, porém o registro dos dependentes **ficam marcados como deletados**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**Inconsistência entra CPF do Cadastro X CPF do arquivo de importação  
  
**Solução**Existem 2 casos em que os registros importados são deletados:

1. Não existir cadastro de dependentes;

2. O CPF do arquivo de importação está diferente do CPF do cadastro de Dependentes (SRB). A importação neste caso irá constar de fato, porém se o CPF (fixo no layout), não é o mesmo do cadastro de dependentes, os registros serão deletados.

**Saiba mais:**[RH - Linha Protheus - GPE - Importação de variáveis tabela RHO - Coparticipação](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXOGZWOQU6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBp2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzU3NDM4MjA4MTQ0ODctUkgtTGluaGEtUHJvdGhldXMtR1BFLUltcG9ydGElQzMlQTclQzMlQTNvLWRlLXZhcmklQzMlQTF2ZWlzLXRhYmVsYS1SSE8tQ29wYXJ0aWNpcGElQzMlQTclQzMlQTNvBjsIVDoOc2VhcmNoX2lkSSIpMDQ1ODY5Y2UtNmMzNC00Y2NjLTlkYWItZjllMzAxOGVjMjBkBjsIRjoJcmFua2kMOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIecHJvdGhldXMgY29wYXJ0aWNpcGHDp8OjbwY7CFQ6EnJlc3VsdHNfY291bnRpAuoD--f8f55575516c7ffae21305b598ad450d6a024a19)  
[RH - Linha Protheus - Importação de variáveis tabela RHO, não soma valores de coparticipação](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjBFAE%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBvGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDA2MjE3NjEtUkgtTGluaGEtUHJvdGhldXMtSW1wb3J0YSVDMyVBNyVDMyVBM28tZGUtdmFyaSVDMyVBMXZlaXMtdGFiZWxhLVJITy1uJUMzJUEzby1zb21hLXZhbG9yZXMtZGUtY29wYXJ0aWNpcGElQzMlQTclQzMlQTNvBjsIVDoOc2VhcmNoX2lkSSIpMjRlYzMzNTAtOTkxNC00M2NiLTg0ZGUtNmY4M2YzOTEzNmYzBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIecHJvdGhldXMgY29wYXJ0aWNpcGHDp8OjbwY7CFQ6EnJlc3VsdHNfY291bnRpAuoD--f034bd89b3350d764b1e68ca597d146e8d1aa87b)  
[RH - Linha Protheus - GPE - Importação de variáveis de coparticipação quando houver mais de 1 dependente ou agregado](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhB%2FfvTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBzWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAzODc5MjUxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtSW1wb3J0YSVDMyVBNyVDMyVBM28tZGUtdmFyaSVDMyVBMXZlaXMtZGUtY29wYXJ0aWNpcGElQzMlQTclQzMlQTNvLXF1YW5kby1ob3V2ZXItbWFpcy1kZS0xLWRlcGVuZGVudGUtb3UtYWdyZWdhZG8GOwhUOg5zZWFyY2hfaWRJIikwNDU4NjljZS02YzM0LTRjY2MtOWRhYi1mOWUzMDE4ZWMyMGQGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIh5wcm90aGV1cyBjb3BhcnRpY2lwYcOnw6NvBjsIVDoScmVzdWx0c19jb3VudGkC6gM%3D--ee1cf0824ffd05b46d149e73a2794e3b6e541cc5)  
[RH - Linha Protheus - GPE - O que conferir quando há inconsistência na importação do txt de coparticipação](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgV%2Bp3UUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIByGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA0OTQwODUzMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTy1xdWUtY29uZmVyaXItcXVhbmRvLWglQzMlQTEtaW5jb25zaXN0JUMzJUFBbmNpYS1uYS1pbXBvcnRhJUMzJUE3JUMzJUEzby1kby10eHQtZGUtY29wYXJ0aWNpcGElQzMlQTclQzMlQTNvBjsIVDoOc2VhcmNoX2lkSSIpMjRlYzMzNTAtOTkxNC00M2NiLTg0ZGUtNmY4M2YzOTEzNmYzBjsIRjoJcmFua2kJOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIecHJvdGhldXMgY29wYXJ0aWNpcGHDp8OjbwY7CFQ6EnJlc3VsdHNfY291bnRpAuoD--ac7f8d9f4021eb94028fcac506b58965d9c86dee)
