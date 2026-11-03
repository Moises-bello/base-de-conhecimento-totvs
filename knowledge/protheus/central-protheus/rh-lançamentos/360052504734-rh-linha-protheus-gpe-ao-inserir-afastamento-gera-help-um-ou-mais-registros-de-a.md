---
article_id: 360052504734
category: RH - Lançamentos
content_hash: a6236488c021ada96427e41e6bc12a7e6b27ba26355f1b56274deb214e4c3402
fetched_at: '2026-06-28T22:43:31.130620+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao inserir afastamento gera Help: Um ou mais registros
  de ausência não se encontram no Catálogo de Períodos'
type: support-article
updated_at: '2025-04-25T20:32:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052504734-RH-Linha-Protheus-GPE-Ao-inserir-afastamento-gera-Help-Um-ou-mais-registros-de-aus%C3%AAncia-n%C3%A3o-se-encontram-no-Cat%C3%A1logo-de-Per%C3%ADodos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31667719381271) Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência**

Ao inserir afastamento para funcionário gera Help: Um ou mais registros de ausência não se encontram no Catálogo de Períodos.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10636408370071)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Causa**

Esse incidente ocorre quando não existe o roteiro **FOL** cadastrado no período mencionado no Log. Para solucionar esse incidente, realize os seguintes passos:  
  
1. Acesse: **Atualizações > Definições de Cálculos > Períodos**

2. Verifique no Processo e Competência indicada no HELP, neste exemplo foi gerado no log o processo 00001 e período 202009 **[00001/202009]**, se possui o roteiro **FOL** cadastrado.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10636414543127)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10636487633431)  
  
3. Caso não possua, cadastre o mesmo para assim conseguir cadastrar a ausência. Para qualquer outro período que conste no Log o processo é o mesmo, este foi apenas um exemplo.

**Saiba Mais:**

[RH - Linha Protheus - GPE - Como Lançar Ausências para um Funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhz5FrSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBlGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxMTQ1NzY1MS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1MYW4lQzMlQTdhci1BdXMlQzMlQUFuY2lhcy1wYXJhLXVtLUZ1bmNpb24lQzMlQTFyaW8GOwhUOg5zZWFyY2hfaWRJIik5Yzc4MTZlNy0xNzMyLTRmYTUtOGU3Ni0zNzRhYmM3MzU0YzIGOwhGOglyYW5raQ06C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhljYWFkc3RybyBkZSBhdXNlbmNpYQY7CFQ6EnJlc3VsdHNfY291bnRpAi4C--6a5e7e5c671ff61255e685d7097fc132e7c1623b)  
[RH - Linha Protheus - GPE - Lançamento de ausência para funcionário em férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiNvYY%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBomh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDkzODEyNjEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUxhbiVDMyVBN2FtZW50by1kZS1hdXMlQzMlQUFuY2lhLXBhcmEtZnVuY2lvbiVDMyVBMXJpby1lbS1mJUMzJUE5cmlhcwY7CFQ6DnNlYXJjaF9pZEkiKTJlYzE1ZjEwLWRmZTMtNGFjMC04YzU3LWNmMmQ2YjQwNTAzOAY7CEY6CXJhbmtpCjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDWF1c2VuY2lhBjsIVDoScmVzdWx0c19jb3VudGkCOwI%3D--60d16e63aa18a87fc48fe39599ea3073e69af345)  
[RH - Linha Protheus - GPE - Anexar atestado na rotina de Ausências - GPEA240](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhBZj4%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBkGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDQ2NDAzMjEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUFuZXhhci1hdGVzdGFkby1uYS1yb3RpbmEtZGUtQXVzJUMzJUFBbmNpYXMtR1BFQTI0MAY7CFQ6DnNlYXJjaF9pZEkiKTJlYzE1ZjEwLWRmZTMtNGFjMC04YzU3LWNmMmQ2YjQwNTAzOAY7CEY6CXJhbmtpCzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDWF1c2VuY2lhBjsIVDoScmVzdWx0c19jb3VudGkCOwI%3D--6ac4d78f7303f5166527f5a2b320c5a998a9ce8c)
