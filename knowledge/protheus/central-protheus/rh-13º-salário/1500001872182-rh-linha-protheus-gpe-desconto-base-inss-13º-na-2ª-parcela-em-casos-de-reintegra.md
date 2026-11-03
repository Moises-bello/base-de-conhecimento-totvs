---
article_id: 1500001872182
category: RH - 13º salário
content_hash: 5435127f54cee32df77cb654aa96320894b76b0505f786bc5d88f7308727a233
fetched_at: '2026-06-28T22:44:00.750467+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Desconto base INSS 13º na 2ª Parcela em casos de
  Reintegração
type: support-article
updated_at: '2025-08-13T14:11:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001872182-RH-Linha-Protheus-GPE-Desconto-base-INSS-13%C2%BA-na-2%C2%AA-Parcela-em-casos-de-Reintegra%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18959629850647) Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Após reintegração do funcionário, no **Cálculo da 2ª parcela de 13°**, o sistema somente deduz o valor do 13º que foi pago na rescisão do líquido, **sem abater o valor da base de INSS.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
Falta de identificador de cálculo específico para abatimento da base de INSS  
  
**Solução**Realizado ajuste no cálculo do 13º salário de funcionário reintegrado para abater o valor de **13º já pago na rescisão da base de INSS**. Nessas situações, tendo a verba criada, será gerado o desconto na verba de ID **1856** (que deve incidir **INSS** e **FGTS**) ao invés da verba referente ao Id **0183** (que apenas possui incidência para **FGTS**). Necessário avaliar se possui a verba criada, caso não, crie conforme abaixo, e aplique o pacote de correção, através dos links do artigo abaixo:

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjeeR7VUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBwGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NzgyOTg1NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1mYXplci1vLWRvd25sb2FkLWJhaXhhci1kby1wYWNvdGUtZGUtZXhwZWRpJUMzJUE3JUMzJUEzby1jb250JUMzJUFEbnVhLWFjdW11bGFkby1kby1SSC1Qcm90aGV1cwY7CFQ6DnNlYXJjaF9pZEkiKTdhYjkxMGZmLWE0M2EtNDBhNS1iNWY4LWE5NGJhZDlkZDE5MgY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkifVJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBDb21vIGZhemVyIG8gZG93bmxvYWQgKGJhaXhhcikgZG8gcGFjb3RlIGRlIGV4cGVkacOnw6NvIGNvbnTDrW51YSAoYWN1bXVsYWRvKSBkbyBSSCBQcm90aGV1cwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--175fe4053b96630d224a3411629b660d371c12f2)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001751921)

Após atualização caso não tenha a verba cadastrada referente ao id 1856, será necessário acessar **Atualizações > Definições de Cálculos > Verbas GPEA040**, para inclui-la.

**Saiba Mais****[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
Essas documentações também podem ser acessadas através da Carolina, veja como acessar a assistente virtual, via Protheus ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>**
