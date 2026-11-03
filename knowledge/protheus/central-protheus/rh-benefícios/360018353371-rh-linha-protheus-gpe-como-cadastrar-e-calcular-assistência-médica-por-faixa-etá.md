---
article_id: 360018353371
category: RH - Benefícios
content_hash: b6b07dc6d5f16e1f7d014eb4a890aef8dde3f48d4a8ad886789b8963a89f8d9d
fetched_at: '2026-06-28T22:44:03.651361+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como cadastrar e calcular assistência médica por
  faixa etária
type: support-article
updated_at: '2025-09-05T10:26:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018353371-RH-Linha-Protheus-GPE-Como-cadastrar-e-calcular-assist%C3%AAncia-m%C3%A9dica-por-faixa-et%C3%A1ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21644942542743) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como cadastrar e calcular assistência médica por faixa etária?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões

**Solução**

1.Cadastre o fornecedor em **Atualizações/ Definições de cálculo/ Manutenção de tabela**, tabela **S016;**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8928517899287)

2. Cadastre o tipo do plano em **Atualizações/Definições de cálculo/Manutenção de tabela**, na tabela **S009;**

**O código dos planos devem ser iguais** para que o sistema altere o plano do funcionário automaticamente conforme a faixa etária.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21648278081175)

3. Cadastre as verbas de assistência médica em **Atualizações/ Definições de cálculo/ Verbas;**

As verbas referente ao **desconto** titular/dependente/agregado **não possuem id de cálculo,** pois serão vinculadas a rotina de **Planos Ativos** e as verbas **parte empresa** podem ser vinculadas a id's ou cadastradas na tabela auxiliar S016. Veja a tabela abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21645221503895)

4. Vincule o funcionário com a assistência médica em **Atualizações/ Benefícios/ Planos de Saúde/ Planos ativos;**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21648321443479)**

- No campo **Tipo**, deve preencher com **Assistência Médica**- A partir deste campo o Sistema filtrará os demais de acordo com o cadastro realizado na rotina de manutenção de tabela  
- Nos campos **verba titular** (RHK\_PD), inclua o códigos da verba correspondente cadastradas no passo anterior  
- Os campos referente a **períodos** determina o início do benefício para o funcionário

Para cadastrar dependente e agregado segue o mesmo processo.

5. Calcule o plano de saúde em **Atualizações/ Benefícios/ Plano de saúde/ Cálculo Plano de Saúde;**

6. Emita o relatório de conferência em **Atualizações/ Benefícios/ Plano de Saúde/ Relatório de cálculo** ou consulte o cálculo individualmente em **Atualizações/ Planos ativos/ Outras ações/ Consultar cálculo**

7. Após conferência do Relatório, integre com a folha em **Atualizações/ Benefícios/ Planos de Saúde/  Integração com a folha.**

**Saiba Mais:**[RH - Linha Protheus - GPE - Como funciona a rotina de Planos Saúde Ativos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhZqgPVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NjA3Mjc5My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1mdW5jaW9uYS1hLXJvdGluYS1kZS1QbGFub3MtU2ElQzMlQkFkZS1BdGl2b3MGOwhUOg5zZWFyY2hfaWRJIikyNzlkNzg4Ni04MjY4LTQ3YzYtOGI3MC05ZDhmNjZiZDllNmEGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhxyb3RpbmEgZGUgcGxhbm9zIGF0aXZvcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--8d29ed59a3583fc064e7a4ae3b44c4bda7334c5d)  
[RH - Linha Protheus - GPE - Relatório de cálculo assistência medica GPER008](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXvigHAwQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBm2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MTEwNTE1MjM3MzUtUkgtTGluaGEtUHJvdGhldXMtR1BFLVJlbGF0JUMzJUIzcmlvLWRlLWMlQzMlQTFsY3Vsby1hc3Npc3QlQzMlQUFuY2lhLW1lZGljYS1HUEVSMDA4BjsIVDoOc2VhcmNoX2lkSSIpMjQzNDI1NWItYjZhNi00Y2RhLWE2NDAtODhhZDQyMDM1NzU1BjsIRjoJcmFua2kHOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIMR1BFUjAwOAY7CFQ6EnJlc3VsdHNfY291bnRpAo0B--09362054ee3cee78faaedde8e1916f4b934f66fe)  
[RH - Linha Protheus - GPE - Cadastro das verbas referente a assistência médica](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjqfhzVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NzcwMDA3NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ2FkYXN0cm8tZGFzLXZlcmJhcy1yZWZlcmVudGUtYS1hc3Npc3QlQzMlQUFuY2lhLW0lQzMlQTlkaWNhBjsIVDoOc2VhcmNoX2lkSSIpNDY3OGE4NjItYmUzZi00OTY1LWI3YzEtMThkMmNkMTlkMjZjBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIedmVyYmFzIGFzc2lzdGVuY2lhIG1lZGljYQY7CFQ6EnJlc3VsdHNfY291bnRpAugB--19f018a17eb4c3eaf95527efc90d750f12045955)  
[RH - Linha Protheus - GPE - Como consultar o cálculo de assistência médica individualmente](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXJeauXRM6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBq2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzIxMjkzMDg3MjA0NzU5LVJILUxpbmhhLVByb3RoZXVzLUdQRS1Db21vLWNvbnN1bHRhci1vLWMlQzMlQTFsY3Vsby1kZS1hc3Npc3QlQzMlQUFuY2lhLW0lQzMlQTlkaWNhLWluZGl2aWR1YWxtZW50ZQY7CFQ6DnNlYXJjaF9pZEkiKWYxYzI3Zjc5LWI2MzgtNDUzYi1hM2ZjLWYyNTcwMDM3ZTFkYQY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiJmNvbnN1bHRhciBjYWxjdWxvIGluZGl2aWR1YWxtZW50ZQY7CFQ6EnJlc3VsdHNfY291bnRpAjwE--2f42fefe581f889cba0020042f8842455ed14fe2)
