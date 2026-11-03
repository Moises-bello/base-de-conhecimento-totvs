---
article_id: 360017547832
category: RH - Benefícios
content_hash: 7327e6ddba78369aadb289922648ec5e5bbece1cf4586926c2d822c1f24cb8b5
fetched_at: '2026-06-28T22:44:03.696137+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como cadastrar e calcular Assistência Odontológica
  por valor fixo
type: support-article
updated_at: '2025-09-26T13:49:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017547832-RH-Linha-Protheus-GPE-Como-cadastrar-e-calcular-Assist%C3%AAncia-Odontol%C3%B3gica-por-valor-fixo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21893357489431) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como cadastrar e calcular Assistência Odontológica por valor fixo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões

**Solução:**

**1.** Cadastre o fornecedor em **Atualizações> Definições de cálculo> Manutenção de tabela**, tabela **S017;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21893995873047)

**2.** Cadastre o tipo do plano em **Atualizações> Definições de cálculo> Manutenção de tabela**, na tabela **S030;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21893995883799)**

**3.** Cadastre as verbas de assistência odontológica em **Atualizações> Definições de cálculo> Verbas;**

As verbas referente ao desconto titular/dependente/agregado não possuem id de cálculo, pois serão vinculadas a rotina de **Planos Ativos** e as verbas parte empresa podem ser vinculadas a id's ou cadastradas na tabela auxiliar S017. Veja a tabela abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21893995896983)

**4.** Vincule o funcionário com a assistência odontológica em **Atualizações> Benefícios> Planos de Saúde/ Planos Ativos;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21893995911447)**

- No campo **Tipo**, deve preencher com **Ass. Odontologica**- A partir deste campo o Sistema filtrará os demais de acordo com o cadastro realizado na rotina de manutenção de tabela  
- Nos campos **verba titular** (RHK\_PD), inclua o códigos da verba correspondente cadastradas no passo anterior  
- Os campos referente a **períodos** determina o início do benefício para o funcionário

Para cadastrar dependente e agregado segue o mesmo processo.

**5.** Calcule o plano em **Atualizações> Benefícios> Plano de saúde> Cálculo Plano de Saúde;**

**6.** Emita o relatório de conferência em **Atualizações> Benefícios> Plano de Saúde> Relatório de cálculo** ou consulte o cálculo individualmente em **Atualizações> Planos ativos> Outras ações> Consultar cálculo**

**7.** Após conferência do Relatório, integre com a folha em **Atualizações> Benefícios> Planos de Saúde>  Integração com a folha.**

**ATENÇÃO**  
Os valores **não serão enviados automaticamente para DIRF**, quando utilizado o lançamento fixo. Orientamos que **utilize as rotinas própria para cálculo de plano de saúde e odontológico**, pois dessa maneira as informações serão levadas automaticamente para DIRF.  
Segue documentação para lançar manual na DIRF, caso necessário:

[RH - Linha Protheus - GPE - Quando os planos de saúde são informados manualmente para o funcionário o que fazer para DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwisFvXSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIByGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyMTU2MzA1Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUXVhbmRvLW9zLXBsYW5vcy1kZS1zYSVDMyVCQWRlLXMlQzMlQTNvLWluZm9ybWFkb3MtbWFudWFsbWVudGUtcGFyYS1vLWZ1bmNpb24lQzMlQTFyaW8tby1xdWUtZmF6ZXItcGFyYS1ESVJGBjsIVDoOc2VhcmNoX2lkSSIpMjI3NDQ5NGMtOGM5Zi00YWI0LTljMWEtMGViNWY3OGMwZjVlBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIBfFJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBRdWFuZG8gb3MgcGxhbm9zIGRlIHNhw7pkZSBzw6NvIGluZm9ybWFkb3MgbWFudWFsbWVudGUgcGFyYSBvIGZ1bmNpb27DoXJpbyBvIHF1ZSBmYXplciBwYXJhIERJUkYGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--1b458e2502798436e6830470819a29936a5fe4e3)

**Saiba Mais:**[RH - Linha Protheus - GPE - Como funciona a rotina de Planos Saúde Ativos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhZqgPVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NjA3Mjc5My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1mdW5jaW9uYS1hLXJvdGluYS1kZS1QbGFub3MtU2ElQzMlQkFkZS1BdGl2b3MGOwhUOg5zZWFyY2hfaWRJIikyNzlkNzg4Ni04MjY4LTQ3YzYtOGI3MC05ZDhmNjZiZDllNmEGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhxyb3RpbmEgZGUgcGxhbm9zIGF0aXZvcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--8d29ed59a3583fc064e7a4ae3b44c4bda7334c5d)  
[RH - Linha Protheus - GPE - Relatório de cálculo assistência medica GPER008](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXvigHAwQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBm2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MTEwNTE1MjM3MzUtUkgtTGluaGEtUHJvdGhldXMtR1BFLVJlbGF0JUMzJUIzcmlvLWRlLWMlQzMlQTFsY3Vsby1hc3Npc3QlQzMlQUFuY2lhLW1lZGljYS1HUEVSMDA4BjsIVDoOc2VhcmNoX2lkSSIpMjQzNDI1NWItYjZhNi00Y2RhLWE2NDAtODhhZDQyMDM1NzU1BjsIRjoJcmFua2kHOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIMR1BFUjAwOAY7CFQ6EnJlc3VsdHNfY291bnRpAo0B--09362054ee3cee78faaedde8e1916f4b934f66fe)  
[RH - Linha Protheus - GPE - Cadastro das verbas referente ao plano odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiGVhzVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBlGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NzY4OTczNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ2FkYXN0cm8tZGFzLXZlcmJhcy1yZWZlcmVudGUtYW8tcGxhbm8tb2RvbnRvbCVDMyVCM2dpY28GOwhUOg5zZWFyY2hfaWRJIikzNjFkNTE0MS00ZTJiLTQ5ZWYtODhjZi1jMDliOTQ3MGY3MjcGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIiJjYWRhc3RybyBkYXMgdmVyYmFzIHJlZmVyZW50ZQY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--eb804b30eacec294da30775b3d472e74310b4e1f)  
[RH - Linha Protheus - GPE - Como consultar o cálculo de assistência médica individualmente](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXJeauXRM6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBq2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzIxMjkzMDg3MjA0NzU5LVJILUxpbmhhLVByb3RoZXVzLUdQRS1Db21vLWNvbnN1bHRhci1vLWMlQzMlQTFsY3Vsby1kZS1hc3Npc3QlQzMlQUFuY2lhLW0lQzMlQTlkaWNhLWluZGl2aWR1YWxtZW50ZQY7CFQ6DnNlYXJjaF9pZEkiKWYxYzI3Zjc5LWI2MzgtNDUzYi1hM2ZjLWYyNTcwMDM3ZTFkYQY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiJmNvbnN1bHRhciBjYWxjdWxvIGluZGl2aWR1YWxtZW50ZQY7CFQ6EnJlc3VsdHNfY291bnRpAjwE--2f42fefe581f889cba0020042f8842455ed14fe2)
