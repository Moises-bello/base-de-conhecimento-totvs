---
article_id: 360049408533
category: RH - Benefícios
content_hash: 1346973bf521063bb5562ef1f9f54c0ceb383eb1f1c1f897a8ead83bc76dca09
fetched_at: '2026-06-28T22:44:04.926877+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - O que conferir quando há inconsistência na importação
  do txt de coparticipação
type: support-article
updated_at: '2025-09-26T16:05:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049408533-RH-Linha-Protheus-GPE-O-que-conferir-quando-h%C3%A1-inconsist%C3%AAncia-na-importa%C3%A7%C3%A3o-do-txt-de-coparticipa%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32950664043671) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**O que conferir quando há inconsistência na importação do txt de coparticipação?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**As conferências a serem realizadas são:  
1- Avalie as posições no Arquivo txt e as Fórmulas informadas no layout, verifique se os dados configurados estão de acordo com o esperado.

**ATENÇÃO:** Sempre que finalizar uma linha no arquivo TXT, é necessário pressionar ENTER para iniciar a próxima linha.  
Essa prática também deve ser seguida ao concluir o layout, garantindo que o ENTER seja inserido antes de salvar o arquivo, para que a nova linha seja corretamente reconhecida.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32950664045975)

Exemplo: A matrícula está configurada para ocupar as posições 3 a 8 no layout. Portanto, no arquivo TXT, a matrícula deve estar exatamente nessa mesma posição. No meu caso, a matrícula é “000105”.

2- Verifique as informações de beneficiários do plano e que tem valores a serem lançados

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32950664046999)

Verifique o campo **RHO\_TPFONR** (Dados do Tipo do Fornecedor), que pode conter duas opções:

* 1 — Assistência Médica
* 2 — Assistência Odontológica

No exemplo, foi informando no arquivo TXT, na coluna 09 , o valor **1**, que corresponde à Assistência Médica.

Além disso, o fornecedor está configurado com **01**, conforme consta na rotina de planos ativos.

Por fim, verifique que foi informado o valor de **R$ 15,38** para ser importado, conforme registrado no arquivo TXT nas colunas 35 a 40.

3- Confirme se os parâmetros informados no momento da importação estão de acordo com o txt e layout definido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32950664049687)

Verifique que o campo **RHO\_COMPPG** (Dados da Competência de Pagamento a ser descontada ) está corretamente preenchido. É fundamental que esse dado esteja de acordo com a folha vigente “Aberta”. No exemplo, ele consta no arquivo TXT entre as colunas 18 a 23, e deve refletir o mesmo mês e ano informados no parâmetro.

Por fim, confirme que o código informado no parâmetro corresponde exatamente ao código configurado no layout.

**Saiba Mais:**[RH - Linha Protheus - GPE - Como realizar a importação de variáveis](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgT%2B8bSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBkmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxODU0MTMzMS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1yZWFsaXphci1hLWltcG9ydGElQzMlQTclQzMlQTNvLWRlLXZhcmklQzMlQTF2ZWlzBjsIVDoOc2VhcmNoX2lkSSIpODlmNjk4NjAtMmZlOC00MTMyLTk0MTEtN2E0N2Q3MmQyNDEwBjsIRjoJcmFua2kJOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIeaW1wb3J0YcOnw6NvIGRlIHZhcmlhdmVpcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--4827697a6843361631f2ef4bc5814ff8b98ae957)  
[RH - Linha Protheus - GPE - Importação de variáveis tabela RGB](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhRfCXVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1ODI4OTIzMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtSW1wb3J0YSVDMyVBNyVDMyVBM28tZGUtdmFyaSVDMyVBMXZlaXMtdGFiZWxhLVJHQgY7CFQ6DnNlYXJjaF9pZEkiKTg5ZjY5ODYwLTJmZTgtNDEzMi05NDExLTdhNDdkNzJkMjQxMAY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiHmltcG9ydGHDp8OjbyBkZSB2YXJpYXZlaXMGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--b6aae035c5a15b630310768a1d2affaf7148277a)  
[RH - Linha Protheus - GPE - Importação de variáveis tabela SRK](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiabwA%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDA1Nzk0ODItUkgtTGluaGEtUHJvdGhldXMtR1BFLUltcG9ydGElQzMlQTclQzMlQTNvLWRlLXZhcmklQzMlQTF2ZWlzLXRhYmVsYS1TUksGOwhUOg5zZWFyY2hfaWRJIik4OWY2OTg2MC0yZmU4LTQxMzItOTQxMS03YTQ3ZDcyZDI0MTAGOwhGOglyYW5raQg6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIh5pbXBvcnRhw6fDo28gZGUgdmFyaWF2ZWlzBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--632268aff7cb0d93619dd43d4e5075f12bb74dd8)  
[RH - Linha Protheus - GPE - Importação de variáveis tabela RHO - Coparticipação](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXOGZWOQU6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBp2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzU3NDM4MjA4MTQ0ODctUkgtTGluaGEtUHJvdGhldXMtR1BFLUltcG9ydGElQzMlQTclQzMlQTNvLWRlLXZhcmklQzMlQTF2ZWlzLXRhYmVsYS1SSE8tQ29wYXJ0aWNpcGElQzMlQTclQzMlQTNvBjsIVDoOc2VhcmNoX2lkSSIpODlmNjk4NjAtMmZlOC00MTMyLTk0MTEtN2E0N2Q3MmQyNDEwBjsIRjoJcmFua2kLOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIeaW1wb3J0YcOnw6NvIGRlIHZhcmlhdmVpcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--9bd5584a95b5b15214f866b8efbf4807730148b8)  
[RH - Linha Protheus - Importação de variáveis tabela RHO, não soma valores de coparticipação](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjBFAE%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBvGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDA2MjE3NjEtUkgtTGluaGEtUHJvdGhldXMtSW1wb3J0YSVDMyVBNyVDMyVBM28tZGUtdmFyaSVDMyVBMXZlaXMtdGFiZWxhLVJITy1uJUMzJUEzby1zb21hLXZhbG9yZXMtZGUtY29wYXJ0aWNpcGElQzMlQTclQzMlQTNvBjsIVDoOc2VhcmNoX2lkSSIpODlmNjk4NjAtMmZlOC00MTMyLTk0MTEtN2E0N2Q3MmQyNDEwBjsIRjoJcmFua2kMOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIeaW1wb3J0YcOnw6NvIGRlIHZhcmlhdmVpcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--6b8354a5228f6975665a0857564d1068caba373b)  
[RH - Linha Protheus - GPE - Importação de variáveis Coparticipação, dependentes ficam deletados na RHO](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwguOdTTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBvmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAzNjE4NjQxNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtSW1wb3J0YSVDMyVBNyVDMyVBM28tZGUtdmFyaSVDMyVBMXZlaXMtQ29wYXJ0aWNpcGElQzMlQTclQzMlQTNvLWRlcGVuZGVudGVzLWZpY2FtLWRlbGV0YWRvcy1uYS1SSE8GOwhUOg5zZWFyY2hfaWRJIik4OWY2OTg2MC0yZmU4LTQxMzItOTQxMS03YTQ3ZDcyZDI0MTAGOwhGOglyYW5raQ06C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIh5pbXBvcnRhw6fDo28gZGUgdmFyaWF2ZWlzBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--e2b39d1d808ca49688e3a0d816a712069d00a5e9)
