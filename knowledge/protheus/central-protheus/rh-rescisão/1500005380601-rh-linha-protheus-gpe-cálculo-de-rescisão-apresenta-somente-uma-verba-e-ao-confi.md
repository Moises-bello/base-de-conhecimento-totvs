---
article_id: 1500005380601
category: RH - Rescisão
content_hash: 40bea394090a35e4abbd04a5c42cffcb64f74e41f76d248b345bef2b3ffbf367
fetched_at: '2026-06-28T22:43:48.533803+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE - Cálculo de rescisão apresenta somente uma verba
  e ao confirmar o cálculo é gerado aviso: FWNOWIDTH Valor atribuído difere do campo
  (C. de Custo)'
type: support-article
updated_at: '2025-07-17T12:32:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005380601-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-rescis%C3%A3o-apresenta-somente-uma-verba-e-ao-confirmar-o-c%C3%A1lculo-%C3%A9-gerado-aviso-FWNOWIDTH-Valor-atribu%C3%ADdo-difere-do-campo-C-de-Custo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24285014174615) Tempo aproximado para leitura: 00:02:00 min

**Ocorrência**  
Cálculo de rescisão apresenta somente uma verba e ao confirmar o cálculo é gerado aviso: FWNOWIDTH Valor atribuído difere do campo (C. de Custo):  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007242322)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
O problema ocorre pois o tamanho do campo Centro de Custo entre as tabelas SRA, SRR, RGB e CTT estão diferentes.  
  
**Solução**É necessário ajustar o tamanho do campo Centro de Custo entre as tabelas SRA, SRR, RGB e CTT.  
Após validação e correção do tamanho do campo Centro de Custo, o cálculo da rescisão apresentará todas a verbas.

Para ajuste no campo Centro de Custo siga o procedimento abaixo:

1. Acesse Configurador > Base de Dados > Dicionário > **Bases de Dados**;

2. Clique em Dicionário de Dados, selecione a tabela do campo, e clique em **Editar**;

3. Expanda a tabela, clique em **Campos** e localize o campo que vai alterar;

4. Clique sobre o campo e clique em **Editar**;

5. Em **Tamanho**, digite o novo tamanho do campo e clique em **Salvar**;

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)

[RH - Linha Protheus - GPE - Como gerar relatório com todo o cadastro de verbas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgUPlLSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBk2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxMDg5MDc3Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1nZXJhci1yZWxhdCVDMyVCM3Jpby1jb20tdG9kby1vLWNhZGFzdHJvLWRlLXZlcmJhcwY7CFQ6DnNlYXJjaF9pZEkiKTZhNjAxY2MxLTQ3MWEtNDhlNS1hMzQyLTMzMmEzYzVjYWFlOQY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiVFJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBDb21vIGdlcmFyIHJlbGF0w7NyaW8gY29tIHRvZG8gbyBjYWRhc3RybyBkZSB2ZXJiYXMGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--39a9e56849f8a930b0c6c543be58daaf35469aaf)   
[RH - Linha Protheus - GPE - "Valor atribuído difere do tamanho do campo (HORAS/DIAS)" ao calcular rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwh%2B9jrTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBsGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyNjE0MjMzNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtVmFsb3ItYXRyaWJ1JUMzJUFEZG8tZGlmZXJlLWRvLXRhbWFuaG8tZG8tY2FtcG8tSE9SQVMtRElBUy1hby1jYWxjdWxhci1yZXNjaXMlQzMlQTNvBjsIVDoOc2VhcmNoX2lkSSIpNTkzM2NlNDQtNjZmOC00NDMzLTk1MTEtNWU4OGQ5MWRhYzI5BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJxUkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtICJWYWxvciBhdHJpYnXDrWRvIGRpZmVyZSBkbyB0YW1hbmhvIGRvIGNhbXBvIChIT1JBUy9ESUFTKSIgYW8gY2FsY3VsYXIgcmVzY2lzw6NvBjsIVDoScmVzdWx0c19jb3VudGkI--ff96afe699822a17bea9d2204b40d16fa738a08d)   
[RH - Linha Protheus - GPE - Sistema não está apresentando tela de opções para a geração de rescisões complementares](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060953013-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-est%C3%A1-apresentando-tela-de-op%C3%A7%C3%B5es-para-a-gera%C3%A7%C3%A3o-de-rescis%C3%B5es-complementares?source=search)
