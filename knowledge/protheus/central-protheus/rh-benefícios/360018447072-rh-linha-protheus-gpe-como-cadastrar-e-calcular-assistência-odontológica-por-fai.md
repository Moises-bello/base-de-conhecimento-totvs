---
article_id: 360018447072
category: RH - Benefícios
content_hash: ee01b6b069d72cd806c9f907f3321c08bf05d97c85715b6892c36ef8bd371833
fetched_at: '2026-06-28T22:44:03.684320+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como cadastrar e calcular Assistência Odontológica
  por Faixa Salarial
type: support-article
updated_at: '2025-08-28T02:48:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018447072-RH-Linha-Protheus-GPE-Como-cadastrar-e-calcular-Assist%C3%AAncia-Odontol%C3%B3gica-por-Faixa-Salarial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22004250058519) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como cadastrar e calcular Assistência Odontológica por Faixa Salarial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**

**1 -** Cadastre o fornecedor em **Atualizações > Definições de Cálculo > Manutenção de Tabela > Tabela S017:** **![](https://centraldeatendimento.totvs.com/hc/article_attachments/22007970065559)**

**2 -** Cadastre o tipo do plano em **Atualizações > Definições de Cálculo > Manutenção de Tabela > Tabela S013.**Os códigos dos planos devem **ser iguais** para que o sistema altere o plano do Funcionário automaticamente conforme a faixa salarial:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/22007970098711)**

**3 -** Cadastre as **verbas** de assistência odontológica em **Atualizações > Definições de Cálculo > Verbas.**As verbas referente ao **desconto** do titular/dependente/agregado **não possuem id de cálculo,** pois serão vinculadas a rotina de **Planos Ativos,** e as verbas **parte empresa** podem ser vinculadas a id's ou cadastradas na tabela auxiliar **S017**. Veja a tabela abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22004370093079)

**4 -** Vincule o Funcionário com a assistência odontológica em **Atualizações > Benefícios > Planos de Saúde > Planos Ativos:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22007970119447)

- No campo **Tipo**, deve ser preenchido com a opção **Ass. Odontológica;**- A partir deste campo, o Sistema filtrará os demais de acordo com o cadastro realizado na rotina de **Manutenção de Tabela;**  
- No campo **Verba Titular** (RHK\_PD), inclua o código da verba correspondente cadastrada no passo anterior;  
- Os campos referente a **Períodos,** determinam o **início/fim do benefício** para o Funcionário.  
**OBS:** Para cadastro de  **dependentes e agregados,** siga os mesmos passos.

**5** - Calcule o plano em **Atualizações > Benefícios > Plano de Saúde > Cálculo Plano de Saúde;**

**6 -** Emita o relatório de conferência em **Atualizações > Benefícios > Plano de Saúde > Relatório de Cálculo** ou consulte o cálculo individualmente em **Atualizações > Planos Ativos > Outras Ações > Consultar Cálculo.**

**7 -** Após conferência do Relatório, integre o roteiro **PLA** com a Folha em **Atualizações > Benefícios > Planos de Saúde > Integração com a Folha.**

**ATENÇÃO**  
Os valores **não serão enviados automaticamente para DIRF** quando utilizado o lançamento fixo. Orientamos que **utilize as rotinas próprias para cálculo de Plano de Saúde e Odontológico**, pois dessa maneira as informações serão levadas automaticamente para DIRF.  
Para fazer o lançamento de forma manual na DIRF, consulte [esta documentação.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021563052-RH-Linha-Protheus-GPE-Quando-os-planos-de-sa%C3%BAde-s%C3%A3o-informados-manualmente-para-o-funcion%C3%A1rio-o-que-fazer-para-DIRF)

**Saiba Mais:**[RH - Linha Protheus - GPE - Como funciona a rotina de Planos Saúde Ativos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhZqgPVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NjA3Mjc5My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1mdW5jaW9uYS1hLXJvdGluYS1kZS1QbGFub3MtU2ElQzMlQkFkZS1BdGl2b3MGOwhUOg5zZWFyY2hfaWRJIikyNzlkNzg4Ni04MjY4LTQ3YzYtOGI3MC05ZDhmNjZiZDllNmEGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhxyb3RpbmEgZGUgcGxhbm9zIGF0aXZvcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--8d29ed59a3583fc064e7a4ae3b44c4bda7334c5d)  
[RH - Linha Protheus - GPE - Relatório de cálculo assistência medica GPER008](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXvigHAwQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBm2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MTEwNTE1MjM3MzUtUkgtTGluaGEtUHJvdGhldXMtR1BFLVJlbGF0JUMzJUIzcmlvLWRlLWMlQzMlQTFsY3Vsby1hc3Npc3QlQzMlQUFuY2lhLW1lZGljYS1HUEVSMDA4BjsIVDoOc2VhcmNoX2lkSSIpMjQzNDI1NWItYjZhNi00Y2RhLWE2NDAtODhhZDQyMDM1NzU1BjsIRjoJcmFua2kHOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIMR1BFUjAwOAY7CFQ6EnJlc3VsdHNfY291bnRpAo0B--09362054ee3cee78faaedde8e1916f4b934f66fe)  
[RH - Linha Protheus - GPE - Cadastro das verbas referente ao plano odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiGVhzVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBlGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NzY4OTczNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ2FkYXN0cm8tZGFzLXZlcmJhcy1yZWZlcmVudGUtYW8tcGxhbm8tb2RvbnRvbCVDMyVCM2dpY28GOwhUOg5zZWFyY2hfaWRJIikzNjFkNTE0MS00ZTJiLTQ5ZWYtODhjZi1jMDliOTQ3MGY3MjcGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIiJjYWRhc3RybyBkYXMgdmVyYmFzIHJlZmVyZW50ZQY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--eb804b30eacec294da30775b3d472e74310b4e1f)  
[RH - Linha Protheus - GPE - Como consultar o cálculo de assistência médica individualmente](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXJeauXRM6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBq2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzIxMjkzMDg3MjA0NzU5LVJILUxpbmhhLVByb3RoZXVzLUdQRS1Db21vLWNvbnN1bHRhci1vLWMlQzMlQTFsY3Vsby1kZS1hc3Npc3QlQzMlQUFuY2lhLW0lQzMlQTlkaWNhLWluZGl2aWR1YWxtZW50ZQY7CFQ6DnNlYXJjaF9pZEkiKWYxYzI3Zjc5LWI2MzgtNDUzYi1hM2ZjLWYyNTcwMDM3ZTFkYQY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiJmNvbnN1bHRhciBjYWxjdWxvIGluZGl2aWR1YWxtZW50ZQY7CFQ6EnJlc3VsdHNfY291bnRpAjwE--2f42fefe581f889cba0020042f8842455ed14fe2)  
[RH - Linha Protheus - GPE - Quando os planos de saúde são informados manualmente para o funcionário o que fazer para DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021563052-RH-Linha-Protheus-GPE-Quando-os-planos-de-sa%C3%BAde-s%C3%A3o-informados-manualmente-para-o-funcion%C3%A1rio-o-que-fazer-para-DIRF)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
