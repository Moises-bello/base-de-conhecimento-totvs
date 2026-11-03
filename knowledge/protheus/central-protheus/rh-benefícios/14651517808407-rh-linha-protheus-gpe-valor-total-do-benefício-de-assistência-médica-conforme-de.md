---
article_id: 14651517808407
category: RH - Benefícios
content_hash: 6e28dd1566a393ce73a85cc3dcd1c3361751928e35dc3f54cec020ddd4d084be
fetched_at: '2026-06-28T22:44:04.826673+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Valor total do benefício de assistência médica
  conforme determinação do MOS da versão S-1.0
type: support-article
updated_at: '2025-10-24T19:37:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14651517808407-RH-Linha-Protheus-GPE-Valor-total-do-benef%C3%ADcio-de-assist%C3%AAncia-m%C3%A9dica-conforme-determina%C3%A7%C3%A3o-do-MOS-da-vers%C3%A3o-S-1-0
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23722649641111) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como informar o valor total do benefício de assistência médica e odontológica conforme determinação do MOS da versão S-1.0?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**No **MOS da versão S-1.0**, determina que os valores de parcelas salariais in natura devem ser informados pelo valor total e não apenas em relação à parte custeada pelo empregador.   
  
Para o **benefício de assistência médica e odontológica** foram criados os Id's de cálculo 1862 a 1867 para gerar o valor total do benefício ao **efetuar a integração do roteiro PLA.**

|  |  |
| --- | --- |
| Tipo | Verba |
| Valor Total -Assist. Médica Titular | Verba vinculada ao **ID 1862** |
| Valor Total - Assist. Médica Dependente | Verba vinculada ao **ID 1863** |
| Valor Total - Assist. Médica Agregado | Verba vinculada ao **ID 1864** |
| Valor Total - Assist. Odontológica Titular | Verba vinculada ao **ID 1865** |
| Valor Total - Assist. Odontológica Dependente | Verba vinculada ao **ID 1866** |
| Valor Total - Assist. Odontológica Agregado | Verba vinculada ao **ID 1867** |
| Desconto do funcionário -  Assist. Médica Titular | Verba cadastrada no campo RHK\_PD |
| Desconto do funcionário -  Assist. Médica Dependente | Verba cadastrada no campo RHL\_PD |
| Desconto do funcionário -  Assist. Médica Agregado | Verba cadastrada no campo RHM\_PD |
| Desconto do funcionário -  Assist. Odontológica Titular | Verba cadastrada no campo RHK\_PD |
| Desconto do funcionário -  Assist. Odontológica Dependente | Verba cadastrada no campo RHL\_PD |
| Desconto do funcionário -  Assist. Odontológica Agregado | Verba cadastrada no campo RHM\_PD |
| Parte da Empresa -  Assist. Médica Titular | Verba vinculada ao ID 0213 ou cadastrada no campo "Vb. Emp. Ass. Med. Tit." da tabela auxiliar S016 |
| Parte da Empresa -  Assist. Médica Dependente | Verba vinculada ao ID 0725 ou cadastrada no campo "Vb. Emp. Ass. Med. Dep." da tabela auxiliar S016 |
| Parte da Empresa -  Assist. Médica Agregado | Verba vinculada ao ID 0726 ou cadastrada no campo "Vb. Emp. Ass. Med. Agr." da tabela auxiliar S016 |
| Parte da Empresa -  Assist. Odontológica Titular | Verba vinculada ao ID 0717 ou cadastrada no campo "Vb. Emp. Ass. Odo. Tit." da tabela auxiliar S017 |
| Parte da Empresa -  Assist. Odontológica Dependente | Verba vinculada ao ID 0718 ou cadastrada no campo "Vb. Emp. Ass. Odo. Dep." da tabela auxiliar S017 |
| Parte da Empresa -  Assist. Odontológica Agregado | Verba vinculada ao ID 0719 ou cadastrada no campo "Vb. Emp. Ass. Odo. Agr." da tabela auxiliar S017 |

**Obs.:** A natureza de rubrica para assistência médica é 9911.

**Saiba Mais**[RH - Linha Protheus - GPE - Quais as documentações relacionadas a rotina de plano de saúde](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXEfwyNQo6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBq2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExMjIzNjA0OTI0Njk1LVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFpcy1hcy1kb2N1bWVudGElQzMlQTclQzMlQjVlcy1yZWxhY2lvbmFkYXMtYS1yb3RpbmEtZGUtcGxhbm8tZGUtc2ElQzMlQkFkZQY7CFQ6DnNlYXJjaF9pZEkiKWQ3NWEzZTc5LTk1ZjEtNDU3NC04YjBmLWI2YjMyNTFlZWI3NAY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiI2RvY3VtZW50YcOnw7VlcyBwbGFubyBkZSBzYXVkZQY7CFQ6EnJlc3VsdHNfY291bnRpAjMD--14f4a5a78d47e6f0144678bd3489b372b6be6da6)  
[RH - Linha Protheus - GPE - Quais as documentações relacionadas a rotina de plano odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXoi9HOgo6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBr2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExMjQ1NDE4Njg0OTUxLVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFpcy1hcy1kb2N1bWVudGElQzMlQTclQzMlQjVlcy1yZWxhY2lvbmFkYXMtYS1yb3RpbmEtZGUtcGxhbm8tb2RvbnRvbCVDMyVCM2dpY28GOwhUOg5zZWFyY2hfaWRJIik5YTI5NjA3My03ZmUwLTQ2MDEtODAyNi02MzI2M2UwNzkzMjIGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIjNRdWFpcyBhcyBkb2N1bWVudGHDp8O1ZXMgcmVsYWNpb25hZGFzIGEgcm90aW5hBjsIVDoScmVzdWx0c19jb3VudGkC6QM%3D--ceebc1526759483a9b28a23b93135cd8271b8260)

**MOS da versão S-1.0:** <https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-0-consolidada-ate-a-no-s-1-0-04-2021.pdf>

**Boletim Técnico:**<https://tdn.totvs.com/pages/releaseview.action?pageId=630365963#beneficios-BEN>
