---
article_id: 360057700074
category: RH - Benefícios
content_hash: 8bc68b96f89feb9a755531838cf9008d6cdaf437b704c11d61e7e50412f25a78
fetched_at: '2026-06-28T22:44:03.501884+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Cadastro das verbas referente a assistência médica
type: support-article
updated_at: '2025-10-30T20:09:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057700074-RH-Linha-Protheus-GPE-Cadastro-das-verbas-referente-a-assist%C3%AAncia-m%C3%A9dica
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21351901371415) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como cadastrar as verbas referente a assistência médica?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.33  
  
**Solução**

As **verbas de desconto** titular/dependente/agregado**não possuem id de cálculo,** pois serão vinculadas a rotina de **Planos Ativos** nos campos RHK\_PD, RHL\_PD e RHM\_PD.  
  
As verbas serão do tipo **Desconto**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21352256415895)

As verbas **parte empresa** podem ser vinculadas a id's **ou** cadastradas sem id's e vinculadas a tabela auxiliar S016.

**ID 0213** - Base parte Empresa Assist. Medica  
**ID 0725** - Base parte Empresa Assist. Medica Dependentes  
**ID 0726 -** Base parte Empresa Assist. Medica Agregados

As verbas serão do tipo **Base Provento.**  
  
Tabela Auxiliar S016, **não deve ser preenchido o campo Filial e deve haver somente um cadastro por CNPJ**:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21352975079447)

Além disso, foram criados novos id's para gerar o **valor total** do benefício ao efetuar a integração do roteiro PLA (MOS da versão S-1.0), conforme a documentação:  
[RH - Linha Protheus - GPE - Valor total do benefício de assistência médica conforme determinação do MOS da versão S-1.0](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXr4NSUw06D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB12h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE0NjUxNTE3ODA4NDA3LVJILUxpbmhhLVByb3RoZXVzLUdQRS1WYWxvci10b3RhbC1kby1iZW5lZiVDMyVBRGNpby1kZS1hc3Npc3QlQzMlQUFuY2lhLW0lQzMlQTlkaWNhLWNvbmZvcm1lLWRldGVybWluYSVDMyVBNyVDMyVBM28tZG8tTU9TLWRhLXZlcnMlQzMlQTNvLVMtMS0wBjsIVDoOc2VhcmNoX2lkSSIpNjc0YmM5NTAtNjI4OS00YTJlLWEwMzktOWJjZmI4ODU4ZTYxBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIBfVJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBWYWxvciB0b3RhbCBkbyBiZW5lZsOtY2lvIGRlIGFzc2lzdMOqbmNpYSBtw6lkaWNhIGNvbmZvcm1lIGRldGVybWluYcOnw6NvIGRvIE1PUyBkYSB2ZXJzw6NvIFMtMS4wBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--861453b4b629a29657954eafa986d9792d668be1)

**Saiba Mais**[RH - Linha Protheus - GPE - Histórico de planos ativos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgmRrrUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBe2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MTI2MzAxNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtSGlzdCVDMyVCM3JpY28tZGUtcGxhbm9zLWF0aXZvcwY7CFQ6DnNlYXJjaF9pZEkiKWZiMGQwYmYxLTNhNTEtNDczNC04NGQxLTI2NTE4Y2I1ZjczOAY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiGXJvdGluYSBwbGFub3MgYXRpdm9zBjsIVDoScmVzdWx0c19jb3VudGkCDwE%3D--e5767e786e2c9040d5fb4d91632cb2386bb37ac4)  
[RH - Linha Protheus - GPE - Como funciona a rotina de Planos Saúde Ativos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhZqgPVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NjA3Mjc5My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1mdW5jaW9uYS1hLXJvdGluYS1kZS1QbGFub3MtU2ElQzMlQkFkZS1BdGl2b3MGOwhUOg5zZWFyY2hfaWRJIilmYjBkMGJmMS0zYTUxLTQ3MzQtODRkMS0yNjUxOGNiNWY3MzgGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhlyb3RpbmEgcGxhbm9zIGF0aXZvcwY7CFQ6EnJlc3VsdHNfY291bnRpAg8B--b0a195776bf2ab6f5f24fba6c97ed45e46bad021)  
[RH - Linha Protheus - GPE - Cancelamento do Plano de Saúde/Odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjlUajUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBkWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDA4NjM3My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ2FuY2VsYW1lbnRvLWRvLVBsYW5vLWRlLVNhJUMzJUJBZGUtT2RvbnRvbCVDMyVCM2dpY28GOwhUOg5zZWFyY2hfaWRJIilmYjBkMGJmMS0zYTUxLTQ3MzQtODRkMS0yNjUxOGNiNWY3MzgGOwhGOglyYW5raQk6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhlyb3RpbmEgcGxhbm9zIGF0aXZvcwY7CFQ6EnJlc3VsdHNfY291bnRpAg8B--c86cdd7b9b91c9275d7ab88c3fe60ec81a655eef)  
[RH - Linha Protheus - GPE - Quais as documentações relacionadas a rotina de plano de saúde](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXEfwyNQo6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBq2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExMjIzNjA0OTI0Njk1LVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFpcy1hcy1kb2N1bWVudGElQzMlQTclQzMlQjVlcy1yZWxhY2lvbmFkYXMtYS1yb3RpbmEtZGUtcGxhbm8tZGUtc2ElQzMlQkFkZQY7CFQ6DnNlYXJjaF9pZEkiKTM2NGY4ODFiLTJlOTMtNGQwYi05ZTIyLWE3ZTA1ZWE1MGZjZQY7CEY6CXJhbmtpDzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiGXJvdGluYSBwbGFub3MgYXRpdm9zBjsIVDoScmVzdWx0c19jb3VudGkCDwE%3D--563db3d7534365debbcb04a5eed8f49023bdb1b8)  
[RH - Linha Protheus - GPE - Quais as documentações relacionadas a rotina de plano odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXoi9HOgo6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBr2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExMjQ1NDE4Njg0OTUxLVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFpcy1hcy1kb2N1bWVudGElQzMlQTclQzMlQjVlcy1yZWxhY2lvbmFkYXMtYS1yb3RpbmEtZGUtcGxhbm8tb2RvbnRvbCVDMyVCM2dpY28GOwhUOg5zZWFyY2hfaWRJIikzNjRmODgxYi0yZTkzLTRkMGItOWUyMi1hN2UwNWVhNTBmY2UGOwhGOglyYW5raQ46C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhlyb3RpbmEgcGxhbm9zIGF0aXZvcwY7CFQ6EnJlc3VsdHNfY291bnRpAg8B--3afa7c06a73d5c5bab82666b49de5144334986da)
