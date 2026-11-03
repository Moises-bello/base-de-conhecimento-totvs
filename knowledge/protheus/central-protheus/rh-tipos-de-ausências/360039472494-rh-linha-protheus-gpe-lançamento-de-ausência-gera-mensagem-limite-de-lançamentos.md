---
article_id: 360039472494
category: RH - Tipos de Ausências
content_hash: ed8aadeef2c0b8936dc81378e3c2664add4fb8fa9404ee0d58952df1fbe06156
fetched_at: '2026-06-28T22:43:21.007577+00:00'
product: protheus
section_id: 360011967353
source: central-protheus
title: RH - Linha Protheus - GPE - Lançamento de ausência, gera mensagem Limite de
  lançamentos do mesmo tipo para um mesmo período alcançado
type: support-article
updated_at: '2025-01-22T17:46:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039472494-RH-Linha-Protheus-GPE-Lan%C3%A7amento-de-aus%C3%AAncia-gera-mensagem-Limite-de-lan%C3%A7amentos-do-mesmo-tipo-para-um-mesmo-per%C3%ADodo-alcan%C3%A7ado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16007547602967) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao lançar uma **nova** ausência/ afastamento para o funcionário dentro do mesmo mês, Sistema emite alerta:   

**Help:** HELP  
**Problema:** Limite de lançamentos do mesmo tipo para um mesmo período alcançado. Deverá cadastrar um novo tipo de ausência ou alterar verba aceitar mais lançamentos  
  
**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053033233)**

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse o tipo de ausência para verificar a verba utilizada pelo menu **Atualizações > Definições de Cálculo > Tipos de Ausências.**Selecione a ausência em questão e clique em **manutenção**. Verifique a verba informada.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052130074)

2. Acesse o cadastro de verbas em  **Atualizações > Definições de Cálculo > Verbas**.

Altere o campo **Lcto Diario** **(RV\_LCTODIA)** para **S.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052130174)

3. Acesse a rotina para lançar os afastamentos, **Atualizações > Lançamentos > Ausências**:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052130254)

**Saiba Mais**

[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)

[RH - Linha Protheus - GPE - Quais os parâmetros utilizados para o lançamento de ausências](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9071036090007-RH-Linha-Protheus-GPE-Quais-os-par%C3%A2metros-utilizados-para-o-lan%C3%A7amento-de-aus%C3%AAncias-?source=search)

[RH - Linha Protheus - GPE - Quais os pontos de entrada disponíveis na rotina GPEA240-Lançamentos de Ausências](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5421742901399--RH-Linha-Protheus-GPE-Quais-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEA240-Lan%C3%A7amentos-de-Aus%C3%AAncias?source=search)

[RH - Linha Protheus - GPE - Modificações para abatimento de cálculos em casos de Ausência na versão 12](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051996134-RH-Linha-Protheus-GPE-Modifica%C3%A7%C3%B5es-para-abatimento-de-c%C3%A1lculos-em-casos-de-Aus%C3%AAncia-na-vers%C3%A3o-12?source=search)

[RH - Linha Protheus - GPE - Como Lançar Ausências para um Funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011457651-RH-Linha-Protheus-GPE-Como-Lan%C3%A7ar-Aus%C3%AAncias-para-um-Funcion%C3%A1rio?source=search)

[RH - Linha Protheus - GPE - Como excluir um afastamento do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055985393-RH-Linha-Protheus-GPE-Como-excluir-um-afastamento-do-funcion%C3%A1rio?source=search)

[RH - Linha Protheus - GPE - Como informar data fim de afastamentos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006476621-RH-Linha-Protheus-GPE-Como-informar-data-fim-de-afastamentos?source=search)

[RH - Linha Protheus - GPE - Como informar afastamentos de estagiários](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjcI23SUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBimh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxMjY1MzUzMi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1pbmZvcm1hci1hZmFzdGFtZW50b3MtZGUtZXN0YWdpJUMzJUExcmlvcwY7CFQ6DnNlYXJjaF9pZEkiKTg1MzRlZGEyLTE0MmMtNDAwZC1hMmUyLTk4N2ZkZjNkM2M5YQY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiS1JIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBDb21vIGluZm9ybWFyIGFmYXN0YW1lbnRvcyBkZSBlc3RhZ2nDoXJpb3MGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--f4a0ff2869b09d84445bbd71a395d4d1a6ee4bef)

[RH - Linha Protheus - GPE - O que Analisar quando ao Lançar uma Nova Ausência, o sistema exibe a mensagem "Limite de Lançamentos do Mesmo Tipo Para o Mesmo Período Alcançado"](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwha1jzUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSICBQFodHRwczovL2NlbnRyYWxkZWF0ZW5kaW1lbnRvLnRvdHZzLmNvbS9oYy9wdC1ici9hcnRpY2xlcy8zNjAwNDMwNDIzOTQtUkgtTGluaGEtUHJvdGhldXMtR1BFLU8tcXVlLUFuYWxpc2FyLXF1YW5kby1hby1MYW4lQzMlQTdhci11bWEtTm92YS1BdXMlQzMlQUFuY2lhLW8tc2lzdGVtYS1leGliZS1hLW1lbnNhZ2VtLUxpbWl0ZS1kZS1MYW4lQzMlQTdhbWVudG9zLWRvLU1lc21vLVRpcG8tUGFyYS1vLU1lc21vLVBlciVDMyVBRG9kby1BbGNhbiVDMyVBN2Fkby0GOwhUOg5zZWFyY2hfaWRJIik0NmM5NDM1YS05MTcxLTRjMzYtYjQ2OC00ZmY1ZjJiZDM0MWIGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIgGzUkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIE8gcXVlIEFuYWxpc2FyIHF1YW5kbyBhbyBMYW7Dp2FyIHVtYSBOb3ZhIEF1c8OqbmNpYSwgbyBzaXN0ZW1hIGV4aWJlIGEgbWVuc2FnZW0gIkxpbWl0ZSBkZSBMYW7Dp2FtZW50b3MgZG8gTWVzbW8gVGlwbyBQYXJhIG8gTWVzbW8gUGVyw61vZG8gQWxjYW7Dp2FkbyIGOwhUOhJyZXN1bHRzX2NvdW50aQc%3D--2caf490f4264cd2fa613b51d304074c24484ac2f)
