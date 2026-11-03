---
article_id: 16913390371735
category: RH - Relatórios Cadastros/Funcionários
content_hash: a6473cf0bae4790496e89673f0de05e0bdf8816c3ab65b44b920b5ef565a7c29
fetched_at: '2026-06-28T22:43:18.499803+00:00'
product: protheus
section_id: 360010843654
source: central-protheus
title: RH - Linha Protheus - GPE - Relatório Por Período Horizontal (GPER103) desalinhado
type: support-article
updated_at: '2025-09-12T17:01:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16913390371735-RH-Linha-Protheus-GPE-Relat%C3%B3rio-Por-Per%C3%ADodo-Horizontal-GPER103-desalinhado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16913378263319) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Relatório Por Período Horizontal (GPER103) desalinhado  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.33  
  
**Causa**Geração em impressora virtuais (não homologado), ou o fonte GPER103 com data anterior à 01/08/2023  
  
**Solução**Mesmo que o relatório seja em PDF, são utilizados informações de drivers de impressão .drv da pasta system e drivers da impressora local.   
O relatório **não está homologado** para impressora virtuais (PDF).  
  
**Exemplos:**   
Opção PDF + ***Servidor***= homologado, com exceção de impressoras virtuais (Ex. Microsoft to Print)

Opção Arquivo + ***Servidor*** = homologado, com exceção de impressoras virtuais (Ex. Microsoft to Print)

Opção PDF + ***Cliente(Local)*** = homologado

Opção Arquivo + ***Cliente(Local)*** = homologado, com exceção de impressoras virtuais (Ex. Microsoft to Print)

Para maiores informações acesse:

* [Impressão de relatório TReport](https://tdn.totvs.com/pages/releaseview.action?pageId=712483557)
* [TOTVS Printer - Instalação](https://tdn.totvs.com/pages/viewpage.action?pageId=364910001)
* [DT Rel.Per.Horizontal desalinhado](https://tdn.totvs.com/x/97eJLg)

Caso o fonte GPER103 esteja com data inferior a 01/08/2023 recomendamos que o sistema seja atualizado com o ultimo pacote de expedição continua do RH.

**Saiba Mais:**[RH - Linha Protheus - GPE - Como emitir um relatório por verba](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhaALPUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBg2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDc4NjM5NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1lbWl0aXItdW0tcmVsYXQlQzMlQjNyaW8tcG9yLXZlcmJhBjsIVDoOc2VhcmNoX2lkSSIpMjFjNGQ5NzItOWUxOC00ZGEzLTgwZmYtMzE3ZDY2NjJkMDVhBjsIRjoJcmFua2kHOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIMR1BFUjEwMwY7CFQ6EnJlc3VsdHNfY291bnRpAek%3D--8ff4665b19d3e1fa8524dadfa4173d2ffb3d15ed)  
[RH - Linha Protheus - GPE - Quais relatórios demonstram os valores da folha de pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXlpiMLQk6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBn2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzEwMDkxMjM2OTg4NTY3LVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFpcy1yZWxhdCVDMyVCM3Jpb3MtZGVtb25zdHJhbS1vcy12YWxvcmVzLWRhLWZvbGhhLWRlLXBhZ2FtZW50bwY7CFQ6DnNlYXJjaF9pZEkiKTIxYzRkOTcyLTllMTgtNGRhMy04MGZmLTMxN2Q2NjYyZDA1YQY7CEY6CXJhbmtpDToLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDEdQRVIxMDMGOwhUOhJyZXN1bHRzX2NvdW50aQHp--513176371d3e9335e3228a6130c3e72a1dc5c3df)  
[RH - Linha Protheus - GPE - Quais relatórios de Lançamentos são gerados em formato planilha](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjdHNvUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzQxNTEzMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUXVhaXMtcmVsYXQlQzMlQjNyaW9zLWRlLUxhbiVDMyVBN2FtZW50b3MtcyVDMyVBM28tZ2VyYWRvcy1lbS1mb3JtYXRvLXBsYW5pbGhhBjsIVDoOc2VhcmNoX2lkSSIpMjFjNGQ5NzItOWUxOC00ZGEzLTgwZmYtMzE3ZDY2NjJkMDVhBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIMR1BFUjEwMwY7CFQ6EnJlc3VsdHNfY291bnRpAek%3D--ce207e69756259c3e417629b8bddb030edda3b95)
