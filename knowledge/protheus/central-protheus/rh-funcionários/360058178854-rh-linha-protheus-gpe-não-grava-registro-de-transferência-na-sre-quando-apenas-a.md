---
article_id: 360058178854
category: RH - Funcionários
content_hash: 203f6ddd48d44cbf3e016b4dabd4519c1ac07e5c84d83c311fc945ac4fcf8bad
fetched_at: '2026-06-28T22:43:28.609178+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Não grava registro de Transferência na SRE quando
  apenas a matrícula é alterada
type: support-article
updated_at: '2025-08-28T15:00:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058178854-RH-Linha-Protheus-GPE-N%C3%A3o-grava-registro-de-Transfer%C3%AAncia-na-SRE-quando-apenas-a-matr%C3%ADcula-%C3%A9-alterada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22866602788375) Tempo aproximado para leitura: 00:01:00 min****Dúvida**Por que o sistema não grava registro de Transferência na SRE quando apenas a matrícula é alterada?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A **alteração de** **matrícula** é permitida apenas no **mês de admissão** do Funcionário (quando a mesma foi cadastrada errada), por este motivo, **não é necessário gravar uma linha de histórico da SRE - Transferência**, visto que não existe alteração histórica para o Funcionário, ou seja, apenas foi feito o ajuste da matrícula.  
O sistema só gera linha de histórico na SRE **quando há movimentação entre as tabelas,** como exemplo, se for alterado Centro de Custo, Departamento, Filial, etc.

**Saiba Mais:**[RH - Linha Protheus - GPE - Inclusão de funcionário com matrícula incorreta](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj1HLnUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MTE4NjkzMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtSW5jbHVzJUMzJUEzby1kZS1mdW5jaW9uJUMzJUExcmlvLWNvbS1tYXRyJUMzJUFEY3VsYS1pbmNvcnJldGEGOwhUOg5zZWFyY2hfaWRJIiliMWFiMDdlNS00MmMzLTRjMzQtOTgzNy0yZTYyY2QyZDcyNGIGOwhGOglyYW5raQg6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIh90cmFuc2ZlcmVuY2lhIGRlIG1hdHJpY3VsYQY7CFQ6EnJlc3VsdHNfY291bnRpAhcH--9fcaeb444bb161c93f6fbd339fecd7a8885475b1)  
[RH - Linha Protheus - GPE - Bloqueio de matrícula na transferência individual - MV\_BLOQMAT](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjh0zDTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBomh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyNTQ3ODExMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQmxvcXVlaW8tZGUtbWF0ciVDMyVBRGN1bGEtbmEtdHJhbnNmZXIlQzMlQUFuY2lhLWluZGl2aWR1YWwtTVYtQkxPUU1BVAY7CFQ6DnNlYXJjaF9pZEkiKWIxYWIwN2U1LTQyYzMtNGMzNC05ODM3LTJlNjJjZDJkNzI0YgY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiH3RyYW5zZmVyZW5jaWEgZGUgbWF0cmljdWxhBjsIVDoScmVzdWx0c19jb3VudGkCFwc%3D--7da3361e5fe32a745416966981016386de7e8c9d)  
[RH - Linha Protheus - GPE - Transferência individual ou em lote com a matrícula já existente no destino](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwi%2FqSXTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBtmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyNDc0NjQzMS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtVHJhbnNmZXIlQzMlQUFuY2lhLWluZGl2aWR1YWwtb3UtZW0tbG90ZS1jb20tYS1tYXRyJUMzJUFEY3VsYS1qJUMzJUExLWV4aXN0ZW50ZS1uby1kZXN0aW5vBjsIVDoOc2VhcmNoX2lkSSIpYjFhYjA3ZTUtNDJjMy00YzM0LTk4MzctMmU2MmNkMmQ3MjRiBjsIRjoJcmFua2kNOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIfdHJhbnNmZXJlbmNpYSBkZSBtYXRyaWN1bGEGOwhUOhJyZXN1bHRzX2NvdW50aQIXBw%3D%3D--03b27eb67dd0b3bf351ced164569f919241b49c2)
