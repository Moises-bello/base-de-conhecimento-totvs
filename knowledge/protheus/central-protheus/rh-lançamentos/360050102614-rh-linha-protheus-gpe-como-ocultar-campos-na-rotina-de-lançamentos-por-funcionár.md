---
article_id: 360050102614
category: RH - Lançamentos
content_hash: 70a4bc9f374965462265341f1edfd5de3affe0a0c5b1026b3d1f7c09aeae7a8f
fetched_at: '2026-06-28T22:43:31.231309+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Como ocultar campos na rotina de Lançamentos por
  Funcionário
type: support-article
updated_at: '2024-09-09T19:25:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050102614-RH-Linha-Protheus-GPE-Como-ocultar-campos-na-rotina-de-Lan%C3%A7amentos-por-Funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26236771718551)Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como ocultar campo em lançamentos por funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**No exemplo a seguir, a rotina **lançamentos por funcionário** possui o campo **Aulas Semana**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26236803521559)

Siga as instruções para ocultar o campo.  
**1 -** Acesso ao configurador SIGACFG com senha de **administrador**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26236803523991)

**2 -** Clique em **Base de Dados > Dicionário > Base de Dados**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26237175561367)

**3 -** Clique em **Dicionário e Dados** e pesquise a tabela RGB e clique em **editar.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26236803524631)

**4 -** Clique em **Incidências > Campos > Editar** e  escolha o campo a ser oculto.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26236771727383)

**5 -** Clique em **Uso** e deixe as 3 opções **em branco** e clique em **salvar.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26236803527703)

**6 -** Após Salvar clique em **Incidências** novamente e depois em **Confirmar.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26237175562903)**

**7 -** Para atualizar o **Dicionário de Dados** do ambiente, clique em **Atualizar Base de Dados > Avançar e Atualizar**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26237175567767)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26237175572631)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26237124275223)

Após alteração no Configurador, ao acessar a rotina de Lançamentos > Por Funcionário, o campo **Aulas Semana**não será apresentado.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26237124284183)

**Saiba Mais**

[RH - Linha Protheus - GPE - Lançamentos por Funcionário Nenhum Roteiro foi definido como Ordinário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwibmbHRUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBsWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAwMDM2MjkwNy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTGFuJUMzJUE3YW1lbnRvcy1wb3ItRnVuY2lvbiVDMyVBMXJpby1OZW5odW0tUm90ZWlyby1mb2ktZGVmaW5pZG8tY29tby1PcmRpbiVDMyVBMXJpbwY7CFQ6DnNlYXJjaF9pZEkiKWU4MWQ2MjI3LTcxMGMtNGIzZi1hYzk5LTIwYTA3NWFmYzNiZAY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiImxhbsOnYW1lbnRvcyBwb3IgZnVuY2lvbsOhcmlvBjsIVDoScmVzdWx0c19jb3VudGkC7gM%3D--4493a2a014b1610524d423d799f3ea756099a9ef)

[RH - Linha Protheus - GPE - No lançamento por funcionário é apresentada a mensagem: Não permitida a inclusão de lançamentos para esta verba](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwg5PGrUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB6Gh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA0NjAxNzU5My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTm8tbGFuJUMzJUE3YW1lbnRvLXBvci1mdW5jaW9uJUMzJUExcmlvLSVDMyVBOS1hcHJlc2VudGFkYS1hLW1lbnNhZ2VtLU4lQzMlQTNvLXBlcm1pdGlkYS1hLWluY2x1cyVDMyVBM28tZGUtbGFuJUMzJUE3YW1lbnRvcy1wYXJhLWVzdGEtdmVyYmEGOwhUOg5zZWFyY2hfaWRJIillODFkNjIyNy03MTBjLTRiM2YtYWM5OS0yMGEwNzVhZmMzYmQGOwhGOglyYW5raQg6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIiJsYW7Dp2FtZW50b3MgcG9yIGZ1bmNpb27DoXJpbwY7CFQ6EnJlc3VsdHNfY291bnRpAu4D--c516346c1a9a2b3748a6d7da5994886f5c1859aa)

[RH - Linha Protheus - GPE - Como realizar o cálculo do lançamento pela rotina Lançamentos por funcionários GPEA580](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj1NU%2FVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBxmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA2MTAyMzczMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1yZWFsaXphci1vLWMlQzMlQTFsY3Vsby1kby1sYW4lQzMlQTdhbWVudG8tcGVsYS1yb3RpbmEtTGFuJUMzJUE3YW1lbnRvcy1wb3ItZnVuY2lvbiVDMyVBMXJpb3MtR1BFQTU4MAY7CFQ6DnNlYXJjaF9pZEkiKWU4MWQ2MjI3LTcxMGMtNGIzZi1hYzk5LTIwYTA3NWFmYzNiZAY7CEY6CXJhbmtpCToLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiImxhbsOnYW1lbnRvcyBwb3IgZnVuY2lvbsOhcmlvBjsIVDoScmVzdWx0c19jb3VudGkC7gM%3D--1788c83da79138e392e950949a002342ff6e9e75)

[RH - Linha Protheus - GPE - Como excluir verbas em lote que constam nos Lançamentos por Funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjGk%2BHTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBrmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAzNzA2MTU3NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1leGNsdWlyLXZlcmJhcy1lbS1sb3RlLXF1ZS1jb25zdGFtLW5vcy1MYW4lQzMlQTdhbWVudG9zLXBvci1GdW5jaW9uJUMzJUExcmlvcwY7CFQ6DnNlYXJjaF9pZEkiKWU4MWQ2MjI3LTcxMGMtNGIzZi1hYzk5LTIwYTA3NWFmYzNiZAY7CEY6CXJhbmtpCzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiImxhbsOnYW1lbnRvcyBwb3IgZnVuY2lvbsOhcmlvBjsIVDoScmVzdWx0c19jb3VudGkC7gM%3D--11dba6c039cea01a226cf82ab8e1c45cd148acd0)

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
