---
article_id: 360057689734
category: RH - Benefícios
content_hash: ace6b7fc09db25f8b5aa73b87c4e361e199efee1d653054f7b2e185e2fa2db12
fetched_at: '2026-06-28T22:44:03.506194+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Cadastro das verbas referente ao plano odontológico
type: support-article
updated_at: '2025-10-30T20:09:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057689734-RH-Linha-Protheus-GPE-Cadastro-das-verbas-referente-ao-plano-odontol%C3%B3gico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21300622424471) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como cadastrar a verba de plano odontológico parte funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.33  
  
**Solução**

As **verbas de desconto** titular/dependente/agregado**não possuem id de cálculo,** pois serão vinculadas a rotina de **Planos Ativos** nos campos RHK\_PD, RHL\_PD e RHM\_PD.  
  
As verbas serão do tipo **Desconto**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21301632699415)

As verbas **parte empresa** podem ser vinculadas a id's **ou** cadastradas sem id's e vinculadas a tabela auxiliar S017.

**ID 0717-** Parte Empresa Assistência Odontológica Titular   
**ID 0718-** Parte Empresa Assistência Odontológica Dependente  
**ID 0719-** Parte Empresa Assistência Odontológica Agregado

As verbas serão do tipo **Base Provento.**  
  
Tabela Auxiliar S017, **não deve ser preenchido o campo Filial e deve haver somente um cadastro por CNPJ**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21301652830871)

Além disso, foram criados novos id's para gerar o valor total do benefício ao efetuar a integração do roteiro PLA (MOS da versão S-1.0), conforme a documentação:  
[RH - Linha Protheus - GPE - Valor total do benefício de assistência médica conforme determinação do MOS da versão S-1.0](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXr4NSUw06D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB12h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE0NjUxNTE3ODA4NDA3LVJILUxpbmhhLVByb3RoZXVzLUdQRS1WYWxvci10b3RhbC1kby1iZW5lZiVDMyVBRGNpby1kZS1hc3Npc3QlQzMlQUFuY2lhLW0lQzMlQTlkaWNhLWNvbmZvcm1lLWRldGVybWluYSVDMyVBNyVDMyVBM28tZG8tTU9TLWRhLXZlcnMlQzMlQTNvLVMtMS0wBjsIVDoOc2VhcmNoX2lkSSIpNjc0YmM5NTAtNjI4OS00YTJlLWEwMzktOWJjZmI4ODU4ZTYxBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIBfVJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBWYWxvciB0b3RhbCBkbyBiZW5lZsOtY2lvIGRlIGFzc2lzdMOqbmNpYSBtw6lkaWNhIGNvbmZvcm1lIGRldGVybWluYcOnw6NvIGRvIE1PUyBkYSB2ZXJzw6NvIFMtMS4wBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--861453b4b629a29657954eafa986d9792d668be1)

**Saiba Mais**  
[RH - Linha Protheus - GPE - Cancelamento do Plano de Saúde/Odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050086373-RH-Linha-Protheus-GPE-Cancelamento-do-Plano-de-Sa%C3%BAde-Odontol%C3%B3gico?source=search)  
[RH - Linha Protheus - GPE - Como Alterar a Assistência Médica/Odontológica do Funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025334874-RH-Linha-Protheus-GPE-Como-Alterar-a-Assist%C3%AAncia-M%C3%A9dica-Odontol%C3%B3gica-do-Funcion%C3%A1rio?source=search)  
[RH - Linha Protheus - GPE - Como descontar plano de saúde/odontológico apenas para o dependente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9941786531095-RH-Linha-Protheus-GPE-Como-descontar-plano-de-sa%C3%BAde-odontol%C3%B3gico-apenas-para-o-dependente?source=search)  
[RH - Linha Protheus - GPE - Como fazer reajuste de valores do plano de saúde e odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053108474-RH-Linha-Protheus-GPE-Como-fazer-reajuste-de-valores-do-plano-de-sa%C3%BAde-e-odontol%C3%B3gico?source=search)
