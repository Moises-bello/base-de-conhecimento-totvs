---
article_id: 360050528693
category: RH - Cadastros
content_hash: f772e8c6605f25fb1b26b9243d7e94c2a89fc1c1a370b84e32df2f51323b3c77
fetched_at: '2026-06-28T22:43:25.910846+00:00'
product: protheus
section_id: 360010781894
source: central-protheus
title: RH - Linha Protheus - GPE - Consulta Genérica não demonstra campos que são
  tipo Memo
type: support-article
updated_at: '2026-06-25T10:59:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050528693-RH-Linha-Protheus-GPE-Consulta-Gen%C3%A9rica-n%C3%A3o-demonstra-campos-que-s%C3%A3o-tipo-Memo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22469981035159) Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**  
Consulta Genérica não demonstra campos que são tipo Memo  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**  
Isso ocorre pois por padrão do Protheus, o comportamento é de que **nenhum campo do tipo** **Memo** seja apresentado no***browser***e na impressão da **Consulta Genérica** gerada via CSV ou XML, pois o tamanho do campo é muito grande para que seja apresentado nos locais citados.

**Saiba Mais**  
[RH - Linha Protheus - GPE - Como configurar e gerar Relatórios Totvs Report - PREPORT](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgX%2BIr%2BBAQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MTk0OTY5MDA2MzEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tY29uZmlndXJhci1lLWdlcmFyLVJlbGF0JUMzJUIzcmlvcy1Ub3R2cy1SZXBvcnQtUFJFUE9SVAY7CFQ6DnNlYXJjaF9pZEkiKTAxOTJkZTEwLTI1MDctNGI2Ny04NzBhLWUxY2M4ZGVlNzRhYQY7CEY6CXJhbmtpCDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiF3JlbGF0w7NyaW8gcHJlcG9ydAY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--64989520737356edbd6b4f2f3d3a53e6c82dbf60)  
[RH - Linha Protheus - GPE - Como gerar relatório através da consulta genérico relacional](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwihq%2Fg%2BXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDAwNzA1NjEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tZ2VyYXItcmVsYXQlQzMlQjNyaW8tYXRyYXYlQzMlQTlzLWRhLWNvbnN1bHRhLWdlbiVDMyVBOXJpY28tcmVsYWNpb25hbAY7CFQ6DnNlYXJjaF9pZEkiKTlhNjRkMTMzLWE1MjEtNDg4Ni04NmVlLTQ5ZGE3NDliNDE4ZQY7CEY6CXJhbmtpCDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiF2NvbnN1bHRhIGdlbsOpcmljYQY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--deb06e341f9941e7df35b8d5952f0373770e3451)  
[RH - Linha Protheus - GPE - Como gerar um relatório com a informação da situação do funcionário: admitido, demitido, férias ou afastado através da consulta genérica](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjFuUvVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSICDgFodHRwczovL2NlbnRyYWxkZWF0ZW5kaW1lbnRvLnRvdHZzLmNvbS9oYy9wdC1ici9hcnRpY2xlcy8zNjAwNjA3OTUzMzMtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tZ2VyYXItdW0tcmVsYXQlQzMlQjNyaW8tY29tLWEtaW5mb3JtYSVDMyVBNyVDMyVBM28tZGEtc2l0dWElQzMlQTclQzMlQTNvLWRvLWZ1bmNpb24lQzMlQTFyaW8tYWRtaXRpZG8tZGVtaXRpZG8tZiVDMyVBOXJpYXMtb3UtYWZhc3RhZG8tYXRyYXYlQzMlQTlzLWRhLWNvbnN1bHRhLWdlbiVDMyVBOXJpY2EGOwhUOg5zZWFyY2hfaWRJIik5YTY0ZDEzMy1hNTIxLTQ4ODYtODZlZS00OWRhNzQ5YjQxOGUGOwhGOglyYW5raQ86C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhdjb25zdWx0YSBnZW7DqXJpY2EGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--66acf64df0be4d854377bb76cdc561660389d649)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
