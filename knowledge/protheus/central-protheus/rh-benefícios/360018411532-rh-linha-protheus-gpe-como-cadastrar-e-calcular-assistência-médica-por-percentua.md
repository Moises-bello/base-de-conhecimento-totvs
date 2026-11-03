---
article_id: 360018411532
category: RH - Benefícios
content_hash: 5872411da3d61e6149c5f0e3565618f0dc8ce32a8fc48c264ba08e113ccfaa02
fetched_at: '2026-06-28T22:44:03.670619+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como cadastrar e calcular Assistência Médica por
  Percentual de Salário
type: support-article
updated_at: '2025-10-30T20:19:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018411532-RH-Linha-Protheus-GPE-Como-cadastrar-e-calcular-Assist%C3%AAncia-M%C3%A9dica-por-Percentual-de-Sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21293184254103) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como cadastrar e calcular Assistência Médica por Percentual de Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução****1.** Cadastre o fornecedorem **Atualizações > Definições de Cálculo > Manutenção de Tabela**, na tabela S016. [**Atenção:**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30317054879127-RH-Linha-Protheus-GPE-eSocial-S-1210-Como-enviar-as-informa%C3%A7%C3%B5es-de-plano-de-sa%C3%BAde-odonto-para-o-S-1210)  
\* O **campo filial** não deve ser preenchido  
\* O campo **Mês/Ano** se preenchido o sistema calculará somente para a data informada   
\* Cadastrar o **CNPJ** somente uma, vez. Não repetir mesmo o CNPJ  
\* As **verbas** devem ser diferentes das verbas de desconto funcionario  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21293338874903)

**2.** Cadastre o tipo do plano em **Atualizações > Definições de Cálculo > Manutenção de Tabela,** na tabela S029:![](https://centraldeatendimento.totvs.com/hc/article_attachments/21300514027671)  
**Obs:** O campo **TETO DESCONTO** precisa ser preenchido com um valor determinado de teto, pois com a configuração 0.00, a rotina entenderá que este valor é o teto e só apresentará a parte empresa. Caso não possua teto, configurar com 9.999.999,99. 

**3.** Cadastre as verbas de assistência médica em **Atualizações > Definições de Cálculos > Verbas:**As verbas referente ao **desconto** titular/dependente/agregado **não possuem id de cálculo,** pois serão vinculadas a rotina de **Planos Ativos** e as verbas **parte empresa** podem ser vinculadas a ids ou cadastradas na tabela auxiliar S016. Veja a tabela abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21300514050839)

**4.** Vincule o Funcionário com a Assistência Médicaem **Atualizações > Benefícios > Plano de Saúde > Planos Ativos:****![](https://centraldeatendimento.totvs.com/hc/article_attachments/21300499229719)**

- No campo **Tipo**, deve preencher com **Assistência Médica**- A partir deste campo, o sistema filtrará os demais de acordo com os cadastros das tabelas na Manutenção de Tabela  
- No campo **verba titular** (RHK\_PD), inclua o código da verba correspondente cadastrada no passo anterior  
- Os campos referente a **períodos** determinam o início do benefício para o Funcionário.  
- Para cadastrar dependente e agregado, devem ser seguidos os mesmos passos.

**5.** Calcule o Plano de Saúde em **Atualizaçõess > Benefícioss > Plano de Saúde > Cálculo Plano de Saúde.**

**6.** Emita o relatório de conferência em **Atualizações > Benefícios > Plano de Saúde > Relatório de Cálculo** ou consulte o cálculo individualmente em **Atualizações > Planos Ativos > Outras Ações > Consultar Cálculo.**

**7.** Após a conferência do Relatório, integre com a Folha em **Atualizaçõess > Benefícios > Planos de Saúde > Integração com a Folha.****Saiba Mais**[RH - Linha Protheus - GPE - Como funciona a rotina de Planos Saúde Ativos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhZqgPVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NjA3Mjc5My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1mdW5jaW9uYS1hLXJvdGluYS1kZS1QbGFub3MtU2ElQzMlQkFkZS1BdGl2b3MGOwhUOg5zZWFyY2hfaWRJIikyNzlkNzg4Ni04MjY4LTQ3YzYtOGI3MC05ZDhmNjZiZDllNmEGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhxyb3RpbmEgZGUgcGxhbm9zIGF0aXZvcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--8d29ed59a3583fc064e7a4ae3b44c4bda7334c5d)  
[RH - Linha Protheus - GPE - Relatório de cálculo assistência medica GPER008](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXvigHAwQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBm2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MTEwNTE1MjM3MzUtUkgtTGluaGEtUHJvdGhldXMtR1BFLVJlbGF0JUMzJUIzcmlvLWRlLWMlQzMlQTFsY3Vsby1hc3Npc3QlQzMlQUFuY2lhLW1lZGljYS1HUEVSMDA4BjsIVDoOc2VhcmNoX2lkSSIpMjQzNDI1NWItYjZhNi00Y2RhLWE2NDAtODhhZDQyMDM1NzU1BjsIRjoJcmFua2kHOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIMR1BFUjAwOAY7CFQ6EnJlc3VsdHNfY291bnRpAo0B--09362054ee3cee78faaedde8e1916f4b934f66fe)  
[RH - Linha Protheus - GPE - Quais as documentações relacionadas a rotina de plano de saúde](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXEfwyNQo6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBq2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExMjIzNjA0OTI0Njk1LVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFpcy1hcy1kb2N1bWVudGElQzMlQTclQzMlQjVlcy1yZWxhY2lvbmFkYXMtYS1yb3RpbmEtZGUtcGxhbm8tZGUtc2ElQzMlQkFkZQY7CFQ6DnNlYXJjaF9pZEkiKWZiZWFhOGY3LWY4YTktNGNiMy1iOTQyLTZjODE4OTJjNDg3MgY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiH3JlbGFjaW9uYWRhIHBsYW5vIGRlIHNhdWRlBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--a90f836dec2aaa2ebf6bf5f8f745a5e083307913)  
[RH - Linha Protheus - GPE - Quais as tabelas S relacionadas ao roteiro PLA - Plano de Saúde](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXO27DSAo6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBoGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExMzA3NjMyNzA0NDA3LVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFpcy1hcy10YWJlbGFzLVMtcmVsYWNpb25hZGFzLWFvLXJvdGVpcm8tUExBLVBsYW5vLWRlLVNhJUMzJUJBZGUGOwhUOg5zZWFyY2hfaWRJIilmYmVhYThmNy1mOGE5LTRjYjMtYjk0Mi02YzgxODkyYzQ4NzIGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIh9yZWxhY2lvbmFkYSBwbGFubyBkZSBzYXVkZQY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--1ec02a96c9722d29e3ca66e954cbf90b43271d87)
