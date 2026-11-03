---
article_id: 360035801214
category: RH - Benefícios
content_hash: 5000fcc3b64eebe4db4232e7d35fecdc0fbf103c56a235625f6ac723cfb21f0a
fetched_at: '2026-06-28T22:44:03.450054+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Ao cadastrar um novo benefício na tabela S011 e
  acessar a rotina "Definição de Outros Benefícios", o novo benefício não é apresentado.
type: support-article
updated_at: '2025-09-29T16:47:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035801214-RH-Linha-Protheus-GPE-Ao-cadastrar-um-novo-benef%C3%ADcio-na-tabela-S011-e-acessar-a-rotina-Defini%C3%A7%C3%A3o-de-Outros-Benef%C3%ADcios-o-novo-benef%C3%ADcio-n%C3%A3o-%C3%A9-apresentado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31937372606231) Tempo aproximado para leitura: 00:01:00 min****Ocorrência**Ao cadastrar um novo benefício na tabela S011 e acessar a rotina "Definição de Outros Benefícios", o novo benefício não é apresentado.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33068412633495)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33068426994327)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**  
O benefício **já está vinculado** aos cadastros de Vale Refeição, Vale Alimentação ou Vale Transporte.   
  
**Solução**Para confirmar que o benefício não está vinculado à nenhum cadastro, realize os procedimentos abaixo:

1. Acesse : Atualizações / Benefícios / VT/VR/VA / Cadastro Vale Refeição ou Cadastro Vale Alimentação, e confirme se o código informado no campo **Tipo Benef.** (RFO\_TPBEN) não está preenchido com o código do novo cadastro da tabela S011;  
  
2. Acesse : Atualizações / Benefícios / VT/VR/VA / Meios Transporte, e confirme se o código informado no campo **Tipo Benef.** (RN\_TPBEN) não está preenchido com o código do novo cadastro da tabela S011;  
  
No exemplo apresentado, o beneficio de código 86 está vinculado ao cadastro de vale refeição (Roteiro VRF), então não poderá ser vinculado na rotina de Definição de Benefícios (Roteiro BEN).  
A empresa deve avaliar em qual beneficio o código ficará vinculado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33068426995095)

**Saiba Mais:**[RH - Linha Protheus - GPE - Como fazer o cadastro de Outros Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgZciHVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBi2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1ODAyNDQ3My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1mYXplci1vLWNhZGFzdHJvLWRlLU91dHJvcy1CZW5lZiVDMyVBRGNpb3MGOwhUOg5zZWFyY2hfaWRJIik2MzRkYTdhMS1lYzMyLTRjNzctYjEyNy1iNTViMGU5YjFmNTIGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhZvdXRyb3MgYmVuZWZpY2lvcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--435fb350f42ac90e1d31f7932664e295362d4dec)  
[RH - Linha Protheus - GPE - Relatório de Outros Benefícios em planilha (GPER065)](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj2h9rUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzM3NzAxNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUmVsYXQlQzMlQjNyaW8tZGUtT3V0cm9zLUJlbmVmJUMzJUFEY2lvcy1lbS1wbGFuaWxoYS1HUEVSMDY1LQY7CFQ6DnNlYXJjaF9pZEkiKTYzNGRhN2ExLWVjMzItNGM3Ny1iMTI3LWI1NWIwZTliMWY1MgY7CEY6CXJhbmtpCDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiFm91dHJvcyBiZW5lZmljaW9zBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--7b64d6fc248fb23763dd6c40bb36c09eb55f1951)  
[RH - Linha Protheus - GPE - É possível realizar o cálculo de 1 benefício quando o funcionário tem 2 cadastrados no roteiro BEN](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj1ZcDUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB12h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MTY2NDM3My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtJUMzJTg5LXBvc3MlQzMlQUR2ZWwtcmVhbGl6YXItby1jJUMzJUExbGN1bG8tZGUtMS1iZW5lZiVDMyVBRGNpby1xdWFuZG8tby1mdW5jaW9uJUMzJUExcmlvLXRlbS0yLWNhZGFzdHJhZG9zLW5vLXJvdGVpcm8tQkVOBjsIVDoOc2VhcmNoX2lkSSIpNjM0ZGE3YTEtZWMzMi00Yzc3LWIxMjctYjU1YjBlOWIxZjUyBjsIRjoJcmFua2kKOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIWb3V0cm9zIGJlbmVmaWNpb3MGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--952a6892c9cd10c706acf852d24d633cec561a5b)
