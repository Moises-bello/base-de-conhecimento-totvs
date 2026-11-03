---
article_id: 360024549674
category: RH - Funcionários
content_hash: 58915bf1a970b89eafa762a3b8a908592541b68ba61ac3b1e903a6177cd4185b
fetched_at: '2026-06-28T22:43:28.533666+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Inclusão de funcionário com mesmo CPF já existente
  na SRA
type: support-article
updated_at: '2025-04-17T20:50:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024549674-RH-Linha-Protheus-GPE-Inclus%C3%A3o-de-funcion%C3%A1rio-com-mesmo-CPF-j%C3%A1-existente-na-SRA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15909548841367) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Inclusão de funcionário com mesmo CPF já existente na SRA  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O Padrão, o sistema realmente **permite o usuário incluir o mesmo funcionário**, isso por conta de possibilidade de existir **múltiplos vínculos**, inclusive dentro da mesma filial, em cargos diferentes, por exemplo.  
  
Existe um ponto de entrada na rotina GPEA010 chamado **Gp010ValPE**. Ele valida os dados de inclusão/alteração, assim, pode ser usado para incluir uma mensagem quando o CPF for igual, questionando se o usuário deseja continuar ou não o processo, por exemplo.  
  
Documentação do Ponto de Entrada Gp010ValPE

<http://tdn.totvs.com/pages/releaseview.action?pageId=6079099>

Caso precise de auxílio nesse ajuste via ponto de entrada, orientamos o agendamento de um analista in loco, visto que o help desk não auxilia.

**Saiba Mais:**

[RH - Linha Protheus - GPE - Como realizar cadastro de Estagiário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgoxKjSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBhWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNjU2MTE5Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1yZWFsaXphci1jYWRhc3Ryby1kZS1Fc3RhZ2klQzMlQTFyaW8GOwhUOg5zZWFyY2hfaWRJIiljMTNhMmVmOC03MzU5LTQ3NDgtYTg4Zi01Yzk2MWFhNGY4ZTkGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIkZSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyByZWFsaXphciBjYWRhc3RybyBkZSBFc3RhZ2nDoXJpbwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--eb10cb958691ade950900a97c6e0667ce394ac6f)  
[RH - Linha Protheus - GPE - Como fazer o cadastro de jovem aprendiz](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwikgsPSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBg2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxODMxMzg5Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1mYXplci1vLWNhZGFzdHJvLWRlLWpvdmVtLWFwcmVuZGl6BjsIVDoOc2VhcmNoX2lkSSIpNDQ1YjAwYzMtZjA4Mi00NzFiLTkzMjUtZTZhMmU1ODcwYmJjBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIWY2FkYXN0cm8gYXByZW5kaXoGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--e06e9c4bd46cd925d9dd6b5ff5636340302a8950)  
[RH - Linha Protheus - GPE - Como cadastrar um Autônomo ou Pró-labore](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhBjMbUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjA2NzM5My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jYWRhc3RyYXItdW0tQXV0JUMzJUI0bm9tby1vdS1QciVDMyVCMy1sYWJvcmUGOwhUOg5zZWFyY2hfaWRJIilhNDZjNmRiYS1mNzNmLTRiNGMtYmUwNi0yZGYwMjg2OTdmNjgGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIktSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyBjYWRhc3RyYXIgdW0gQXV0w7Rub21vIG91IFByw7MtbGFib3JlBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--c2b4c4c7483f439896da0b83c8564eec81d8f480)  
[RH - Linha Protheus - GPE - Como cadastrar um funcionário de categoria horista](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXaOrXAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBlGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MTAyNTg5MDkzMzUtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tY2FkYXN0cmFyLXVtLWZ1bmNpb24lQzMlQTFyaW8tZGUtY2F0ZWdvcmlhLWhvcmlzdGEGOwhUOg5zZWFyY2hfaWRJIilhNDZjNmRiYS1mNzNmLTRiNGMtYmUwNi0yZGYwMjg2OTdmNjgGOwhGOglyYW5raQw6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIktSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyBjYWRhc3RyYXIgdW0gQXV0w7Rub21vIG91IFByw7MtbGFib3JlBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--771c546c89a87b5c23f3a0211525ce867f5d1d4a)  
[RH - Linha Protheus - GPE - Onde alterar os dados cadastrais do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwh7babSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBkGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNjQwNzkzMS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtT25kZS1hbHRlcmFyLW9zLWRhZG9zLWNhZGFzdHJhaXMtZG8tZnVuY2lvbiVDMyVBMXJpbwY7CFQ6DnNlYXJjaF9pZEkiKWE0NmM2ZGJhLWY3M2YtNGI0Yy1iZTA2LTJkZjAyODY5N2Y2OAY7CEY6CXJhbmtpDzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiS1JIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBDb21vIGNhZGFzdHJhciB1bSBBdXTDtG5vbW8gb3UgUHLDsy1sYWJvcmUGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--8310d8a1d6919be42c1c2202d46927b034eef98e)  
[RH - Linha Protheus - GPE - Quais os Pontos de Entrada disponíveis na rotina GPEA010 - Cadastro de Funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjqRCbTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBt2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyNDc4NjE1NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUXVhaXMtb3MtUG9udG9zLWRlLUVudHJhZGEtZGlzcG9uJUMzJUFEdmVpcy1uYS1yb3RpbmEtR1BFQTAxMC1DYWRhc3Ryby1kZS1GdW5jaW9uJUMzJUExcmlvcwY7CFQ6DnNlYXJjaF9pZEkiKTA3OTM4MWZkLWVmZWUtNGMzYy1iODkxLWU2Y2NmMTdiNmU2NAY7CEY6CXJhbmtpCDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiD0dwMDEwVmFsUEUGOwhUOhJyZXN1bHRzX2NvdW50aQg%3D--b78236cee6ea6a546b4d914cec301d21ea50a8d8)
