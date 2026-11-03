---
article_id: 360025478113
category: RH - Transferência
content_hash: 8e788314b3bf8a30fd96657af6ee48477b393e830162bf7e445d509d69571288
fetched_at: '2026-06-28T22:43:23.429022+00:00'
product: protheus
section_id: 360010781974
source: central-protheus
title: RH - Linha Protheus - GPE - Bloqueio de matrícula na transferência individual
  - MV_BLOQMAT
type: support-article
updated_at: '2025-07-11T13:31:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025478113-RH-Linha-Protheus-GPE-Bloqueio-de-matr%C3%ADcula-na-transfer%C3%AAncia-individual-MV-BLOQMAT
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22647278700055) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Bloqueio de matrícula na transferência individual - **MV\_BLOQMAT**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - a partir da versão 11.80  
  
**Solução**O parâmetro **MV\_BLOQMAT** determina o **bloqueio/liberação** da modificação da matrícula de destino na **transferência** de um funcionário.  
  
Para utilização ou bloqueio dessa funcionalidade, configure o parâmetro com os seguintes conteúdos:  
**.T.** = Para bloquear a modificação da matrícula de destino na transferência  
**.F.** = Para permitir a alteração da matrícula de destino na transferência (conteúdo padrão do parâmetro pois é o tratamento já efetuado no padrão do SIGAGPE).

**Procedimentos de utilização:****1.** No ambiente **Configurador,**acesse **Atualizações > Cadastros > Parâmetros,** clique na seta ao lado da Empresa e em seguida **Parâmetros:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/22647252494871)

**2.** Clique na **Lupa** e pesquise o parâmetro **MV\_BLOQMAT:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22647278731799)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22647278739095)**

**3.** Configure o parâmetro **MV\_BLOQMAT** com conteúdo **.T.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22647278749463)****4.** Ao fazer uma **Transferência (GPEA180)**, o campo **Matrícula** para os dados de **Destino** estará **bloqueado**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22647278762903)

**Observação:** Para correta utilização e entendimento da funcionalidade do parâmetro, deve-se observar os seguintes itens:  
- O bloqueio da mudança de matrícula não se aplica à **Transferência em Lote;**- Se assumido o **conteúdo .F.**para o parâmetro **MV\_BLOQMAT,** só serão permitidas as transferências com modificação de matrícula nas situações já tratadas pelo sistema, [conforme esta documentação.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051186933-RH-Linha-Protheus-GPE-Inclus%C3%A3o-de-funcion%C3%A1rio-com-matr%C3%ADcula-incorreta)

**Saiba Mais:**[RH - Linha Protheus - GPE - Inclusão de funcionário com matrícula incorreta](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj1HLnUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MTE4NjkzMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtSW5jbHVzJUMzJUEzby1kZS1mdW5jaW9uJUMzJUExcmlvLWNvbS1tYXRyJUMzJUFEY3VsYS1pbmNvcnJldGEGOwhUOg5zZWFyY2hfaWRJIikwM2VjY2VkYy0zMDU5LTRhMDYtYTBkNi0zZWU1ZTNkZWQxODQGOwhGOglyYW5raQs6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhx0cmFuc2ZlcmVuY2lhIG1hdHJpY3VsYQY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--c4985d62bf18e5e977e6ca9f62c995cf456a35e3)  
[RH - Linha Protheus - GPE - Como funciona o processo de transferências na versão 12](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwggEfrSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyMTg4OTMxMi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1mdW5jaW9uYS1vLXByb2Nlc3NvLWRlLXRyYW5zZmVyJUMzJUFBbmNpYXMtbmEtdmVycyVDMyVBM28tMTIGOwhUOg5zZWFyY2hfaWRJIik4MTNmMmFiOC05MzVjLTQzMTQtYjhiMC1jZTYxNjExN2QyMGMGOwhGOglyYW5raQo6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhJ0cmFuc2ZlcmVuY2lhBjsIVDoScmVzdWx0c19jb3VudGkCSAU%3D--969a943c066bf1fbd48cf40c4aca8f86b107865d)  
[RH - Linha Protheus - GPE - Transferência individual ou em lote com a matrícula já existente no destino](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwi%2FqSXTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBtmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyNDc0NjQzMS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtVHJhbnNmZXIlQzMlQUFuY2lhLWluZGl2aWR1YWwtb3UtZW0tbG90ZS1jb20tYS1tYXRyJUMzJUFEY3VsYS1qJUMzJUExLWV4aXN0ZW50ZS1uby1kZXN0aW5vBjsIVDoOc2VhcmNoX2lkSSIpMDNlY2NlZGMtMzA1OS00YTA2LWEwZDYtM2VlNWUzZGVkMTg0BjsIRjoJcmFua2kIOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIcdHJhbnNmZXJlbmNpYSBtYXRyaWN1bGEGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--feeb666f4b11cf4fc39ff9c7fcea85a1ae2d5085)  
[RH - Linha Protheus - GPE - Transferência de funcionário para outra empresa/filial com a matrícula incorreta, como acertar](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjNwDfVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIByGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1OTQ4NjQxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtVHJhbnNmZXIlQzMlQUFuY2lhLWRlLWZ1bmNpb24lQzMlQTFyaW8tcGFyYS1vdXRyYS1lbXByZXNhLWZpbGlhbC1jb20tYS1tYXRyJUMzJUFEY3VsYS1pbmNvcnJldGEtY29tby1hY2VydGFyBjsIVDoOc2VhcmNoX2lkSSIpMDNlY2NlZGMtMzA1OS00YTA2LWEwZDYtM2VlNWUzZGVkMTg0BjsIRjoJcmFua2kJOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIcdHJhbnNmZXJlbmNpYSBtYXRyaWN1bGEGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--2af26bdc003f396f4f4e3ec23030f7481240be46)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
