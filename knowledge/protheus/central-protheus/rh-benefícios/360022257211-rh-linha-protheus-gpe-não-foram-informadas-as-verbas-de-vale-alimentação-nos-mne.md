---
article_id: 360022257211
category: RH - Benefícios
content_hash: de393257dcab853b478935637616a907d7f1970fee12eb554b738a4e0f0f4a64
fetched_at: '2026-06-28T22:44:04.915073+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Não foram informadas as verbas de vale alimentação
  nos mnemônicos P_PDVAEMP e/ou P_PDVADES. Vale alimentação não foi integrado
type: support-article
updated_at: '2025-05-06T20:13:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022257211-RH-Linha-Protheus-GPE-N%C3%A3o-foram-informadas-as-verbas-de-vale-alimenta%C3%A7%C3%A3o-nos-mnem%C3%B4nicos-P-PDVAEMP-e-ou-P-PDVADES-Vale-alimenta%C3%A7%C3%A3o-n%C3%A3o-foi-integrado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31914775812119) Tempo aproximado para leitura: 00:02:00min**

**Ocorrência**Ao integrar o roteiro de vale alimentação, o sistema retorna a mensagem: Não foram informadas as verbas de vale alimentação nos mnemônicos **P\_PDVAEMP e/ou P\_PDVADES**. Vale alimentação não foi integrado.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Causa**  
Os mnemônicos **P\_PDVAEMP e/ou P\_PDVADES** não possuem verbas cadastradas.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse Atualizações/ Definições de cálculo/Verbas  e localize ou cadastre caso não tenha, as verbas de **Desconto Vale Alimentação (**tipo Desconto) e **Base VA Empresa (**tipo Base Provento) **ambas sem ID de Cálculo**, conforme abaixo:

Verba de Desconto de Vale Alimentação![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6171724323351)

Verba de Base parte Empresa

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6171764300055)

2. Acesse **Atualizações/ Definições de cálculo/ Mnemônicos,** localize primeiramente o Mnemônico **P\_PDVADES**, inclua no campo conteúdo a verba de Desconto de Vale Alimentação entre aspas duplas e confirme.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6171792681239)  
  
3. Localize o **Mnemônico P\_PDVAEMP**, inclua no campo conteúdo a verba **Base VA Empresa,** entre aspas duplas e confirme.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6171757236247)  
  
  
4. Prossiga com o processo de integração do Roteiro VAL  
  
  
**Saiba Mais:**[RH - Linha Protheus - GPE - Cadastro e Cálculo do Vale Alimentação](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhIMmXTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBkWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyODkxMDE1Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ2FkYXN0cm8tZS1DJUMzJUExbGN1bG8tZG8tVmFsZS1BbGltZW50YSVDMyVBNyVDMyVBM28GOwhUOg5zZWFyY2hfaWRJIillMWQ2NDNhYy00ODBjLTQ1MzQtODI4ZS00YmMxZGU0ZjQxYjIGOwhGOglyYW5raQk6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhByb3RlaXJvIFZBTAY7CFQ6EnJlc3VsdHNfY291bnRpArcE--1c9f4d39833e378f196ee06504cdc8ae44b7e689)  
[RH - Linha Protheus - GPE - Pontos de Entrada da rotina GPEA131](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgBKSrTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBgGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyNTA0MTE1My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUG9udG9zLWRlLUVudHJhZGEtZGEtcm90aW5hLUdQRUExMzEtBjsIVDoOc2VhcmNoX2lkSSIpMzUwNThiMmYtY2U2OC00YjJmLTk5M2EtZWVkMjI4ZTEwOTgwBjsIRjoJcmFua2kPOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIXdmFsZSBhbGltZW50YcOnw6NvBjsIVDoScmVzdWx0c19jb3VudGkCCAY%3D--882d9b536a7d0928c7d46b685f174e71d491bfcc)  
[RH - Linha Protheus - GPE - Ao realizar a Integração do roteiro VAL com a folha gera o valor de desconto integral para o funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgX44%2BS5Qg6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB1Gh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzk3ODIwOTk0MzYzMTEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUFvLXJlYWxpemFyLWEtSW50ZWdyYSVDMyVBNyVDMyVBM28tZG8tcm90ZWlyby1WQUwtY29tLWEtZm9saGEtZ2VyYS1vLXZhbG9yLWRlLWRlc2NvbnRvLWludGVncmFsLXBhcmEtby1mdW5jaW9uJUMzJUExcmlvBjsIVDoOc2VhcmNoX2lkSSIpZTFkNjQzYWMtNDgwYy00NTM0LTgyOGUtNGJjMWRlNGY0MWIyBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIQcm90ZWlybyBWQUwGOwhUOhJyZXN1bHRzX2NvdW50aQK3BA%3D%3D--88f05c7319abd89717fdd81316a96c15f5c504a7)
