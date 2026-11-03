---
article_id: 360059010854
category: RH - Lançamentos
content_hash: af94c4b5528013b71f3336c82c12fe7d3a1f8c14c8b70ed059e963f5a9242f6d
fetched_at: '2026-06-28T22:43:31.109562+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Alerta para quantidade máxima de verbas lançadas
  na rotina GPEA110 Valores futuros
type: support-article
updated_at: '2025-07-23T17:35:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059010854-RH-Linha-Protheus-GPE-Alerta-para-quantidade-m%C3%A1xima-de-verbas-lan%C3%A7adas-na-rotina-GPEA110-Valores-futuros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26297463581719) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Alerta para quantidade máxima de verbas lançadas na rotina GPEA110 Valores futuros.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Ao realizar uma grande quantidade de **lançamentos** da **mesma verba** pela rotina **GPEA110** - **Valores Futuros,** o sistema apresenta o seguinte alerta: **Quantidade máxima de lançamentos atingida. Verifique no cadastro de verba o campo "Quantidade de Lançamentos" - Verba XXX.**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000592021)

Para solucionar este problema, realize os seguinte procedimento:  
  
1. Acesse o cadastro da **verbas** em questão pelo caminho: **Atualizações > Definições de Cálculo > Verbas (GPEA040)** clique em **Alterar** e deixe os campos **Qtde. Lancto. = 9** e habilite o campo**Lcto Diário = SIM**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26297480225303)

Desta forma, o Sistema permitirá realizar **até** **9 lançamentos** para esta mesma verba, não emitindo o alerta de quantidade de lançamentos.  
Em casos específicos que existe a necessidade de **mais de 9 lançamentos**, sugerimos a criação de uma **nova verba** com as mesmas configurações desta já existente para seguir com os lançamentos.  
  
**Importante**  
Ressaltamos que **não é permitida inclusão de mais de uma verba com mesmo id de cálculo** no Sistema. Em caso de dúvidas, acione o Suporte Protheus para análise do cenário e orientações de acordo com seu cenário.

**Saiba Mais**  
[RH - Linha Protheus - GPE - Como atualizar o dicionário de dados (arquivo SXSBRA.TXT) do Protheus 12](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXLby0QxM6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzIxMTgxNTE1OTY3ODk1LVJILUxpbmhhLVByb3RoZXVzLUdQRS1Db21vLWF0dWFsaXphci1vLWRpY2lvbiVDMyVBMXJpby1kZS1kYWRvcy1hcnF1aXZvLVNYU0JSQS1UWFQtZG8tUHJvdGhldXMtMTIGOwhUOg5zZWFyY2hfaWRJIik5YWM0MWYxNC0yYWJjLTQ2NDctYjFhMy00MTA3OTlkNGM0YjEGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIiNhdHVhbGl6YXIgZGljaW9uw6FyaW8gZGUgZGFkb3MGOwhUOhJyZXN1bHRzX2NvdW50aQI%2BBA%3D%3D--c16abafbde48835a4371bbf3f2f791a35024a9b0)

[RH - Linha Protheus - GPE - Lançamentos por Funcionário Nenhum Roteiro foi definido como Ordinário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwibmbHRUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBsWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAwMDM2MjkwNy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTGFuJUMzJUE3YW1lbnRvcy1wb3ItRnVuY2lvbiVDMyVBMXJpby1OZW5odW0tUm90ZWlyby1mb2ktZGVmaW5pZG8tY29tby1PcmRpbiVDMyVBMXJpbwY7CFQ6DnNlYXJjaF9pZEkiKWU4MWQ2MjI3LTcxMGMtNGIzZi1hYzk5LTIwYTA3NWFmYzNiZAY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiImxhbsOnYW1lbnRvcyBwb3IgZnVuY2lvbsOhcmlvBjsIVDoScmVzdWx0c19jb3VudGkC7gM%3D--4493a2a014b1610524d423d799f3ea756099a9ef)

[RH - Linha Protheus - GPE - No lançamento por funcionário é apresentada a mensagem: Não permitida a inclusão de lançamentos para esta verba](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwg5PGrUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB6Gh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA0NjAxNzU5My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTm8tbGFuJUMzJUE3YW1lbnRvLXBvci1mdW5jaW9uJUMzJUExcmlvLSVDMyVBOS1hcHJlc2VudGFkYS1hLW1lbnNhZ2VtLU4lQzMlQTNvLXBlcm1pdGlkYS1hLWluY2x1cyVDMyVBM28tZGUtbGFuJUMzJUE3YW1lbnRvcy1wYXJhLWVzdGEtdmVyYmEGOwhUOg5zZWFyY2hfaWRJIillODFkNjIyNy03MTBjLTRiM2YtYWM5OS0yMGEwNzVhZmMzYmQGOwhGOglyYW5raQg6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIiJsYW7Dp2FtZW50b3MgcG9yIGZ1bmNpb27DoXJpbwY7CFQ6EnJlc3VsdHNfY291bnRpAu4D--c516346c1a9a2b3748a6d7da5994886f5c1859aa)

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
